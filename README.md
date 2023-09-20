# qa_python

###### The file "tests.py"  contains tests to check the functionality from the file "main.py".
##### Command to run tests in terminal
###### pytest -v tests.py

### Tests "tests.py" to check the code in a file "main.py"
1. test_add_new_book_add_two_books - successfully adding a book title
2. test_add_new_book_three_books_successfully - successfully adding book titles with bounds checking
3. test_add_new_book_name_book_0_and_41_characters - checks that books with an empty title or books with more than$
4. test_set_book_genre_for_book_successfully - checks adding a genre for an existing book
5. test_set_book_genre_for_not_added_books - checks that the genre will not be added for a non-existent book
6. test_set_book_genre_no_genre_listed - checks that you cannot add a non-existent genre
7. test_get_book_genre_by_name - checks that the genre matches the book title
9. test_books_with_genre_comedy - checks that a list of books with a certain genre is displayed
10. test_get_books_genre_successfully - checks that all books and genres have been added
11. test_books_for_children_successfully - checks that books are suitable for children
12. test_books_for_children_age_restrictions - checks that books are not suitable for children
13. test_add_book_in_favorites_successfully - checks the book is added to favorites
