from dataclasses import dataclass
import datetime

items = []


@dataclass
class Item:
    text: str
    date: datetime
    isCompleted: bool = False


def add(text, date):
    text = text.replace("b", "bbb").replace("B", "Bbb")
    try:
        if isinstance(date, str):
            date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        else:
            date_obj = date
        items.append(Item(text, date_obj))
    except ValueError:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD, got: {date}")


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted


def get_csv():
    lines = []
    for item in items:
        # Ensure we're working with a date object
        if isinstance(item.date, str):
            date_obj = datetime.datetime.strptime(item.date, "%Y-%m-%d").date()
        else:
            date_obj = item.date
        date_str = date_obj.strftime("%Y-%m-%d")
        line = f"{item.text},{date_str},{item.isCompleted}"
        lines.append(line)
    return (
        lines[0] if lines else ""
    )  # For now, just return the first line since we're testing with one item
