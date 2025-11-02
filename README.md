# Worker

A simple **Python project** that defines a `Worker` class with attributes and methods for managing employee information, searching workers, and calculating salary bonuses.

---

## Description

This program allows you to:
- Add new workers and display their details
- Search for workers by number or name
- Calculate salary bonuses based on work experience
- Remove workers from the list

It is a beginner-friendly example of **object-oriented programming (OOP)** in Python.

---

## Features

- `worker_information()` – prints worker data (name, age, salary, experience)
- `salary_bonus()` – calculates a bonus depending on experience
- `add_worker()` and `remove_worker()` – modify the worker list
- `search_by_name_experience()` – find workers with a given name and experience

---

## Example Usage

```python
from Worker import Worker

# Create a worker
worker = Worker(1, "Teodora", "Ivanova", 7, 2500, 25)

# Show information
worker.worker_information()

# Calculate bonus
print("Bonus:", worker.salary_bonus())
