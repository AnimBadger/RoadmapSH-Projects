# GitHub User Activity CLI

A simple Python CLI tool that fetches and displays the recent public activity of a GitHub user directly in the terminal — built to satisfy the **GitHub User Activity** project challenge on [RoadmapSH](https://roadmap.sh/projects/github-user-activity).

---

## 🧠 Project Overview

This command-line application allows you to:

- Accept a GitHub username as input.
- Fetch the user’s recent public activity from the GitHub API.
- Display it in a clean, readable format in the terminal.
- Handle edge cases like invalid usernames, network failures, empty input, and malformed API responses.

🎯 No external libraries or frameworks are used to fetch data — only Python’s standard library (`urllib`, `json`).

---

## 🚀 Features

- **CLI Interface** — Runs from terminal with a username prompt.
- **API Integration** — Uses GitHub’s public API to retrieve event data.
- **Error Handling Logic**:
  - Detects invalid or empty usernames.
  - Gracefully handles HTTP errors (e.g., user not found).
  - Handles network errors and API anomalies.
- **Readable Output** — Activity events shown with clear labels and time stamps.
- **Test Coverage** — Includes unit tests covering all edge cases.

---

## 📌 How to Use

### Run from Terminal

Execute the CLI:

```bash
python github_activity.py
```
