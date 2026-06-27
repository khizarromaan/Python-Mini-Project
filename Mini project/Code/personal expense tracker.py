
expenses = []
monthly_budget = 0.0

while True:
    print("\n====== PERSONAL EXPENSE TRACKER ======")
    print("Current Budget: Rs. {:.2f}".format(monthly_budget))
    print("1. Set Budget       2. Add Expense")
    print("3. View All         4. Budget & Category Report")
    print("5. Exit")
    
    choice = input("Choice (1-5): ")

    if choice == '1':
        try:
            monthly_budget = float(input("Enter new monthly budget: "))
            print("Budget set successfully!")
        except ValueError:
            print("Invalid input!")

    elif choice == '2':
        try:
            desc = input("Enter Description: ")
            category = input("Enter Category (Food/Travel/Bills/Other): ")
            amount = float(input("Enter Amount: "))
            if amount <= 0:
                print("Amount must be greater than zero!")
            else:
                date = input("Enter Date (DD-MM-YYYY): ")
                expenses.append({'desc': desc, 'category': category, 'amount': amount, 'date': date})
                print("Expense added successfully!")
        except ValueError:
            print("Invalid amount!")

    elif choice == '3':
        print("\n--- All Expenses ---")
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("{:<4} | {:<12} | {:<15} | {:<10} | {}".format('No.', 'Date', 'Description', 'Category', 'Amount'))
            for i in range(len(expenses)):
                e = expenses[i]
                print("{:<4} | {:<12} | {:<15} | {:<10} | Rs. {:.2f}".format(i+1, e['date'], e['desc'], e['category'], e['amount']))

    elif choice == '4':
        if not expenses:
            print("No data to generate report.")
        else:
            category_totals = {}
            total_spent = 0.0
            
            for e in expenses:
                cat = e['category']
                amt = e['amount']
                total_spent += amt
                if cat in category_totals:
                    category_totals[cat] += amt
                else:
                    category_totals[cat] = amt
            
            print("\n=== CATEGORY SUMMARY ===")
            top_category = ""
            max_spent = 0.0
            for cat, total in category_totals.items():
                print("{}: Rs. {:.2f}".format(cat, total))
                if total > max_spent:
                    max_spent = total
                    top_category = cat
            print("\nTop Spending Category: {} (Rs. {:.2f})".format(top_category, max_spent))
            
            print("\n=== BUDGET REPORT ===")
            print("Total Spent   : Rs. {:.2f}".format(total_spent))
            print("Budget Limit  : Rs. {:.2f}".format(monthly_budget))
            
            if monthly_budget > 0:
                remaining = monthly_budget - total_spent
                percent = (total_spent / monthly_budget) * 100
                print("Remaining     : Rs. {:.2f}".format(remaining))
                print("Used          : {:.2f}%".format(percent))
                
                if percent > 100:
                    print("! WARNING: You have EXCEEDED your budget !")
                elif percent >= 80:
                    print("! WARNING: You have used 80% or more of your budget !")

    elif choice == '5':
        print("Exiting...")
        break
