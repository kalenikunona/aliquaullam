def handle_column(column):
    switch = {
        'ColTitle': lambda: print("Handling title column"),
        'ColAuthor': lambda: print("Handling author column"),
        'ColYear': lambda: print("Handling year column"),
    }
    # Call the function associated with the column, or handle unknown columns
    switch.get(column, lambda: print("Unknown column type"))()

handle_column('ColTitle')
handle_column('ColAuthor')
handle_column('ColYear')
handle_column('UnknownColumn')
