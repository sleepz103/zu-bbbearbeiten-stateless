import pytest
import helper
import datetime


def test_add():
    # Given: I want to add a to-do with a date
    text = "Lorem ipsum"
    date = "2023-09-02"

    # When: I add the item
    helper.add(text, date)

    # Then: The most recently added to-do should have a date
    item = helper.items[-1]
    assert isinstance(item.date, datetime.date)

def test_get_csv():
    # Given: I have a to-do item
    text = "Lorem ipsum"
    date = "2023-09-02"
    helper.add(text, date)

    # When: I get the CSV representation
    csv = helper.get_csv()

    # Then: Return string in CSV format
    assert csv == "Lorem ipsum,2023-09-02,False"
