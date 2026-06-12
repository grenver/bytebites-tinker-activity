# ByteBites — UML Class Diagram

```mermaid
classDiagram
    class Customer {
        -String name
        -List~Transaction~ purchaseHistory
        +isRealUser() bool
        +addTransaction(Transaction t) void
    }

    class FoodItem {
        -String name
        -double price
        -String category
        -double popularityRating
    }

    class Menu {
        -List~FoodItem~ items
        +addItem(FoodItem item) void
        +filterByCategory(String category) List~FoodItem~
    }

    class Transaction {
        -List~FoodItem~ selectedItems
        -Customer customer
        +computeTotal() double
        +addItem(FoodItem item) void
    }

    Menu "1" o-- "*" FoodItem : holds
    Transaction "1" *-- "*" FoodItem : contains
    Customer "1" --> "*" Transaction : purchaseHistory
    Transaction "*" --> "1" Customer : belongs to
```

## Class Responsibilities

| Class | Attributes (from spec) | Key behavior |
|-------|------------------------|--------------|
| **Customer** | `name`, `purchaseHistory` | Verify they're a real user (via purchase history) |
| **FoodItem** | `name`, `price`, `category`, `popularityRating` | Pure data holder |
| **Menu** | `items` (full collection) | Filter by category ("Drinks", "Desserts") |
| **Transaction** | `selectedItems`, `customer` | Compute total cost |

## Relationship Notes

- `Menu o-- FoodItem` (**aggregation**) — the menu holds items, but items can exist independently of any one menu.
- `Transaction *-- FoodItem` (**composition**) — a transaction groups the picked items; could be aggregation if items are shared references.
- `Customer --> Transaction` — the purchase history is a one-to-many link used for verification.
