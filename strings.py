def capitalize(self) :
    """
    Converts the first character to upper case
    """
    self[0] = self[0].upper()

def casefold(self) :
    """
	Converts string into lower case
    """
    "".join(c.lower() for c in self)

def center():
    """
    Returns a centered string
    """
    pass

def count(self, value):
    """
    Returns the number of times a specified value occurs in a string
    """
    times = 0
    i = 0
    valLen = len(value)
    maxI = len(self) + valLen
    while(i < maxI) :
        times += self[i:i+valLen] == value
        i += 1
    return times

def encode():
    """
    Returns an encoded version of the string
    """
    pass

def endswith(self, value):
    """
    Returns true if the string ends with the specified value
    """
    return self[-len(value):] == value

def expandtabs():
    """
    Sets the tab size of the string
    """
    pass

def find(self, value):
    """
    Searches the string for a specified value and returns the position of where it was found
    """
    i = 0
    valLen = len(value)
    maxI = len(self) + valLen
    while(i < maxI) :
        if self[i:i+valLen] == value :
            return i
        i += 1
    raise Exception("The value is not included in the string")

def format():
    """
    Formats specified values in a string
    """
    pass

def format_map():
    """
    Formats specified values in a string
    """
    pass

def index():
    """
    Searches the string for a specified value and returns the position of where it was found
    """
    i = 0
    valLen = len(value)
    maxI = len(self) + valLen
    while(i < maxI) :
        if self[i:i+valLen] == value :
            return i
        i += 1
    raise Exception("The value is not included in the string")

def isalnum():
    """
    Returns True if all characters in the string are alphanumeric
    """
    pass

def isalpha():
    """
    Returns True if all characters in the string are in the alphabet
    """
    pass

def isascii():
    """
    Returns True if all characters in the string are ascii characters
    """
    pass

def isdecimal():
    """
    Returns True if all characters in the string are decimals
    """
    pass

def isdigit(self):
    """
    Returns True if all characters in the string are digits
    """
    digits = '0123456789'
    return all(c in digits for c in self)

def isidentifier():
    """
    Returns True if the string is an identifier
    """
    pass

def islower(self):
    """
    Returns True if all characters in the string are lower case
    """
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return all(c not in maj for c in self)

def isnumeric():
    """
    Returns True if all characters in the string are numeric
    """
    pass

def isprintable():
    """
    Returns True if all characters in the string are printable
    """
    pass

def isspace():
    """
    Returns True if all characters in the string are whitespaces
    """
    return all(c == " " for c in self)

def istitle():
    """
    Returns True if the string follows the rules of a title
    """
    pass

def isupper():
    """
    Returns True if all characters in the string are upper case
    """
    min = "abcdefghijklmnopqrstuvwxyz"
    return all(c not in min for c in self)

def join(self, data):
    """
    Converts the elements of an iterable into a string
    """
    res = str(data)
    for i in range(1, len(data)) :
        res += self + data[i]



def ljust():
    """
    Returns a left justified version of the string
    """
    pass

def lower(self):
    """
    Converts a string into lower case
    """
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    min = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(self)) :
        self[i] = min[maj.index(self[i])] if self[i] in maj else self[i]


def lstrip():
    """
    Returns a left trim version of the string
    """
    pass

def maketrans(x, y = None, z = ""):
    """
    Returns a translation table to be used in translations
    """
    if type(x) == type({}) :
        if not y :
            return x
        raise TypeError('first maketrans argument must be a string if there is a second argument')
    if not y :
        raise TypeError("if you give only one argument to maketrans it must be a dict")

    if len(x) != len(y) :
        raise ValueError("the first two maketrans arguments must have equal length")

    translation = { ord(pat):ord(val) for pat,val in zip(x, y)}
    translation.update({ord(pat):None for pat in z})
    return translation



def partition():
    """
    Returns a tuple where the string is parted into three parts
    """
    pass

def replace(self, patt, val):
    """
    Returns a string where a specified value is replaced with a specified value
    """
    i = 0
    length = len(patt)
    mylen = len(self)
    newstr = ""
    while i + length < mylen :
        if self[i:i+length] == patt :
            newstr += val
            i += length
        else :
            i += 1



def rfind():
    """
    Searches the string for a specified value and returns the last position of where it was found
    """
    pass

def rindex():
    """
    Searches the string for a specified value and returns the last position of where it was found
    """
    pass

def rjust():
    """
    Returns a right justified version of the string
    """
    pass

def rpartition():
    """
    Returns a tuple where the string is parted into three parts
    """
    pass

def rsplit():
    """
    Splits the string at the specified separator, and returns a list
    """
    pass

def rstrip():
    """
    Returns a right trim version of the string
    """
    pass

def split():
    """
    Splits the string at the specified separator, and returns a list
    """
    pass

def splitlines(self):
    """
    Splits the string at line breaks and returns a list
    """
    return self.split('\n')

def startswith(self, val):
    """
    Returns true if the string starts with the specified value
    """
    return self[0:len(val)] == val


def strip():
    """
    Returns a trimmed version of the string
    """
    pass

def swapcase(self):
    """
    Swaps cases, lower case becomes upper case and vice versa
    """
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    min = "abcdefghijklmnopqrstuvwxyz"
    trans = self.maketrans(maj+min, min+maj)
    return self.translate(trans)

def title():
    """
    Converts the first character of each word to upper case
    """
    pass

def translate():
    """
    Returns a translated string
    """
    pass

def upper():
    """
    Converts a string into upper case
    """
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    min = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(self)) :
        self[i] = maj[min.index(self[i])] if self[i] in min else self[i]

def zfill():
    """
    Fills the string with a specified number of 0 values at the beginning
    """
    pass
