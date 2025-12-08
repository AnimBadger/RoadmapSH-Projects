# Task Tracker (Python CLI)

This is my Python implementation of the [Task Tracker](https://roadmap.sh/projects/task-tracker) project from roadmap.sh — a simple command‑line tool to help you manage your to‑do list, track tasks, and mark their status.

## 🚀 Project Overview

With this CLI app you can:

- Add new tasks
- Update or delete existing tasks
- Mark tasks as **in‑progress** or **done**
- List all tasks or filter by status (e.g. todo, in‑progress, done)

Tasks are stored in a local JSON file. If the file doesn’t exist, the app will create it automatically.

## 🧰 How to Use

```bash
# Clone the repo
git clone https://github.com/AnimBager/RoadmapSH-Projects.git
cd Task tracker

# Run the CLI (assuming using Python 3.x)
python -m task_tracker.cli add "Buy groceries"
python -m task_tracker.cli list
python -m task_tracker.cli mark-in-progress 1
python -m task_tracker.cli mark-done 1
python -m task_tracker.cli update 1 "Buy groceries and cook dinner"
python -m task_tracker.cli delete 1
```
