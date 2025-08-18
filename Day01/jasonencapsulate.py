# store.py
import json, os, tempfile
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).parent.resolve()
DATA = ROOT / "data"
DATA.mkdir(parents=True, exist_ok=True)
ORDERS = DATA / "orders.json"

def _atomic_write_json(path: Path, obj) -> None:
    # temp file in SAME folder (same drive) → os.replace works on Windows
    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8", dir=path.parent) as tf:
        json.dump(obj, tf, indent=2, ensure_ascii=False)
        tmp_name = tf.name
    os.replace(tmp_name, path)

def load_orders() -> list[dict]:
    if not ORDERS.exists():
        ORDERS.write_text("[]", encoding="utf-8")
        return []
    try:
        return json.loads(ORDERS.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        # fall back to empty if corrupt (caller may rebuild)
        return []

def save_orders(orders: Iterable[dict]) -> None:
    _atomic_write_json(ORDERS, list(orders))

def append_order(order: dict) -> None:
    data = load_orders()
    data.append(order)
    save_orders(data)

def update_status(order_id: int, new_status: str) -> bool:
    data = load_orders()
    found = False
    for rec in data:
        if rec.get("id") == order_id:
            rec["status"] = new_status
            found = True
            break
    if found:
        save_orders(data)
    return found

# Minimal validation helper (optional, extend in hackathon)
def normalize_order(rec: dict) -> dict:
    return {
        "id": int(rec.get("id", -1)),
        "customer": str(rec.get("customer", "Unknown")),
        "value": float(rec.get("value", 0)),
        "status": str(rec.get("status", "Pending")),
    }

if __name__ == "__main__":
    # Demo: append and update
    append_order(normalize_order({"id": 200, "customer": "Nora", "value": 199.0, "status": "Pending"}))
    updated = update_status(200, "Shipped")
    print("Updated:", updated)
    print("Total orders:", len(load_orders()))
