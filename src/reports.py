
def total_expense(expenses):
    return sum(e.amount for e in expenses)


def category_summary(expenses):
    summary = {}
    for e in expenses:
        category = e.category.lower().strip()
        summary[category] = summary.get(category, 0) + e.amount
    return summary


