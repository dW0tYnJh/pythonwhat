import os
import unittest

from os.path import exists
from unittest.mock import patch

from pythonbackend.Exercise import Exercise
from pythonbackend import utils

import helper

class TestFunctionBase(unittest.TestCase):

  def setUp(self):
    self.data = {
      "DC_PEC": '''
# pec comes here
      ''',
      "DC_CODE": '''
print(5 / 8)
print(7 + 10)
      ''',
      "DC_SOLUTION": '''
print(5 / 8)
print(7 + 10)
'''
    }

  def test_Pass(self):
    self.data["DC_SCT"] = '''
msg = "Don't remove the first statement. It is an example which is coded for you!"
test_operator(1, incorrect_op_msg = msg, incorrect_result_msg = msg, not_found_msg = msg)
test_operator(2, not_found_msg = "You should add a second operation, as instructed.",
  incorrect_op_msg = "Your second operation is wrong, be sure to add `7` to `10`.",
  incorrect_result_msg = "The operation you added should add up to `17`.")
test_function("print", 1)
test_function("print", 2)

success_msg("Great!")
    '''
    self.exercise = Exercise(self.data)
    self.exercise.runInit()
    output = self.exercise.runSubmit(self.data)
    sct_payload = helper.get_sct_payload(output)
    self.assertEqual(sct_payload['correct'], True)
    self.assertEqual(sct_payload['message'], "Great!")

class TestFunctionExerciseNumpy(unittest.TestCase):

  def setUp(self):
    self.data = {
      "DC_PEC": '''
# pec comes here
      ''',
      "DC_CODE": '''
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
      ''',
      "DC_SOLUTION": '''
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
'''
    }

  def test_Pass(self):
    self.data["DC_SCT"] = '''
msg = "You don't have to change or remove the predefined variables."
test_object("baseball", undefined_msg = msg, incorrect_msg = msg)

test_import("numpy", same_as = False)

test_object("np_baseball", do_eval = False)
test_function("numpy.array", not_called_msg = "Be sure to call [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array).",
                             incorrect_msg = "You should call `np.array(baseball)` to make a 2D numpy array out of `baseball`.")
test_object("np_baseball", incorrect_msg = "Assign the correct value to `np_baseball`.")

msg = "Make sure to print out the type of `np_baseball` like this: `print(type(np_baseball))`."
test_function("type", 1, incorrect_msg = msg)
test_function("print", 1, incorrect_msg = msg)

test_function("print", 2, incorrect_msg = "You can print the shape of `np_baseball` like this: `np_baseball.shape`.")

success_msg("Great! You're ready to convert the actual MLB data to a 2D Numpy array now!")
    '''
    self.exercise = Exercise(self.data)
    self.exercise.runInit()
    output = self.exercise.runSubmit(self.data)
    sct_payload = helper.get_sct_payload(output)
    self.assertEqual(sct_payload['correct'], True)
    self.assertEqual(sct_payload['message'], "Great! You're ready to convert the actual MLB data to a 2D Numpy array now!")

class TestFunctionImporting(unittest.TestCase):

  def setUp(self):
    self.data = {
      "DC_PEC": '''
# pec comes here
      ''',
      "DC_CODE": '''
# Open a file
file = open('moby_dick.txt' , 'r') # 'r' is to read only.

# Print it
print(file.read())

# Check whether file is closed
print(file.close)

# Close file
file.close()

# Check whether file is closed
print(file.closed)
      ''',
      "DC_SOLUTION": '''
# Open a file
file = open('moby_dick.txt' , 'r') # 'r' is to read only.

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)
'''
    }

  def test_Fail(self):
    self.data["DC_SCT"] = '''
test_function("open", incorrect_msg = "Pass the correct arguments to `open()`" )
file_read_msg = "Make sure to print out the contents of the file like this: `print(file.read())`."
test_function("file.read", incorrect_msg = file_read_msg)
test_function("print", 1, args = [], incorrect_msg = file_read_msg)
file_closed_msg = "Make sure to call `print()` the attribute `file.closed` twice, once before you closed the `file` and once after."
test_function("print", 2, incorrect_msg = file_closed_msg)
test_function("print", 3, incorrect_msg = file_closed_msg)
test_expression_output(incorrect_msg = file_read_msg)
test_function("file.close", not_called_msg = "Make sure to close the file, man!")
success_msg("Good job!")
    '''
    self.exercise = Exercise(self.data)
    self.exercise.runInit()
    output = self.exercise.runSubmit(self.data)
    sct_payload = helper.get_sct_payload(output)
    self.assertEqual(sct_payload['correct'], False)
    self.assertEqual(sct_payload['message'], "Make sure to call <code>print()</code> the attribute <code>file.closed</code> twice, once before you closed the <code>file</code> and once after.")


