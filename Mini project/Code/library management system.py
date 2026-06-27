library = {}

while True:
    print("\n=== LIBRARY MANAGEMENT SYSTEM ===")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search")
    print("5. View Catalog")
    print("6. Exit")
    
    choice = input("Enter choice (1-6): ")

    if choice == '1':
        isbn = input("Enter ISBN: ")
        if isbn in library:
            print("Book with this ISBN already exists!")
        else:
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            # Default state: Available is True, no borrower
            library[isbn] = {'title': title, 'author': author, 'available': True, 'borrower': ''}
            print("Book added successfully!")

    elif choice == '2':
        isbn = input("Enter ISBN to issue: ")
        # Check if book exists
        if isbn in library:
            # Check availability
            if library[isbn]['available'] == True:
                borrower = input("Enter Borrower Name: ")
                library[isbn]['available'] = False
                library[isbn]['borrower'] = borrower
                print("Book issued successfully!")
            else:
                print("Book is already issued to {}.".format(library[isbn]['borrower']))
        else:
            print("Book not found.")

    elif choice == '3':
        isbn = input("Enter ISBN to return: ")
        if isbn in library:
            if library[isbn]['available'] == False:
                library[isbn]['available'] = True
                library[isbn]['borrower'] = ''
                print("Book returned successfully!")
            else:
                print("Book is already available in the library.")
        else:
            print("Book not found.")

    elif choice == '4':
        keyword = input("Enter title or author to search: ").lower()
        found = False
        for isbn, details in library.items():
            # Check if keyword matches title or author (ignoring case)
            if keyword in details['title'].lower() or keyword in details['author'].lower():
                print("Found: {} by {} (ISBN: {})".format(details['title'], details['author'], isbn))
                found = True
        
        if not found:
            print("No matching books found.")

    elif choice == '5':
        print("\n--- Full Library Catalog ---")
        if not library:
            print("The catalog is empty.")
        else:
            for isbn, details in library.items():
                if details['available']:
                    status = "Available"
                else:
                    status = "Issued to {}".format(details['borrower'])
                    
                print("ISBN: {} | Title: {} | Author: {} | Status: {}".format(isbn, details['title'], details['author'], status))

    elif choice == '6':
        print("Exiting Library System. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
