"""
ai_helper.py

Provides a utility functions that integrate with AI.
"""

import json
import os
import pathlib
import re
import subprocess

import requests
from requests import Response

from utils.paths import TESTS_DIR, AI_REPORTS_PATH

API_KEY: str | None = os.getenv("OPENROUTER_API_KEY")
MODEL: str = (
    "deepseek/deepseek-chat-v3-0324:free"  # free models allow only 50 usages per day
)

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


def generate_ai_summary() -> None:
    """
    Generates a summary of AI suggestions for failed tests.
    """
    print("\n\nAsking AI for help with failed tests...")

    suggestions: list = ask_ai_about_failures()
    if not suggestions:
        print("No test failures found.\n")
        return

    AI_REPORTS_PATH.mkdir(parents=True, exist_ok=True)
    md_lines: list = ["# AI Suggestions for Test Failures\n", "## Failed tests\n"]

    # Table of contents
    for suggestion in suggestions:
        test_name: str = suggestion["test"]
        anchor: str = re.sub(r"[^\w\- ]", "", test_name).replace(" ", "").lower()
        md_lines.append(f"- [{test_name}](#{anchor})")
    md_lines.append("")

    # Suggestions
    for suggestion in suggestions:
        md_lines.append(f"## {suggestion["test"]}\n{suggestion['ai_suggestion']}\n")

    # Save to md file
    md_summary_path: pathlib.Path = pathlib.Path(AI_REPORTS_PATH / "ai_summary.md")
    md_summary_path.write_text("\n".join(md_lines), encoding="utf-8")

    # Convert Markdown to HTML
    html_summary_path = AI_REPORTS_PATH / "ai_summary.html"
    subprocess.run(
        ["grip", str(md_summary_path), "--export", str(html_summary_path)],
        check=True,
    )

    print("AI summary was generated and saved to ai_summary.md and ai_summary.html\n")
