# Assume that num is a string that is either an integer (like "1337") or not an integer (like "100.0" or "foo")
def validate_input(num):
    if (num.isdigit() == False):
        print("Number " + str(num) + " is not a digit. Please enter a valid integer larger than 0")
        return False
    elif (int(num) < 2):
        print("Number " + num + " may not be divided into prime factors. Please enter a valid integer larger than 1")
        return False
    else:
        return True

from math import sqrt
from itertools import count, islice

# Gets a list of prime factors for 'num'
# Assumes that num is an integer larger but not equal than 1
# If same prime factor occurs many time (such as 8 = 2*2*2), it will be included
# in the returned list as many times (in contrary to returning only unique prime factors)
def get_prime_factors(num):
    # Save a temporary variable
    # The idea is to "mine" factors from the original number,
    # then divide the original number with the found factors and continue iterating
    # until we have hitted the bottom
    numToCrunch = num

    # List of prime factors of given number to be returned
    factorList = []

    while numToCrunch > 1:

        # Check if number to crunch is already in database
        fac_in_db = dbhandler.find_factors_from_database(numToCrunch)
        if (fac_in_db != []):
            factorList += fac_in_db
            break
        
	# If number to crunch is a prime, quit! It has no other factors than 1 and itself
        imax = int(sqrt(numToCrunch) - 1)
        if (all(numToCrunch % z for z in islice(count(2), imax))):
            factorList.append(numToCrunch)
            break

	# Find prime factors of numToCrunch
        for i in islice(count(2), imax):

            # Check if i is a prime
            isprime = all(i % z for z in islice(count(2), int(sqrt(i) - 1)))
            if (isprime == False):
                continue

	    # Check if i divides numToCrunch

            if (numToCrunch % i == 0):
                # i is a prime factor of numToCrunch
                numToCrunch = int(numToCrunch / i)
                factorList.append(i)

    return factorList

import dbhandler
    
def main():
    
    # Take the number as user input; read inputs until got a valid input or interrupt
    num_ok = False
    while (num_ok == False):
        n = input("Enter a number to be factorized: ")
        num_ok = validate_input(n)

    from timeit import default_timer as timer

    start = timer()
    
    #prime_factors = dbhandler.find_factors_from_database(n)
    #if (prime_factors == []):
        # Did not find the factors from database
        # or there was no database. Better start crunching!
        
    num = int(n)
    prime_factors = get_prime_factors(num)

    # Finally, update the database with the new factors gotten
    dbhandler.add_to_database(n, prime_factors)


    print("Prime factors of " + n + " are: " + str(prime_factors))
            
    end = timer()
    print("Finding prime factors took %.3f" % (end - start) + " seconds")

    # In addition, output the results into a file
    file_out = open("prime_factors_out", "w")
    file_out.write("Prime factors of " + n + " are: " + str(prime_factors) + "\n")
    file_out.close()
    
# Not sure if this is cool but let's do it this way
main()
