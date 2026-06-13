# ByteBites — Data Models
#
# Summary of the four core classes (see bytebites_design.md for the full UML):
#
# Customer    - Holds a customer's name and their past purchase history;
#               can confirm a "real" user via prior transactions (is_real_user).
# FoodItem    - A single sellable item: name, price, category, popularity rating.
# Menu        - Holds the catalog of FoodItems; supports filtering by category.
# Transaction - Groups the FoodItems a customer selected into one purchase
#               and computes the total cost.

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class FoodItem:
    """A single sellable item: name, price, category, and popularity rating."""

    name: str
    price: float
    category: str
    popularity_rating: float


class Customer:
    """Holds a customer's name and their past purchase history."""

    def __init__(self, name: str,
                 purchase_history: list[Transaction] | None = None) -> None:
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []

    def get_name(self) -> str:
        return self.name

    def get_purchase_history(self) -> list[Transaction]:
        return self.purchase_history

    def add_transaction(self, transaction: Transaction) -> None:
        self.purchase_history.append(transaction)

    def is_real_user(self) -> bool:
        """A "real" user is verified by having at least one past transaction."""
        return len(self.purchase_history) > 0

    def __repr__(self) -> str:
        return f"Customer(name={self.name!r}, purchase_history={self.purchase_history!r})"


class Menu:
    """Holds the full catalog of FoodItems; supports filtering by category."""

    def __init__(self, items: list[FoodItem] | None = None) -> None:
        self.items = items if items is not None else []

    def add_item(self, item: FoodItem) -> None:
        self.items.append(item)

    def remove_item(self, item: FoodItem) -> None:
        self.items.remove(item)

    def get_items(self) -> list[FoodItem]:
        return self.items

    def filter_by_category(self, category: str) -> list[FoodItem]:
        target = category.lower()
        return [item for item in self.items if item.category.lower() == target]

    def __repr__(self) -> str:
        return f"Menu(items={self.items!r})"


class Transaction:
    """Groups the FoodItems a customer selected and computes the total cost."""

    def __init__(self, selected_items: list[FoodItem] | None = None) -> None:
        self.selected_items = selected_items if selected_items is not None else []

    def add_item(self, item: FoodItem) -> None:
        self.selected_items.append(item)

    def get_items(self) -> list[FoodItem]:
        return self.selected_items

    def compute_total(self) -> float:
        return round(sum(item.price for item in self.selected_items), 2)

    def __repr__(self) -> str:
        return f"Transaction(selected_items={self.selected_items!r})"
