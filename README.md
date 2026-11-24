# Personal Expense and Budget Analyzer (Student Pocket Money & Canteen Tracker)

A Python-based expense tracker and budget analyzer built for **Computational Thinking and Programming (2026CSAE100)** at **Bennett University** (Milestone 2).

## Key Features
- **Expense Recording & Validation:** Add expenses with amount, category, and an optional note with `try-except` and positive-value checks.
- **CSV Persistence:** Automatically saves transactions to `expenses_data.csv` using `csv` and `os`.
- **OOP Architecture:** Uses `Transaction` (base class), `Expense` (inherits from `Transaction`), and `BudgetAnalyzer` (encapsulates budget and manages analytics).
- **Nested Budget Alerts:** Warns when spending reaches **80%+** or **exceeds 100%** of the monthly budget.
- **Category Insights & Visual Bar Chart:** Calculates category-wise totals, percentage shares, average spend, and displays an ASCII bar chart.

## Repository Contents
- `budget_analyser.py` — Main Python source code
- `expenses_data.csv` — Recorded transaction data
- `Milestone 2 Project 1.0.pdf` — Complete Milestone 2 report (including EL Activities 3–7)
- `Personal Expense & Budget Analyser 1.01.pptx` — Milestone 2 presentation deck

## Team Members
- **Satyam Singh** (`S26CSEU2136`)
- **Adil Saifi** (`S26CSEU2125`)
- **Om Singh** (`S26CSEU1955`)
