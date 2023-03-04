# AirBnB clone - The console

This repository contains the console from a lite clone of AirBnB, the console is complete and will be merged with the website on next stages, it specifies classes for <b>User</b>, <b>State</b>, <b>City</b>, <b>Amenity</b> and <b>Review</b>; all of them inherit from the <b>BaseModel</b> class.

## Requirements

* This console requires Python 3.4 or later.

## Usage in interactive mode

* This program automatically displays a prompt for the user after first command is executed:

        $ ./console.py

        (hbnb) quit

        $

## Usage in non-interactive mode

* The same commands can be used to run non-interactive mode with some modifications will produce the same results as above:

        $ echo "create City" | ./console.py

        (hbnb) ed1101f4-1a64-4dba-afd6-5fd19ed7c137

        $

## known bugs

* There are not any known bugs at the moment.

## Flowchart

<img src=""/>

### Test

* This time we are using the Python <a href="https://docs.python.org/3.4/library/unittest.html">Unittest module</a>.
 - We are running all tests individually.

        python3 -m unittest tests/test_models/test_base_model.py
        ....
        ----------------------------------------------------------------------
        Ran 4 tests in 0.001s

        OK

## Examples

* 

## Authors

@Jagucan

- https://github.com/Jagucan

@YeosCRN

- https://github.com/YeosCRN
