"""
Employee Record System — Skeleton (Challenge Version)
Fill in the TODOs during the mini-project.
"""

import json, os, tempfile
from pathlib import Path
1
# ---------------- Paths ----------------
ROOT = Path(__file__).parent.resolve()
DATA = ROOT / "data"
DATA.mkdir(parents=True, exist_ok=True)
EMP_FILE = DATA / "employees.json"

# ---------------- Utils ----------------
def atomic_write_json(path: Path, obj) -> None:
    """Write JSON atomically (temp file in same folder; Windows-safe)."""
    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8", dir=path.parent) as tf:
        json.dump(obj, tf, indent=2, ensure_ascii=False)
        tmp = tf.name
    os.replace(tmp, path)

# ---------------- Persistence (TODOs) ----------------
def load_employees() -> list[dict]:
    """
    TODO:
    - If EMP_FILE doesn't exist, create it with "[]", then return [].
    - If it exists, read JSON and return a list of dicts.
    - Handle JSONDecodeError by returning [] (and optionally print a warning).
    """
    # HINT:
    # if not EMP_FILE.exists(): EMP_FILE.write_text("[]", encoding="utf-8"); return []
    # import json; data = json.loads(EMP_FILE.read_text(encoding="utf-8"))
    raise NotImplementedError

def save_employees(items: list[dict]) -> None:
    """
    TODO:
    - Save 'items' to EMP_FILE using atomic_write_json.
    """
    raise NotImplementedError

# ---------------- Validation (optional stretch) ----------------
def normalize_employee(rec: dict) -> dict:
    """
    OPTIONAL TODO:
    - Return a normalized dict with keys: id(int), name(str), dept(str), role(str), salary(float).
    - Provide defaults: dept="General", role="Employee".
    """
    return rec  # keep simple for now

def validate_employee(rec: dict) -> tuple[bool, str]:
    """
    OPTIONAL TODO:
    - Ensure id >= 0, name non-empty, salary >= 0.
    - Return (True, "") if ok, else (False, "reason").
    """
    return True, ""

# ---------------- CRUD (TODOs) ----------------
def add_employee(db: list[dict]) -> None:
    """
    TODO:
    - Read inputs (id, name, dept, role, salary)
    - Convert types (int/float as needed); handle ValueError
    - (Optional) normalize + validate; prevent duplicate IDs
    - Append to db
    - Print success/failure message
    """
    # HINT:
    # rec = {...}; db.append(rec)
    pass

def list_employees(db: list[dict]) -> None:
    """
    TODO:
    - If empty, print 'No employees.'
    - Else, print a small table of records.
    """
    pass

def search_employee(db: list[dict]) -> None:
    """
    TODO:
    - Ask for a name query (case-insensitive, partial match)
    - Print matching records or 'No matches.'
    """
    pass

def update_employee(db: list[dict]) -> None:
    """
    TODO:
    - Ask for ID to update; find record
    - Ask for new role/salary (blank to keep old)
    - Update fields; print confirmation or 'Not found.'
    """
    pass

def delete_employee(db: list[dict]) -> None:
    """
    TODO:
    - Ask for ID to delete; remove record if present
    - Print confirmation or 'Not found.'
    """
    pass

# ---------------- Reports (TODO) ----------------
def report_summary(db: list[dict]) -> None:
    """
    TODO:
    - Print total count
    - Print count by department
    - Print top 3 salaries (id, name, salary)
    """
    pass

# ---------------- Main ----------------
MENU = """
--- Employee Record System ---
1. Add
2. List
3. Search (by name)
4. Update (role/salary)
5. Delete
6. Summary
7. Save & Exit
Choose: """

def main():
    # TODO: load employees at start
    db = []  # replace with load_employees()

    while True:
        choice = input(MENU).strip()
        if choice == "1":
            add_employee(db)
        elif choice == "2":
            list_employees(db)
        elif choice == "3":
            search_employee(db)
        elif choice == "4":
            update_employee(db)
        elif choice == "5":
            delete_employee(db)
        elif choice == "6":
            report_summary(db)
        elif choice == "7":
            # TODO: save_employees(db)
            print(f"💾 (Pretend) Saved to {EMP_FILE}")
            break
        else:
            print("Invalid choice. Try 1–7.")

if __name__ == "__main__":
    main()
