"""Tests for the ByteBites backend models.

Each test describes one externally observable behavior of the system
(what it should do from the outside), not how the code is written.
"""

import pytest

from models import FoodItem, Menu, Customer, Transaction


# --- Fixtures --------------------------------------------------------------
# Reusable sample items so each test reads clearly and stays isolated.

@pytest.fixture
def burger():
    return FoodItem("Spicy Burger", 10.00, "Mains", 4.5)


@pytest.fixture
def soda():
    return FoodItem("Large Soda", 5.00, "Drinks", 4.0)


@pytest.fixture
def cola():
    return FoodItem("Cola", 2.50, "Drinks", 3.9)


@pytest.fixture
def cake():
    return FoodItem("Choc Cake", 5.25, "Desserts", 4.8)


# --- Transaction totals (the "happy path") --------------------------------

def test_calculate_total_with_multiple_items(burger, soda):
    # A transaction with a $10 burger and a $5 soda should total $15.
    transaction = Transaction([burger, soda])
    assert transaction.compute_total() == 15.00


def test_order_total_is_zero_when_empty():
    # A transaction with no items should total $0, not crash.
    transaction = Transaction()
    assert transaction.compute_total() == 0.00


def test_total_updates_after_adding_item(burger, soda):
    # Adding an item to a transaction should increase the total by its price.
    transaction = Transaction([burger])
    transaction.add_item(soda)
    assert transaction.compute_total() == 15.00


def test_total_is_rounded_to_two_decimals():
    # Summing prices that drift in float math should round to a clean money value.
    transaction = Transaction([
        FoodItem("a", 0.10, "x", 1.0),
        FoodItem("b", 0.20, "x", 1.0),
    ])
    assert transaction.compute_total() == 0.30


# --- Menu filtering by category -------------------------------------------

def test_filter_returns_only_matching_category(soda, cola, burger):
    # Filtering by "Drinks" should return only the drink items, nothing else.
    menu = Menu([soda, cola, burger])
    assert menu.filter_by_category("Drinks") == [soda, cola]


def test_filter_is_case_insensitive(soda, cola):
    # Filtering should match regardless of the caller's casing.
    menu = Menu([soda, cola])
    assert menu.filter_by_category("drinks") == [soda, cola]


def test_filter_unknown_category_returns_empty(burger, soda):
    # Filtering by a category no item has should return an empty list.
    menu = Menu([burger, soda])
    assert menu.filter_by_category("Sushi") == []


# --- Customer verification -------------------------------------------------

def test_new_customer_is_not_a_real_user():
    # A customer with no purchase history is not yet a verified real user.
    customer = Customer("Ada")
    assert customer.is_real_user() is False


def test_customer_with_history_is_a_real_user(burger):
    # Once a customer has at least one transaction, they are a verified real user.
    customer = Customer("Ada")
    customer.add_transaction(Transaction([burger]))
    assert customer.is_real_user() is True
