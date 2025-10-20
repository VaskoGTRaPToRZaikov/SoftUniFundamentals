shelf_with_books = input().split("&")

while True:
    command = input()

    if command == "Done":
        print(", ".join(shelf_with_books))
        break

    parts = command.split(" | ")
    action = parts[0]

    if action == "Add Book":
        book_name = parts[1]
        if book_name not in shelf_with_books:
            shelf_with_books.insert(0, book_name)

    elif action == "Take Book":
        book_name = parts[1]
        if book_name in shelf_with_books:
            shelf_with_books.remove(book_name)

    elif action == "Swap Books":
        book1 = parts[1]
        book2 = parts[2]
        if book1 in shelf_with_books and book2 in shelf_with_books:
            index_book1 = shelf_with_books.index(book1)
            index_book2 = shelf_with_books.index(book2)
            shelf_with_books[index_book1], shelf_with_books[index_book2] =\
                shelf_with_books[index_book2], shelf_with_books[index_book1]

    elif action == "Insert Book":
        book_name = parts[1]
        if book_name not in shelf_with_books:
            shelf_with_books.append(book_name)

    elif action == "Check Book":
        index = int(parts[1])
        if 0 <= index < len(shelf_with_books):
            print(shelf_with_books[index])