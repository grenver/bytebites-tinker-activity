# ByteBites — Data Models
#
# Summary of the four core classes (see bytebites_design.md for the full UML):
#
# Customer    - Holds a customer's name and their past purchase history;
#               can confirm a "real" user via prior transactions (isReturning).
# FoodItem    - A single sellable item: name, price, category, popularity rating.
# Menu        - Holds the catalog of FoodItems; supports filtering by category.
# Transaction - Groups the FoodItems a customer selected into one purchase
#               and computes the total cost.
