# PrimeFactorizer
## Python Programming Exam for Vala Group

The solution for the task to find the prime factors of a given number by Eljas Hyyrynen.

The code was implemented, tested and documented in 3 hours. It was made using Python 3.7.2

### Features:
- Ask the user a number `>= 2` as an input, validate the input
- Find prime factors for the input
- Output the prime factors into a file `prime_factors_out`
- Save the prime factors into a database file `database`
- If the input or any its factors occur in the database, return the result immediately without calculating the factors from scratch ("early exit")
- Print the factors into the console

### Not implemented, "nice to have"
- Some other UI than console
- Use state-of-the-art algorithms such as Miller-Rabin for prime checks or Pollard's rho for integer factorization
- Automated tests
- Find out if it is faster to look up the prime from database or do prime check from scratch (depends on whether the number is big or small!)
- Performance profiler - if it is necessary
- Use different algorithms based on the number scale for maximum perf

### Known bugs:
- If the user inputs `num=`, for example `1337=`, the program crashes to a ValueError when casting to int

### Tests done:
- Checked if the program is able to parse invalid user inputs
- Checked if the program is able to create the db from scratch
- Checked with known factors if the results are sane (this is very easy to automate)
- Tested with "big numbers": 1e12 tier number that wasn't in the db (and any if its factors wasn't in the db either) took 10 seconds
- Tested that the program makes an output file
- Tested that the program writes output into the console as well

### Usage:
- Install Python 3.7
(https://www.python.org/downloads/)

- Run prime_factors.py
`python3 prime_factors.py`

- Input your number
- ???
- PROFIT

### Database format:

The database will hold the number and its factor in the following format:

`number;factor1;factor2;...;factorn`

For example:

`9039207968;2;2;2;2;2;7;7;7;7;7;7;7;7;7;7`
