# Equipment Request Application

A simple Python console application for an introductory 3000-level programming course.

## Run the application

1. Install Python 3 if needed.
2. Download this repository using GitHub's **Code > Download ZIP**, then extract it.
3. Open a terminal in the extracted folder.
4. Run:

```bash
python equipment_request_app.py
```

On Windows, you can also use `py equipment_request_app.py`. On macOS or Linux, use `python3 equipment_request_app.py` if needed.

## Menu

- **1. Add equipment request:** Enter an equipment name, your name, and High, Medium, or Low priority. Priority input is not case-sensitive.
- **2. View requests:** Start with High priority requests. Type All, High, Medium, or Low to change the view, or Back to return to the main menu. Each view shows a matching count.
- **3. Exit:** Close the application.

Blank names and invalid menu or priority choices are checked. Requests are stored in memory and are cleared when the program closes. No extra packages or database are needed.

## Code overview

The program uses a list of dictionaries, functions, loops, and if/elif/else statements. `add_request` collects information, `view_requests` displays it, and `main` runs the menu.

Exercise 6 adds exact-priority filtering. See [the specification](docs/priority-filter-spec.md) for the rules and verification results.

## Quick manual check

Add a request for each priority. Open View requests and confirm High is shown first. Try Medium, Low, All, an invalid filter, and Back. Confirm All still contains every request. Run automated checks with `python -m unittest discover -s tests -v`.

## Exercise 7: requirements review

The repository-scoped skill lives in `.agents/skills/requirements-reviewer/SKILL.md`. In a Codex session opened on this repository, invoke:

```text
$requirements-reviewer Review the priority-filter feature against docs/priority-filter-spec.md. Do not change files.
```

The reviewer compares acceptance criteria with code and tests, cites evidence, reports gaps and data concerns, and does not edit files unless asked.
