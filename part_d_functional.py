from part_c_procedural import expenses


def get_total_functional(expense_list):
    """Calculate total using sum() and a generator expression."""
    return sum(e["amount"] for e in expense_list)


def get_category_totals_functional(expense_list):
    """
    Build the category to total mapping using a dict comprehension
    and a generator expression.
    """
    categories = {e["category"] for e in expense_list}
    return {
        category: sum(e["amount"] for e in expense_list if e["category"] == category)
        for category in categories
    }


def get_above_average_functional(expense_list):
    """
    Return expenses above the average amount using filter() and lambda.
    """
    average = get_total_functional(expense_list) / len(expense_list)
    return list(filter(lambda e: e["amount"] > average, expense_list))


def format_expenses(expense_list):
    """
    Return formatted strings for each expense using map() and lambda.
    """
    return list(
        map(
            lambda e: f"{e['date']} | {e['category']:<13} | {e['description']:<22} | ${e['amount']:.2f}",
            expense_list,
        )
    )


if __name__ == "__main__":
    from part_c_procedural import (
        get_total, get_category_totals, get_above_average
    )

    assert round(get_total_functional(expenses), 2) == round(get_total(expenses), 2), \
        "D1 total mismatch"

    assert get_category_totals_functional(expenses) == get_category_totals(expenses), \
        "D2 category totals mismatch"

    proc_ids = {id(e) for e in get_above_average(expenses)}
    func_ids = {id(e) for e in get_above_average_functional(expenses)}
    assert proc_ids == func_ids, "D3 above-average mismatch"

    print("All assertions passed.")
    print("\nFormatted expenses:")
    for line in format_expenses(expenses):
        print(line)
