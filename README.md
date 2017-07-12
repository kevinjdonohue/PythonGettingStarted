# Python: Getting Started
A repo for notes, example code, etc.. from the Python: Getting Start course by Bo Milanovich on PluralSight

### Types, Statements, and Other Goodies

Dynamic types; no need to declare a variable's type before creating and using it.

#### Type Hinting

```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```

#### Integers and Floats

```python
answer = 42
pi = 3.14159
answer + pi = 45.14159 # don't worry about conversion
int(pi) == 3

float(answer) == 42.0
```

#### Strings

```python
'Hello World' == "Hello World" == """Hello World"""
# triple quoted strings are often used as multi-line comments

"hello".capitalize() == "Hello"
"hello".replace("e", "a") == "Hello"
"hello".isalpha() == True
"123".isdigit() == True # useful when converting to an int

"some, csv, values".split(",") == ["some", "csv", "values"]
```

##### String Format

```python
name = "PythonBo"
machine = "HAL"

"Nice to meet you {0}. I am {1}".format(name, machine)

f"Nice to meet you {name}.  I am {machine}" # with Python 3 - string interpolation
```

#### Boolean and None

```python
python_course = True
java_course = False
int(python_course) == 1
int(java_course) == 0
str(python_course) == "True"

aliens_found = None
```

#### If Statements

```python
number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is NOT 5")
```

##### Truthy and Falsy Values

```python
text = "python"
if text:
    print("Text is defined and truthy")
```

##### Boolean and None

```python
python_course = True
if python_course:  #note:  not python_course == True
    print("This will execute")
    
aliens_found = None
if aliens_found:
    print("This will NOT execute")
```

##### Not If

```python
number = 5
if number != 5:
    print("This will not execute")

python_course = True
if not python_course:
    print("This will also not execute")
```

##### Multiple If Conditions

```python
number = 3
python_course = True
if number == 3 and python_course:
    print("This will execute")
    
if number == 17 or python_course:
    print("This will also execute")
```

##### Ternary If Statements

```python
a = 1
b = 2
"bigger" if a > b else "smaller"
```

#### Lists

```python
student_names = []
student_names = ["Mark", "Katarina", "Jessica"]
student_names[0] == "Mark"
student_names[2] == "Jessica"
student_names[-1] == "Jessica" # last element is a list; first element from the right
student_names[3] = "Homer" # you can't do this
student_names.append("Homer") # adds item to the end
student_names == ["Mark", "Katarina", "Jessica", "Homer"]

"Mark" in student_names == True # Mark is found in the list

len(student_names) == 4 # number of elements in the list

del student_names[2] # removes Jessica from the list

student_names = ["Mark", "Katarina", "Homer"]
```

##### List Slicing

```python
student_names = ["Mark", "Katarina", "Homer"]

student_names[1:] == ["Katarina", "Homer"]
student_names[1:-1] == ["Katarina"]
```

#### For Loops

```python
student_names = ["Mark", "Katarina", "Jessica"]

print(student_names[0])
print(student_names[1])
print(student_names[2])

for name in student_names:
    print("Student name is {0}".format(name))
    
for name is student_names:
    print(f"Student name is {name}")
    
x = 0
for index in range(10):
    x += 10
    print(f"The value of X is {x}")
    
# range with 2 arguments allows you to start from an index other than 0
x = 0
for index in range(5, 10):
    x += 10
    print(f"The value of X is {x}")
    
# range can also be called with 3 arguments:  starting index, ending index, increment
x = 0
for index in range(5, 10, 2):
    x += 10
    print(f"The value of X is {x}")
```

#### Break and Continue

```python
student_names = ["James", "Katarina", "Jessica", "Mark", "Bort", "Frank Grimes", "Max Power"]

for name in student_names:
    if name == "Mark":
        print(f"Found him! {name}")
        break
        
    print(f"Currently testing {name}")
    
for name in student_names:
    if name == "Bort":
        continue
        print(f"Found him! {name}")

    print(f"Currently testing {name}")    
```

#### While Loop

```python
x = 0
while x < 10:
    print(f"Count is {x}")
    x += 1
```

#### Dictionaries

These are very JSON-like data structures with keys and values.

```python
student = {
  "name": "Mark",
  "student_id": 15163,
  "feedback": None
}

student["name"] == "Mark"
student["last_name"] == KeyError # will throw this if the key is not found
student.get("last_name", "Unknown") # alternative is to use get and specific a default value
student.keys() = ["name", "student_id", "feedback"]
student.values() = ["Mark", 15163, None]
student["name"] = "James"
del student["name"]

# note the brackets here to indicate a list - in this case a list of dictionaries
all_students = [
  {"name": "Mark", "student_id": 15163, "feedback": None},
  {"name": "Katarina", "student_id": 63112, "feedback": None},
  {"name": "Jessica", "student_id": 30021, "feedback": None}
]
```

#### Exceptions

```python
student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

student["last_name"] = "Kowalski"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name

except KeyError:
    print("Error finding last name")

except TypeError as error:
    print("Can't add these two together!")
    print(error)

except Exception:
    print("Unknown error")

print("This code executes!")
```

#### Other Data Types (Complex, Bytes, ByteArray, Tuple, Set, FrozenSet)

```python
complex
long # python 2 
bytes
bytearray
tuple = (3, 5, 1, "Mark")
set
frozenset
set([3, 2, 3, 1, 5]) == (1, 2, 3, 5)
```

### Functions, Files, Yield and Lambda

#### Functions

##### Built In Functions Examples

```python
print("Hello World")
str(3) == "3"
int("15") == 15
username = input("Enter the user's name: ")
```

#### Function Arguments

```python
def add_student(student_id,  name):
    students = []
    student = {"student_id": student_id, "name": name}
    students.append(student)
    
    
add_student(student_id=1, name="Kevin")  # named arguments    


def variable_arguments(name, *args):  # variable number of parameters
    print(args)

    
def keyword_variable_arguments(name, **kwargs):  # variable number of parameters with keywords
    print(kwargs["parameter1"], kwargs["parameter2"])     
```

#### Lambda Functions

```python
# standard function
def double1(x):
    return x * 2

# lambda equivalent
double2 = lambda x: x * 2

# call either function in the same way:
result1 = double1(2)

result2 = double2(2)
```

#### Classes

In general, classes are OO constructs similar to other OO languages.

There are some Python specific details:

* Class names should be capitalized while function and attribute names should be lowercase
* No access modifiers for classes or their functions
* `__init__` works an a constructor-like method in Python
    * Not the use of the `self` keyword in the parameter list - think of it as `self.`
    * example: `self.student_name` creates a instance attribute in the Student class for storing a student's name
* `__str__` allows the return of a string representation of the object
* `__repr__`?
* Classes can contain class (static) attributes as well as instance attributes
    * example:  school_name below is a class (static) attribute of the Student class
* No interfaces
* By convention, naming a function with an underscore is an indication that it is "private" and shouldn't be overridden
* No override keyword; you can simply override a function in a derived class by using the same name
* Inheritance is achieved by passing the class within the parenthesis of the new class
    * Example:  `class DerivedFoo(Foo):` would indicate a new class DerivedFoo inheriting from class Foo
* Multiple inheritance is allowed
    * The `super()`keyword is used to access the functions and properties of the class being derived from

```python
class Student:

    school_name = "Springfield Elementary"

    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        students.append(self)

    #string representation of the object
    #what about __repr__?
    def __str__(self):
        return "Student: " + self.student_name

    def get_name_capitalize(self):
        return self.student_name.capitalize()

    def get_school_name(self):
        return self.school_name
```