class TestTestFunctionInWith(unittest.TestCase):

  def setUp(self):
    self.data = {
      "DC_PEC": '''
# pec comes here
      ''',
      "DC_CODE": '''
# Import pickle package
import pickle

# Open pickle file and load data
with open('data.p','rb') as file:
    d = pickle.load(file)

# Print data
print(d)

# Print datatype
print(type(d))
      ''',
      "DC_SOLUTION": '''
# Import pickle package
import pickle

# Open pickle file and load data
with open('data.p','rb') as file:
    d = pickle.load(file)

# Print data
print(d)

# Print datatype
print(type(d))
'''
    }

  def test_Pass(self):
    self.data["DC_SCT"] = '''
# Test: import pickle package
import_msg = "Did you import `pickle` correctly?"
test_import("pickle", same_as = True, not_imported_msg = import_msg, incorrect_as_msg = import_msg)

# For testing statements inside with statement
def test_with_body():
    test_object("d")
    test_function("pickle.load", do_eval = False)

# Test: Context manager
test_with(
    1,
    context_vals = True,
    context_tests = lambda: test_function("open"),
    body = test_with_body
)

# Test: print() statement
test_function("print", index = 0)

# Test: print() statement and call to type()
type_msg = "Print out the type of `d` as follows: `print(type(d))`."
test_function("type", index = 0, incorrect_msg = type_msg)
test_function("print", index = 1, incorrect_msg = type_msg)

success_msg("Awesome!")
    '''
    self.exercise = Exercise(self.data)
    self.exercise.runInit()
    output = self.exercise.runSubmit(self.data)
    sct_payload = helper.get_sct_payload(output)
    self.assertEqual(sct_payload['correct'], True)

  def test_Fail(self):
    self.data["DC_CODE"] = '''
# Import pickle package
import pickle

# Open pickle file and load data
with open('data.p','rb') as file:
    d = pickle.load('something_else')

# Print data
print(d)

# Print datatype
print(type(d))
      '''
    self.data["DC_SCT"] = '''
# Test: import pickle package
import_msg = "Did you import `pickle` correctly?"
test_import("pickle", same_as = True, not_imported_msg = import_msg, incorrect_as_msg = import_msg)

# For testing statements inside with statement
def test_with_body():
    test_function("pickle.load", do_eval = False)
    test_object("d")

# Test: Context manager
test_with(
    1,
    context_vals = True,
    context_tests = lambda: test_function("open"),
    body = test_with_body
)

# Test: print() statement
test_function("print", index = 0)

# Test: print() statement and call to type()
type_msg = "Print out the type of `d` as follows: `print(type(d))`."
test_function("type", index = 0, incorrect_msg = type_msg)
test_function("print", index = 1, incorrect_msg = type_msg)

success_msg("Awesome!")
    '''
    self.exercise = Exercise(self.data)
    self.exercise.runInit()
    output = self.exercise.runSubmit(self.data)
    sct_payload = helper.get_sct_payload(output)
    self.assertEqual(sct_payload['correct'], False)
    self.assertEqual(sct_payload['message'], 'Check the body of the <code>with</code> statement on line 6. Did you call <code>pickle.load()</code> with the correct arguments? Call on line 7 has wrong arguments. The 1st argument seems to be incorrect.')

