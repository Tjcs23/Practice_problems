"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
"""
Recipe's base baketime
"""


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(bake_time):
    """Calculate the bake time remaining.
        constant expected bake time minus current bake time. 
    """
    print(bake_time_remaining.__doc__)
    return EXPECTED_BAKE_TIME - bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.

def preparation_time_in_minutes(number_of_layers):
    """
    every layer is two minutes of prep time.
    this function returns the total prep time.
    """
    print(preparation_time_in_minutes.__doc__)
    return 2 * number_of_layers

#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    This function gets prep time and adds to elapsed bake time for the total time elapsed cooking.
    """
    
    sum_mins = (number_of_layers * 2) + elapsed_bake_time
    return sum_mins



# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
