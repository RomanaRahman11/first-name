has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("Eligible for loan 1")
if has_high_income or has_good_credit:
    print("Eligible for loan 2")

if has_good_credit and not has_criminal_record:
    print("Eligible for loan 3")
