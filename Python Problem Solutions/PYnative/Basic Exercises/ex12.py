def calculate_income_tax(income):
    """Calculates the income tax based on the given rules.

    Rules:
    - First $10,000: 0%
    - Next $10,000: 10%
    - The remaining: 20%
    """
    tax_payable = 0

    if income <=1000:
        # First $10,000 at 0%
        tax_payable = 0

    elif income <=20000:
        # First $10,000 at 0%, remaining at 10%
        taxable_at_10 = income - 10000
        tax_payable = taxable_at_10*0.10
    else:
        # First $10,000 at 0%
        # Next $10,000 ($10,001 to $20,000) at 10%
        tax_payable += 10000*0.10

        tax_payable_at_20 = income - 20000
        tax_payable += tax_payable_at_20*0.20

    return tax_payable

print(calculate_income_tax(45000))
