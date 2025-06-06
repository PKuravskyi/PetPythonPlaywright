"""
ai_helper.py

Provides a utility functions that integrate with AI.
"""

import json
import os
import pathlib
import re

import requests
from requests import Response

from utils.paths import TESTS_DIR

API_KEY: str | None = os.getenv("OPENROUTER_API_KEY")
MODEL: str = "deepseek/deepseek-chat-v3-0324:free"

HEADERS: dict[str, str] = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}


def ___get_test_failures(
    report_path: pathlib.Path = TESTS_DIR / "tests_report.json",
) -> list:
    """
    Reads test report and returns a list of failed tests with error messages.

    Args:
        report_path (Path): Path to the report file with test results
    """
    with open(report_path, "r", encoding="utf-8") as file:
        data: dict = json.load(file)

    failures: list = []
    for test in data["tests"]:
        if test["outcome"] == "failed":
            failures.append(
                {"name": test["nodeid"], "message": test["call"]["longrepr"]}
            )

    return failures


def ask_ai_about_failures() -> list:
    """
    Sends failed test info to AI and returns AI suggestions for fixing them.
    """
    failures: list = ___get_test_failures()

    responses: list = []
    for fail in failures:
        prompt = f"""Test `{fail['name']}` failed with error:\n{fail['message']}\n
        Give a short explanation of what likely caused the failure, and how to fix it."""

        payload: dict = {
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "You're a Python QA engineer that helps debug automated Playwright test failures.",
                },
                {"role": "user", "content": prompt},
            ],
        }

        response: Response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers=HEADERS,
            data=json.dumps(payload),
            timeout=10,
        )

        if response.status_code == 200:
            content = response.json()["choices"][0]["message"]["content"]
            responses.append({"test": fail["name"], "ai_suggestion": content})
        else:
            responses.append(
                {
                    "test": fail["name"],
                    "ai_suggestion": f"Error from API: {response.status_code} - {response.text}",
                }
            )

    return responses


def generate_failure_ai_summary() -> None:
    """
    Generates a Markdown summary of AI suggestions for failed tests.
    Saves it as ai_summary.md.
    """
    print("\n\n🤖 Asking AI for help with failed tests...")

    suggestions: list = ask_ai_about_failures()
    if not suggestions:
        print("✅ No test failures found.\n")
        return

    md_lines: list = ["# 🤖 AI Suggestions for Test Failures\n", "## Failed tests\n"]

    # Table of contents
    for suggestion in suggestions:
        test_name: str = suggestion["test"]
        anchor: str = re.sub(r"[^\w\- ]", "", test_name).replace(" ", "").lower()
        md_lines.append(f"- [{test_name}](#{anchor})")
    md_lines.append("")

    # Suggestions
    for suggestion in suggestions:
        md_lines.append(f"## {suggestion["test"]}\n{suggestion['ai_suggestion']}\n")

    # Save to file
    summary_path: pathlib.Path = pathlib.Path(TESTS_DIR / "ai_summary.md")
    summary_path.write_text("\n".join(md_lines), encoding="utf-8")

    print("🤖 AI summary was generated and saved to ai_summary.md\n")
