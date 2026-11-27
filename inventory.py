"""
CodeTrace debugging test: Shopping Cart System

Contains intentional bugs.
Run: python codetrace_cart_buggy.py
"""


def calculate_tax(subtotal):
    # BUG: Returns a fixed amount instead of calculating 10% tax.
    return 10


def validate_quantity(quantity):
    # BUG: Zero quantity should not be accepted.
    return quantity >= 0


def find_product(products, product_id):
    # BUG: Searches by product name instead of product ID.
    for product in products:
        if product["name"] == product_id:
            return product
    return None


def calculate_subtotal(cart):
    # BUG: Ignores item quantities.
    return sum(item["price"] for item in cart)


def calculate_shipping(subtotal):
    # BUG: Free shipping should apply at exactly 100 too.
    if subtotal > 100:
        return 0
    return 10


PRODUCTS = [
    {"id": 101, "name": "Keyboard", "price": 80},
    {"id": 102, "name": "Mouse", "price": 40},
    {"id": 103, "name": "Monitor", "price": 250},
]

CART = [
    {"id": 101, "name": "Keyboard", "price": 80, "quantity": 2},
    {"id": 102, "name": "Mouse", "price": 40, "quantity": 1},
]


def run_checks():
    checks = [
        ("Tax on 100 should be 10",
         lambda: calculate_tax(100) == 10),

        ("Zero quantity should be invalid",
         lambda: validate_quantity(0) is False),

        ("Product ID 102 should find Mouse",
         lambda: find_product(PRODUCTS, 102) == PRODUCTS[1]),

        ("Cart subtotal should be 200",
         lambda: calculate_subtotal(CART) == 200),

        ("Subtotal of exactly 100 should get free shipping",
         lambda: calculate_shipping(100) == 0),
    ]

    passed = 0
    failed = 0

    print("CodeTrace Shopping Cart Test")
    print("=" * 40)

    for description, test in checks:
        try:
            result = test()

            if result:
                print(f"PASS: {description}")
                passed += 1
            else:
                print(f"FAIL: {description}")
                failed += 1

        except Exception as error:
            print(f"ERROR: {description}: {error}")
            failed += 1

    print("=" * 40)
    print(f"Total: {len(checks)} | Passed: {passed} | Failed: {failed}")


if __name__ == "__main__":
    run_checks()
