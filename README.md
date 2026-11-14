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
- **2. View all requests:** Display every request in the order it was added.
- **3. Exit:** Close the application.

Blank names and invalid menu or priority choices are checked. Requests are stored in memory and are cleared when the program closes. No extra packages or database are needed.

## Code overview

The program uses a list of dictionaries, functions, loops, and if/elif/else statements. `add_request` collects information, `view_requests` displays it, and `main` runs the menu.

Priority filtering is intentionally not implemented. It is reserved for Exercise 6.

## Quick manual check

View requests before adding any, then add one request for each priority. View all requests and confirm each name and priority appears. Try an invalid priority and an invalid menu choice, then exit.
