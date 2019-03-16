import os

# Check if the factors of integer 'num' are in the database
# If the factors are found, return them
# If the factors are not found, return an empty list
# If there is no database, create one and return an empty list
def find_factors_from_database(num):
    # Check if file exists
    if (os.path.isfile("database") == False):
        # Create the file later; see function 'add_to_database'
        print("Did not find database. Creating new database")
        db_file = open("database", "w")
        db_file.close()
        return []

    # The database file format is: first column is the "key" or "number",
    # the columns after that are the prime factors of that number
    # elements in db are comma separated
    # NOTE: it was not required to put the elapsed time into database so we choose not to do it
    # as it would not be useful and anyway the run times depend on hardware...
    
    db_file = open("database", "r")
    for line in db_file:
        # Remove newline
        line = line.rstrip()
        elems = line.split(";")
        if (str(num) == elems[0]):
            # Remove the first element to return only factors
            elems.pop(0)
            db_file.close()
            # Use list comprehension to create list of strings into list of ints
            return [int(i) for i in elems]

    # If got here, the number was not in the database
    db_file.close()
    return []

# Add the newly found list of prime factors for number num to the database
def add_to_database(num, prime_factors):
    
    db_file = open("database", "a")
    db_file.write(str(num))
    for p in prime_factors:
        db_file.write(";" + str(p))
        
    db_file.write("\n")
    db_file.close()
