from datetime import datetime

date_format= "%d-%m-%Y"
CATEGORIES={"I": "Income","E":"Expense"}

def get_date(prompt, allow_default=False):
    date_str= input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime("%d-%m-%Y")
    
    try:
        valid_date= datetime.strptime(date_str,"%d-%m-%Y")
        return valid_date.strftime("%d-%m-%Y")
    
    except ValueError:
        print("Invalid date format. Please enter the data in 'dd-mm-yyyy' format")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount= float(input("Enter the amount"))
        if amount<=0:
           raise ValueError("Amount must be a non-nagative non-zerovalue")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    category= input("Enter the category (I for income or E for expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    print("Invalid category. Please enter 'I' for income or 'E' for expense. ")
    return get_category()

def get_description():
    return input("Enter a description(optional):")