class TestTestFunctionAndTestCorrectInWith(unittest.TestCase):
  def setUp(self):
    self.data = {
      "DC_PEC": '''
# pec comes here
      ''',
      "DC_CODE": '''
# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type that we have created
print(type(mat))
      ''',
      "DC_SOLUTION": '''
# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type that we have created
print(type(mat))
'''
    }

  def test_Pass(self):
    self.data["DC_SCT"] = '''
# Test: import scipy.io
test_import("scipy.io", same_as = True)

# Test: call to scipy.io.loadmat() and 'mat' variable
test_correct(
    lambda: test_object("mat"),
    lambda: test_function("scipy.io.loadmat", do_eval = False)
)

# Test: print() statement and call to type()
type_msg = "Print out the type of `mat` as follows: `print(type(mat))`."
test_function("type", incorrect_msg = type_msg)
test_function("print", incorrect_msg = type_msg)

success_msg("Great job!")
    '''
    self.exercise = Exercise(self.data)
    self.exercise.runInit()
    output = self.exercise.runSubmit(self.data)
    sct_payload = helper.get_sct_payload(output)
    self.assertEqual(sct_payload['correct'], True)

  def test_Fail(self):
    self.data["DC_CODE"] = '''
# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('test')

# Print the datatype type that we have created
print(type(mat))
      '''
    self.data["DC_SCT"] = '''
# Test: import scipy.io
# test_import("scipy.io", same_as = True)

# Test: call to scipy.io.loadmat() and 'mat' variable
test_correct(
    lambda: test_object("mat"),
    lambda: test_function("scipy.io.loadmat", do_eval = False)
)

# Test: print() statement and call to type()
type_msg = "Print out the type of `mat` as follows: `print(type(mat))`."
test_function("type", incorrect_msg = type_msg)
test_function("print", incorrect_msg = type_msg)

success_msg("Great job!")
    '''
    self.exercise = Exercise(self.data)
    self.exercise.runInit()
    output = self.exercise.runSubmit(self.data)
    sct_payload = helper.get_sct_payload(output)
    self.assertEqual(sct_payload['correct'], False)
    self.assertEqual(sct_payload['message'], 'Did you call <code>scipy.io.loadmat()</code> with the correct arguments? Call on line 6 has wrong arguments. The 1st argument seems to be incorrect.')

class TestTestFunctionAndTestCorrectWithoutWith(unittest.TestCase):
  def setUp(self):
    self.data = {
      "DC_PEC": '''
# pec comes here
      ''',
      "DC_CODE": '''
# Import package
import tweepy

# Store OAuth authentication credentials in relevant variables
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
      ''',
      "DC_SOLUTION": '''
# Import package
import tweepy

# Store OAuth authentication credentials in relevant variables
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
'''
    }

  def test_Pass(self):
    self.data["DC_SCT"] = '''
# Test: import tweepy
import_msg = "Did you correctly import the required package?"
test_import("tweepy", same_as = True, not_imported_msg = import_msg, incorrect_as_msg = import_msg)

# Test: Predefined code
predef_msg = "You don't have to change any of the predefined code."
test_object("access_token", undefined_msg = predef_msg, incorrect_msg = predef_msg)
test_object("access_token_secret", undefined_msg = predef_msg, incorrect_msg = predef_msg)
test_object("consumer_key", undefined_msg = predef_msg, incorrect_msg = predef_msg)
test_object("consumer_secret", undefined_msg = predef_msg, incorrect_msg = predef_msg)

# Test: call to tweepy.OAuthHandler() and 'auth' variable
test_object("auth", do_eval = False)
test_function("tweepy.OAuthHandler")

# Test: call to auth.set_access_token()
test_function("auth.set_access_token")

success_msg("Awesome!")
    '''
    self.exercise = Exercise(self.data)
    self.exercise.runInit()
    output = self.exercise.runSubmit(self.data)
    sct_payload = helper.get_sct_payload(output)
    self.assertEqual(sct_payload['correct'], True)


if __name__ == "__main__":
    unittest.main()
