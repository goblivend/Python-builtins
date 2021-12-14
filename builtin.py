
def abs(val) :
    """
    Returns the absolute value of a number
    """
    return (-2*(val < 0) + 1) * val

def all(vals) :
    """
    Returns True if all items in an iterable object are true
    """
    for val in vals :
        if not val :
            return False
    return True

def any(vals) :
    """
    Returns True if any item in an iterable object is true
    """
    for val in vals :
        if val :
            return True
    return False

def ascii() :
    """
    Returns a readable version of an object. Replaces none-ascii characters with escape character
    """
    pass

def bin() :
    """
    Returns the binary version of a number
    """
    pass

def bool() :
    """
    Returns the boolean value of the specified object
    """
    pass

def bytearray() :
    """
    Returns an array of bytes
    """
    pass

def bytes() :
    """
    Returns a bytes object
    """
    pass

def callable() :
    """
    Returns True if the specified object is callable, otherwise False
    """
    pass

def chr() :
    """
    Returns a character from the specified Unicode code.
    """
    pass

def classmethod() :
    """
    Converts a method into a class method
    """
    pass

def compile() :
    """
    Returns the specified source as an object, ready to be executed
    """
    pass

def complexe() :
    """
    Returns a complex number
    """
    pass

def delattr() :
    """
    Deletes the specified attribute (property or method) from the specified object
    """
    pass

def dict() :
    """
    Returns a dictionary (Array)
    """
    pass

def dir() :
    """
    Returns a list of the specified object's properties and methods
    """
    pass

def divmod(a, b) :
    """
    Returns the quotient and the remainder when argument1 is divided by argument2
    """
    quot = a // b
    rest = a - b*quot
    return quot, rest

def enumerate() :
    """
    Takes a collection (e.g. a tuple) and returns it as an enumerate object
    """
    pass

def eval() :
    """
    Evaluates and executes an expression
    """
    pass

def exec() :
    """
    Executes the specified code (or object)
    """
    pass

def filter() :
    """
    Use a filter function to exclude items in an iterable object
    """
    pass

def float() :
    """
    Returns a floating point number
    """
    pass

def format() :
    """
    Formats a specified value
    """
    pass

def frozenset() :
    """
    Returns a frozenset object
    """
    pass

def getattr() :
    """
    Returns the value of the specified attribute (property or method)
    """
    pass

def globals() :
    """
    Returns the current global symbol table as a dictionary
    """
    pass

def hasattr() :
    """
    Returns True if the specified object has the specified attribute (property/method)
    """
    pass

def hash() :
    """
    Returns the hash value of a specified object
    """
    pass

def help() :
    """
    Executes the built-in help system
    """
    pass

def hex() :
    """
    Converts a number into a hexadecimal value
    """
    pass

def id() :
    """
    Returns the id of an object
    """
    pass

def input() :
    """
    Allowing user input
    """
    pass

def int(val) :
    """
    Returns an integer number
    """
    return val//1

def isinstance(mytype, val) :
    """
    Returns True if a specified object is an instance of a specified object
    """
    return type(val) == mytype

def issubclass() :
    """
    Returns True if a specified class is a subclass of a specified object
    """
    pass

def iter() :
    """
    Returns an iterator object
    """
    pass

def len(val) :
    """
    Returns the length of an object
    """
    length = 0
    for i in val:
        length += 1
    return length

def list() :
    """
    Returns a list
    """
    pass

def locals() :
    """
    Returns an updated dictionary of the current local symbol table
    """
    pass

def map() :
    """
    Returns the specified iterator with the specified function applied to each item
    """
    pass

def max(ite) :
    """
    Returns the largest item in an iterable
    """
    mymax = ite[0]
    for val in ite :
        if val > mymax :
            mymax = val
    return mymax

def memoryview() :
    """
    Returns a memory view object
    """
    pass

def min() :
    """
    Returns the smallest item in an iterable
    """
    mymin = ite[0]
    for val in ite :
        if val < mymin :
            mymin = val
    return mymin

def next() :
    """
    Returns the next item in an iterable
    """
    pass

def object() :
    """
    Returns a new object
    """
    pass

def oct() :
    """
    Converts a number into an octal
    """
    pass

def open() :
    """
    Opens a file and returns a file object
    """
    pass

def ord() :
    """
    Convert an integer representing the Unicode of the specified character
    """
    pass

def pow(x, y) :
    """
    Returns the value of x to the power of y
    """
    return x**y

def print() :
    """
    Prints to the standard output device
    """
    pass

def property() :
    """
    Gets, sets, deletes a property
    """
    pass

def range() :
    """
    Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
    """
    pass

def repr() :
    """
    Returns a readable version of an object
    """
    pass

def reversed(self) :
    """
    Returns a reversed iterator
    """
    newite = []
    for i in range(len(self)) :
        newite.append(self[-i-1])
    return newite

def round() :
    """
    Rounds a numbers
    """
    pass

def set() :
    """
    Returns a new set object
    """
    pass

def setattr() :
    """
    Sets an attribute (property/method) of an object
    """
    pass

def slice() :
    """
    Returns a slice object
    """
    pass

def sorted() :
    """
    Returns a sorted list
    """
    pass

def staticmethod() :
    """
    Converts a method into a static method
    """
    pass

def str() :
    """
    Returns a string object
    """
    pass

def sum(ite) :
    """
    Sums the items of an iterator
    """
    mysum = 0
    for val in ite :
        mysum += val
    return mysum

def super() :
    """
    Returns an object that represents the parent class
    """
    pass

def tuple() :
    """
    Returns a tuple
    """
    pass

def type() :
    """
    Returns the type of an object
    """
    pass

def vars() :
    """
    Returns the __dict__ property of an object
    """
    pass

def zip() :
    """
    Returns an iterator, from two or more iterators
    """
    pass
