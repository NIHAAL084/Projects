## Document 12
**Source**: https://gleam.run/cheatsheets/gleam-for-python-users/

Gleam for Python users
Hello productive pragmatic Pythonistas!

a soft wavey boundary between two sections of the website
Comments
Variables
Match operator
Variables type annotations
Functions
Exporting functions
Function type annotations
Referencing functions
Labelled arguments
Operators
Constants
Blocks
Data types
Strings
Tuples
Lists
Dicts
Flow control
Case
Try
Type aliases
Custom types
Records
Unions
Opaque custom types
Modules
Imports
Named imports
Unqualified imports
Comments
Python
In Python, comments are written with a # prefix.

# Hello, Joe!
A docstring (matching “””) that occurs as the first statement in a module, function, class, or method definition will become the __doc__ attribute of that object.

def a_function():
    """Return some important data."""
    pass
Gleam
In Gleam, comments are written with a // prefix.

// Hello, Joe!
Comments starting with /// are used to document the following statement. Comments starting with //// are used to document the current module.

//// This module is very important.

/// The answer to life, the universe, and everything.
const answer: Int = 42
Variables
You can reassign variables in both languages.

Python
size = 50
size = size + 100
size = 1
Python has no specific variable keyword. You choose a name and that’s it!

Gleam
Gleam has the let keyword before its variable names.

let size = 50
let size = size + 100
let size = 1
Match operator
Python
Python supports basic, one directional destructuring (also called unpacking). Tuple of values can be unpacked and inner values can be assigned to left-hand variable names.

(a, b) = (1, 2)
# a == 1
# b == 2

# works also for for-loops
for key, value in enumerate(a_dict):
    print(key, value)
Gleam
In Gleam, let and = can be used for pattern matching, but you’ll get compile errors if there’s a type mismatch, and a runtime error if there’s a value mismatch. For assertions, the equivalent let assert keyword is preferred.

let #(x, _) = #(1, 2)
let assert [] = [1] // runtime error
let assert [y] = "Hello" // compile error, type mismatch
Variables type annotations
Python
Python is a dynamically typed language. Types are only checked at runtime and a variable can have different types in its lifetime.

Type hints (Python 3+) are optional annotations that document the code with type information. These annotations are accessible at runtime via the __annotations__ module-level variable.

These hints will mainly be used to inform static analysis tools like IDEs, linters…

some_list: list[int] = [1, 2, 3]
Gleam
In Gleam type annotations can optionally be given when binding variables.

let some_list: List(Int) = [1, 2, 3]
Gleam will check the type annotation to ensure that it matches the type of the assigned value. It does not need annotations to type check your code, but you may find it useful to annotate variables to hint to the compiler that you want a specific type to be inferred.

Functions
Python
In Python, you can define functions with the def keyword. In that case, the return keyword is mandatory.

def sum(x, y):
    return x + y
Anonymous functions returning a single expression can also be defined with the lambda keyword and be assigned into variables.

mul = lambda x, y: x * y
mul(1, 2)
Gleam
Gleam’s functions are declared using a syntax similar to Rust or JavaScript. Gleam’s anonymous functions have a similar syntax and don’t need a . when called.

pub fn sum(x, y) {
  x + y
}

let mul = fn(x, y) { x * y }
mul(1, 2)
Exporting functions
Python
In Python, top level functions are exported by default. There is no notion of private module-level functions.

Gleam
In Gleam, functions are private by default and need the pub keyword to be public.

// this is public
pub fn sum(x, y) {
  x + y
}

// this is private
fn mul(x, y) {
  x * y
}
Function type annotations
Python
Type hints can be used to optionally annotate function arguments and return types.

Discrepancies between type hints and actual values at runtime do not prevent interpretation of the code.

Static code analysers (IDE tooling, type checkers like mypy) will be required to detect those errors.

def sum(x: int, y: int) -> int:
    return x + y

def mul(x: int, y: int) -> bool:
    # no errors from the interpreter.
    return x * y
Gleam
Functions can optionally have their argument and return types annotated in Gleam. These type annotations will always be checked by the compiler and throw a compilation error if not valid. The compiler will still type check your program using type inference if annotations are omitted.

pub fn add(x: Int, y: Int) -> Int {
  x + y
}

pub fn mul(x: Int, y: Int) -> Bool { // compile error, type mismatch
  x * y
}
Referencing functions
Python
As long as functions are in scope they can be assigned to a new variable. There is no special syntax to assign a module function to a variable.

Gleam
Gleam has a single namespace for value and functions within a module, so there is no need for a special syntax to assign a module function to a variable.

fn identity(x) {
  x
}

fn main() {
  let func = identity
  func(100)
}
Labelled arguments
Both Python and Gleam have ways to give arguments names and in any order.

Python
Keyword arguments are evaluated once at function definition time, and there is no evidence showing a noticeable performance penalty when using named arguments.

When calling a function, arguments can be passed

positionally, in the same order of the function declaration
by name, in any order
def replace(inside: str, each: str, with_string: str):
    pass

# equivalent calls
replace('hello world', 'world', 'you')
replace(each='world', inside='hello world',  with_string='you')
Gleam
In Gleam arguments can be given a label as well as an internal name. Contrary to Python, the name used at the call-site does not have to match the name used for the variable inside the function.

pub fn replace(inside string, each pattern, with replacement) {
  go(string, pattern, replacement)
}
replace(each: ",", with: " ", inside: "A,B,C")
There is no performance cost to Gleam’s labelled arguments as they are optimised to regular function calls at compile time, and all the arguments are fully type checked.

Operators
Operator	Python	Gleam	Notes
Equal	==	==	In Gleam both values must be of the same type
Strictly equal to	==	==	Comparison in Gleam is always strict. (see note for Python)
Reference equality	is	 	True only if the two objects have the same reference
Not equal	!=	!=	In Gleam both values must be of the same type
Greater than	>	>	In Gleam both values must be ints
Greater than	>	>.	In Gleam both values must be floats
Greater or equal	>=	>=	In Gleam both values must be ints
Greater or equal	>=	>=.	In Gleam both values must be floats
Less than	<	<	In Gleam both values must be ints
Less than	<	<.	In Gleam both values must be floats
Less or equal	<=	<=	In Gleam both values must be ints
Less or equal	<=	<=.	In Gleam both values must be floats
Boolean and	and	&&	In Gleam both values must be bools
Logical and	and	 	Not available in Gleam
Boolean or	or	||	In Gleam both values must be bools
Logical or	or	 	Not available in Gleam
Add	+	+	In Gleam both values must be ints
Add	+	+.	In Gleam both values must be floats
Subtract	-	-	In Gleam both values must be ints
Subtract	-	-.	In Gleam both values must be floats
Multiply	*	*	In Gleam both values must be ints
Multiply	*	*.	In Gleam both values must be floats
Divide	/	/	In Gleam both values must be ints
Divide	/	/.	In Gleam both values must be floats
Remainder	%	%	In Gleam both values must be ints, in Gleam negative values behave differently: Use int.modulo to mimick Python’s behavior.
Concatenate	+	<>	In Gleam both values must be strings
Pipe	 	|>	Gleam’s pipe can pipe into anonymous functions. This operator does not exist in python
Some notes for Python:

== is by default comparing by value:

scalars will have their value compared
the only type cast will be for 0 and 1 that will be coerced to False and True respectively
variables that point to the same object will be equal with ==
two objects with the same members values won’t be equal:

no structural equality, unless the __eq__ operator is redefined.
Python operators are short-circuiting as in Gleam.
Python operators can be overloaded and be applied to any types with potential custom behaviors
Constants
Python
In Python, top-level declarations are in the global/module scope is the highest possible scope. Any variables and functions defined will be accessible from anywhere in the code.

There is no notion of constant variables in Python.

# in the global scope
THE_ANSWER = 42
Gleam
In Gleam constants can be created using the const keyword.

const the_answer = 42

pub fn main() {
  the_answer
}
Blocks
Python
Python blocks are always associated with a function / conditional / class declarations… There is no way to create multi-line expressions blocks like in Gleam.

Blocks are declared via indentation.

def a_func():
    # A block here
    pass
Gleam
In Gleam braces { } are used to group expressions.

pub fn main() {
  let x = {
    some_function(1)
    2
  }
  let y = x * {x + 10} // braces are used to change arithmetic operations order
  y
}
Data types
Strings
In Python, strings are stored as unicode code-points sequence. Strings can be encoded or decoded to/from a specific encoding.

In Gleam all strings are UTF-8 encoded binaries.

Python
"Hellø, world!"
Gleam
"Hellø, world!"
Tuples
Tuples are very useful in Gleam as they’re the only collection data type that allows mixed types in the collection.

Python
Python tuples are immutable, fixed-size lists that can contain mixed value types. Unpacking can be used to bind a name to a specific value of the tuple.

my_tuple = ("username", "password", 10)
_, password, _ = my_tuple
Gleam
let my_tuple = #("username", "password", 10)
let #(_, password, _) = my_tuple
Lists
Lists in Python are allowed to have values of mixed types, but not in Gleam.

Python
Python can emulate the cons operator of Gleam using the * operator and unpacking:

list = [2, 3, 4]
[head, *tail] = list
# head == 2
# tail == [3, 4]
Gleam
Gleam has a cons operator that works for lists destructuring and pattern matching. In Gleam lists are immutable so adding and removing elements from the start of a list is highly efficient.

let list = [2, 3, 4]
let list = [1, ..list]
let [1, second_element, ..] = list
[1.0, ..list] // compile error, type mismatch
Dictionaries
In Python, dictionaries can have keys of any type as long as:

the key type is hashable, such as integers, strings, tuples (due to their immutable values), functions… and custom mutable objects implementing the __hash__ method.
the key is unique in the dictionary. and values of any type.
In Gleam, dicts can have keys and values of any type, but all keys must be of the same type in a given dict and all values must be of the same type in a given dict.

There is no dict literal syntax in Gleam, and you cannot pattern match on a dict. Dicts are generally not used much in Gleam, custom types are more common.

Python
{"key1": "value1", "key2": "value2"}
{"key1":  "1", "key2": 2}
Gleam
import gleam/dict

dict.from_list([#("key1", "value1"), #("key2", "value2")])
dict.from_list([#("key1", "value1"), #("key2", 2)]) // Type error!
Flow control
Case
Case is one of the most used control flows in Gleam. It can be seen as a switch statement on steroids. It provides a terse way to match a value type to an expression. Gleam’s case expression is fairly similar to Python’s match statement.

Python
Matching on primitive types:

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
Matching on tuples with variable capturing:

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f""X={x}, Y={y}"")
    case _:
        raise ValueError("Not a point")
Matching on type constructors:

match point:
    case Point(x=0, y=0):
        print("Origin is the point's location.")
    case Point(x=0, y=y):
        print(f"Y={y} and the point is on the y-axis.")
    case Point(x=x, y=0):
        print(f"X={x} and the point is on the x-axis.")
    case Point():
        print("The point is located somewhere else on the plane.")
    case _:
        print("Not a point")
The match expression supports guards, similar to Gleam:

match point:
    case Point(x, y) if x == y:
        print(f"The point is located on the diagonal Y=X at {x}.")
    case Point(x, y):
        print(f"Point is not on the diagonal.")
Gleam
The case operator is a top level construct in Gleam:

case some_number {
  0 -> "Zero"
  1 -> "One"
  2 -> "Two"
  n -> "Some other number" // This matches anything
}
The case operator especially coupled with destructuring to provide native pattern matching:

case xs {
  [] -> "This list is empty"
  [a] -> "This list has 1 element"
  [a, b] -> "This list has 2 elements"
  _other -> "This list has more than 2 elements"
}
The case operator supports guards:

case xs {
  [a, b, c] if a >. b && a <=. c -> "ok"
  _other -> "ko"
}
and disjoint union matching:

case number {
  2 | 4 | 6 | 8 -> "This is an even number"
  1 | 3 | 5 | 7 -> "This is an odd number"
  _ -> "I'm not sure"
}
Try
Error management is approached differently in Python and Gleam.

Python
Python uses the notion of exceptions to interrupt the current code flow and pop up the error to the caller.

An exception is raised using the keyword raise.

def a_function_that_fails():
    raise Exception("an error")
The callee block will be able to capture any exception raised in the block using a try/except set of blocks:

try:
    print("executed")
    a_function_that_fails()
    print("not_executed")
except Exception as e:
    print("doing something with the exception", e)

Gleam
In contrast in Gleam, errors are just containers with an associated value.

A common container to model an operation result is Result(ReturnType, ErrorType).

A Result is either:

an Error(ErrorValue)
or an Ok(Data) record
Handling errors actually means to match the return value against those two scenarios, using a case for instance:

case int.parse("123") {
  Error(e) -> io.println("That wasn't an Int")
  Ok(i) -> io.println("We parsed the Int")
}
In order to simplify this construct, we can use the use expression with the try function from the gleam/result module.

bind a value to the providing name if Ok(Something) is matched
interrupt the flow and return Error(Something)
let a_number = "1"
let an_error = "ouch"
let another_number = "3"

use int_a_number <- try(parse_int(a_number))
use attempt_int <- try(parse_int(an_error)) // Error will be returned
use int_another_number <- try(parse_int(another_number)) // never gets executed

Ok(int_a_number + attempt_int + int_another_number) // never gets executed
Type aliases
Type aliases allow for easy referencing of arbitrary complex types. Even though their type systems does not serve the same function, both Python and Gleam provide this feature.

Python
A simple variable can store the result of a compound set of types.

type Headers = list[tuple[str, str]]

# can now be used to annotate a variable
headers: Headers = [("Content-Type", "application/json")]
Gleam
The type keyword can be used to create aliases:

pub type Headers =
  List(#(String, String))

let headers: Headers = [#("Content-Type", "application/json")]
Custom types
Records
Custom type allows you to define a collection data type with a fixed number of named fields, and the values in those fields can be of differing types.

Python
Python uses classes to define user-defined, record-like types. Properties are defined as class members and initial values are generally set in the constructor.

By default the constructor does not provide base initializers in the constructor so some boilerplate is needed:

class Person:
    name: str
    age: int

    def __init__(name: str, age: int) -> None:
        self.name = name
        self.age = age

person = Person(name="Jake", age=20)
# or with positional arguments Person("Jake", 20)
name = person.name
More recent alternatives are to use dataclasses or to leverage the NamedTuple base type to generate a constructor with initializers.

By default a class created with the dataclass decorator is mutable (although you can pass options to the dataclass decorator to change the behavior):

from dataclasses import dataclasses

@dataclass
class Person:
    name: str
    age: int

person = Person(name="Jake", age=20)
name = person.name
person.name = "John"  # The name is now "John"
NamedTuples on the other hand are immutable:

from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int

person = Person(name="Jake", age=20)
name = person.name

# cannot reassign a value
person.name = "John"  # error
Gleam
Gleam’s custom types can be used in much the same way that structs are used in Elixir. At runtime, they have a tuple representation and are compatible with Erlang records.

type Person {
  Person(name: String, age: Int)
}

let person = Person(name: "Jake", age: 35)
let name = person.name
An important difference to note is there is no OOP in Gleam. Methods can not be added to types.

Unions
In Python unions can be declared with the | operator.

In Gleam functions must always take and receive one type. To have a union of two different types they must be wrapped in a new custom type.

Python
def int_or_float(x: int | float) -> str:
    if isinstance(x, int):
        return f"It's an integer: {x}"
    else:
        return f"It's a float: {x}"
Gleam
type IntOrFloat {
  AnInt(Int)
  AFloat(Float)
}

fn int_or_float(x) {
  case x {
    AnInt(1) -> "It's an integer: 1"
    AFloat(1.0) -> "It's a float: 1.0"
  }
}
Opaque custom types
In Python, constructors cannot be marked as private. Opaque types can be imperfectly emulated using a class method and some magic property that only updates via the class factory method.

In Gleam, custom types can be defined as being opaque, which causes the constructors for the custom type not to be exported from the module. Without any constructors to import other modules can only interact with opaque types using the intended API.

Python
class OnlyCreatable:

    __create_key = object()

    @classmethod
    def create(cls, value):
        return OnlyCreatable(cls.__create_key, value)

    def __init__(self, create_key, value):
        assert(create_key == OnlyCreatable.__create_key), \
            "OnlyCreatable objects must be created using OnlyCreatable.create"
        self.value = value
Gleam
pub opaque type Identifier {
  Identifier(Int)
}

pub fn get_id() {
  Identifier(100)
}
Modules
Python
There is no special syntax to define modules as files are modules in Python

Gleam
Gleam’s file is a module and named by the file name (and its directory path). Since there is no special syntax to create a module, there can be only one module in a file.

// in file foo.gleam
pub fn identity(x) {
  x
}
// in file main.gleam
import foo // if foo was in a folder called `lib` the import would be `lib/foo`
pub fn main() {
  foo.identity(1)
}
Imports
Python
# inside module src/nasa/moon_base.py
# imports module src/nasa/rocket_ship.py
from nasa import rocket_ship

def explore_space():
    rocket_ship.launch()
Gleam
Imports are relative to the root src folder.

Modules in the same directory will need to reference the entire path from src for the target module, even if the target module is in the same folder.

// inside module src/nasa/moon_base.gleam
// imports module src/nasa/rocket_ship.gleam
import nasa/rocket_ship

pub fn explore_space() {
  rocket_ship.launch()
}
Named imports
Python
import unix.cat as kitty
Gleam
import unix/cat as kitty
Unqualified imports
Python
from animal.cat import Cat, stroke

def main():
    kitty = Cat(name="Nubi")
    stroke(kitty)
Gleam
import animal/cat.{Cat, stroke}

pub fn main() {
  let kitty = Cat(name: "Nubi")
  stroke(kitty)
}

## Document 13
**Source**: https://towardsdatascience.com/gpt-from-scratch-with-mlx-acf2defda30e

GPT from Scratch with MLX
Define and train GPT-2 on your MacBook
Pranav Jadhav
Towards Data Science
Pranav Jadhav

·
Follow

Published in
Towards Data Science

31 min read
·
2 days ago

Table of Contents
Preparing the data
Coding GPT-2
Input Embeddings
Positional Embeddings
Self Attention
Keys, Queries, and Values
Multi-Head Attention
MLP
Block
Layernorms and Skip Connections
Forward Pass
Sampling
Initialization
Training Loop
References
Preparing the data
Install mlx and run the following imports.

import mlx.core as mx
import mlx.nn as nn
import mlx.optimizers as optim
import mlx.utils as utils
import numpy as np
import math
The first step to training an LLM is collecting a large corpus of text data and then tokenizing it. Tokenization is the process of mapping text to integers, which can be fed into the LLM. Our training corpus for this model will be the works of Shakespeare concatenated into one file. This is roughly 1 million characters and looks like this:

First Citizen:
Before we proceed any further, hear me speak.

All:
Speak, speak.

First Citizen:
You are all resolved rather to die than to famish?

All:
Resolved. resolved.

First Citizen:
First, you know Caius Marcius is chief enemy to the people.
...
First, we read the file as a single long string into the text variable. Then we use the set() function to get all the unique characters in the text which will be our vocabulary. By printing vocab you can see all the characters in our vocabulary as one string, and we have a total of 65 characters which till be our tokens.

# Creating the vocabulary
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()
vocab = sorted(list(set(text)))
vocab_size = len(vocab)

print(''.join(vocab))
# !$&',-.3:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
print(vocab_size)
# 65
Production models will use tokenization algorithms like byte-pair encoding to generate a larger vocabulary of sub-word chunks. Since our focus today is on the architecture, we will continue with character-level tokenization. Next, we will map our vocabulary to integers known as token IDs. Then we can encode our text into tokens and decode them back to a string.

# Create mapping from vocab to integers
itos = {i:c for i,c in enumerate(vocab)} # int to string
stoi = {c:i for i,c in enumerate(vocab)} # string to int
encode = lambda x: [stoi[c] for c in x]
decode = lambda x: ''.join([itos[i] for i in x])

print(encode("hello world"))
# [46, 43, 50, 50, 53, 1, 61, 53, 56, 50, 42]
print(decode(encode("hello world")))
# hello world
We use theenumerate() function to iterate over all characters and their index in the vocabulary and create a dictionary itos which maps integers to characters and stoi which maps strings to integers. Then we use these mappings to create our encode and decode functions. Now we can encode the entire text and split training and validation data.

data = encode(text)
split = int(0.9 * len(data))
train_data = data[:split]
val_data = data[split:]
Currently, our training data is just a very long string of tokens. However, we are trying to train our model to predict the next token some given previous tokens. Therefore our dataset should be comprised of examples where the input is some string of tokens and the label is the correct next token. We need to define a model parameter called context length which is the maximum number of tokens used to predict the next token. Our training examples will be the length of our context length.

Let’s look at the first ctx_len+1 tokens.

ctx_len = 8
print(train_data[:ctx_len + 1])
# [18, 47, 56, 57, 58,  1, 15, 47, 58]
# x: [18, 47, 56, 57, 58,  1, 15, 47] | y: 58
This is one training example where the input is “18, 47, 56, 57, 58, 1, 15, 47” and the desired output is “58”. This is 8 tokens of context. However, we also want to train the model to predict the next token given only 7, 6, 5 … 0 tokens as context which is needed during generation. Therefore we also consider the 8 sub examples packed into this example:

ctx_len = 8
print(train_data[:ctx_len + 1])
# [18, 47, 56, 57, 58,  1, 15, 47, 58]
# 8 sub examples
# [18] --> 47
# [18, 47] --> 56
# [18, 47, 56] --> 57
# [18, 47, 56, 57] --> 58
# [18, 47, 56, 57, 58] --> 1
# [18, 47, 56, 57, 58, 1] --> 15
# [18, 47, 56, 57, 58, 1, 15] --> 47
# [18, 47, 56, 57, 58, 1, 15, 47] --> 58
Notice that the labels are simply the inputs shifted left.

print("inputs: ", train_data[:ctx_len])
print("labels: ", train_data[1:ctx_len+1]) # labels = inputs indexed 1 higher
# inputs: [18, 47, 56, 57, 58,  1, 15, 47]
# labels: [47, 56, 57, 58,  1, 15, 47, 58]
At index 0 the input is 18 and the label is 47. At index 1 the input is everything before and including index 1 which is [18, 47] and the label is 56, etc. Now that we understand that the labels are simply the input sequence indexed one higher we can build our datasets.

# Creating training and validation datasets
ctx_len = 8
X_train = mx.array([train_data[i:i+ctx_len] for i in range(0, len(train_data) - ctx_len, ctx_len)])
y_train = mx.array([train_data[i+1:i+ctx_len+1] for i in range(0, len(train_data) - ctx_len, ctx_len)])
X_val = mx.array([val_data[i:i+ctx_len] for i in range(0, len(val_data) - ctx_len, ctx_len)])
y_val = mx.array([val_data[i+1:i+ctx_len+1] for i in range(0, len(val_data) - ctx_len, ctx_len)])
We loop through the data and take chunks of size ctx_len as the inputs (X) and then take the same chunks but at 1 higher index as the labels (y). Then we take these Python lists and create mlx array objects from them. The model internals will be written with mlx so we want our inputs to be mlx arrays.

One more thing. During training we don’t want to feed the model one example at a time, we want to feed it multiple examples in parallel for efficiency. This group of examples is called our batch, and the number of examples in a group is our batch size. Thus we define a function to generate batches for training.

def get_batches(X, y, b_size, shuffle=True):
    if shuffle:
        ix = np.arange(X.shape[0])
        np.random.shuffle(ix)
        ix = mx.array(ix)
        X = X[ix]
        y = y[ix]
    for i in range(0, X.shape[0], b_size):
        input = X[i:i+b_size]
        label = y[i:i+b_size]
        yield input, label
If shuffle=True, we shuffle the data by indexing it with a randomly shuffled index. Then we loop through our dataset and return batch-size chunks from input and label datasets. These chunks are known as mini-batches and are just stacked examples that we process in parallel. These mini-batches will be our input to the model during training.

Here’s an example of a minibatch of 4 examples with context length 8.


A single minibatch (image by author)
This minibatch packs 32 next-token prediction problems. The model will predict the next token for each token in the input and the labels will be used to calculate the loss. Notice that the labels contain the next token for each index of the inputs.

You’ll want to keep this picture in your mind because the shapes of these tensors will get hairy. For now, just remember that we will input a tensor of shape (batch_size, ctx_len) to the model.

Coding GPT-2
Let’s look at the GPT-2 architecture to get an overview of what we are trying to implement.


GPT-2 Architecture (image by author)
Don’t worry if this looks confusing. We will implement it step by step from bottom to top. Let’s start by implementing the input embeddings.

Input Embeddings
The purpose of the input embedding layer is to map token IDs to vectors. Each token will be mapped to a vector which will be its representation as it is forwarded through the model. The vectors for each token will accumulate and exchange information as they pass through the model and eventually be used to predict the next token. These vectors are called embeddings.

The simplest way to map token IDs to vectors is through a lookup table. We create a matrix of size (vocab_size, n_emb) where each row is the embedding vector for the corresponding token. This matrix is known as the embedding weights.


Embedding Layer (image by author)
The diagram shows an example embedding layer of size (65, 6). This means there are 65 tokens in the vocabulary and each one will be represented by a length 6 embedding vector. The inputted sequence will be used to index the embedding weights to get the vector corresponding to each token. Remember the minibatches we input into the model? Originally the minibatch is size (batch_size, ctx_len). After passing through the embedding layer it is size (batch_size, ctx_len, n_emb). Instead of each token being a single integer, each token is now a vector of length n_emb.

Let’s define the embedding layer in code now.

n_emb = 6 # You can add these hyperparams at the top of your file
class GPT(nn.Module):
    def __init__(self):
        super().__init__()
        self.wte = nn.Embedding(vocab_size, n_emb)
We will define a class to organize our implementation. We subclass nn.Module to take advantage of mlx’s features. Then in the init function, we call the superclass constructor and initialize our token embedding layer called wte .

Positional Embeddings
Next up is the positional embeddings. The purpose of positional embeddings is to encode information about the position of each token in the sequence. This can be added to our input embeddings to get a complete representation of each token that contains information about the token’s position in the sequence.

class GPT(nn.Module):
    def __init__(self):
        super().__init__()
        self.wte = nn.Embedding(vocab_size, n_emb) # token embeddings
        self.wpe = nn.Embedding(ctx_len, n_emb) # position embeddings
The position embeddings work the same as token embeddings, except instead of having a row for each token we have a row for each possible position index. This means our embedding weights will be of shape (ctx_len, n_emb). Now we implement the __call__ function in our GPT class. This function will contain the forward pass of the model.

# Tensor shapes commented
def __call__(self, x):
    B, T = x.shape # (B = batch_size, T = ctx_len)
    tok_emb = self.wte(x) # (B, T, n_emb)
    pos_emb = self.wpe(mx.arange(T)) # (T, n_emb)
    x = tok_emb + pos_emb # (B, T, n_emb)
First, we break out the dimensions of our input into variables B and T for easy handling. In sequence modeling contexts B and T are usually used as shorthand for “batch” and “time” dimensions. In this case, the “time” dimension of our sequence is the context length.

Next, we calculate token and position embeddings. Notice that for the position embeddings, our input is mx.arange(T) . This will output an array of consecutive integers from 0 to T-1 which is exactly what we want because those are the positions we want to embed. After passing that through the embedding layer we will have a tensor of shape (T, n_emb) because the embedding layer plucks out the n_emb length vector for each of the T positions. Note that even though pos_emb is not the same shape as tok_emb we can add the two because mlx will broadcast, or replicate pos_emb across the batch dimension to allow elementwise addition. Finally, we perform the addition to get the new representations of the tokens with positional information.

Self-Attention
So far the representation vectors for each token have been calculated independently. They have not had the opportunity to exchange any information. This is intuitively bad in language modeling because the meaning and usage of words depend on the surrounding context. Self-attention is how we incorporate information from previous tokens into a given token.

First, let’s consider a naive approach. What if we simply represented each token as the average of its representation vector and the vectors of all the tokens before it? This achieves our goal of packing information from previous tokens into the representation for a given token. Here’s what it would look like.


image by author
But self-attention doesn’t involve writing a for-loop. The key insight is we can achieve this previous token averaging with matrix multiplication!


image by author
By multiplying our input sequence on the left by a special matrix we get the desired result. This matrix is known as the attention weights. Notice that each row of the attention weight matrix specificies “how much” of each other token goes into the representation for any given token. For example in row two, we have [0.5, 0.5, 0, 0]. This means that row two of the result will be 0.5*token1 + 0.5*token2 + 0*token3 + 0*token4 , or the average of token1 and token2. Note that the attention weights are a lower-triangular matrix (zeros in upper right entries). This ensures that future tokens will not be included in the representation of a given token. This ensures that tokens can only communicate with the previous tokens because during generation the model will only have access to previous tokens.

Let’s look at how we can construct the attention weight matrix.


image by author
Notice that if we create an array of zeros with -inf in the upper right entries and then perform row-wise softmax we get the desired attention weights. A good exercise is to step through the softmax calculation for a row to see how this works. The takeaway is that we can take some array of size (ctx_len, ctx_len) and softmax each row to get attention weights that sum to one.

Now we can leave the realm of naive self-attention. Instead of simply averaging previous tokens, we use arbitrary weighted sums over previous tokens. Notice what happens when we do row-wise softmax of an arbitrary matrix.


image by author
We still get weights that sum to one on each row. During training, we can learn the numbers in the matrix on the left which will specify how much each token goes into the representation for another token. This is how tokens pay “attention” to each other. But we still haven’t understood where this matrix on the left came from. These pre-softmax attention weights are calculated from the tokens themselves, but indirectly through three linear projections.

Keys, Queries, and Values

image by author
Each token in our sequence emits 3 new vectors. These vectors are called keys, queries, and values. We use the dot product of the query vector of one token and the key vector of another token to quantify the “affinity” those two tokens have. We want to calculate the pairwise affinities of each token with every other token, therefore we multiply the query vector (4x3) with the key vector transposed (3x4) to get the raw attention weights (4x4). Due to the way matrix multiplication works the (i,j) entry in the raw attention weights will be the query of token i dot the key of token j or the “affinity” between the two. Thus we have calculated interactions between every token. However, we don’t want past tokens interacting with future tokens so we apply a mask of -inf to the upper right entries to ensure they will zero out after softmax. Then we perform row-wise softmax to get the final attention weights. Instead of multiplying these weights directly with the input, we multiply them with the value projection. This results in the new representations.

Now that we understand attention conceptually, let’s implement it.

class Attention(nn.Module):
    def __init__(self, head_size):
        super().__init__()
        self.head_size = head_size
        self.k_proj = nn.Linear(n_emb, head_size, bias=False)
        self.q_proj = nn.Linear(n_emb, head_size, bias=False)
        self.v_proj = nn.Linear(n_emb, head_size, bias=False)

We start by defining the key, query, and value projection layers. Note that instead of going from n_emb to n_emb, we project from n_emb to head_size. This doesn’t change anything, it just means the new representations calculated by attention will be dimension head_size.

class Attention(nn.Module):
    def __init__(self, head_size):
        super().__init__()
        self.head_size = head_size
        self.k_proj = nn.Linear(n_emb, head_size, bias=False)
        self.q_proj = nn.Linear(n_emb, head_size, bias=False)
        self.v_proj = nn.Linear(n_emb, head_size, bias=False)
    def __call__(self, x): # shapes commented
        B, T, C = x.shape # (batch_size, ctx_len, n_emb)
        K = self.k_proj(x) # (B, T, head_size)
        Q = self.q_proj(x) # (B, T, head_size)
        V = self.v_proj(x) # (B, T, head_size)
The forward pass begins by calculating the key, query, and value projections. We also break out the input shape into the variables B, T, and C for future convenience.

class Attention(nn.Module):
    def __init__(self, head_size):
        super().__init__()
        self.head_size = head_size
        self.k_proj = nn.Linear(n_emb, head_size, bias=False)
        self.q_proj = nn.Linear(n_emb, head_size, bias=False)
        self.v_proj = nn.Linear(n_emb, head_size, bias=False)
    def __call__(self, x):
        B, T, C = x.shape # (batch_size, ctx_len, n_emb)
        K = self.k_proj(x) # (B, T, head_size)
        Q = self.q_proj(x) # (B, T, head_size)
        V = self.v_proj(x) # (B, T, head_size)
        attn_weights = (Q @ K.transpose([0, 2, 1])) / math.sqrt(self.head_size)
        # attn_weights.shape = (B, T, T)
Next, we calculate the attention weights. We only want to transpose the last two dimensions of the key tensor, because the batch dimension is just there so we can forward multiple training examples in parallel. The mlx transpose function expects the new order of the dimensions as input, so we pass it [0, 2, 1] to transpose the last two dimensions. One more thing: we scale the attention weights by the inverse square root of head_size. This is known as scaled attention and the purpose is to ensure that when Q and K are unit variance, attn_weights will be unit variance. If the variance of attn_weights is high, then the softmax will map these small and large values to 0 or 1which results in less complex representations.

The next step is to apply the mask to ensure we are doing causal language modeling i.e. ensuring tokens cannot attend to future tokens.

class Attention(nn.Module):
    def __init__(self, head_size):
        super().__init__()
        self.head_size = head_size
        self.k_proj = nn.Linear(n_emb, head_size, bias=False)
        self.q_proj = nn.Linear(n_emb, head_size, bias=False)
        self.v_proj = nn.Linear(n_emb, head_size, bias=False)
        indices = mx.arange(ctx_len)
        mask = indices[:, None] < indices[None] # broadcasting trick
        self._causal_mask = mask * -1e9
    def __call__(self, x):
        B, T, C = x.shape # (batch_size, ctx_len, n_emb)
        K = self.k_proj(x) # (B, T, head_size)
        Q = self.q_proj(x) # (B, T, head_size)
        V = self.v_proj(x) # (B, T, head_size)
        attn_weights = (Q @ K.transpose([0, 2, 1])) / math.sqrt(self.head_size)
        # attn_weights.shape = (B, T, T)
We create the mask with a clever broadcasting trick. Let’s say our ctx_len=4 like in the diagrams above. First, we use mx.arange(4) to set the indices variable to [0, 1, 2, 3].


image by author
Then we can index like so indices[:, None] to generate a column vector with the values of indices. Similarly, we can get a row vector using indices[None]. Then when we do the < comparison, mlx broadcasts the vectors because they have mismatching shapes so they can’t be compared elementwise. Broadcasting means mlx will replicate the vectors along the lacking dimension. This results in an elementwise comparison of two (4, 4) matrices which makes sense. Side note: I recommend familiarizing yourself with the details of broadcasting by reading this, it comes up all the time when dealing with tensors.

After the elementwise comparison, we are left with the following tensor:

[[False,  True,  True,  True],
 [False, False,  True,  True],
 [False, False, False,  True],
 [False, False, False, False]]
Multiplying this tensor by -1e9, we get:

[[-0e+00, -1e+09, -1e+09, -1e+09],
 [-0e+00, -0e+00, -1e+09, -1e+09],
 [-0e+00, -0e+00, -0e+00, -1e+09],
 [-0e+00, -0e+00, -0e+00, -0e+00]]
Now we have an additive mask. We can add this matrix to our attention weights to make all the upper right entries very large negative numbers. This will cause them to be zeroed out after the softmax operation. Also, note that we add “_” as a prefix to the attribute name _causal_mask which marks it as a private variable. This signals to mlx that it is not a parameter and should not be updated during training.

class Attention(nn.Module):
    def __init__(self, head_size):
        super().__init__()
        self.head_size = head_size
        self.k_proj = nn.Linear(n_emb, head_size, bias=False)
        self.q_proj = nn.Linear(n_emb, head_size, bias=False)
        self.v_proj = nn.Linear(n_emb, head_size, bias=False)
        indices = mx.arange(ctx_len)
        mask = indices[:, None] < indices[None] # broadcasting trick
        self._causal_mask = mask * -1e9
    def __call__(self, x):
        B, T, C = x.shape # (batch_size, ctx_len, n_emb)
        K = self.k_proj(x) # (B, T, head_size)
        Q = self.q_proj(x) # (B, T, head_size)
        V = self.v_proj(x) # (B, T, head_size)
        attn_weights = (Q @ K.transpose([0, 2, 1])) / math.sqrt(self.head_size)
        # attn_weights.shape = (B, T, T)
        attn_weights = attn_weights + self._causal_mask
        attn_weights = mx.softmax(attn_weights, axis=-1)
        o = (attn_weights @ V) # (B, T, head_size)
Now we can softmax row-wise to get the final attention weights and multiply these weights by the values to get our output. Note we pass axis=-1 to softmax which specifies that we want to softmax across the last dimension which are the rows.

The final step is output linear projection and dropout.

dropout = 0.1 # add this with hyperparams at top of file
class Attention(nn.Module):
    def __init__(self, head_size):
        super().__init__()
        self.head_size = head_size
        self.k_proj = nn.Linear(n_emb, head_size, bias=False)
        self.q_proj = nn.Linear(n_emb, head_size, bias=False)
        self.v_proj = nn.Linear(n_emb, head_size, bias=False)
        indices = mx.arange(ctx_len)
        mask = indices[:, None] < indices[None] # broadcasting trick
        self._causal_mask = mask * -1e9
        self.c_proj = nn.Linear(head_size, n_emb) # output projection
        self.resid_dropout = nn.Dropout(dropout)
    def __call__(self, x):
        B, T, C = x.shape # (batch_size, ctx_len, n_emb)
        K = self.k_proj(x) # (B, T, head_size)
        Q = self.q_proj(x) # (B, T, head_size)
        V = self.v_proj(x) # (B, T, head_size)
        attn_weights = (Q @ K.transpose([0, 2, 1])) / math.sqrt(self.head_size)
        # attn_weights.shape = (B, T, T)
        attn_weights = attn_weights + self._causal_mask
        attn_weights = mx.softmax(attn_weights, axis=-1)
        o = (attn_weights @ V) # (B, T, head_size)
        o = self.c_proj(self.resid_dropout(o))
        return o
We add two new layers, c_proj and resid_dropout which are the output projection and residual dropout. The output projection is to return the vectors to their original dimension n_emb. The dropout is added for regularization and training stability which is important as we start layering the transformer blocks to get a deep network. And that’s it for implementing one attention head!

Multi-Head Attention
Instead of having just one attention head LLMs often use multiple attention heads in parallel and concatenate their outputs to create the final representation. For example, let’s say we had one attention head with head_size=64 so the vector it produced for each token was 64 dimensional. We could achieve the same thing with 4 parallel attention heads each with head_size=16 by concatenating their outputs to produce a 16x4 = 64 dimensional output. Multi-head attention allows the model to learn more complex representations because each head learns different projections and attention weights.

n_heads = 4
class MultiHeadAttention(nn.Module): # naive implementation
    def __init__(self):
        super().__init__()
        self.heads = [Attention(head_size // n_heads) for _ in range(n_heads)]
    def __call__(self, x):
        return mx.concatenate([head(x) for head in self.heads], axis=-1)
The straightforward implementation is to create a list of n_heads attention heads where each one has size equal to our final head size divided by n_heads. Then we concatenate the output of each head over the last axis. However, this implementation is inefficient and does not take advantage of the speed of tensors. Let’s implement multi-head attention with the power of tensors.

head_size = 64 # put at top of file
class MultiHeadAttention(nn.Module):
    def __init__(self):
        super().__init__()
        self.k_proj = nn.Linear(n_emb, head_size, bias=False)
        self.q_proj = nn.Linear(n_emb, head_size, bias=False)
        self.v_proj = nn.Linear(n_emb, head_size, bias=False)
        indices = mx.arange(ctx_len)
        mask = indices[:, None] < indices[None] # broadcasting trick
        self._causal_mask = mask * -1e9
        self.c_proj = nn.Linear(head_size, n_emb) # output projection
        self.resid_dropout = nn.Dropout(dropout)
    def __call__(self, x):
        B, T, C = x.shape # (batch_size, ctx_len, n_emb)
        K = self.k_proj(x) # (B, T, head_size)
        Q = self.q_proj(x) # (B, T, head_size)
        V = self.v_proj(x) # (B, T, head_size)
We start with our single-head attention implementation. The __init__() function has not changed. The forward pass begins as normal with the creation of the key, query, and value projections.

head_size = 64 # put at top of file
n_heads = 8 # put at top of file
class MultiHeadAttention(nn.Module):
    def __init__(self):
        super().__init__()
        self.k_proj = nn.Linear(n_emb, head_size, bias=False)
        self.q_proj = nn.Linear(n_emb, head_size, bias=False)
        self.v_proj = nn.Linear(n_emb, head_size, bias=False)
        indices = mx.arange(ctx_len)
        mask = indices[:, None] < indices[None] # broadcasting trick
        self._causal_mask = mask * -1e9
        self.c_proj = nn.Linear(head_size, n_emb) # output projection
        self.resid_dropout = nn.Dropout(dropout)
    def __call__(self, x):
        B, T, C = x.shape # (batch_size, ctx_len, n_emb)
        K = self.k_proj(x) # (B, T, head_size)
        Q = self.q_proj(x) # (B, T, head_size)
        V = self.v_proj(x) # (B, T, head_size)
        mha_shape = (B, T, n_heads, head_size//n_heads)
        K = mx.as_strided(K, (mha_shape)) # (B, T, n_heads, head_size//n_heads)
        Q = mx.as_strided(Q, (mha_shape)) # (B, T, n_heads, head_size//n_heads)
        V = mx.as_strided(V, (mha_shape)) # (B, T, n_heads, head_size//n_heads)
The next thing we need to do is introduce a new dimension for the number of heads n_heads . In the naive implementation, we had separate attention objects each with their own key, query, and value tensors but now we have them all in one tensor, therefore we need a dimension for the heads. We define the new shape we want in mha_shape . Then we use mx.as_strided() to reshape each tensor to have the head dimension. This function is equivalent to view from pytorch and tells mlx to treat this array as a different shape. But we still have a problem. Notice that we if try to multiply Q @ K_t (where K_t is K transposed over it’s last 2 dims) to compute attention weights as we did before, we will be multiplying the following shapes:

(B, T, n_heads, head_size//n_heads) @ (B, T, head_size//n_heads, n_heads)
Result shape: (B, T, n_heads, n_heads)
This would result in a tensor of shape (B, T, n_heads, n_heads) which is incorrect. With one head our attention weights were shape (B, T, T) which makes sense because it gives us the interaction between each pair of tokens. So now our shape should be the same but with a heads dimension: (B, n_heads, T, T) . We achieve this by transposing the dimensions of keys, queries, and values after we reshape them to make n_heads dimension 1 instead of 2.

head_size = 64 # put at top of file
n_heads = 8 # put at top of file
class MultiHeadAttention(nn.Module):
    def __init__(self):
        super().__init__()
        self.k_proj = nn.Linear(n_emb, head_size, bias=False)
        self.q_proj = nn.Linear(n_emb, head_size, bias=False)
        self.v_proj = nn.Linear(n_emb, head_size, bias=False)
        indices = mx.arange(ctx_len)
        mask = indices[:, None] < indices[None] # broadcasting trick
        self._causal_mask = mask * -1e9
        self.c_proj = nn.Linear(head_size, n_emb) # output projection
        self.attn_dropout = nn.Dropout(dropout)
        self.resid_dropout = nn.Dropout(dropout)
    def __call__(self, x):
        B, T, C = x.shape # (batch_size, ctx_len, n_emb)
        K = self.k_proj(x) # (B, T, head_size)
        Q = self.q_proj(x) # (B, T, head_size)
        V = self.v_proj(x) # (B, T, head_size)
        mha_shape = (B, T, n_heads, head_size//n_heads)
        K = mx.as_strided(K, (mha_shape)).transpose([0, 2, 1, 3]) # (B, n_heads, T, head_size//n_heads)
        Q = mx.as_strided(Q, (mha_shape)).transpose([0, 2, 1, 3]) # (B, n_heads, T, head_size//n_heads)
        V = mx.as_strided(V, (mha_shape)).transpose([0, 2, 1, 3]) # (B, n_heads, T, head_size//n_heads)
        attn_weights = (Q @ K.transpose([0, 1, 3, 2])) / math.sqrt(Q.shape[-1]) # (B, n_heads, T, T)
        attn_weights = attn_weights + self._causal_mask[:T, :T]
        attn_weights = mx.softmax(attn_weights, axis=-1)
        attn_weights = self.attn_dropout(attn_weights)
        o = (attn_weights @ V) # (B, n_heads, T, head_size//n_heads)

Now we can calculate the correction attention weights. Notice that we scale the attention weights by the size of an individual attention head rather than head_size which would be the size after concatenation. We also apply dropout to the attention weights.

Finally, we perform the concatenation and apply the output projection and dropout.

head_size = 64 # put at top of file
n_heads = 8 # put at top of file
class MultiHeadAttention(nn.Module):
    def __init__(self):
        super().__init__()
        self.k_proj = nn.Linear(n_emb, head_size, bias=False)
        self.q_proj = nn.Linear(n_emb, head_size, bias=False)
        self.v_proj = nn.Linear(n_emb, head_size, bias=False)
        indices = mx.arange(ctx_len)
        mask = indices[:, None] < indices[None] # broadcasting trick
        self._causal_mask = mask * -1e9
        self.c_proj = nn.Linear(head_size, n_emb) # output projection
        self.attn_dropout = nn.Dropout(dropout)
        self.resid_dropout = nn.Dropout(dropout)
    def __call__(self, x):
        B, T, C = x.shape # (batch_size, ctx_len, n_emb)
        K = self.k_proj(x) # (B, T, head_size)
        Q = self.q_proj(x) # (B, T, head_size)
        V = self.v_proj(x) # (B, T, head_size)
        mha_shape = (B, T, n_heads, head_size//n_heads)
        K = mx.as_strided(K, (mha_shape)).transpose([0, 2, 1, 3]) # (B, n_heads, T, head_size//n_heads)
        Q = mx.as_strided(Q, (mha_shape)).transpose([0, 2, 1, 3]) # (B, n_heads, T, head_size//n_heads)
        V = mx.as_strided(V, (mha_shape)).transpose([0, 2, 1, 3]) # (B, n_heads, T, head_size//n_heads)
        attn_weights = (Q @ K.transpose([0, 1, 3, 2])) / math.sqrt(Q.shape[-1]) # (B, n_heads, T, T)
        attn_weights = attn_weights + self._causal_mask[:T, :T]
        attn_weights = mx.softmax(attn_weights, axis=-1)
        attn_weights = self.attn_dropout(attn_weights)
        o = (attn_weights @ V) # (B, n_heads, T, head_size//n_heads)
        o = o.transpose([0, 2, 1, 3]).reshape((B, T, head_size)) # concat heads
        o = self.c_proj(self.resid_dropout(o))
        return o
Since we have everything in one tensor, we can do some shape manipulation to do the concatenation. First, we move n_heads back to the second to last dimension with the transpose function. Then we reshape back to the original size to undo the splitting into heads we performed earlier. This is the same as concatenating the final vectors from each head. And that’s it for multi-head attention! We’ve gotten through the most intense part of our implementation.

MLP
The next part of the architecture is the multilayer perception or MLP. This is a fancy way of saying 2 stacked linear layers. There’s not much to be said here, it is a standard neural network.

class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.c_fc = nn.Linear(n_emb, 4 * n_emb)
        self.gelu = nn.GELU()
        self.c_proj = nn.Linear(4 * n_emb, n_emb)
        self.dropout = nn.Dropout(dropout)
    def __call__(self, x):
        x = self.gelu(self.c_fc(x))
        x = self.c_proj(x)
        x = self.dropout(x)
        return x
We take the input and project it to a higher dimension with c_fc . Then we apply gelu nonlinearity and project it back down to the embedding dimension with c_proj . Finally, we apply dropout and return. The purpose of the MLP is to allow for some computation after the vectors have communicated during attention. We will stack these communication layers (attention) and computation layers (mlp) into a block.

Block
A GPT block consists of attention followed by an MLP. These blocks will be repeated to make the architecture deep.

class Block(nn.Module):
    def __init__(self):
        super().__init__()
        self.mlp = MLP()
        self.mha = MultiHeadAttention()
    def __call__(self, x):
        x = self.mha(x)
        x = self.mlp(x)
        return x
Now, we need to add two more features to improve training stability. Let’s take a look at the architecture diagram again.

Layernorms and Skip Connections

image by author
We still need to implement the components highlighted in red. The arrows are skip connections. Instead of the input being transformed directly, the effect of the attention and MLP layers is additive. Their result is added to the input instead of directly replacing it. This is good for the training stability of deep networks since in the backward pass, the operands of an addition operation will receive the same gradient as their sum. Gradients can thus flow backwards freely which prevents issues like vanishing/exploding gradients that plague deep networks. Layernorm also helps with training stability by ensuring activations are normally distributed. Here is the final implementation.

class Block(nn.Module):
    def __init__(self):
        super().__init__()
        self.mlp = MLP()
        self.mha = MultiHeadAttention()
        self.ln_1 = nn.LayerNorm(dims=n_emb)
        self.ln_2 = nn.LayerNorm(dims=n_emb)
    def __call__(self, x):
        x = x + self.mha(self.ln_1(x))
        x = x + self.mlp(self.ln_2(x))
        return x
Layernorm is applied before multi-head attention and MLP. The skip connections are added with x = x + ... making the operations additive.

Forward Pass
With the Block defined, we can finish the full GPT-2 forward pass.

n_layers = 3 # put at top of file
class GPT(nn.Module):
    def __init__(self):
        super().__init__()
        self.wte = nn.Embedding(vocab_size, n_emb) # token embeddings
        self.wpe = nn.Embedding(ctx_len, n_emb) # position embeddings
        self.blocks = nn.Sequential(
            *[Block() for _ in range(n_layers)],
        ) # transformer blocks
        self.ln_f = nn.LayerNorm(dims=n_emb) # final layernorm
        self.lm_head = nn.Linear(n_emb, vocab_size) # output projection
    # Tensor shapes commented
    def __call__(self, x):
        B, T = x.shape # (B = batch_size, T = ctx_len)
        tok_emb = self.wte(x) # (B, T, n_emb)
        pos_emb = self.wpe(mx.arange(T)) # (T, n_emb)
        x = tok_emb + pos_emb # (B, T, n_emb)
        x = self.blocks(x) # (B, T, n_emb)
        x = self.ln_f(x) # (B, T, b_emb)
        logits = self.lm_head(x) # (B, T, vocab_size)
        return logits
We create a container for the blocks using nn.Sequential which takes any input and passes it sequentially through the contained layers. Then we can apply all the blocks with self.blocks(x) . Finally, we apply a layer norm and then the lm_head. The lm_head or language modeling head is just a linear layer that maps from the embedding dimension to the vocab size. The model will output a vector containing some value for each word in our vocabulary, or the logits. We can softmax the logits to get a probability distribution over the vocabulary which we can sample from to get the next token. We will also use the logits to calculate the loss during training. There are just two more things we need to implement before we begin training.

Sampling
We need to write a generate function to sample from the model once training is complete. The idea is that we start with some sequence of our choice, then we predict the next token and append this to our sequence. Then we feed the new sequence in and predict the next token again. This continues until we decide to stop.

# method of GPT class
def generate(self, max_new_tokens):
  ctx = mx.zeros((1, 1), dtype=mx.int32)
We prompt the model with a single token, zero. Zero is the newline character so it is a natural place to start the generation since we just want to see how Shakespeare-like our model can get. Note that we initialize the shape to (1, 1) to simulate a single batch with a sequence length of one.

# method of GPT class
def generate(self, max_new_tokens):
  ctx = mx.zeros((1, 1), dtype=mx.int32)
  for _ in range(max_new_tokens):
    logits = self(ctx[:, -ctx_len:]) # pass in last ctx_len characters
    logits = logits[:, -1, :] # get logits for the next token
    next_tok = mx.random.categorical(logits, num_samples=1)
    ctx = mx.concatenate((ctx, next_tok), axis=1)
return ctx
Then we get the logits for the next token by passing in the last ctx_len characters to the model. However, our model output is of shape (B, T, vocab_size) since it predicts the next token logits for each token in the input. We use all of that during training, but now we only want the logits for the last token because we can use this to sample a new token. Therefore we index the logits to get the last element in the first dimension which is the sequence dimension. Then we sample the next token using the mx.random.categorical() function which takes the logits and the number of samples we want as input. This function will softmax the logits to turn them into a probability distribution and then randomly sample a token according to the probabilities. Finally, we concatenate the new token to the context and repeat the process max_new_tokens number of times.

Initialization
The last thing to do is handle weight initialization which is important for training dynamics.

# method of GPT
def _init_parameters(self):
    normal_init = nn.init.normal(mean=0.0, std=0.02)
    residual_init = nn.init.normal(mean=0.0, std=(0.02 / math.sqrt(2 * n_layers)))
First, we define two different nn.init.normal functions. The first one is for initializing all linear and embedding layers. The second one is for initializing linear layers that are specifically residual projections i.e. the last linear layer inside multi-head attention and MLP. The reason for this special initialization is that it checks accumulation along the residual path as model depth increases according to the GPT-2 paper [2].

In mlx we can change the parameters of the model using the mx.update() function. Checking the docs, it expects a complete or partial dictionary of the new model parameters. We can see what this dictionary looks like by printing out self.parameters() inside the GPT class.

{'wte': {'weight': array([[-0.025084, -0.0197523, -0.0341617, ..., -0.0979123, -0.0830218, -0.0784692],
       [-0.00777913, -0.117002, -0.0310708, ..., 0.0128591, 0.122941, 0.000414443],
       [0.0240044, -0.0859084, 0.0253116, ..., 0.108967, 0.0767123, 0.0221565],
       ...,
       [0.050729, -0.04578, 0.0685943, ..., -0.0496998, -0.00350879, -0.00631825],
       [0.00518804, 0.0499818, 0.0330045, ..., 0.0300661, 0.0431054, 0.000958906],
       [-0.0323007, 0.0132046, 0.0208218, ..., -0.0785159, 0.00436121, -0.00726994]], dtype=float32)}, 'wpe': {'weight': array([[0.000797923, -0.0396898, -0.029047, ..., -0.0132273, 0.00684483, -0.0067624],
       [-0.0247021, -0.0274349, 0.0310587, ..., -0.100099, 0.0301566, -0.0178732],
       [0.0929172, -0.0468649, 0.0101506, ..., -0.0341086, -0.0516283, 0.0447596],
       ...,
       [-0.0508172, 0.0892201, -0.00183612, ..., -0.00341944, 0.023437, 0.0296461],
       [0.0105829, 0.0688093, 0.146744, ..., -0.0836337, 0.0206679, 0.0184166],
       [-0.00578717, -0.0606196, -0.0917056, ..., -0.0641549, -0.0490424, 0.0998114]], dtype=float32)}, 'blocks': {'layers': [{'mlp': {'c_fc': {'weight': array([[0.0169199, 0.00264431, 0.0316978, ..., -0.0596867, -0.0153549, 0.0176386],
       ...
It’s a nested dictionary containing each model weight as an mx.array. So to initialize the parameters of our model we need to build up a dictionary like this with our new params and pass them to self.update() . We can achieve this as follows:

# method of GPT
def _init_parameters(self):
    normal_init = nn.init.normal(mean=0.0, std=0.02)
    residual_init = nn.init.normal(mean=0.0, std=(0.02 / math.sqrt(2 * n_layers)))
    new_params = []
    for name, module in self.named_modules():
        if isinstance(module, nn.layers.linear.Linear):
            new_params.append((name + '.weight', normal_init(module.weight)))
        elif isinstance(module, nn.layers.embedding.Embedding):
            new_params.append((name + '.weight', normal_init(module.weight)
We maintain a list of tuples called new_params which will contain tuples of (parameter_name, new_value). Next, we loop through each nn.Module object in our model with self.named_modules() which returns tuples of (name, module). If we print out the module names within the loop we see that they look like this:

lm_head
blocks
blocks.layers.4
blocks.layers.3
blocks.layers.3.ln_2
blocks.layers.3.ln_1
blocks.layers.3.mha
blocks.layers.3.mha.resid_dropout
blocks.layers.3.mha.c_proj
blocks.layers.3.mha.attn_dropout
blocks.layers.3.mha.c_attn
...
blocks.layers.0.mlp.dropout
blocks.layers.0.mlp.c_proj
blocks.layers.0.mlp.gelu
blocks.layers.0.mlp.c_fc
wpe
wte
We use the isinstance() function to find the linear and embedding layers and then add them to our list. For example, say we are looping and reach “blocks.layers.0.mlp.c_fc” which is the first linear layer in the MLP. This would trigger the first if statement, and the tuple ("block.layers.0.mlp.c_fc.weight", [<normally initialized weight here>]) would be added to our list. We have to add “.weight” to the name because we specifically want to initialize the weight in this way, not the bias. Now we need to handle the residual projection initialization.

# method of GPT
def _init_parameters(self):
    normal_init = nn.init.normal(mean=0.0, std=0.02)
    residual_init = nn.init.normal(mean=0.0, std=(0.02 / math.sqrt(2 * n_layers)))
    new_params = []
    for name, module in self.named_modules():
        if isinstance(module, nn.layers.linear.Linear):
            if 'c_proj' in name: # residual projection
                new_params.append((name + '.weight', residual_init(module.weight)))
            else:
                new_params.append((name + '.weight', normal_init(module.weight)))
        elif isinstance(module, nn.layers.embedding.Embedding):
            new_params.append((name + '.weight', normal_init(module.weight)))
After checking if the module is a linear layer, we check if “c_proj” is in the name because that’s how we named the residual projections. Then we can apply the special initialization. Finally, we need to initialize the biases to be zero.

# method of GPT
def _init_parameters(self):
    normal_init = nn.init.normal(mean=0.0, std=0.02)
    residual_init = nn.init.normal(mean=0.0, std=(0.02 / math.sqrt(2 * n_layers)))
    new_params = []
    for name, module in self.named_modules():
        if isinstance(module, nn.layers.linear.Linear):
            if 'c_proj' in name:
                new_params.append((name + '.weight', residual_init(module.weight)))
            else:
                new_params.append((name + '.weight', normal_init(module.weight)))
            if 'bias' in module:
                new_params.append((name + '.bias', mx.zeros(module.bias.shape)))
        elif isinstance(module, nn.layers.embedding.Embedding):
            new_params.append((name + '.weight', normal_init(module.weight)))
    self = self.update(utils.tree_unflatten(new_params))
We add another if statement under our linear branch to check if the nn.Module object has a bias attribute. If it does, we add it to the list initialized to zeros. Finally, we need to transform our list of tuples into a nested dictionary. Luckily mlx has some functions implemented for dealing with parameter dictionaries, and we can use util.tree_unflatten() to convert this list of tuples to a nested parameter dictionary. This is passed into the update method to initialize the parameters. Now we can call _init_parameters() in the constructor.

class GPT(nn.Module):
    def __init__(self):
        super().__init__()
        self.wte = nn.Embedding(vocab_size, n_emb) # token embeddings
        self.wpe = nn.Embedding(ctx_len, n_emb) # position embeddings
        self.blocks = nn.Sequential(
            *[Block() for _ in range(n_layers)],
        ) # transformer blocks
        self.ln_f = nn.LayerNorm(dims=n_emb) # final layernorm
        self.lm_head = nn.Linear(n_emb, vocab_size) # output projection
        self._init_parameters() # <-- initialize params
        # print total number of params on initialization
        total_params = sum([p.size for n,p in utils.tree_flatten(self.parameters())])
        print(f"Total params: {(total_params / 1e6):.3f}M")
    # Tensor shapes commented
    def __call__(self, x):
        B, T = x.shape # (B = batch_size, T = ctx_len)
        tok_emb = self.wte(x) # (B, T, n_emb)
        pos_emb = self.wpe(mx.arange(T)) # (T, n_emb)
        x = tok_emb + pos_emb # (B, T, n_emb)
        x = self.blocks(x) # (B, T, n_emb)
        x = self.ln_f(x) # (B, T, b_emb)
        logits = self.lm_head(x) # (B, T, vocab_size)
        return logits
    def generate(self, max_new_tokens):
        ctx = mx.zeros((1, 1), dtype=mx.int32)
        for _ in range(max_new_tokens):
          logits = self(ctx[:, -ctx_len:]) # pass in last ctx_len characters
          logits = logits[:, -1, :] # get logits for the next token
          next_tok = mx.random.categorical(logits, num_samples=1)
          ctx = mx.concatenate((ctx, next_tok), axis=1)
        return ctx
    def _init_parameters(self):
        normal_init = nn.init.normal(mean=0.0, std=0.02)
        residual_init = nn.init.normal(mean=0.0, std=(0.02 / math.sqrt(2 * n_layers)))
        new_params = []
        for name, module in self.named_modules():
            if isinstance(module, nn.layers.linear.Linear):
                if 'c_proj' in name:
                    new_params.append((name + '.weight', residual_init(module.weight)))
                else:
                    new_params.append((name + '.weight', normal_init(module.weight)))
                if 'bias' in module:
                    new_params.append((name + '.bias', mx.zeros(module.bias.shape)))
            elif isinstance(module, nn.layers.embedding.Embedding):
                new_params.append((name + '.weight', normal_init(module.weight)))
        self = self.update(utils.tree_unflatten(new_params))

We also add 2 lines of code in the constructor to print the total number of params. Finally, we are ready to build the training loop.

Training Loop
To train the model we need a loss function. Since we are predicting classes (next token) we use cross-entropy loss.

def loss_fn(model, x, y):
    logits = model(x)
    B, T, C = logits.shape # (batch_size, seq_len, vocab_size)
    logits = logits.reshape(B*T, C)
    y = y.reshape(B*T)
    loss = nn.losses.cross_entropy(logits, y, reduction='mean')
    return loss
First, we get the logits from the model. Then we reshape logits to make a list of vocab_size length arrays. We also reshape y, the correct token ids, to have the same length. Then we use the built-in cross-entropy loss function to calculate the loss for each example and average them to get a single value.

model = GPT()
mx.eval(model.parameters()) # Create the model params (mlx is lazy evaluation)
loss_and_grad = nn.value_and_grad(model, loss_fn)
lr = 0.1
optimizer = optim.AdamW(learning_rate=lr)
Next, we instantiate the model, but since mlx is lazy evaluation it won’t allocate and create the parameters. We need to call mx.eval on the parameters to ensure they get created. Then we can use nn.value_and_grad() to get a function that returns the loss and gradient of model parameters w.r.t the loss. This is all we need to optimize. Finally, we initialize an AdamW optimizer.

A quick note on nn.value_and_grad(). If you are used to PyTorch you might expect us to use loss.backward() which goes through the computation graph and updates the .grad attribute of each tensor in our model. However, mlx automatic differentiation works on functions instead of computation graphs [3]. Therefore, mlx has built-ins that take in a function and return the gradient function such as nn.value_and_grad() .

Now we define the training loop.

num_epochs=20
batch_size=32
for epoch in range(num_epochs):
    model.train(True)
    running_loss = 0
    batch_cnt = 0
    for input, label in get_batches(X_train, y_train, batch_size):
        batch_cnt += 1
        loss, grads = loss_and_grad(model, input, label)
        optimizer.update(model, grads)
        running_loss += loss.item()
        # compute new parameters and optimizer state
        mx.eval(model.parameters(), optimizer.state)
    avg_train_loss = running_loss / batch_cnt
    model.train(False) # set eval mode
    running_loss = 0
    batch_cnt = 0
    for input, label in get_batches(X_val, y_val, batch_size):
        batch_cnt += 1
        loss = loss_fn(model, input, label)
        running_loss += loss.item()
    avg_val_loss = running_loss / batch_cnt
    print(f"Epoch {epoch:2} | train = {avg_train_loss:.4f} | val = {avg_val_loss:.4f}")
The outer loop runs through the epochs. We first set the model to training mode because some modules have different behaviors during training and testing such as dropout. Then we use our get_batches function from earlier to loop through batches of the training data. We get the loss over the batch and the gradient using loss_and_grad . Then we pass the model and gradients to the optimizer to update the model parameters. Finally we call mx.eval (remember mlx does lazy evaluation) to ensure the parameters and optimizer state get updated. Then we calculate the average train loss over the data to print later. This is one pass through the training data. Similarly, we calculate the validation loss and then print the average train and val loss over the epoch.

completion = decode(model.generate(1000)[0].tolist())
print(completion)
with open('completions.txt', 'w') as f:
    f.write(completion)
Finally, we add some code to generate from our model. Since the generation output is still in the (B, T) shape we have to index it at 0 to make it 1D and then convert it from an mlx array to a Python list. Then we can pass it to our decode function from earlier, and write it to a file.

These are the parameters we will use for training (you can play around with this):

ctx_len = 128
n_emb = 128
dropout = 0.1
head_size = 128
n_heads = 4
n_layers = 3
num_epochs = 20
batch_size = 64
lr = 1e-3
Now we can run the file to start training. With the settings above training took around 10 minutes on my m2 MacBook. I achieved the following training loss last epoch.

Epoch 19 | train = 1.6961 | val = 1.8143
Let’s look at some output.

GLOUCESTER:
But accomes mo move it.

KING EDWARD:
Where our that proclaim that I curse, or I sprithe.

CORIOLANUS:
Not want:
His bops to thy father
At with hath folk; by son and fproathead:
The good nor may prosperson like it not,
What, the beggares
More hath, when that made a,
Your vainst Citizen:
Let here are go in queen me and knife
To my deserved me you promise: not a fettimes,
That one the will not.

CORIOLANUS:
And been of queens,
Thou to do we best!

JULIET:
Not, brother recourable this doth our accuse
Into fight!
Not bad for just 10 minutes of training with a tiny model that is predicting characters! It clearly has the form of Shakespeare, although it is nonsense. The only difference between our model and the real GPT-2 now is scale! Now I encourage you to experiment — try out different settings, maybe tinker with the architecture, and see how low of a loss you can achieve.

References
[1] Karpathy A (2015).Tiny Shakespeare [Data set]. https://github.com/karpathy/char-rnn (MIT license)

[2] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, I. Sutskever, Language Models are Unsupervised Multitask Learners (2019), OpenAI

[3] Automatic Differentiation — mlx docs

## Document 14
**Source**: https://blog.reedsy.com/short-story/a3gstd/

My eyes felt like galaxies—holding the swirling glow of countless memories—as I took in our childhood home. Its siding looked like remnants of driftwood after a bonfire. I swore I smelled the smoky char of pine creep into my nostrils. It’s wild how the past stays with you like that. It can feel more visceral and real than the tangible things right in front of you.

“Jesus, it feels like just yesterday.” I placed a trembling hand over my heart, struggling to steady my breath.

My brother, Perry, pulled me into a tight embrace, his strength grounding me like an anchor.

“The house hasn’t changed much,” he said, his voice steady and comforting. “But we have.” His certainty made me question, Have I really changed?

Between the two of us, Perry was as solid and stoic as a mountain range. Good thing, because I was like the wind—flighty and unpredictable. Over the years, Perry had learned to handle even my harshest hurricanes.

Being his older sister—even if only by four minutes—I always wished I’d been his protector rather than the other way around. But that demon burning deep in my belly also flashed a crooked smile, knowing that Perry would never abandon me, especially since I got sober.

I hadn’t had a drink in exactly seven hundred and thirty days, and although it remained unsaid, I knew Perry was terrified of leaving me to my own devices in fear I would relapse.

Our sibling bond was iron-clad. After we lost our parents in the fire (my mother didn’t properly butt out her 2:00 am cigarette and well, the rest is history), all Perry and I had was each other. But let’s call a spade a spade; we were also as fucked up and as co-dependent as it gets. Who mutually decides to visit the catalyst of your alcohol addiction on the anniversary of your sobriety?

The house’s dilapidated front door creaked as Perry gently pushed it open. The rusted metal hinges were holding it up by a thread.

“After you.” Perry gestured me in, squinting from the sunlight. He was a gentleman, even in such obscurity.

As he held the door open, the shallow scar on his right cheek taunted me like some kind of schoolyard bully. His wound often pulled me in like that. Some days, I was sure I would dive right into it and drown. Other days, I prayed to God and the Devil himself to just let me fucking drown, already.

That mark became permanently etched on Perry’s face on the day I quit drinking, exactly seven hundred and thirty days ago. That was the day Perry screamed bloody murder at me from the passenger seat, “Jackie! Stop the fucking car!” But my bloodstream was far too poisoned with Bacardi Limon to listen. All I remember next was my vehicle being wrapped around a tree. I could have died that day, but what truly disturbed me in the middle of the night was the fact that I almost killed Perry.

A lot can happen in seven hundred and thirty days. But I assure you, forgiving yourself isn’t one of them.

“Well? You coming in?” Perry was still holding the door ajar.

I shook it off and gave my brother a knowing glance. I swear, even though we were fraternal, we had twin telepathy. I exhaled and walked in.

“Watch your step,” I warned, my forehead tense.

I imagined the rickety floorboards collapsing, crashing us into what had once been our dad’s “man cave”. That’s where he was passed out, the night of the fire.

“Kids, stay here. Do not move,” our mother demanded after getting us out of the house safely. I remember the black soot on her face and the spiderweb veins in her eyes. She shook us firmly by the forearms. “I’m getting your father.”

Perry and I held each other, shaking. The heat from the inferno felt like standing in a volcano. We never saw our parents again.

Two decades later, there we were—Perry and I—-making our way through the wreckage of our home. It was midday, yet the inside of the house screamed a tone of pale blue midnight. My shoulders were up to my ears, as though we were walking through a haunted house attraction.

I coughed into my forearm. The ocean of dust was thick like butter. As I cleared my lungs, Perry called out from behind me.

“Jacks, look at this! The fireplace,” Perry's voice was filled with awe.

“Unbelievable. It’s still here,” I whispered, a lump forming in my throat.

It was as though a Fairy Godmother breezed by and brought the decaying living room to life with her magical paintbrush. Kind of like in “Titanic”, when they showed the sunken ship underwater, versus in its prestige as it sailed across the Atlantic.

We made our way over to the fireplace and sat cross-legged on the floor.

“This was our favorite spot, remember?” I avoided his gaze, overwhelmed by the flood of memories.

“Yeah,” Perry murmured, his eyes softening with nostalgia.

For a moment, the taste of crispy, fire roasted marshmallows superseded the saturated stench of mildew.

“Remember our s’mores nights?” I asked.

“Duh. What about all our fireplace movie nights?” Perry proceeded to do his best, nasally, childhood impersonation of me, “But mom! I want to watch Beauty and the Beast!! Perry always gets to pick the movie!!”

I punched him in the arm, “First of all, I never sounded like that. And second. So what? I knew what I wanted.”

The corners of Perry’s mouth lifted. He had such a sincere sparkle about him, as though a storm cloud of confetti followed him overhead wherever he went, “You really did, kiddo.”

My chest went heavy. How could Perry love me after everything I had done? After all the relationships I’d ruined? All the jobs I’d lost? All of his relationships I’d ruined? How could he still choose me, when so often I had chosen a forty of Jack Daniels over him?

How could Perry still love me after I almost fucking killed him?

Perry’s gaze widened, “Hey! Remember when Mom would bring out those hot drinks she always made?” He paused, almost as if he was searching for the right term. “Apple… something? Apple ssshhh…”

I snapped my fingers, “Apple-Schnapple!”

“Yes!”

“I mean, looking back it was basically just hot apple cider, but damn it was good.” And it really was.

Our laughs echoed throughout the abandoned asylum we once called home.

Perry leaned back, holding himself up with his hands. “I loved our fireplace hangs. Especially our movie nights down here. But nothing beats our movies up in the projector room.”

I tilted my head, “We never had a projector room.”

Perry playfully “shoo’d” me away.

“No. Perry. I would remember us having a projector room. Our movie nights together were our favorite thing. You even just said it yourself.”

The house suddenly became pin-drop silent as Perry leaned in. "Memories are quite something, aren’t they?" The slight shift in his tone made my skin crawl. Perry was always wistful, but this felt different, almost… clinical, "We often remember things in ways that are… easier for us to digest."

I was fidgety. “Gees Perry. You sound like Dr. Lasko.”

He seemed to enjoy my little joke.

Dr. Lasko had been my therapist since the accident, and I would go out on a limb and say that he would not have approved of this self-inflicted exposure therapy I was subjecting myself to by visiting the house.

Perry seemingly snapped out of his little therapist moment and went right back to being his sparkly confetti self. As I watched his amicable face scan the mantle above the fireplace, I felt a sickening uneasiness. Imagine you had actually fucking killed him.

“Man, I can still picture all our family photos up there,” Perry’s childlike wonder destroyed me.

My face went flush. I could feel the water rising in my eyes like the tides. How pathetic and infuriating was it that after everything I’d done, I was still somehow the victim.

“Hey.” He took my hand.

“Oh Perry,”  I threw myself into him. “I’m so sorry.”

My brother held me with his usual care that I didn’t deserve.

“Jacks, it’s ok. I’m still here. We’re both still here.”

As my chin rested on my brother’s shoulder, I looked ahead of me at the remains of the house. Something felt off, and it wasn’t just the overall unsettling environment. My brow furrowed. “Wasn’t the doorway to the kitchen on the other side of the living room?”

I felt Perry shrug, “I don’t think so.”

I was staring into the out of place doorway like I was trying to pull a recollection towards me. And that’s when I saw them in the kitchen: the translucent memory of mom and dad. Mom was getting our Apple-Schnapples ready. She was pacing, unlike Dad, who was sitting motionless at the table. His face was planted on its mahogany surface. His glass of Apple-Schnapple was empty, and so was the bottle of Jim Beam beside it.

Mom floated into the living room, our warm beverages in hand and a cigarette in her mouth, “Kids, your father’s not feeling well. Let’s have our Apple-Schnapples in here.”

Oh my God. The bruise on her face.

Perry jarred me back to reality with the gut punch of what he had to say next, “You’re remembering the truth about mom and dad, aren’t you?”

I pushed myself off and away from him. “How did you…”

My brother looked down, delicately tracing the floor with his finger, “We always put them on a pedestal after they died.”

I felt a shiver run down my spine, “What are you talking about?”

As Perry continued to speak, his words grew even more detached. "Do you remember that first drink Dad ever gave you?"

My eyes darted around the room as my jugular pulsed in my neck. As much as I tried to escape what Perry had just said, I did remember.

I could hear my dad’s slurring words of encouragement, “Come on, Jackie. Just one drink. It’ll be our special time, just you and me.”

The bitterness of that first sip of beer made me squirm, but sharing a “special time” with my dad—and the desperate yearning that maybe he did love me, afterall—was the overwhelm of the full moon swallowing me whole. I was only a child, and much like how my mom turned a blind eye to my father’s drinking, she did the exact same when it came to her daughter.

I’d used the death of my parents as the excuse for my alcoholism for so long, because admitting that they helped create the monster I would eventually become was like a knife to the heart. And knowing I had been too weak to conquer the addiction from my own volition just made the weapon twist in my chest.

The room was spinning. My face was blistering hot like the night of the fire. Or was that the warm heat from the fireplace when we were kids? The childhood fireplace memories ran through my mind, frame by frame, until…..they eventually vaporized to nothing. I crouched over, thinking I might vomit.

“We never had a fireplace.” Perry was nodding, very matter-of-factly.

My fingernails dug into my thighs when I looked at the fireplace and: it was gone. Only a blank wall of faded, forest green wallpaper remained. Our house was once on fire, yes, but that was it. There was never a happy childhood fireplace. Ever.

My hands were cold and clammy. I fell back onto the wall behind me. “Perry. Where are we?”

He stood up and glided towards the staircase. One hand on the banister, his footsteps creaked, one by one, as he made his way to the second floor.

My mouth was bone dry, “Perry!”

He stopped and turned towards me, “Come to the projector room. We love watching movies together, don’t we? There’s a movie I’d like to show you.”

As my brother disappeared from sight, I did what any classic horror movie trope would tell you to do: I went upstairs.

I found Perry standing at the end of the ominous hallway. Large, empty picture frames lined the oxblood walls leading up to him. Through the doorway where Perry stood, particles in the air danced in the projector’s cone-shaped light. That telltale winding of a film reel was the only sound in the deafening quiet of this house that I no longer recognized.

Half of Perry’s face—the one with the scar—was perfectly illuminated, as though he was wearing the mask from “The Phantom of the Opera”. “I think you’re ready to see how this movie ends, Jackie. This is the most progress you’ve made since we’ve been coming here.”

I gripped my thumbs in the palms of my hands, “Perry, you’re freaking the fuck out of me!”

I thought my knees might buckle as my brother’s face glitched, like a flash of static snow on a television set. As his face settled back to normal to a deadpan gaze, he disappeared in the innocuous room. I followed, running on nothing but fumes.

Clutching the doorway, my mouth fell agape. Perry was gone. I darted to the middle of the room.

As I frantically searched for my brother, I shielded my eyes with the back of my hand from the projector’s light. And that’s when, from behind me, I heard five words that made my blood run cold, “Jackie! Stop the fucking car!”

I was convulsing yet paralyzed. Moving as slowly as cold molasses, I rotated on the spot towards my worst nightmare, shown on 35 mm. On the projector screen was Perry and me in my car, exactly seven hundred and thirty days ago, the day I almost kill—

Oh my God.

My head pounded as fragmented memories surged. The reality of what happened began to crystallize, unrelenting.

My joints ached and my stomach churned. Clamping a hand over my mouth to stifle a scream, I stumbled down the hallway as it began caving in on itself. The picture frames were sucked into the walls. The floorboards cracked into distorted peaks and valleys. Wooden beams swung down from the ceiling like pendulums. I tried to spit out the chalky grit of disintegrating drywall that made the hallway look like a winter squall.

Panting heavily, I stopped dead in my tracks at the stained glass window. My body trembled with an all-too-familiar dread. Each time I faced this, I wondered if this fall would be the one that would finally end it all.

Maybe it’d be better if it did.

Holding my breath, I threw myself through the glass, my hands clawing the air for dear life. Free falling two stories feels like an eternity when you’re watching the memory of your childhood home fall apart before your very eyes. But when the weight of my body finally made contact with the earth I—

I gasped. The cold air of the hospital room shocked my lungs. I sat up, ripping the suction cups from my face and body. My gown was clinging to me, soaked in sweat. Medical equipment beeped all around me like a metronome.

Dr. Lasko, my therapist since the accident, sat across the stark white room, sighing as he rubbed his forehead. He, too, was connected to a plethora of suction cups and wires. He looked a little worn out in the fluorescent overhead lighting. Ever since I was hospitalized and later incarcerated, Dr. Lasko had been helping me delve into my memories, namely the ones that were too excruciating for me to face. And as such, Dr. Lasko had been appearing in the simulations as my brother Perry, the love of my life who died in the car crash, seven hundred and thirty days prior.

Disoriented, I blinked rapidly, the vividness of the memory contrasting sharply with the sterile, geometric ceiling tiles above me.

“I don’t ever want to do that again!” I was venomous.

“Jackie,” Dr. Lasko started.

“Don’t start,” I pulled up four fingers for air quotes, “‘Jackie, don’t give up. This was the closest you’ve ever come to facing the truth.”

As the initial burst of adrenal and cortisol left my body, I fell back on my pillow. I was depleted. Quiet rivers flowed down my cheeks.

Removing his own suction cups, Dr. Lasko approached my bedside and took a seat. He treaded lightly. “Jackie, I understand how challenging this is for you, but you did an incredible job today. If we continue making progress like this, there's a real possibility you'll gain your freedom sooner.”

I looked at the well-meaning doctor, but all I could see was Perry. Multicolored confetti fell softly around him like that first November snow. His face was the sun. His eyes reflected the whole world back to me.

Perry.

With a weak grip, I took Dr. Lasko’s hand. My vocal cords were like sandpaper. “I’ll leave this place one day, doc.” A single tear dripped from my chin onto my collarbone. “But I’m not sure if I’ll ever be free.”

Dr. Lasko didn’t say a word, but I felt him squeeze my hand, just a little bit tighter.

I licked the cracks on my lips as my eyes closed shut, imagining the oaky comfort of bourbon on my tongue. I felt myself drift, and good thing, because I needed the rest. Dr. Lasko and I would be delving into my memories again the following day.

No matter how masochistic it felt, I vowed to keep showing up for the simulations. Even if I never forgave myself for what I did, at least in my memories, I got to see Perry.

## Document 15
**Source**: http://www.chakoteya.net/DoctorWho/40-1.html

Space Babies

Original Airdate: 11 May 2024

[Tardis]
(Ruby has walked into the unlocked Tardis at the end of The Church on Ruby Road.)
RUBY: Who are you?
DOCTOR: I'm the Doctor. You don't have to stand over there. Come and have a look. It's called the Tardis.
(Snaps his fingers and the lighting changes.)
RUBY: Ooo! Nice! But hold on. I can't call you Doctor. No, I want to know your name.
DOCTOR: Yeah, that's er... that's tricky, because I was adopted, and the planet that took me in, they were kind of... they were kind of posh. They'd use titles like the Doctor, or the Bishop, or the Rani, or the Conquistador. Say Doctor for a thousand years and it becomes my name.
RUBY: Okay. The planet. Parking that. Thousand years, double parked. So you're a doctor, but you're... the police?
DOCTOR: Police box. No. No, no, no, no, that's a disguise.
RUBY: Oh.
DOCTOR: Inside, it's a Time and Space machine, but outside, it's like a chameleon, 'cos once I landed in 1963 and they used to have police boxes on street corners.
RUBY: 1963?
DOCTOR: Yep.
RUBY: Okay. Ooo, jukebox. I like that.
DOCTOR: Mmm.
RUBY: Okay, so, back to the planet.
DOCTOR: My world was called Gallifrey.
RUBY: Gallifrey? And where's that?
DOCTOR: Gone! Ruby, it's gone. It's gone. They died. There was a genocide, and they died. So the one that was adopted was the only one left. I am the last of the Time Lords. And I am so, so glad to be alive. This thing flies. Do you want to see?
(The gravity goes off, the Tardis dematerialises, gravity back on. Never done that before.)
DOCTOR: Let's have a random landing.
RUBY: Whoa!
DOCTOR: Hoo-hoo! Ooo... 150 million years in the past.
RUBY: No!
DOCTOR: Really.
RUBY: No, you've got to be k... You are kidding. Don't be so ridiculous. Are there dinosaurs out there?
DOCTOR: I don't know. Go and have a look.
RUBY: Wait! No. Is it safe? What if I change history by stepping on a butterfly or summat?
DOCTOR: Well, that's not going to happen, is it? Who steps on butterflies? You'd literally have to be like, "Wait. Come 'ere, butterfly! "Come 'ere, 'ave it!"

[Prehistoric Earth]

RUBY: Oh, my God. That... that's so beautiful.
DOCTOR: And Tardis stands for Time And Relative Dimension In Space, huh? So we've moved location as well. This will be North America. One day, this is Wyoming. A little town called Green River.
(A boot steps on a butterfly.)
DOCTOR: Oh!
(Ruby is no longer a human.)
RUBATHON: What's wrong? Did I do something wrong? Because I am Rubathon Blue of the 57th Hemisphere Hatchlings, and I do not do wrong things, Dok-tah.
DOCTOR: But...
RUBATHON: If you have made an incorrect accusation, I will have to kill you.
DOCTOR: No, no, no. Just wait, wait a minute. Just...
RUBATHON: What are you doing?
DOCTOR: Nothing, just...
(He scoops up the butterfly, breathes on it, and it flies off. The human is back.)
RUBY: Am I missing summat?
DOCTOR: Nothing. Let's try that again, okay?
RUBY: Thank you.
DOCTOR: Yeah. Yeah, yeah, yeah.

[Tardis]

DOCTOR: Okay. Controls are new. Completely forgot... the butterfly compensation switch. Good. Right. Yes. Let's go forward. Give me a number. Give me a year.
RUBY: Er, two.
DOCTOR: Two.
RUBY: One.
DOCTOR: One.
RUBY: Five.
DOCTOR: Five.
RUBY: Oh.
DOCTOR: Oh.
RUBY: Ah, six!
DOCTOR: Six! Ah! Five numbers! I like it!
(The Tardis travels the Vortex.)

[Space station]

RUBY: But we're indoors. We got through walls. Ah-ha. Is that like a matter transporter, like in Star Trek?
DOCTOR: We've got to visit them one day.
RUBY: Hey, but you said the Tardis was like a chameleon, but it still looks like a police box.
DOCTOR: Oh, it's, er... it's broken. Most of the universe is knackered, babes. Okay. Come, come, come, come.
RUBY: Oh, it stinks
DOCTOR: Something is wrong with this place. It is a space station reaching overload. Whoa! Whoa!
RUBY: No, you've made it worse.
(Something snarls nearby. They both jump.)
DOCTOR: No, that is worse.
RUBY: Is that a monster?
DOCTOR: No. No, don't be silly, Ruby. There's no such thing as monsters, there's just... just creatures you haven't met yet. Hi there.
(The creature roars.)
RUBY: Run?
DOCTOR: Run! Run! Run!
(They and the monster are visible on monitors as they run down passages.)
DOCTOR: Come on! In here, in here, in here, in here.
RUBY: But...now we're trapped! Now we're trapped! Push the button! Doctor!
DOCTOR: Okay.
(The tiny one-person lift takes them up. The Doctor's hand is over Ruby's eyes.)
DOCTOR: Oh, yeah, yeah.
(The lift abruptly arrives.)

[Birth Zone 6]

DOCTOR: The question is, why did I run?
RUBY: 'Cos it was scary.
DOCTOR: It was new. I love meeting new things, so why did it give me the shivers? I couldn't run fast enough. I was like whoosh!
RUBY: Well, it'd help if we knew where we were.
DOCTOR: Yet again, push the button.
(The lights come on so they can see all the glassware, containing...)
DOCTOR: Oh. Oh, we're on a baby farm. Ha-ha! A parthenogenesis machine. What is it with you and babies?
RUBY: I was going to say the same thing to you.
DOCTOR: We've gone from baby to baby. I'm not saying things are connected, and yet... things connect.
RUBY: Well, I'm the one looking for my parents, and you've got a Time and Space machine. So this place grows babies. What for? Food?
DOCTOR: Food? What? What?! Food? They're not tomatoes!
RUBY: Well, excuse me. There's a big hungry thing downstairs.
DOCTOR: Baby farms boost the population. Sometimes a world goes sterile or... I don't know, goes mad and bans kissing.
RUBY: So these babies are human, yeah?
DOCTOR: Yep, grown for a colony world.
RUBY: And a colony world is not Earth?
DOCTOR: Hey. Okay, one last time, push the button.
(And a shield retracts to reveal that they are in orbit.)
RUBY: We made it. The human race, we survived. We went to the stars. And ten minutes ago, Doctor, just ten minutes ago, you said genocide. Your people are gone.
DOCTOR: Yeah.
RUBY: How do you keep going?
DOCTOR: For days like this, Ruby Sunday. I don't have a people. I don't have a home. But I don't have a job, either. I don't have a boss, or taxes or rent or bills to pay. I don't have a purpose or a cause, or a mission, but I have... ..freedom. And so I keep moving on, to see the next thing, and the next, and the next. And sometimes... it looks even better through your eyes.
RUBY: So where's this, then?
DOCTOR: Oh, er...
(Calls it up on a screen.)
DOCTOR: Huh. Planet Pacifico del Rio.
RUBY: Oh, that's in English. They speak English here? English exists?
DOCTOR: Er, no. No, no, no. Humans all speak one language by this point. A bit like Cantonese. This is what it really looks like, but the Tardis translates. It's got a perception filter, so it helps you fit into every time and place.
RUBY: Right, and my mum, she's long gone now.
DOCTOR: Can I see your phone?
RUBY: Yes.
DOCTOR: So, my sonic screwdriver can make the distance between you and Earth 19,000 years or... one phone call.
RUBY: What?
DOCTOR: Carla. Phone her.
RUBY: But...
DOCTOR: Your mum, Ruby. Call your mum.

[Ruby's home / Birth Zone 6]

CARLA: Well? What is it now?
RUBY: Mum?
CARLA: Yes, Mum, obviously. You've just ran out the door ten seconds ago. Why are you phoning me? You went like the wind. Where are you going?
RUBY: Yeah. Yes, I will... I'll, er... I'll catch up with you in a minute. Bye. Love you. Love you. Merry Christmas!

[Birth Zone 6]

RUBY: That was my mum, on Christmas Eve. On my birthday, ten minutes ago. That's the best signal ever. How much does that cost?
DOCTOR: I want to know what the hell is wrong with this place. Do you see? It's calm up here, but underneath it is seething, just like downstairs with that creature. There's got to be a crew or a captain...
(Enter a child in a motorised push-chair.)
ERIC: This is Eric, reporting from Birth Zone 6. I keep getting these temperature fluctuations. I've opened up safety valves 10 to 16. Tried cross-matching with the CO2 exchange, but until we get that pressure down, I can't...
DOCTOR: Hi.
RUBY: You all right?
ERIC: But... you. Oh. We've been waiting for an awfully long time. Mummy! Daddy!
DOCTOR: Oh, no.
RUBY: No, no. No, darling, we're not...
ERIC: Boys-oh-boys, I've got to tell everybody Mummy and Daddy are here.
(Leaves the room.)
RUBY: A baby farm. Run by babies.
DOCTOR: Ha-ha! Space babies!
(They follow Eric along a corridor with crayon drawings on the lower part of the wall.)

[Control room]

ERIC: They're here. They came at last. Mummy and Daddy are here.
(All the crew are in electric pushchairs.)
BABIES: Mummy and Daddy! They came back!
DOCTOR: Hello, space babies.
BABIES: Hello, Daddy. Hi, Daddy. Hello, Daddy!
DOCTOR: Oh.
POPPY: Everyone, back to work. Show Mummy and Daddy what a good job we've been doing. Make them proud.
(The controls are jury-rigged with string and wooden pointers so the babies can activate them.)
MARCEL?: My job is to keep the pipes clean. I'm proud of the pipes.
ADJANI?: And I keep the oxygen nice and cool. We need oxygen to breathe.
SANDRA?: And I pull this string and that string. I'm not sure what they do, but I pull them very hard.
ERIC: And I made this for you. It's a little flower.
RUBY: Thank you.
POPPY: I'm Captain Poppy and I kept the station running for Mummy and Daddy, because we knew you'd come back for us one day. We waited.
DOCTOR: Right. You're not supposed to be running this place. This isn't Baby World. You got left behind when the adults... ..vamoosed?
POPPY: We took over. We were very brave.
RUBY: Right. That's great. That's, oh, that's good. That's amazing. You've done a really great job.
DOCTOR: I'm sorry, Poppy, I'm so sorry, but we are not your mummy and daddy. I wish we were, but we're not.
ERIC: They left us. Where did they go?
RUBY: I don't know, darling, but... I'm Ruby and this... this is the Doctor. And we're your friends. Yeah, got you. I've got you, I've got you, I've got you, I've got you.
(She picks up Eric from his pushchair.)
BABIES: And me! And me! And me! And me!
DOCTOR: Oh, gosh.
BABIES: And me! And me!
DOCTOR: Captain Poppy, when was the last time that you had a hug?
POPPY: Never.
DOCTOR: Oh. Oh, baby, it's okay. Come here, it's okay. It's okay, it's okay. Shh-shh-shh. Aww, never had a hug.
RUBY: Come on, you can all have a hug.
(Later, with everyone back in their pushchairs.)
POPPY: Did I get things wrong, Doctor
DOCTOR: Well, according to this, the crew went home. They abandoned ship and they left you guys behind. I don't know why, but they left the birth machine running, so you lot grew up, but you stayed the same size. Baby size. Space babies.
POPPY: But are we wrong?
DOCTOR: What do you mean?
POPPY: We're not meant to be like this. Did we grow up wrong?
DOCTOR: Oh, Poppy. Oh, Popsicle. Look at me. Look at me. Nobody grows up wrong. You are what you are, and that is magnificent.
POPPY: But Mummy and Daddy left us.
DOCTOR: That's okay. Mine did, too.
POPPY: What happened?
DOCTOR: Well, I was found.
POPPY: Hooray!
DOCTOR: Yeah. Little baby me was left alone in the middle of outer space, and guess who took me in.
POPPY: I don't know.
DOCTOR: The Time Lords.
POPPY: Ooo.
DOCTOR: Can you say it like me?
POPPY: The Time Lords.
DOCTOR: That's it, P-P-P-P-Pop. But the point is, is that it doesn't matter where I come from, because I am absolutely lovely, aren't I?
(Poppy yawns.)
DOCTOR: That wasn't rhetorical, Pops.
POPPY: Yes, you are.
DOCTOR: And do you want to know my secret? There's no one like me in the whole wide universe. No one like me exists, and that's true of everyone.
It's not a problem, Captain Pops. It's a superpower. High five. Yeah.
POPPY: Yeah!
(Ruby is dandling Eric, with the other babies in a semi-circle.)
RUBY: So you're Eric. And you're Tasha. And Ruben. And then there's Saltine and Boo.
ERIC: I love you, Ruby.
RUBY: Aw, I love you too, Eric. But how do you manage all on your own?
ERIC: We've got Nanny. Say hello, Nanny.
NAN-E: Good afternoon, children, and welcome to our new visitors.
DOCTOR: Oh. Nanomatrix Electroform. Nan-E. Right. Hi, Nan-E. I'm the Doctor, and this is Ruby.
NAN-E: We have visitors, children.
ERIC: Nanny!
NAN-E: Noses must be blown. Activate nose-blow.
DOCTOR: Er...
NAN-E: One, two, three and... blow.
(Mechanical hands on the pushchairs put handkerchiefs to the babies' noses. They blow into them, then the dirty handkies are dropped into a disposal tube.)
NAN-E: Well done, children And now, children, back to work. Nappies are changed at 1800 hours.
RUBY: Oh, can't wait to see that.
DOCTOR: Right. So it's you lot? It's Nan-E And downstairs, is that your pet dog?
(Everyone screams and cries.)
ERIC: That's not a doggo.
RUBY: What is it then, Eric?
ERIC: The Bogeyman.
RUBY: Shush, shush, shush. Shush, shush, shush.
DOCTOR: No. Gosh.
ERIC: We don't like the Bogeyman.
RUBY: No, no, no. Shush, shush. I did not mean to scare you. There is no such thing as the Bogeyman. That thing was more sort of like a er...
DOCTOR: Bogeyman!
RUBY: No, stop it! No, stop it! Nan-E, tell them there's no such thing as the Bogeyman.
NAN-E: Nan-E is scared of the Bogeyman.
DOCTOR: Then what is the Bogeyman doing down there, and why... why is it so scary?
(Puts it on monitor. The babies wail.)
RUBY: Doctor, turn it off.
DOCTOR: Okay.
RUBY: No, listen to me. Listen to me.
DOCTOR: I'm sorry, I'm sorry. I'm sorry, babies. Space babies. I'm sorry.
POPPY: Oh, Ruby...
(The Doctor finds a headset and puts it on, then works a computer.)
DOCTOR: Right. Nan-E. These babies are trying their best - space babies - but this station is in trouble. You have got a build-up of pressure in Hull 3-B. Something is ramping up down where the Bogeyman lives. And if that continues... baby boom.
NAN-E: Portal 3-5-7.
DOCTOR: Okay, what's that?
NAN-E: Access Portal 3-5-7.
DOCTOR: That's on this floor. What is it?
NAN-E: Access Portal 3-5-7.
DOCTOR: Yeah, it is just a storage unit. What would I need to go there for?
NAN-E: Oh, for God's sakes, 3-5-7. Come on!
RUBY: Where do you think you're going?
DOCTOR: Portal 3-5-7!
RUBY: Right. Great. Ok. Coming!

[Corridor]

RUBY: So, is this what you do, Doctor? I mean, in life? You help? That's like your... purpose?
DOCTOR: No, no, I'm just, er... helping babies - space babies. Ha! Listening to my hearts. Two hearts. Plural.
RUBY: Okay. Two hearts. But what if helping the babies takes six weeks? Or ten years? Because my mum's still waiting for me.
DOCTOR: Back home, on your birthday. Yeah, it's strange, your life. You were abandoned, like this lot. If things connect, then you are connecting like crazy. You don't know anything about your birth mother or your father? They didn't leave a note or a scrap of paper...?
RUBY: Nothing. I was... I was just left.
DOCTOR: By the church.
RUBY: In the snow.
DOCTOR: On Ruby Road.
(The Doctor sees a figure point at him by the church.)
RUBY: Doctor...
DOCTOR: What?
RUBY: It's snowing. Okay, what just happened? I said snow, and we've got... ..snowflakes.
DOCTOR: It's like a memory just came through, from the day that you were born.
RUBY: But how? Is this the sort of thing that happens with time travel?
DOCTOR: I have been to the ends of time and back, and I have never seen anything like this before.
RUBY: Then what does it mean?
DOCTOR: I don't know.
(The snow has stopped.)
DOCTOR: Oh, I thought my birth was crazy...
RUBY: Oh, yeah.
DOCTOR: Oh... I wonder who she is. Your mother. The memory changed. She was pointing at me.
(A door opens.)
JOCELYN: I said Portal 3-5-7. Don't just stand there yapping, you pair of idiots. Get inside!
RUBY: Who's she?
DOCTOR: Nan-E. Ha!
RUBY: Oh.

[Portal 357]

RICO [on screen]: This is Captain Rico Trieste, signing off duty from Babystation Beta, Pacifico date 56-56-22. For the record, I'm signing off under protest and wish to condemn this course of action.
LUCIA [on screen]: Chief Engineer Lucia Colasanto signing off, 56-56-22. And I'd like to say for the record, the company's actions are appalling. I will be launching an appeal against this as soon as we're home.
(Jocelyn fixes a gas leak with a blow from a wrench.)
GINA [on screen]: This is Comms Officer Gina Scalzi signing off, 56-56-22.
(Played by Susan Twist. She keeps turning up, does this woman.)
DOCTOR: So the crew went home, and left the babies behind? Space babies.
JOCELYN: It's the recession. The government closed the Babystation to save money, but the law says it's illegal to stop the birth machine.
(Another leak, another thump with the wrench.)
JOCELYN: But how did you arrive? Have you got a way out of here?
DOCTOR: I've got a ship, yeah, it's er... What is your name - sorry, Nan-E?
JOCELYN: Jocelyn, Jocelyn Sancerre. I was the on-site accountant. I don't know how this place works.
(The Doctor plugs his sonic into the computer.)
DOCTOR: Jocelyn, hold on, hold on, hold on. This... this can help. If you leave this to sync up, that should recalibrate the whole shebang.
JOCELYN: Thank you. Wanna swap?
RUBY: Hang on. So the planet down below refused to stop the babies being born... but once they're born, they don't look after them?
JOCELYN: It's a very strange planet.
RUBY: It's not that strange.
DOCTOR: But you stayed behind.
JOCELYN: I couldn't leave them. And I tried with this place. But I'm not an engineer. The machine went out of sync, I patched it back, but then the education software ran out of control. It's a mess. And I've been all on my own, watching the kids, for six years.
DOCTOR: But I don't understand. They are gorgeous. Why would you hide?
JOCELYN: Cos I don't want to see them die. And I don't want them to see me die. 'Cos that's how bad it is. This is a closed station. There's only so much air. There's only so much food. The last thing I'll do is give them the air out of Portal 3-5-7. But then... ..then you came along.
RUBY: Can't you fly somewhere else?
JOCELYN: What do you mean, fly?
DOCTOR: Er, space station. Stationary, no engines. This great big thing can't move. It's just stuck in orbit, which is a shame, because this is a nice little system.
JOCELYN: The fifth planet out, Mondo Caroon, that's a DuBarryDuPlessy world.
DOCTOR: Oh, that's good. DuBarryDuPlessy is a starwide organisation. It means they can take in lots of refugees.
RUBY: Oh. Well, can't we call them for help?
JOCELYN: They don't go and fetch refugees. That's the fate of every refugee in the universe. You physically have to turn up on someone else's shore. And we can't move.
DOCTOR: But now you have a ship. Plenty of room. It's called the Tardis. The trouble is, between us and the ship is the Bogeyman.
JOCELYN: What is that thing?
BOTH: You don't know?
JOCELYN: It's nothing to do with me. It's not part of the manifest. It's not like anything I've ever seen.
DOCTOR: No, nor me. But it reminds me of something. What is it? And what is its skin made of? And why... was I so scared?
JOCELYN: Because it's terrifying.
DOCTOR: Yeah, but I've met a million ugly bugs. I'm an ugly bug. That thing made me run, and I just wonder why.
RUBY: Okay. Thing is, this place is completely mad, but it sort of makes sense. Because you've got babies, you've got a nanny, and you've got the Bogeyman. You've literally got a monster living down below. It's a children's story come to life.
DOCTOR: And every story has its hero.
(They spot someone on the screen.)
RUBY: That's Eric. Is that Eric?
JOCELYN: Eric, get out of there.

[Space station]

NAN-E: Eric, please vacate this area.

[Portal 357]

DOCTOR: Oh, is that how it works?
JOCELYN: Nan-E filter. Eric, get out now.

[Space station]

NAN-E: Eric will leave immediately.
ERIC: No, Nanny! I'm being brave.

[Portal 357]

JOCELYN: Eric, for God's sake, run!

[Space station]

NAN-E: Eric, invoking the deity, accelerate perambulation.
ERIC: I'm doing what Ruby said.

[Portal 357]

RUBY: What?

[Space station]

ERIC: I love Ruby, and she said there's no such thing as the Bogeyman. So I'm going to find the naughty doggo and tell him off.
(He meets the Bogeyman.)
ERIC: But I'm so scared.

[Portal 357]

RUBY: Oh, my God, it's my fault!

[Birth Zone 6]

RUBY: Eric, I'm coming! I'm coming! I'm coming! I'm coming! I'm coming! I'm coming!

[Space station]

(Ruby and the Doctor take the little lift down, and find Eric's pushchair fallen over.)
RUBY: Oh.
DOCTOR: Nan-E, where's the Bogeyman?

[Portal 357]

JOCELYN: It's about 400 metres north-west of you. But still no sign of Eric. I can't get a proper fix. I told you, these systems are a crock of...

[Space station]

NAN-E: ..waste products.
DOCTOR: Mind your language, Nan-E.
RUNY: Okay, Doctor, if we make a ton of noise, then the Bogeyman will come for us and leave Eric alone, yes?
DOCTOR: Yes.
RUBY: Okay, right.
DOCTOR: Yes. Yes, yes.
(They pick up things to hit the pipework with and move off.)
RUBY: Bogeyman! Bogeyman!
BOTH: Bogeyman! Bogeyman!

[Portal 357]

JOCELYN: It's moving. It's heard you.

[Space station]

RUBY: Okay, nice plan, but what now?
DOCTOR: I think... if I was very, very little and I knew the Bogeyman was coming... I would need to change my nappy. 'Cos I can detect...
(In a locker.)
DOCTOR: Space baby! Oh, Eric.
RUBY: We've got you, we've got you.
DOCTOR: Oh, you poor thing. It's okay.
RUBY: I know, I know. I know.

[Portal 357]

JOCELYN: Not west, I meant east.

[Space station]

DOCTOR: Go, go. It's all right, it's all right. It's all right, it's all right, it's all right. All right, all right. It's all right.
RUBY: It's okay, it's okay.
DOCTOR: All right.
(The Bogeyman moves off. They come out of hiding, and there it is. They run.)

[Portal 357]

JOCELYN: Don't you touch them, you...

[Space station]

NAN-E: ..illegitimate person.
DOCTOR: Go! Go. It's a dead end.
(The Bogeyman is there.)
DOCTOR: Whoa! It's okay, it's okay. You're okay.
(The Bogeyman is attacked by flames. It runs away.)
POPPY: Babies to the rescue!
DOCTOR: Ha! Space babies!
RUBY: Babies with a flame-thrower!
DOCTOR: Babies, babies, babies, you did brilliant! You did so great! Space babies, you need to go, okay? Get.. get out of here.
(He whistles up Eric's pushchair.)
RUBY: Okay, let's get you in here, come on. Let's get you in there. Nan-E, tell them what to do.
NAN-E: Children will return to the upper levels or have no expletive dinner.
BABIES: Goodbye.
DOCTOR: Okay, er, you... you go with them. I've got to stay here. Not just for the Tardis, but I've got to find out what that thing is.
RUBY: If that's you telling me to leave you on your own, then... Oh, Doctor. Well, come on.
(They head back through the stinky area.)
DOCTOR: Ooo! Whew! Whew! So how did this begin, Jocelyn?

[Portal 357]

JOCELYN: First I knew, six years ago, it was like a rattling in the pipes. Then the howling began. By the time I got the cameras working, there it was. The Bogeyman. I don't know how it even exists.

[Space station]

RUBY: And that was six years ago?
DOCTOR: Shh-shh-shh.
RUBY: Oh. That's the same time the babies were born.
DOCTOR: It's leaving... some sort of spoor. Man, that's a good word. Spoor.
NAN-E: What the bleep-bleep is that?
RUBY: Oh, Jocelyn, turn the filter off.

[Portal 357]

JOCELYN: What is that stuff?
DOCTOR (on screen): If I could get this to your machine, it could analyse it.
JOCELYN: The machine's got a vent in the basement. Follow the corridor. Left, straight ahead, left again.

[Space station]

DOCTOR: Into the belly of the beast. Yeah, this stuff is slippy, Rubes. Be careful.
(She slips then gets dribbled on from a pipe outlet.)
RUBY: Oh. Ah. Oh, my God. Oh, this is disgusting. Don't call me Rubes!
DOCTOR: Are we almost there, Joce? This gunk stuff is sealing the whole place off. Oh, but never mind, because... Ah! We are right under the parthenogenesis machine. Now, let's make sense of this thing. Ah, according to the machine... Oh.
RUBY: What?
DOCTOR: It has been right in front of us. We've been saying it all along. It's all one machine. One up above, and one down below. The one up above grew the babies. The one down below...
RUBY: It grew the Bogeyman.
DOCTOR: Yes!
RUBY: I said this. I told you so. Six years ago, the machine is mother and father to the babies, and mother and father to the Bogeyman.
DOCTOR: And why? Because Jocelyn said that the educational software ran out of control, and then you said...
RUBY: It's like a story. The teaching software, it told a story.
DOCTOR: It invented the Bogeyman.
RUBY: For the babies.
DOCTOR: For the space babies.
RUBY: The machine is literal, like a computer. It literally said, "Babies need fiction, they need stories, they need monsters."
DOCTOR: Yes. That is why I'm so scared. It's all deliberate, it's infrasound. The Bogeyman is roaring at 17 hertz, that's the exact pitch designed to make you scared. It's scary because it's meant to be. The machine made it tall and big and noisy, and it built it out of... Oh.
RUBY: What.
DOCTOR: Oh, Ruby.
RUBY: What?
DOCTOR: Oh, man.
RUBY: Tell me what it is.
DOCTOR: I can't.
RUBY: Doctor!
DOCTOR: Ruby, I have travelled the universe and back and seen many, many things. Nothing... is as bad as this. A Bogeyman is made out of what?
RUBY: I don't know.
DOCTOR: The machine is literal, and the name is Bogeyman.
RUBY: So?
DOCTOR: Oh, babes. Space babes. We saw it. The nose-blowing. The machine was literal, and so it grew the Bogeyman out of bogeys.
RUBY: What?
DOCTOR: All of this is bogeys.
RUBY: No.
DOCTOR: Yes.
RUBY: No.
DOCTOR: Yes.
RUBY: No.
DOCTOR: No wonder it was shedding its skin. Doesn't everyone?
RUBY: No, no, no, no.
DOCTOR: It's snot.
RUBY: It's not.
DOCTOR: Oh, Ruby, it is a living sneeze!
RUBY: But it's in my...
DOCTOR: I know.
RUBY: Oh, my God! This is the worst thing that has ever happened to anyone! Don't laugh!
DOCTOR: Sorry. Oh, isn't the universe mad?
RUBY: Oh yeah, it just made a monster out of snot.
DOCTOR: Oh, Ruby Sunday, Monday, Tuesday, that is... so funny.
(The monster is in front of them.)
RUBY: Bogeyman.
DOCTOR: Run. Run! Go!
(A barrier blocks their path.)
DOCTOR: No, no, no, no!

[Portal 357]

JOCELYN: Don't worry, it's me. Turn right. It's your device. It's calibrated. It's brilliant! I've got control at last. Now trust me. Turn right!
DOCTOR [on screen]: This isn't the way to the lift!
JOCELYN: Keep going.
(She unlocks doors remotely.)

[Space station]

RUBY: Ah!
DOCTOR: Go, go, go, go!
RUBY: I'm coming, I'm coming!

[Portal 357]

JOCELYN: It's catching up!

[Space station]

RUBY: Coming!
(A door slides closed between them and the Bogeyman.)
DOCTOR: Whoa!
RUBY: Yeah, thanks for using us as bait. Just next time ask!

[Portal 357]

DOCTOR [on screen]: Oh, wait until we tell you what that thing is made of!
JOCELYN: You can tell me later. Once I've got rid of it. I will protect my children and blast that thing into space!

[Airlock door]

DOCTOR: It's an airlock.
(The Bogeyman is hanging on for dear life.)
DOCTOR: It is one of the children, Jocelyn! I... She's got the sonic. Jocelyn, Jocelyn!
COMPUTER: Oxygen field at 10%.
DOCTOR: Okay, okay, okay, okay. We haven't got time. Stop Jocelyn, yeah?
RUBY: Wait...
DOCTOR: Left, second right, next left, you'll get to the lift.
RUBY: What about you?
DOCTOR: Left, second right, next left!
RUBY: Right, okay.
(She runs off.)

[Control room]

COMPUTER: Oxygen field at 9%.
POPPY: You're hurting him.
ERIC: Stop it, Nanny. Stop it!
COMPUTER: Oxygen field at 8%.

[Airlock door]

DOCTOR [memory]: I am the last of the Time Lords.
RUBY [memory]: How do you keep going?
DOCTOR [memory]: For days like this. I'm the only one of me in the whole, wide universe. No one else like me exists, and that is true of everyone.
DOCTOR: The only one of its kind.
COMPUTER: Oxygen field at 7%.
(The Doctor opens the airlock door and holds it open with his body.)
COMPUTER: Oxygen field at 6%.
(Then he goes inside, hanging on, with the Bogeyman just beyond reach.)
COMPUTER: Oxygen field at 5%. Oxygen field at 4%.
(Then he lets go, and lands on the hull between the open outer door and the big red button.)
COMPUTER: Oxygen field at 3%.
DOCTOR: Push...the button.
COMPUTER: Oxygen field at 2%. Venting reverse. Venting reverse.

[Portal 357]

(Ruby runs in and grabs the sonic.)
JOCELYN: No!
RUBY: That's what you do, Jocelyn. You save them all.
COMPUTER: Oxygen field at 1%.
(The outer airlock door is closed, the air stops rushing out. The Doctor and the Bogeyman drop to the floor.)
RUBY: You save them all. Come here. It's okay, it's okay.
(Jocelyn cries in Ruby's arms.)

[Control room]

DOCTOR: Attention! Calling Captain Poppy. Calling all crew. Especially you, Eric. Plus Ruby and Jocelyn Sancerre.
ERIC: Nanny was really naughty.
JOCELYN: I know, and I'm so sorry. All of you. I was just... on my own for such a very long time.
ERIC: We still love you, Nanny.
BABIES: Yay! We do!
DOCTOR: But-but-but-but-but-but... your favourite monster is fine. Look. Look, look, look, look.
BABIES: Yay!
(On a monitor, the Bogeyman howls like a wolf, and the babies copy it.)
DOCTOR: But listen, listen, babies, space babies, your world is over here.
BABIES: Wow!
DOCTOR: The world of Mondo Caroon. But... but you can't get there. Got no engines! Except, turns out, that build-up of pressure in Hull 3-B is from you.
BABIES: Huh?
DOCTOR: Huh? 'Cos the system went wrong, and that's where it stacked up all your nappies. No wonder it was stinking down there. For six years, a great big pile of sh...
JOCELYN: Nan-E filter.
DOCTOR: ..shizzle. A zillion metric tonnes of methane, babies. Space babies. But I am going to let it rip!
(The waste gets vented in a massive grey cloud, and the space station gets propelled out of orbit.)
DOCTOR: Oh, set sail for your new home. Baby World!
RUBY: Come here now. Are you happy now, Eric?
ERIC: I'm very, very happy. I love you, Ruby.

[Outside the Tardis]

RUBY: So that was a normal day for you, then?
DOCTOR: No, no. That was extra-special nuts. And you, Ruby Sunday, get this. Your very own Tardis key.
RUBY: What for?
DOCTOR: I have the whole universe at my fingertips, and I'm all on my own. So I'd love it if you came with me.
RUBY: To what, just travel?
DOCTOR: No job. No boss. Just fun.
RUBY: We did almost die.
DOCTOR: Yes. But we lived so much, too.
RUBY: Yes, we did. Yes, we did. Yes, yes, we did. Yep, we did, we did. We did. Yes.
DOCTOR: Yes?
RUBY: Yes.
DOCTOR: Yes?
RUBY: Yes. Oh, my God.
DOCTOR: Yes? Yes! Yes! Yes! Ruby Sunday said yes!
RUBY: Come on in. Follow me.
DOCTOR: Oh, come on.

[Tardis]

RUBY: Right, mate, let me tell you where we're gonna go.
DOCTOR: Except...
RUBY: Oh, terms and conditions.
DOCTOR: There is one thing that I can never do, Ruby. And that's take you to that church on Ruby Road that Christmas. Absolutely never.
RUBY: But you've got a time machine.
DOCTOR: If you change one thing, a single snowflake, that could change your birth mother's story and then you would never meet me, none of this would ever happen, and we would fall into the deepest, darkest paradox. Ruby, trust me. I think that snow was a warning. I can't. And I won't.
RUBY: Well, that's a pity. 'Cos I disagree. And if you let me finish... we are going to go see my mum. At Christmas. Right now. Come on.

[Ruby's home]

CARLA: (on phone) And Ruby phoned, she said, "I love you," and ran off! No word from her since. What sort of Christmas is this? It all started with this man. He called himself the Doctor. Hold on. What's that noise?
(The Tardis materialises, making a hole in the kitchen ceiling. Not normal Tardis behaviour, that.)
CHERRY: What the blinking flip?
(Tardis door opens.)
RUBY: Hiya, Mummy.
CARLA: But... what are you doing? And what the hell is that? What's it done to my kitchen?

[Tardis]

RUBY [OC]: Hey! Come and say hello!
DOCTOR: Yes. Coming. Tell your mum not to slap me.
(He sonicks up a quick DNA scan of Ruby Sunday.)
DOCTOR: Yes, now, the people from my world, they use titles like the Bishop, the Pedant, the Sagi-shi. My name was...
(He doesn't wait for the results of the scan.)

## Document 16
**Source**: https://stardewvalleywiki.com/Version_History

Version History
(Redirected from Version history)
Jump to navigationJump to search
Stardew Valley was released on 26 February 2016 for Windows PC after almost four years of closed development. Linux and macOS compatibility was released in a free update on 29 July 2016.

For a detailed breakdown of changes specific to console versions of the game see Console Version History.
For a detailed breakdown of changes specific to the mobile version of the game see Mobile Version History.

1.6.8
Stardew Valley 1.6.8 was released on 28 April 2024.

Bug fixes
Fixes a game-breaking crash introduced in 1.6.7 where the game would crash if NPC's reach the island resort changing room.
1.6.7
Stardew Valley 1.6.7 was released on 27 April 2024.

Bug fixes
Fixes a bug preventing players from giving Pierre the Missing Stock List
Fixed some machines and desert festival logic not working for Linux/MacOS players using the compatibility branch.
1.6.6
Stardew Valley 1.6.6 was released on 26 April 2024.

Balance and Gameplay changes
Bee houses now work with flowers in garden pots.
“Minecart depot” alternative layout now only appears in the upper or lava mine areas.
You can now turn the gold clock on or off
Added coal -> mahogany seed trade at raccoons
50% mastery XP now only applies to farming, as originally intended.
Translation changes
Reverted Chinese text to 1.6.3
Reverted Chinese default font to the original
Added an option to use the smooth font introduced in 1.6.4
Added a dialogue font size slider for Chinese
Added complete Russian translated movie & desert festival sprites
Added option for Russian to use the “old” font
Bug fixes
Fixed a case where Mr. raccoon could disappear during the raccoon cutscene in multiplayer
Fixed being able to trash Pierre’s Missing Stocklist, or give it away at the Feast of the Winter Star.
Fixed being able to give a wilted bouquet to your spouse.
Fixed issue causing only 1 omni geode to be produced from the skull cavern chest.
Fixed crash when a save contains some invalid animal home data.
Fixed a crash when talking to Penny in French.
Fixed a malformed Willy farm event in German.
Fixed an incorrectly blocking map tile in the Forest Farm map.
Fixed some machines and some desert festival logic not working for Linux/macOS players using the compatibility branch.
Fixed a case where an area was inaccessible in the volcano dungeon
Fixed sewer event in German
Fixed cases where you’d see Mayor Lewis’ giftbox note again when collecting 15 parsnips from a different chest.
Fixed emily makeover event from being hard to skip
Fixed Calico Egg Rating prize edge cases for farmhands
Fixed prismatic hat effects not working in French.
Fixed being able to “advance” the ready check menu by pressing Y, which lead to many issues.
Fixed island outfits not being loaded for farmhands
Minor optimizations.
Fixes for modded players
Fixed error showing non-flavored roe items.
Fixed error if a mod sets an NPC’s ‘friends and family’ data to null.
Fixed error loading a save containing enchanted weapons whose ID changed or data was removed.
Fixed soft lock when watching weather TV channel if tomorrow’s weather is custom.
Fixed temporary maps that aren’t part of a location not using seasonal tilesheets.
Fixed summit cutscene showing custom fish with wrong sprites.
Changes for mod authors
In Data/Objects, added two new fields: CanBeGivenAsGift and CanBeTrashed. Setting CanBeGivenAsGift: false adds the not_giftable context tag automatically.
1.6.5
Stardew Valley 1.6.5 was released on 20 April 2024.

Bug fixes
Fixed crash when loading dark mine levels in some cases.
Broken villager NPCs (usually due to a removed mod) are now deleted on load. They'll respawn when they're re-added to the data.
1.6.4
Stardew Valley 1.6.4 was released on 18 April 2024. A hotfix was applied on 19 April 2024.

New content & features
Added 20 new 'alternate' mine layouts, which can start appearing after reaching the bottom of the mines.
Added 20 new volcano mines layouts, which can appear after you've unlocked the shortcut between the caldera and the volcano entrance.
Added fish frenzies.
Added a special cutscene after you've helped your new neighbors grow their family to the max.
Added 4 new fairy styles.
You can now place 8 additional non-fish items into fish tanks.
Raccoon shop now includes a trade for mystery boxes and golden mystery boxes.
Vinegar can now be poured onto trees to stop them from ever growing moss.
Shaving enchantment now causes tree-specific drops (fern → fiddlehead fern, mushroom → red mushroom, mahogany → hardwood).
Visual improvements
Qi club coins now show up in the shop menu.
Various map edits and fixes.
Removed Maru's glasses from all beach portraits for consistency.
Translation changes
Many edits and improvements to the Chinese version.
Edits to the Russian, Portuguese, Hungarian, Turkish, and Korean translations.
Changed the Chinese fonts to make them more appealing and readable.
Changed Hungarian number spacing character from a comma to a period.
Some improvements to Russian font.
Balance changes
When you load a save, you'll now unlock missed Steam achievements if needed (e.g. achievements gained while playing offline).
Added mini-shipping bin as an expensive Qi gem shop purchase.
Added more variety, and improvements, to Skull Cave treasure chests.
Life elixirs now only restores health, and energy tonics now only restore energy.
Wild seed spots are now rarer, but yield more seeds.
Doubled the Iridium Golem's chance to drop iridium.
The monsters in the volcano entry level are now randomized each day.
Using a treasure totem indoors no longer works.
Going down a level in the mines now makes you invulnerable for 1 second.
Increased raccoon mystery box reward from 4 to 5.
Farming experience now contributes to mastery experience at a 50% rate.
Ice orb will no longer freeze a spider while it is in the air jumping.
Removed red snapper from winter fishing quest pool, and sardines from the summer quest pool.
You will no longer get calico rating points from going down the normal mines.
Golden mystery boxes now have a small chance to yield an auto petter.
Slightly reduced chance to find mystery boxes.
Mine barrels and coal carts will now "refresh" at the start of each year.
The order of mystery box rewards is now randomized per-player instead of per-save.
Quality of life changes
Added a 1.2-second delay after dropping an item, before it's picked back up by the same player.
Napalm rings are now non-destructive on the farm and inside the slime hutch (i.e. the explosion will only damage monsters).
Added ctrl + right-click as an alternate toolbar drop hotkey.
Receiving a "special notification" (e.g. first geode message) will no longer cancel out player actions such as eating or warping.
Flopping fish no longer fall back into fish ponds.
Crab pots now have a short time period after harvesting from them during which they can't be removed (750ms).
The Junimo bundle menu now only highlights items that can actually be placed in the selected bundle.
Other changes
Minor optimizations.
Added two inappropriate names to the list to exclude from the name generator.
You can no longer give gifts to NPC's during green rain year 1 (prevents incongruous attitudes). This also prevents a portrait issue with Demetrius.
Gameplay fixes
Fishing splash zones and ore pan points are now removed overnight.
The prize ticket machine now consumes your ticket when you get the reward, rather than when you first press the button.
For the purposes of perfection, the level 100 stardrop now has a more robust way to check if it's been acquired. This solves a problem where the flag for eating the lvl 100 stardrop could be missing.
Fixed Monster Compendium not actually doubling all loot.
Fixed geodes no longer dropping on the farm in normal circumstances.
Fixed rare crash when spawning items overnight.
Fixed crash when a certain mine level is chosen (_dark_dark crash).
Fixed player colliding with stuff during event cutscenes.
Fixed pre-1.6 forged weapons having reduced stats.
Fixed not being able to put a torch on the sprinkler you get as a CC reward.
Fixed disappearing pets bug.
Fixed various bugs/crashes related to building a cabin.
Fixed wild seeds in garden pots putting their final crop in the top-left corner of the map instead of the pot.
Fixed "lost and found" chests (from night market and elsewhere) not working anymore in 1.6.
Fixed a duplication bug with the "lost and found" chests.
Fixed slime hutch floors reverting to the default after reloading a game.
Fixed malformed casino shop red fireworks ID.
Fixed pet adoption catch-all case only working with the animal catalogue, and only applying in year 2 specifically, rather than for any year 2 or beyond.
Fixed 'use legacy randomization' option applied inconsistently when loading a save, which caused weird issues like broken green rain days.
Fixed the case where you could permanently miss the ancient seed recipe if you grabbed the ancient seed packet but not the associated recipe, and then closed the museum rewards menu. Missing recipes will also be restored upon loading a file.
Fixed issue with duplicated animals & building interiors from pre ~1.3 saves.
Fixed end tables not being rotateable.
Fixed an issue where empty barns/coops could not be removed by Robin on old saves.
Fixed slime egg incubators letting you reclaim the egg before it hatches.
Fixed farmhouse placement bounds to match the object placement restrictions around it.
Multiplayer fixes
Synced some NPC Gift data in other languages.
Fixed fireworks (and possibly other sprites) drawing behind stuff in multiplayer.
Fixed "Build a Silo" quest not being completed for farmhands.
Fixed Raccoon quest not being removed for all players.
Fixed double trinket issue when a farmhand disconnects/reconnects.
Fixed double and/or missing derby participants sprite issue in multiplayer.
Display text and localization fixes
Many edits and fixes in translation text.
Fixed a text parsing error for Asian languages which caused them to incorrectly wrap in some cases.
Fixed spacing issues in Asian languages.
Fixed several localization issues (day time money box extra space in Chinese, missing Elliott sentence opener, Fizz name untranslated, birthday string de-hardcoded, etc).
Fixed Russian line break issue.
Fixed an issue with the perfection tracker display in Chinese, Korean, and Japanese.
Fixed events not consistently handling gender-dependent text.
Cosmetic fixes
Adjusted basic object layer depth anchor point so it's more centered rather than on the bottom.
Placeable grass now offsets vertically a little if it would clip through a front-layer tile.
Fixed seasonal world map not working for non-English players.
Fixed flying monsters not being draw above things on the farm & volcano.
Fixed reward icon in completed quest menu being visually offset.
Fixed george's TV clipping with farmer during green rain.
Fixed movies not showing layered sprites (e.g. the eyeball in Mysterium).
Fixed Qi club coins drawn below the lightmap.
Fixed Qi coin overlay drawn during minigames.
Fixed crane game audio not stopping when the game is forcefully closed.
Fixed some tooltip padding issues.
Fixed movie theater display issues on the world map.
Fixed repeated dialogue selection sound if a control was plugged in but you are using a mouse.
Fixed quest reward icon input offset issue.
Fixed Joja Warehouse roof drawing above the weather (and possibly other similar cases).
Fixed various map tile issues.
Fixed a visual issue with a shadow in the farm house.
Fixed able to swap two chests of the same type.
Fixed machines sometimes wobbling when they're not processing anything.
Changes for modded players
Improved debug commands:
Added debug commands to change pet types/breeds, to allow migrating older saves (setPreferredPet and changePet). This replaces the former toggleCatPerson command.
The filterLoadMenu <search> command now keeps the original save slot numbers.
Combined removeNpc and killNpc commands. The unified command removes all instances of an NPC, to help fix duplicate NPCs.
Changes for mod authors
C# mods can now hide specific animals from the animal social menu (e.g. animals owned by NPCs) via the FarmAnimal.hideFromAnimalSocialMenu field.
In Data/Buildings, you can now add furniture via IndoorItems.
In Data/FarmAnimals, added fields to set the sleep sprite and whether they eat golden crackers.
In Data/Locations, added fields to set effect of fish-specific bait and whether fish can be caught using a training rod.
In Data/Machines, added option to only let the machine complete overnight.
In Data/Powers, added CustomFields field.
Added missing Id fields in Data/FarmAnimals and Data/Pets.
Added a warning when a farm animal's spritesheet size is invalid, which would previously lead to the animal silently freezing.
You can now use tokenizable strings in event scripts and dialogue text.
De-hardcoded forest waterfall fish into Data/Locations.
Fixes for modded players
Fixed some wallpapers and flooring not appearing in mod item lists.
Fixed pre-1.6 farm maps having broken warps to the bus stop.
Fixed errors and crashes due to mods adding items without a name.
Fixed softlock when a warp leads to an invalid location.
Fixed crash when playing events that use the replaceWithClones command.
Fixed crash if an NPC has invalid temporary dialogue.
Fixed world map showing a glitched texture for custom farm types which don't override it.
Fixed another case of NPC duplication involving the movie theater.
Fixed crash when loading a save if a farm Junimo wasn't properly removed before saving.
Fixed crash if the lost & found contains null items.
Fixed disconnect for Steam players when using mods that send messages before a farmhand has been approved.
Fixed crash on save if shipping bin has empty slots.
Fixed riding the bus to the desert instantly warping you back if mods added warps on the desert road.
Fix multiplayer crash if some players don't have the same NPC textures.
Fixes for mod authors
Fixed farmhands' cellars not applying cellar data from Data/Locations.
Fixed crash if a farm animal has no entry in Data/FarmAnimals.
Fixed festivals ignoring year suffixes for <setup>_additionalCharacters and name fields.
Fixed issues with farm animals which have a custom home building.
Fixed hardcoded assumptions about farm animal spritesheets which could cause counter-intuitive behavior with custom animals.
Further changes were later released without changing the version number:
19 April 2024 "hotfix #1" (Steam announcement)
Fixes issue when dropping a big chest into a small chest
Quarry mine level can no longer be an alternate layout
Prevents the player from running through barriers in certain transit cutscenes
Mine levels 45 and 85 are now also refreshed at the beginning of the year
1.6.3
Stardew Valley 1.6.3 was released on 27 March 2024.

New content & features
You can now access Clint's shop and geode service while your tool is being upgraded.
Added Krobus portrait.
Added minecart shortcut to year 1 Spirit's Eve festival.
You can now paint the new cabins (at third upgrade level).
Balance changes
Increased raccoon bug meat and bat wing request amount.
Harvesting moss now grants 1 foraging exp per moss.
The Infinite Power achievement is now more generous with how it activates, allowing pre-1.6 saves to trigger the achievement.
You now have to collect (not just donate) the four prismatic shards for the "Four Precious Stones" Qi quest.
The Junimo Kart Qi quest now rewards 20 Qi gems (up from 10).
Adult mossy green rain trees boost the moss growth rate of nearby trees.
Moss now grows more slowly on sunny summer days, and recovers more slowly after harvest.
Reduced meteorite prismatic shard chance (100% -> 25%).
Ancient seed packets can no longer be sold at the traveling cart.
Quality of life changes
Waterfall and some other ambient positional sounds now fade out more smoothly.
If you don't have a pet in year two, you can now start adopting them from Marnie's shop.
Bug fixes
Added the new cabin styles to the multiplayer starter layouts.
Starter cabins now appear in the actual order intended.
If a journal quest title is too wide, the clock icon and the rest of the text will be shifted down to make room.
You can now press the Escape or menu button to "go back" on a shipping menu category page.
Made berry bush state consistent overnight and on load (both at 20% plus a small new random bonus chance).
Minor graphical fixes.
Fixed glitch where farming speed is changed depending on the player's direction.
Fixed several translation errors and missing translations.
Fixed large character sprites having a visual glitch (e.g. bear, island frog, or Clint when hammering).
Fixed a visual error in the shop menu if an item's name was longer than the width of the menu.
Fixed a crash related to the new festival.
Fixed a bug that caused excess trash to be fished.
Fixed bug preventing Emily's 10-heart mail and event from triggering.
Fixed graphics issues with the shipping menu.
Fixed several more cases of out-of-bounds spawning.
Changes for mod authors
Fixed items able to have a null Name or DisplayName in 1.6. They now default to the qualified item ID and "Unnamed Item (<id>)" respectively.
The ${...}$ gender-switch syntax now works in events.
The character.EventActor flag is now synced in multiplayer.
Added paint masks for the new cabins style.
The debug whereis command now lists event actors too.
Fixed pet license name delimiter conflicting with unique string ID format.
Fixed NPC duplication bug with movie theater.
Fixed fruit trees above growth stage 4 no longer producing fruit.
Fixed current location's building interiors not being actively synced.
Fixed error processing a machine with no Data/Machines entry.
Fixed broken fruit tree sprite if it's synced from another player and has a custom texture in Data/FruitTrees.
1.6.2
Stardew Valley 1.6.2 was released on 21 March 2024.

Balance changes
Added scaling edibility to juice, jellies, wine, and pickles.
Void egg is now poisonous.
Bug fixes
Fixed an issue with Willy's rod.
Fixed for invisible tea sprites.
Fixed an error in the Luau event in Portuguese.
Fixed visual error with pre-1.6 basic wines.
Fixed a soft-lock if you charged a tool and then strafed to a warp spot, and released the tool while warping.
Fixed inedible ingredients being poisonous after turning into jelly or pickles.
Fixed Volcano dwarf bombs not matching regular dwarf bombs.
Fixed adventure guild open hours on map.
Fixed various translation issues.
1.6.1
Stardew Valley 1.6.1 was released on 19 March 2024.

Bug fixes
Improved cases where the quest title could go off the edge of the quest log.
Fixed botched German egg quest text (for new players going forward).
Fixed animal page crash when clicking on the scroll bar when there are a low number of animals.
Fixed Junimo harvester in save crash.
Fixed Meadowlands farm quest persisting if the farm icon was selected, but then another farm was started.
Fixed the telephone Robin house upgrade question being malformed.
Fixed eyebrow accessory looking weird when fishing.
Fixed errors due to clipboard being set to a null string.
Fixed crash when farmhand reconnects to town during green rain (and potentially other related crashes).
Fixed several map tile issues and places where forage could spawn out of bounds.
1.6
Stardew Valley 1.6.0 was released on 19 March 2024.

New content & features
Added new festivals and events:
The Desert Festival is a three-day event in spring which can be accessed after the bus is repaired.
Two mini fishing festivals: Trout Derby and SquidFest.
A new environmental "event" in summer.
Added a mastery system, accessed via a new area, which grants powerful perks and items…
Added a new farm type: Meadowlands Farm. It has a chewy blue grass that animals love. You also start with a coop and 2 chickens.
Added many new NPC dialogues. That includes...
custom gift reactions;
dynamic dialogues which react to things that happened;
custom flower dance acceptance dialogue;
restored missing dialogue (like Emily and Shane's flower dance custom accept-dance dialogues when married to the player, Shane's dialogue when browsing the Saloon vending machine, Lewis congratulating female farmers after their wedding, a line in Maru's 14-heart event, three dialogues from Sam related to Kent, two randomized dialogues when an NPC buys an item you sold to a shop, two speech bubbles from Marnie and Robin when you enter their shop building, and a fortune teller dialogue for your potential spouse);
and more.
You can now get multiple pets (after getting max hearts with your starter pet).
Added a world map for Ginger Island, visible when visiting the island.
The world map now shows your actual position within the world in real-time (instead of showing you at a fixed point for each location). In multiplayer, you'll see other players' positions in real-time too.
Pets that love you will sometimes give you gifts.
NPCs now have winter outfits.
Festivals now have map and dialogue changes every second year (except the night market and desert festival).
Added a golden Joja parrot, which you can pay to find all remaining golden walnuts on Ginger Island.
Added perfection waivers, a new Joja way to bypass perfection challenges.
Added a prize machine in Lewis' house. You can collect prize tickets as a reward for completing quests and special orders, and from repeated egg/ice festival wins.
A bookseller now comes to town twice a season.
Added mystery boxes.
Added a Big Tree, with a quest line which ultimately gives you some new neighbors.
Added four new crops (carrots, summer squash, broccoli, and powdermelon) which can't be purchased at the store, and two new giant crops.
Added four new home renovations: dining room, attic, expanded corner room, and cubby.
Added new items:
Big Chest, which has almost double the size of a regular chest. It can also be placed "onto" a regular chest to upgrade it.
Dehydrator, which turns fruit into dried fruit and mushroom into dried mushrooms.
Mushroom Log, which produces mushrooms and interacts with nearby trees.
Bait Maker, which can produce fish-specific baits.
Heavy Furnace, which can process more bars at a time, and yield bonus bars.
Fish Smoker, which produces smoked fish, doubling the value of the fish. You get one by default when starting a new riverlands farm.
Text Signs, which can be written on.
Anvil, which allows you to re-roll trinkets.
Mini-Forge, which acts as a Dwarvish Forge.
Statue Of Blessings, which grants a random blessing each day.
Statue Of The Dwarf King, which allows you to select one of two mining buffs for the day.
Tent Kits, which allow you to build a tent which can be slept in for one night.
Treasure Totems, which spawn a ring of diggable spots.
Mystic Tree Seeds, which grow a unique tree which can be tapped.
Mystic Syrup, a valuable tapper product.
Deluxe Bait, gets fish biting faster than regular bait.
Challenge Bait, which allows for up to 3 fish to be caught at once, but loses 1 each time a fish leaves the bobber bar.
Deluxe Worm Bin, which upgrades the regular worm bin to produce deluxe bait.
19 unique Books Of Power, which grant special perks.
Skill Books, which grant experience in a skill.
Book Of Stars, which grants experience in all skills.
Moss, a new resource type which grows on old trees.
Mixed Flower Seeds.
Sonar Bobber, which shows the fish on your line before you catch it.
Raisins, which have a special use.
Sea Jelly, River Jelly, and Cave Jelly, a new item that you can fish.
7 Trinkets, which grant powers related to combat.
Red, Purple, and Green Fireworks.
Stardrop Tea, which makes an excellent gift for anyone.
25 new hats.
280 new furnitures.
New unique furniture catalogues, which contain themed furniture sets.
41 new floor styles.
24 new wallpaper styles.
Golden Animal Crackers.
Mannequins, which can be dressed.
Spouse Portraits which can be purchased after reaching 14 hearts.
Butterfly Powder, which allows you to remove pets...
Blue Grass Starter.
Moss Soup.
Secret items.
Added Goby fish.
Added some new remix bundles.
You can now place hats on cats and dogs.
You can now upgrade the copper pan into steel, gold, and iridium pans.
You can now enchant pans with Archaeologist, Generous, Fisher, and Reaching.
Added a "Special Items & Powers" tab to replace the wallet. The wallet area now tracks a selection of progress markers.
Added an animals tab that shows all your pets & animals.
You can now build pet bowls in Robin's Shop, with three variants.
The farmhouse and pet bowl can now be moved through Robin's menu.
The farm computer can now be used anywhere to see a summary of that location, instead of only the farm.
The mini-jukebox can now be used on the Ginger Island farm.
Added a new interaction with your horse.
Added a new side-tunnel to the Quarry Mine.
The Community Center fish tank now becomes an actual fish tank when you complete it.
Added more secrets & easter eggs.
Added two new cat and dog breeds.
Added turtle pets.
Added 8 new achievements.
Added 4 new cabin variants.
Added a few more accessory options in character creation.
Added a new bobber machine in Willy's shop, with 39 bobber styles to choose from. New styles unlock by catching new kinds of fish.
Added a cameo appearance to Maru's 14-heart event.
Emily has a new rare "socialize" daily quest if you've completed the introduction quest.
You can now add anchors, treasure chests, and pearls to fish tanks.
Pierre now sells a few random items at the winter star booth (at a markup!).
Added a jingling sound when running with the cinderclown shoes on.
Baby toss now has a chance to crit.
Added a skull cavern statue that can be used to toggle hard mode in the skull cave (after completing Qi's challenge).
Added additional chests to Skull Cavern levels 200 and 300.
Added unique skull cavern chest appearance for level 100, 200, and 300 chests.
Added a high note (C5) to flute block.
Added Meowmere from Terraria crossover
Added iridium golem to wilderness farm.
See changes for mod authors.
Visual improvements around the valley
Added waterfalls.
Added more holiday decorations in winter.
Added more pathstones to various maps.
Added jack-o-lanterns after the Stardew Valley Fair in fall.
Added seasonal world map variants.
Added a new rare ambient critter.
Added some rare summer butterfly variants.
Added an uncommon little brown bird variant.
Redrew the world map to better match the in-game locations and be more detailed.
Boat journey textures are now seasonal and reflect the latest valley map.
The bus stop now has a wider map, though the distance to traverse it is the same. (This is to prevent black bars from appearing at the sides of the screen.)
Jelly, pickles, wines, and juices are now colored based on the ingredient item.
Many town trees are now actual tree objects, though you can't cut them down.
Slight adjustment to the way items pop out when dug from the ground.
Updated volcano gold ore node sprite.
Some trees have a chance to lose their leaves in the fall.
Riverbanks and lakeshores in the mountain, town, and forest areas are now less jagged in some places.
Graphical improvements to building interiors.
Improved the art of George & Evelyn's roof.
If you destroy a mines chest, it now shows some graphics debris.
Added special backplates to fortune teller TV show if you get a perfectly good or perfectly bad luck day.
Lighting changes:
It now gets dark an hour earlier in winter.
Night tiles (e.g. town lamps) now activate an hour earlier in all seasons.
Indoor daytime lighting now smoothly transitions to night lighting over the course of two hours.
Night lighting in non-farmhouse indoor locations is now slightly darker.
Farmhouse lighting on rainy days is now slightly moody, and lights stay on all day.
TVs and trees of the Winter Star now give off light at night.
Added light sources to window light glows so there are no more "dark but lit" windows.
Made some improvements to the intro bus drive cutscene.
At night, hats are now drawn at the night-time color in the game menu portraits.
Removed lighting quality option. It's now permanently set to ultra quality.
The submerged fishing bobber is now recolored automatically to match the water.
Multiplayer changes
You can now have up to 8 players on PC.
Many improvements for multiplayer performance and stability. That includes:
Steam players will now use Steam multiplayer authentication, potentially improving connection issues significantly.
Large multiplayer packets are now compressed, reducing bandwidth usage and latency.
Internal optimizations to data syncing.
You now need the same build number (in addition to version) to join a multiplayer server. This prevents crashes due to game changes between builds.
Accepting a Qi challenge that increases mine difficulty now only kicks other players out of the affected mine type, not all mines.
Purple shorts no longer show a chat message when placed into the Luau soup.
Jump down mineshaft sound now plays for all players in the level rather than just the jumper.
Balance changes
Added a box with three tent kits to the Ginger Island jungle.
Weapons found in the wild now have a chance to come with a basic "innate enchantment". You can re-roll "innate enchantments" (if the weapon could have one) at the forge using a dragon tooth.
Slime hutches are now significantly smaller (11x6 → 7x4).
Farm animals now gain a little happiness if you close the animal door behind them at night.
Grass now survives in the winter, though it won't spread. However, cutting grass during winter is much less effective.
The mushroom cave now comes with a free Dehydrator.
Changed recipe skill requirements for:
charcoal kiln (foraging 4→2);
cookout kit (foraging 9→3);
survival burger (foraging level 2→8);
tapper (foraging 3→4);
and worm bin (fishing level 8→4).
Price changes:
Most home renovations now cost money, which is refunded if you undo the renovation. (The game knows whether you bought it though, so refunding a pre-1.6 renovation won't give you free money.)
Reduced fairy dust sell price (500g → 300g).
Reduced tea sapling sell price (500g → 250g).
Reduced life elixir sell price (500g → 250g).
Building cabins no longer requires materials, only the 100g price.
Raised price of second house upgrade (50,000g → 65,000g), but reduced number of hardwood needed (150 → 100).
Reduced worm bin's hardwood needed (25 → 15).
Increased cost of warp totem: farm in casino (500 → 1000)
Raised price of bombs in dwarf shop.
Raised some hat prices from Hat Mouse.
Shop changes:
Put limits on some casino stock.
You can now buy all brazier recipes in Robin's shop at once instead of in sequence.
Item drop changes:
Chopping down a fruit tree now yields the appropriate fruit sapling. If the tree is mature (i.e. the fruit quality is > basic), it will yield a sapling with the same quality as its fruit. The higher the quality, the faster the sapling will mature.
Chopping down a tea bush now gives back a tea sapling.
There's now a small chance to find cosmetic items and other goodies while doing random tasks.
Snake vertebrae are now easier to get.
Train cars which carry wood can now drop hardwood.
Santa's train car can now drop gifts.
Reduced prismatic shard drop rate from iridium nodes (4% → 3.5%).
Rare yellow slimes now drop money.
Brown slimes now drop wood (doesn't affect the copper slimes in the quarry mine).
Botanist perk now applies to items dropped from trees (e.g. coconuts).
Reduced chance of fishing void mayonnaise at the witch swamp.
Gift taste changes:
Adjusted gift tastes for several NPCs.
Treasure chests are now a universally liked gift... except by Linus.
Skill XP changes:
Mushroom Logs and Mushroom Boxes now grant 5 foraging XP on harvest.
Harvesting berry bushes now grants 1 foraging XP per berry.
Harvesting forage crops from wild seeds now give much less foraging experience, but grant some farming experience.
Monsters on the farm now give combat experience, but it's 1/3 of normal value. This excludes slime hutch slimes.
Adjusted combat:
Extended the area of effect of downward facing melee attacks (and slightly extended the side attack of daggers).
Topaz ring now gives +1 defense, rather than the unused precision stat.
Raised insect head's damage (10-20 → 20-30).
Raised kudgel's critical attack power (+4 → +50).
Bombs now affect terrain features (like trees and crops) within the round explosion radius rather than a square area.
Slightly increased rate at which skeletons throw bones or shoot spells.
Adjusted Junimo Kart:
Added grace jumps in Junimo Kart: when you run off the track, you can still jump for a short time to recover.
Your score is now saved if the minigame forcibly exits while playing endless mode.
Noxious gas emitting mushrooms no longer appear in pairs.
Reduced bubble spawn rate on whale level.
Adjusted machines:
Worm bins now need a lower fishing level (level 8→4) and produce more bait (2–5 → 4–5).
Loom now has a higher chance of double cloth when processing quality wool.
Fish ponds now have a chance to produce extra roe whenever they produce roe.
Geode Crushers no longer require coal to operate.
Adjusted penalties when knocked unconscious:
You can no longer lose the Golden Scythe, Infinity weapons, or tools.
You can no longer lose more than three items.
The amount of money lost now scales to how much you have. It's now less punishing if you don't have much money, but more punishing if you have a lot. This also raises the maximum lost from 5000g to 15000g.
Adjusted food buffs:
Joja cola now gives a very short speed buff.
Green tea now gives +0.5 speed.
Mine and dungeon changes:
Added coal nodes to the volcano dungeon.
Barrels now spawn on skull cavern levels divisible by 5.
Reduced the maximum possible effect a bad luck day can have on finding a prismatic slime.
Reduced number of bugs to kill for monster slayer goal from 125 to 80.
Bundle changes:
Made remixed specialty fish bundle (and analogues) reward 5 Dish O' The Sea, to make it consistent with the classic bundle.
River fish bundle now gives deluxe bait.
Improved some community center rewards.
Adjusted crafting recipes:
speed gro now requires 5 Moss instead of 1 Clam .
deluxe speed-gro now requires 5 bone fragments instead of 1 coral.
quality fertilizer now requires 4 sap instead of 2, but produces 2 per craft (still only requires 1 fish).
Spouse changes:
Spouses now have a seven-day "honeymoon" period after marriage which prevents them from laying in bed all day due to being upset.
Kissing your spouse, and giving them a gift on the previous day, each reduce the "minimum heart level threshold" for a bed-ridden day by one heart (12→10 if you do both).
Friendship gain is reduced by 33% for spouses.
Rebalanced the crop fairy event: the chance no longer depends on the number of planted crops, it can no longer happen on the last day of the season (to avoid growing crops that might die overnight), and it can no longer choose dead crops to grow.
Increased the shaving enchantment's effect on giant crops.
Each giant crop now has a 60% chance of dropping an extra six crops while the shaving enchantment is equipped, spread across the number of hits needed to break it. For example, a base axe which breaks the giant crop in three hits gets three 20% chances of dropping 2 crops.
The mushroom cave now provides mushrooms every second day. It was unintentionally changed to daily in Stardew Valley 1.5.
You can no longer plant trees in the beach farm tunnel.
Randomization no longer produces simple repeating patterns in many cases (e.g. clay farming, mushroom level prediction, crab pot fish offset, etc).
(You can enable "Use Legacy Randomization" in the advanced save options to use the old randomization, though some specific patterns may still change due to the underlying changes. That option is mainly intended for speedrunners; most players should keep it disabled for the intended experience.)
Spreading weeds can no longer destroy artifact spots.
Increased the number of monsters that daily monster quests will ask you to slay (in some cases). Added more custom quantities, for example Dust Spirits will ask for 10-20 kills.
Tilled dirt on the island farm now decays in the same way as the regular farm.
Slightly increased time you have to push against farm animals before passing through them.
Slightly boosted quarry output. Daily quarry output now increases each year, up to a limit.
You can no longer plant trees in town.
Secret notes are no longer created during festivals (except passive festivals like the night market and desert festival).
Adjusted fish variety in ice fishing festival.
Quality of life changes
Performance improvements.
NPCs now shove chests out of their way instead of destroying them.
If Pam won't be coming to the bus for any reason, she now leaves a sign informing you and you can drive yourself to the desert.
Audio changes:
Made more sounds positional (mainly players, tools, and machines).
Positional sounds now fade with distance when off-screen, instead of cutting off abruptly.
Softened the bomb fuse sound.
The music now "ducks out" and then resumes when certain sounds are played, instead of stopping.
You can now "strafe" while charging a watering can or hoe, allowing you to reposition your tool hit area without changing your facing direction.
You can now refill slingshot ammo by right-clicking it with the same ammo. Previously that would just swap the item stacks.
Planting cactus seeds on the farm now fails with a message, instead of the seeds dying overnight.
Holding a tea sapling or seed over a garden pot now shows the green/red placement tile.
You can no longer pick up rugs if there's something on it.
Checking a pet bowl will now show a text bubble with the pet's name.
Added a new post-fishing sparkling text to indicate when you've caught something for the first time.
Torches can now be placed on sprinklers.
You can now sit in chairs during festivals.
You can now move filled chests by hitting them twice with a heavy tool (previously only with bare hands). The chests will shift one space at a time.
You can now place flooring underneath most buildings.
Crystalariums now have to be removed and replaced before a different gem can be put inside, to help avoid wasting gems accidentally.
Daily billboard quests now have a more informative tracker notification when you make progress on them.
Added a small checkmark icon on special orders you've completed before (only on town special orders board).
You can now skip the pet adoption scene, which causes you to adopt the pet.
Reduced the amount of time you need to push against a pet before they start shaking and then let you pass through them (1.5 → .75 seconds).
Reduced time for mini-obelisk warp (750ms faster).
Male farmers are no longer forced into wedding clothes on their wedding day, so you can choose your own outfit for the wedding.
Emptying a fish pond with fish still in it will cause the remaining fish to flop out of the pond.
Slime hutch changes:
You can now change the flooring of the slime hutch.
You can now remove the starter incubator in the slime hutch.
Slime balls no longer appear on crafted flooring.
UI improvements:
Added an hourglass cursor shown when you're waiting for something to load on the title screen.
Notification messages in the bottom-left corner now last 50% longer before going away.
"Sound in the night" events now show an icon on the screen to indicate that a sound is playing.
Dialogue question selectors no longer remain selected when you hover away from them, to reduce accidental selections.
Robin's building menu now shows how many days a building will take.
If an item menu exits while you're holding an item, the item is now always retrieved. (Previously only some item menus like chests would do it.)
Marnie's animal shop now centers the camera on an appropriate building when purchasing an animal.
Marnie's animal shop now shows prices in the tooltip, in case the tooltip covers the price display.
The achievement menu now lists all potential achievements. Hidden achievements you haven't unlocked yet are shown as "???".
The museum reward menu now prevents picking up a reward that won't fit in your inventory.
The museum reward menu now lets you exit while holding a reward. It'll be added to your inventory if possible, otherwise it'll drop at your feet.
The save creation farm selector now has two columns instead of one, and no longer overlaps the back button on small screens.
The shipping menu category pages no longer take up the whole screen, as long as the screen is beyond a minimum size.
Inventory tooltips for food that gives a buff now shows the buff duration in the tooltip.
The map now closes when you press the map button again.
Exiting the Junimo Note menu from within the game menu now returns to where you were in the game menu rather than exit the menu.
Shops now truncate item names which would overflow the menu width.
Shops now have a slight delay before you can buy/sell items, to help avoid double-clicks doing it accidentally.
Deleting a save on PC is now much faster.
Significantly reduced save loading time when there are many custom locations.
If a default farm building (like the greenhouse) is somehow removed, it'll now be rebuilt next time you load the save.
"Menu background" is now a drop down option, which includes "Standard", "Graphical", or "None".
Attempting to put something in a machine but failing will no longer cause you to try and consume or activate the object you're holding.
Kent intro event and Robin flute block event are now skippable.
(PC) You can now shift + right-click an item on the toolbar to throw it out of your inventory (if possible).
(PC) You can now press the Y or N key to confirm or cancel the "leave festival" confirmation box.
(PC) Holding left-shift + left-ctrl + 1 when buying from a shop will attempt to buy a stack of 999.
Other changes
Adventure guild now stays open until 2am, though the music will not play after midnight.
Gender-specific clothing variants can now be worn by any gender.
If you have 12 hearts or more with your spouse, the chance they'll say a neutral dialogue in the afternoon (which sometimes comes across as negative) is significantly lower (25% → 5% chance).
Penny's forest picnic event and Leah's forest picnic event now only happen if it's sunny.
NPCs now try to avoid walking through trees and other terrain features.
Cabins have been combined into one entry in Robin's menu.
Replaced pet icons on the inventory tab with the current date.
The “Organize” button now sorts items in a more intelligent way.
You can now drink mayonnaise and jelly, and eat pickles.
Some colored objects now count as their color for qi quest and dye menu.
Clam is now considered a "fish" just like all the other shellfish.
Added more descriptive titles to daily quests.
Added Cyrillic sprite text and some translated world pixel art text.
Adjusted the date/time/money box in Chinese.
The about page now shows the build number.
The Skull Cavern now have a chance to also play music from the upper mines.
Changed parrot flap sound to be different from bat flaps.
Pans now have a chance to yield bone fragments.
Made the character randomization a little less random, and added some of the newer hairstyles and accessories to the mix.
Pan no longer yields the same thing if you pan in the same spot twice in a day.
The about page no longer hides the version if a tip message is shown.
The order that you'll get forge enchantments is now unique per player rather than per farm.
The Ginger Island shrine item pedestals are now normal items. Modded players can spawn them to display items decoratively (though they're not obtainable in vanilla currently).
Map no longer closes if you click on an area of interest.
Fixed some NPC schedules that weren't previously applied:
Lewis visiting the library on winter Sundays;
Maru and Penny hanging out on summer Sundays;
Maru tinkering on summer Mondays;
After reaching six hearts with some NPCs, they won't visit their rival love interest anymore. This affects Alex visiting Haley, Elliott visiting Leah, and Haley visiting Alex.
Gameplay fixes
Fishing fixes:
If you're fishing when the pirate cave changes to pirate mode, you will catch your fish.
Fixed artifacts found in fishing chests not counting for the collection tab.
Fixed fishing crash if a treasure chest appears while the player has a large number of stacked fishing buffs.
Buff fixes:
Fixed a range of bugs like attribute drift and double-debuff.
Fixed food/drink buffs discarded if they have a balanced total of effects (e.g. +2 attack and -2 speed).
Fixed negative custom buffs shown with a double-negative (e.g. "--2 speed").
Fixed Squid Ink Ravioli buff not remaining active if another food buff is added later (although the buff icon was still shown).
Fixed Squid Ink Ravioli not resetting the buff duration when you eat another one, unlike other food buffs.
Fixed Squid Ink Ravioli description having an extra blank line.
Fixed Burnt not showing the -3 Attack effect.
Festival fixes:
Fixed unable to leave the Festival of Ice until it ends.
Fixed two-second pause when entering the Stardew Valley Fair.
Item fixes:
Fixed dropped tools not recovered if they're inside a constructed building.
Fixed potted tea bushes planted in town not being harvestable.
Fixed bee house dropping a generic "Honey" item when you break it, instead of the flavored honey it would produce when harvested normally.
Fixed farm computer counting fiber crops as unwatered.
Fixed geode and lost book message not shown if your first one is from a fishing chest.
Fixed magic bait disabling some fish area checks (e.g. so you could catch river fish in the forest pond).
Fixed heavy tappers not tracked correctly. That caused issues like heavy-tapped trees not ignored when creating mushroom trees in fall.
Fixed rain totem used during a storm incorrectly making the next day stormy instead of rainy.
Fixed secret note #2 not revealing Kent's gift taste if he hasn't returned yet.
Fixed wedding rings being giftable to NPCs.
Fixed watering can's water left and capacity resetting on right-click into chest.
Fixed wilted bouquet not cancelling the wedding if it hasn't happened yet.
Fixed various cases where item-received logic wasn't applied consistently.
Combat fixes:
You can now kill any slime for the "Initiation" quest, not just green slimes.
Fixed player stuck in swimsuit if they collapse from damage while wearing it.
Fixed broken event if the player is defeated in the mines and their name contains a slash.
Fixed issue where you could clear a forest-themed mine level without finding a ladder.
Fixed Magma Sparker's debuff ignoring squid ink ravioli's protection.
Controller fixes:
Pressing the trigger buttons on a gamepad while in the junimo bundle menu now snaps the cursor to the ingredients slot or back.
Improved controller navigation on the Junimo bundle page and world map.
Fixed issue which could cause Junimo Kart to be unplayable with a controller, if you had rebound keys to certain values.
Fixed issue where viewing a letter with multiple pages and positioning the cursor directly above the skip button could cause the next viewed event to be skipped when the A button is pressed to progress text.
UI fixes:
Fixed issue where clicking an item attached to a letter could exit the letter if your inventory was full.
Fixed items from dialogue being lost if your inventory was full. You'll now see a menu to collect them when the dialogue closes.
Fixed gates popping off when opening or closing them while the player overlaps the tile.
Fixed random seeds on Ginger Island being based on the valley's season.
Fixed exploit where you could keep temporary items like Qi Fruit by selling them to Pierre and buying them back later.
Fixed fruit trees being plantable on stone tiles outside the greenhouse.
Fixed tree stumps dropping seeds like full-grown trees.
Fixed riding an orphaned horse (e.g. spawned using debug commands) preventing you from owning or riding other horses.
Fixed some mail not received on the intended day if you don't leave the farmhouse that day.
Fixed bug where it was faster to harvest left-to-right than right-to-left.
Fixed some spots where forage could appear out-of-bounds.
Fixed spot where you could run into the water on the beach farm.
Fixed minecarts unlocked before you've seen the cutscene.
Fixed able to place things underneath the traveling merchant cart and pig.
Fixed some undiggable tiles in Ginger Island dig site.
Fixed geode crusher "off-by-one" bug/exploit.
Fixed speed of Taro growth when grown with agriculturist and hyper speed gro (and generally fixed issues with negative phase durations).
Fixed invisible menu preventing you from moving after closing out of the bulletin board Junimo note, if you were holding a useable object.
NPC fixes
Dialogue fixes:
Fixed NPCs not having custom dialogue when accepting a movie invite for non-English players.
Fixed Abigail showing both default and custom item delivery dialogue.
Fixed Lewis skipping his final dialogue at the Festival of Ice on subsequent player wins.
Fixed the fortune teller nearly always showing the text for your combat skill, instead of your highest skill.
Fixed issue where an NPC who bought an iridium-quality item you sold to a shop could show a low-item-quality dialogue for it.
Fixed issue where NPC dialogue could reveal gift tastes for an invalid item.
Fixed monster grave text only shown in English.
Fixed wrong message shown when placing indoors-only furniture outside.
Fixed the Krobus vs Dwarf event able to happen on Fridays.
Fixed giving a gift not counting toward socialization quests.
Fixed invisible spouses asking to have children.
Fixed able to invite Leo to the movies before he moves to the valley.
Fixed able to interact with NPCs during the ice fishing event.
Fixed NPC spouse chores sometimes not applied on the intended day (e.g. saying they filled the pet water bowl but it's not filled).
Fixed NPC spouses watering crops that don't need it (e.g. fiber seeds or already watered), and almost never showing the crops-were-already-watered dialogue.
Fixed NPCs sometimes not reacting to dumpster diving if the horse is nearby.
Fixed Penny losing items when redecorating if they were placed on a stone slab (or a custom table without Table in the name).
Multiplayer fixes
Mitigated potential remote code execution issue.
Possibly fixed frequent disconnections for some players.
Fixed old/incorrect Steam display names being shown in some cases.
Fixed phantom action cursor over backwoods gravestone if the current player hasn't seen the related event yet.
Fixed copy & paste for invite codes on some Linux/macOS platforms.
Fixed issue where the mines were checking for the luck level of players in the host's current location, rather than players in the mines.
Fixed global chat info messages (like "Abigail caught PlayerName digging through the trash") sometimes showing text in the sender's language instead of yours.
Fixed egg festival requiring 12 eggs to win if there are 5+ players. It now applies the four-player requirement to any player count beyond that.
Fixed farmhands sometimes able to walk out of bounds at festivals.
Fixed farmhands who disconnected while fishing sometimes stuck frozen on reconnect.
Fixed farmhands who disconnected while playing a minigame (like Journey of the Prairie King) still hearing the music on the title screen.
Fixed farmhands who disconnected while in the building placement view being invisible on rejoin.
Fixed farmhands seeing spouse's outdoor area in the wrong spot on the beach farm.
Fixed farmhands experiencing latency able to click a horse, walk to a different location, then get teleported out of bounds.
Fixed farmhands able to collect multiple statues of perfection.
Fixed farmhands unable to enter a movie without all players.
Fixed farmhands' local effects sometimes based on host data (e.g. the host's equipped rings).
Fixed farmhands' prismatic shards sometimes spawning at the host's location instead.
Fixed farmhands' rings leaving lights behind when they disconnect.
Fixed farmhand crash while fishing in rare cases.
Fixed farmhand crash when they warp just as certain things happen (e.g. pet sounds).
Fixed farmhand crash if train approaches while they're mid-warp.
Fixed other players seeing a farmhand's old spouse room if they divorced and remarried in the same session.
Fixed dinos being able to hurt the host when they aren't in the same location.
Fixed monster drops for farmhands sometimes applying the host's ring effects and secret note.
Fixed various visual glitches with other players' tool/fishing animations.
Fixed crash when displaying a player status list which is missing a connected player.
Fixed dialogue being interrupted if another player starts a broadcast event; the event will now start for you when you finish the current dialogue instead.
Fixed enemy projectiles targeted at farmhands able to hit the host player in a different location.
Fixed monsters not taking damage from some hits if multiple players are attacking them at once.
Fixed projectiles causing damage multiple times in multiplayer.
Fixed various cases where values weren't correctly synced between players.
Fixed watered dirt edges not updated for farmhands when they change overnight.
Fixed 'caught snooping' chat message not triggered when Marnie sees the player searching her trash bin.
Fixed cleared-landslide mail only sent to the main player.
Fixed watering can's water left and capacity not synced in multiplayer.
Fixed the local player's step/fishing stats being incremented by other players walking or fishing.
Fixed players sometimes seeing slightly different daily quests or crop fairy event.
Fixed issue where a farmhand donating the 60th museum artifact wouldn't grant the rusty key.
Fixed issue where reading another player's secret notes or journal scraps could lock them out of perfection.
Fixed issue where the host pausing the game while it's raining and a farmhand is moving would cause the frozen rain to slide across the screen.
Fixed exploit where a farmhand would have full energy after passing out if they disconnected while sleeping earlier in the day.
Display text and localization fixes
Spanish prices are now formatted like 15o instead of 15g to match the translated term (oro instead of gold).
Fixed unlocalized text shown for...
the building paint menu's region names (like "Roof" or "Trim");
NPC names in some movie theater dialogue;
NPC names in the spouse pregnancy question;
Professor Snail's name after his first event;
Leo's name in his introductory event for some languages;
fish names for some languages in certain cases;
the 'Miss' text when an attack misses.
Fixed Lewis' letter for Feast of the Winter Star saying it starts at 10am instead of 9am.
Fixed dust sprites called dust spirits in Clint's special order and the summit cutscene.
Fixed various typos, broken tokens, translations that don't match the original, etc.
Fixed NPC name translations applied to horses/pets that share a name with that NPC.
Fixed random name generator able to produce words similar to certain slurs.
Fixed world map tooltip for Pierre's shop still showing "closed on Wednesdays" after he extends his business hours.
Fixed some recipe names not matching the items they produce.
Fixed the hats added in 1.5 translating their internal name instead of setting the display name in some languages.
Fixed museum item descriptions not having an intended newline.
Fixed French formatting times past midnight like "26h" instead of "02h" (e.g. on the fishing TV channel).
Fixed French and Turkish showing broken dialogues about another NPC's gift tastes.
Fixed French-only display text bugs related to the ^ dialogue token.
Fixed German truncating Professor Snail's name in his intro event.
Fixed Japanese and Korean formatting buff effects inconsistently.
Fixed some broken Japanese movie reaction dialogue.
Fixed Korean credit line missing in other languages.
Fixed Russian event for Professor Snail's intro freezing.
Cosmetic fixes
UI fixes:
The perfection tracker now paginates better to fit the current screen size.
Moved "?" icon on dialogue question boxes.
Removed phantom action cursor over island farmhouse drawer.
Fixed toolbar drawn behind the time/money box.
Fixed cursor over NPCs sometimes showing a gift icon when they won't accept or react to the held item.
Fixed some in-game error messages not having an error icon.
Fixed inventory & crafting menus misaligned if you resize the window while they're open.
Fixed flashing tooltips when hovering between elements in the cooking page and collections tab.
Fixed cosmetic issues with the title & shipping screens for higher-resolution displays.
Fixed calendar tooltip when a modded festival and birthday occur on the same day.
Fixed calendar drawing child NPCs lower than intended.
Fixed the ! fish bite icon not shown when fishing in the Stardew Valley Fair and Festival of Ice.
Fixed quality fertilizer showing a green tile on sprouted crops, even though it can't be placed there.
Fixed perfection tracker not skipping the typing effect when it's paginated.
Fixed the forge preview always showing soul level one for a galaxy soul forge.
Fixed advanced save option tooltips being able to extend off-screen, and not shown for some field labels.
Fixed clothing/tools sometimes showing the item-received notification on unequip.
Fixed HUD messages sometimes overlapping.
Fixed fonts sometimes having a 'thin' look.
Fixed world map tooltip for JojaMart disappearing when the movie theater is built.
Fixed stack numbers not drawn for machine output when the stack is > 1.
Fixed animal purchase menu having unnecessary padding on the right.
Fixed wiggling bottom of energy bar.
Placed object fixes:
Crab pots no longer appear during the moonlight jellies.
Tub o' flowers now shows the correct sprite on the day it is placed, and now always blooms indoors.
Fixed beds or chests that were hidden for an event not reappearing afterwards.
Fixed furniture drawn over sitting players if it has no front texture.
Fixed bombs being invisible when placed on the summit.
Fixed bombs able to remove stick bugs' sticks.
Fixed colored objects not drawn correctly when placed on tables or eaten.
Fixed prismatic hats not displayed properly on alien rarecrows.
Fixed lanterns and other furniture lights not turning on after save/load if they are on a table.
Possibly fixed clumping issue for weather debris like the spring petals.
Fixed layering issues with seagulls and Willy's house.
Fixed fruit tree leaves not rustling in winter even if they're in a non-seasonal location like the greenhouse.
Fixed barren trees having a leafy shadow.
Fixed weeds being less varied than intended in summer.
Fixed weeds able to grow on top of buildings on spring 1.
Fixed intro cutscene position not adjusted when the farmhouse is moved by a mod.
Fixed pre-built cabins sometimes placed on top of a bush or log.
Fixed many things on Ginger Island applying the valley's season or weather (including fiber seeds, seasonal decor, seasonal plants, tea bushes, and tubs o' flowers).
Fixed Elliott appearing twice during the egg hunt.
Fixed Lewis' saloon drinking animation having an incorrect frame.
Fixed bombed objects becoming tiny and sometimes showing wrong sprite index while they flash before removal.
Fixed building placement visual/sound effects playing even for players who are nowhere near it.
Fixed speech bubbles sometimes shown over invisible NPCs.
Fixed crane minigame's music sometimes continuing a few seconds after the minigame ends.
Fixed 'you received X' message & animation showing wrong item if you switch held item right as it's triggered.
Fixed some events fading in after a scene change before they're fully ready, which caused issues like NPCs visibly warping into place or mid-fade flashes.
Fixed ginger showing a watered dirt tile if you water it. This incorrectly implied that ginger needs to be watered.
Fixed missing explosion tiles in mega bomb explosions.
Fixed town festivals not showing the right version of Pam's house and community center.
Fixed an incorrect frame in Lewis' saloon drinking animation.
Fixed layering draw issue in the fishing fair minigame.
Fixes for modded players
Festivals now only set sunny weather in their location context. (For example, a custom festival in the desert no longer changes weather in the valley.)
Monsters no longer spawn at night by default on custom farm types.
Non-binary NPCs can now pathfind through any gendered route (e.g. men's or women's locker room), instead of defaulting to female routes.
Fixed crashes when...
loading a save with unknown locations or farm type, NPCs with no sprite texture, or null world objects.
the farm map has no grass spawn tile and you walk through crops or grass.
the data for an item, animal, tree, etc no longer exists.
painting a building if its sprite changed to a smaller one since it was last painted.
playing audio which doesn't exist (it now logs an error and plays a default 'quiet click' sound instead).
a farmhand warps to a location which doesn't exist locally yet.
an NPC can't parse its dialogue (it now logs the error and defaults to "..." instead).
a special order's data can't be parsed.
a mini-jukebox has an invalid track selected (it now turns off instead).
a mini-shipping bin has null items.
a statue of endless fortune tries to produce a gift for an NPC whose first loved gift is a category or context tag (it now now chooses the first valid gift taste, and falls back to a non-birthday gift if none was found);
a farm animal warps home in rare cases;
the player's NPC spouse no longer exists (e.g. the mod which added it was removed).
Fixed calendar support for multiple events on the same day (including multiple weddings, multiple birthdays, birthdays on a festival day, etc).
Fixed horses in indoor locations or mine/volcano levels unable to return home.
Fixed event setup not allowing more than 9 players.
Fixed events not exiting correctly if they crash before the first script command.
Fixed event errors not logged to the console.
Fixed potential event crash if a custom NPC name contains 'farmer'.
Fixed save loading very slowly if it has a broken outdoors location in some cases.
Fixed some items being unremovable when spawned by players. This affects incubators, mushroom boxes, slime balls, and three unused items (locked doors and alternate wicked statues).
Fixed issue when warping to Sandy early using mods where she could give daily quests as soon as you met her, but didn't accept items until you fixed the bus.
Fixed issue where sleeping in a location where an event starts the next day would skip overnight events and soft-lock the game.
Fixed invalid game state when the day of month increases past 28 due to a mod issue. Any day past 28 is now treated as the last day of the season.
Other bug fixes
Fixed crash when taking a screenshot on macOS if the ~/.local folder doesn't exist.
Fixed crash when removing light glows in rare cases.
Fixed window resize on character creation resetting profit margins & starting cabins, and desyncing the 'skip intro' checkbox.
Fixed able to equip a staircase as pants to obtain trimmed lucky purple shorts.
Fixed being able to place a yellow couch in a loom.
Fixed wilderness farm spawning a stone in water.
Fixed hill-top farm spawning grass inside of stumps.
Fixed Trash Bear treated as a villager (e.g. it could theoretically be picked for quests).
Fixed save folder collision if you set the save's name & seed to the same value as an existing save.
Fixed selecting small buildings in the construction menu's farm view. This fixes the gap above the shipping bin where it can't be selected, and fixes small buildings selectable by hovering three tiles above them.
Fixed the build number not set on Linux/macOS.
Fixed unable to write vanilla error logs for players with special characters in their name.
1.5.6
Stardew Valley 1.5.6 was released on 21 December 2021. Hotfixes were applied on 22 December 2021 (twice) and 18 January 2022.

Quality of life changes
On multi-monitor setups, the game now remembers and restores on the last used monitor.
Bug fixes
Possibly fixed a random crash that could occur at the end of the night.
Fixed issue where some farm types' wallpapers and floors weren't applied when starting a new game.
Fixed pressing ESC to dismiss the level up screen also skipping the level up itself, causing it to reappear every night.
Fixed tilled dirt still decaying under forage items on the farm. This means that dirt under freshly grown seasonal forage seeds can no longer disappear randomly.
Fixed grass placed indoors dying when the season changes to Winter.
Fixed unable to harvest tea saplings placed in garden pots on Ginger Island.
Fixed the Z key unbindable after resetting controls to the default.
Fixed map screenshots not working on Linux.
Fixed modding issues.
Internal changes
Updated Steamworks.NET to 20.0.0.
Further changes were later released without changing the version number:
22 December 2021 (announcement)
Fixed crash when starting the game on the compatibility branch on macOS.
Fixed unable to move the game window from one desktop to another in some monitor configurations.
Fixed issue that prevented selecting a profession using a gamepad. You should be able to re-select any missed professions the next day.
Fixed garden pots automatically harvesting when moused over.
Fixed Emily's patio decorations being one tile above where they should be.
22 December 2021
Fixed issue initializing Steam SDK in 1.5.6.
18 January 2022 "Hotfix #3" (appended to 1.5.6 announcement)
The version shown on the title screen ? menu now reflects hotfixes.
Changed how the Stardew valley logo is scaled on the title screen for resolutions with lower heights.
Removed the numeric hotkey displays along the top of the inventory screen menu when playing on a controller.
Fixed player/horse placement issues after triggering an event on the farm while on horseback (including an issue that could cause a farmhand to become stuck in a wall after viewing Leah's 6-heart event).
Fixed Korean/English dialogue line swapped for collapsed-in-Volcano scene.
Fixed exclusive fullscreen mode being off-center or incorrectly sized when Window's zoom isn't set to 100% on main-branch builds.
Added failsafe when maximizing/windowing from the title screen to clamp to the upper-right corner of the current display in fullscreen mode.
1.5.5
Stardew Valley 1.5.5 was released to the Steam beta branch on 17 August 2021 for mod authors, announced in the forums on 07 September 2021, and released to all players on 30 November 2021. Hotfixes were applied on 3 December 2021, 5 December 2021, and 7 December 2021.

Architectural changes
Added support for Xbox Game Pass.
This migrates the game on Windows from .NET Framework 4.5.2 to .NET 5. You may need to launch the vanilla game once through Steam/GOG to install the new dependencies.
Added internal changes for mod authors (see mod author migration guide and completed modding wishlist items).
Quality of life changes
Holding Control + Shift now lets you purchase or craft stacks of 25 items at a time.
Many in-game settings now remember their last value when you start a new save. (Some settings like zoom level, gamepad mode, and multiplayer server privacy aren't copied over.)
You can now build or move farm buildings onto artifact spots (which will destroy the artifact spots).
You can now nudge pets out of the way while building/moving a building by clicking on them.
You can now buy back items accidentally sold in the same shopping session.
The in-game time is now shown on the upper-right hand corner of the screen when playing Journey of the Prairie King in multiplayer.
Grass placed using grass starters during winter no longer disappears when the game is reloaded (but it still won't grow or spread). Grass that's outdoors in winter now takes on the appearance of the grass found in the frost section of the mines.
Added /printdiag chat command which prints some diagnostic info to the chat window.
Localization fixes
Fixed Shane's 6-heart event soft-locking in the Hungarian translation.
Fixed incorrect '\' characters in various events in the Hungarian localization.
Fixed typos in the French localization.
Fixed a typo in Livin' Off The Land that incorrectly states that super cucumber can be caught in Winter.
Cosmetic fixes
Added commas to the price display on Robin and the Wizard's building menus.
Adjusted collisions on the desert map to avoid sorting issue on the top-left edge of raised cliffside.
Fixed issue where Sebastian's sprite would shift into an invalid position at 1:00 PM when he's working on his bike on the farm.
General fixes
After completing the Cryptic Note quest, reaching floor 100 of the Skull Cavern again will guarantee a chest.
Fixed issue where the harder Mines could become permanently enabled and unable to change back.
Fixed radioactive bars not affected by the Blacksmith profession.
Fixed explosion radius not centered when dislodging flooring and certain other types of items.
Fixed garden pots clearing their fertilizers when a crop is harvested.
Fixed placing a garden pot on Ginger Island on a rainy day not watering its dirt.
Fixed multiplayer hosts registering their lobbies before fully loading a save, causing the games not to appear in the multiplayer games list.
Fixed moving a cabin with a cellar causing the stairs to the cellar to warp the players out of bounds for the rest of the play session.
Fixed a case where entering the Farm from the south on horseback and triggering an event could cause the player to get stuck in a wall.
Fixed various invisible tiles preventing certain spots in the Mountain lake from spawning fish activity bubbles.
Fixed the tile holding the plant on Elliott's table not being passable.
Fixed some tiles on the left side of the beach farm being unbuildable.
Further changes were later released without changing the version number:
3 December 2021 (announcement, release notes appended to 1.5.5 post)
Fixed widescreen and UHD displays not handled correctly.
Fixed crash in the French localization for the "It Howls In The Rain" movie.
Fixed GOG builds not optimized for release, which caused errors with some mods.
Fixed gamepad issues on Linux and macOS with the main 64-bit branch.
5 December 2021
Reverted gamepad fix in the previous update, which caused crashes for some players.
7 December 2021 (see announcement for release, revert, and re-release)
Fixed a memory leak related to sound effects.
Fixed an issue where quitting the game in exclusive fullscreen would revert to windowed borderless upon reloading the game.
Fixed an issue where the last-used volume levels weren't properly applied when starting a new game.
Fixed special orders board appearing distorted during festivals.
(Modding) Fixed [HOURS_24_00] not properly zero padded.
1.5.4
Stardew Valley 1.5.4 was released on 22 January 2021. A hotfix was applied on 2 June 2021.

Changes
Pam no longer visits the Island resort on Sandy's birthday.
The Stardew Valley Fair shop no longer sells multiples of the randomly chosen items.
The Stardew Valley Fair shop now sells triple shot espresso instead of tea sapling.
Multiplayer fixes
Fixed a rare crash that could occur when watching an event in multiplayer as the clock hits midnight or 1am.
Fixed the sound of fiber crops being harvested being audible when you're in another area.
General fixes
Items related to Qi challenges and special orders are now properly removed from both Marlon's Item Recovery Service, and items requested to be recovered are now removed from the mailbox once the quest expires.
Fixed perfection check not accounting for games where the farm switched to the Joja route partway through a Community Center playthrough.
Fixed lucky rings losing their luck bonus overnight.
Fixed softlock when fishing with multiple rods in your inventory after catching a treasure and casting from a different rod. This fixes the common fishing rod softlock next to Willy's house and during the Festival of Ice.
Fixed exploit where entering the Skull Cavern would immediately unlock all 120 floors for the elevator in The Mines.
Fixed exploit where you could find lost books by storing and retrieving certain wallpapers in chests.
Fixed a rare issue where a charged hoe could dislodge a non-empty chest and destroying its contents if it was placed in a specific configuration next to other chests.
Fixed issue where the buttons in the CalicoJack and Calico Spin minigames wouldn't respond to controller input if the UI scale setting didn't match zoom level setting.
Fixed issue where bombing certain floor tiles in the quarry would spawn items.
Fixed palm trees in the desert producing golden coconuts.
Fixed being able to interact with objects while warping with the return scepter.
Fixed trees able to grow on top of placed furniture items.
Fixed a minor graphical inconsistency with the quality indicator on procedurally-colored objects such as flowers.
Fixed Leo's first event unable to complete when playing in the Korean localization.
Fixed the special order board being invisible during summer in the Korean localization.
Various localization corrections.
Further changes were later released without changing the version number:
2 June 2021 (announcement)
Adjusted the randomization of the mummified bat drop.
Fixed multiplayer issues on macOS.
Fixed text wrapping issue on the Special Orders board in the Korean localization.
Fixed some stardrops not always counted for the perfection score. Reaching max stamina now counts as having found all stardrops.
1.5.3
Stardew Valley 1.5.3 was released on 15 January 2021. A hotfix was applied on 16 January 2021.

Balance changes
The stone owl is now rarer.
The strange capsule now only spawns once per game.
Prismatic slimes are now more common (0.8% chance to 1.2% chance), and their spawn rate is now affected by daily luck.
Fixed exploit where Qi beans/fruit weren't removed from machines/craftables after the challenge expires.
You can no longer catch Qi Beans when fishing during festivals.
Minor changes
Adjusted Leo's gift tastes.
Tweaked stone owl sprite.
Penny's 14 heart event now places your existing bed in a chest rather than replacing it.
Furniture is no longer visible and can no longer block movement during events that take place outside of the farm.
Multiplayer fixes
Crab pots now check the professions of the player who refilled them. This fixes a case in multiplayer where a player's profession (such as Mariner) would appear to not work because the crab pot was originally placed in the water by someone else.
Fixed the summit event not triggered if the player is married to another player.
Fixed the menu backgrounds option displayed incorrectly when playing in split-screen mode on a rainy day.
Fixed incorrect button mapping shown on Local Coop Join screen.
General fixes
Experimentally fixed rendering on ultra-wide displays.
Potentially fixed various cases where the player could get stuck or softlocked in an animation after using a tool (including the the horse flute softlock and possibly fishing softlocks).
The Farmer no longer blinks while charging a tool. This was causing a minor visual issue.
Fixed summit event being repeatable if its music wasn't marked as heard. The music is now saved as soon as the event is started.
Fixed issue where a character could spawn on the upper-left corner of the island map when skipping the Ginger Island departure event while the character is still pathing.
Fixed Leo using the wrong schedule on Wednesdays after his six-heart event.
Fixed issue where the quality bobber wasn't applying its bonus.
Fixed magic bait not working to catch Night Market fish in the southwest corner of the beach.
Fixed issue where you could get softlocked if you hooked a fish just as the pirate cave event begins.
Fixed some minor data entry issues on normal bundles that also appear in remixed bundles (Animal Bundle requiring a small brown egg instead of a large white egg, and normal cheese not being an option in the Artisan Bundle).
Fixed bug preventing prismatic slimes from not dropping prismatic jelly in rare cases.
Fixed bug where the strange capsule would leave a residual light glow.
Fixed overnight lost & found tool logic not checking the island farmhouse fridge.
Fixed crash that could occur if a dust sprite's stone-breaking move would cause a Qi Bean to spawn.
Fixed a long delay after talking to Gourmand when you've got the crop he's requested growing, but it's not yet fully grown.
Fixed the daytime music from Ginger Island not being playable on the Saloon jukebox.
Fixed a crash when using a warp totem while the mermaid show is playing.
Fixed issue where you couldn't go back to sleep immediately after waking up after passing out.
Fixed item duplication glitches related to moving rings around in certain menus.
Fixed certain gemstones appearing on the daily quest board before they're actually accessible in-game.
Fixed various localization issues.
(Modding) A randomized bundle containing an invalid item now shows a more detailed error message.
(Modding) Fixed big craftables losing mod data when picked up.
(Modding) Fixed issue where going from one floor to another on horseback inside the Volcano would position the player incorrectly on the next floor.
Further changes were later released without changing the version number:
16 January 2021 (announcement)
Fixed exploit where Qi beans/fruit weren't removed from Marlon's item recovery service after the challenge expires.
Fixed a multiplayer fishing softlock added in 1.5.3.
1.5.2
Stardew Valley 1.5.2 was released on 8 January 2021.

Feature changes
You can now dismiss the level-up menu by pressing the ESC key.
Balance changes
Qi fruit can now be grown on the farm during winter.
Tools now track the previous two enchantments applied to them so they're not reselected when you reapply an enchantment.
Coral and other aquatic forage items are now included for the "Botanist" profession.
Added dark cowboy hat to Skull Cavern chest loot table.
You can no longer increase speed buffs using Qi seasoning.
Buff durations from Qi seasoned food/drinks are now 50% longer.
You can no longer complete the "Danger In The Deep" Qi Challenge by visiting the Skull Cavern.
Reduced price when selling cookout kits from 3000g to 80g.
Reduced price when selling ducks from 4000g to 1200g.
Fixed ducks not selling for the appropriate price.
Ginger Island fixes
Adjusted a journal scrap treasure map to better represent the in-game location.
Added failsafe to prevent players from warping to the upper-left corner of the southern island map.
Passing out in Qi's secret room no longer causes you to wake up on the mainland.
Fixed Junimos not harvesting crops if you spent the night on the island or when you're not physically present.
Fixed unable to place mini-fridges in the Island farmhouse.
Fixed unable to collect honey from bee houses on the island farm in winter.
Fixed garden pots on the island farm becoming watered on days when it's raining in the valley.
Fixed forage crops disappearing overnight on the island farm on Saturdays/Sundays.
Multiplayer fixes
Fixed most minigames appearing misaligned in split-screen mode.
Fixed a crash that could occur in the mermaid show in split-screen mode.
Fixed farmhands getting stuck if two split-screen players choose the same farmhand at the same time.
Fixed a crash when crab pots are removed by a farmhand.
General fixes
You can no longer sit on chairs if the game is currently pausing your character due to an animation (such as using a tool or kissing your spouse).
You can no longer instantly kill Fector as a zombie in Journey of the Prairie King.
Adjusted the rendering of very wide furniture items so that they do not extend too far past an inventory slot.
Fixed issue preventing 100% perfection score in the Joja route.
Fixed graphical issues with the post-perfection event.
Fixed coral not considered red instead of pale violet red for dyes, etc.
Fixed hearts dropped during Qi's Hungry Challenge not collectable if the inventory is full.
Fixed the level-up screen's OK button positioned offscreen in some cases.
Fixed the Key to the City not allowing you into Pierre's shop if you completed the game through the Joja route.
Fixed issue where large amounts of beets placed in a mill wouldn't produce the proper amount of sugar.
Fixed gifting-related special order objectives not correctly checking the minimum liked value of gifted items.
Fixed special order-related items stored in Junimo chests not properly removed once the special order expires.
Fixed fruit tree saplings and seeds sold at festivals not properly reflecting the profit margins setting.
Fixed sign items no longer showing their placement indicator once a fish pond had been built on the farm.
Fixed combined rings only showing the stat buffs from their first component ring.
Fixed combined rings not properly using their localized name.
Fixed a ring duplication glitch in the dye pot menu.
Fixed a crash and other issues related to obtaining the Iridium Krobus item.
Potentially fixed a random crash that occurs when going to bed.
Potentially fixed a crash in the mines.
Fixed a crash when fishing from the pond on your farm using magic bait.
Fixed a bug causing cheese cauliflower to not display in the collections tab.
Fixed breaking open geodes and artifact troves incorrectly counted as two item collects in the collections tab.
Fixed a crash that could occur when clicking in the scrollbar region of a shop menu when there are less than four items available.
Fixed issue where placing a bomb and sleeping could cause the fuse sound to play indefinitely.
Fixed issue where weeds could appear as batteries.
Fixed weapon cooldown timers no longer displaying on weapons in the shop menu.
(Modding) Fixed order/naming of tilesheets on the beach farm inconsistent with the other farm types.
Localization fixes
Fixed a missing event in Willy's shop from the Hungarian localization.
Fixed an issue with Leo's six-Heart event in the German localization. This fix is applied retroactively.
Fixed an issue where some weapons added in 1.5 would display an incorrect weapon name in the German localization.
Fixed crashes related to Lewis' phone call in various localizations.
Fixed various minor typos.
Various localization fixes.
1.5.1
Stardew Valley 1.5.1 was released on 24 December 2020.

Feature changes
The crystal cave puzzle now gradually gets easier after repeated misses.
Spouses no longer stand around looking at rug-type furniture items. This fixes a case where a spouse might stare at a floor divider, which could cause them to block the player's way through a narrow hallway.
Multiplayer fixes
Fixed exploit where you could regain stamina in bed in multiplayer even if the game was paused.
Fixed rare issue where the host player would warp to an invalid position if a farmhand had just completed a Community Center bundle.
Localization fixes
Various localization fixes and changes.
Fixed a crash when bombing the cave entrance next to the Field Office when playing in Spanish.
Fixed issues with Lewis's phone call in various localizations.
Fixed bug in the Spanish translations preventing Birdie's introduction event from completing.
Fixed bug in the German translations preventing male characters from completing Birdie's quest.
General fixes
When dismissing the forge menu, items that can't fit in your inventory are now dropped downward instead of upward to avoid items being dropped into the lava.
Fixed pets sometimes warping out of bounds.
Fixed being able to place objects in some parts of the void in the farmhouse.
Fixed "spawn monsters on the farm" advanced game option resetting when you choose a different farm type after changing it.
Fixed redeeming a stack of items at the Stardew Valley Fair granting a single item, instead of the whole stack.
Fixed an issue related to having a child named Leo or Kent, where existing friendship points for these characters would be transferred over to your children.
Fixed some new hairstyles clipping through hats.
Fixed issue where purchasing the master slingshot would give the player a normal slingshot.
Fixed unable to select the Beach Farm on the new game screen when playing with a controller at minimum resolution.
Fixed Leo available as secret santa if he's not in town.
Fixed being able to place objects in certain tiles that block player movement such as the landslide that blocks the path to the Mines.
Fixed issue where killing big slimes carrying hearts during Qi's Hungry Challenge, while wearing the burglar's ring, would cause the hearts to be collectable in the player's inventory.
Fixed a crash that occurs when demolishing cabins.
Fixed a crash that could occur overnight if you place the Auto-Petter anywhere that isn't a coop or a barn.
Fixed Maru standing on the wrong tile outside the farm on Saturdays if you're married to her.
Fixed hair #56 accidentally replaced.
Fixed Birdie's item trade quest removing all stacks of an item when they're given to their intended recipient.
(Modding) Fixed the return scepter not returning to overwritten farmhouse entry positions.
1.5
Stardew Valley 1.5.0 was released on 21 December 2020. Hotfixes were applied on 21 December 2020, 22 December 2020, and 23 December 2020.

New world area
1.5 adds an entire new region of the world, Ginger Island in the Fern Islands:
Added new locations, dialogue, events, minigames, puzzles, and a quest line involving multiple NPCs.
Added Leo, a new NPC with his own backstory, plot line, events, etc.
Added new secondary NPCs: Birdie, Gourmand Frog, and Professor Snail.
Added a volcano dungeon which changes each time you visit it similar to the mines.
Added Qi challenges which unlock rare or unique items.
Added an unlockable island farm and farmhouse area, where you can plant crops in any season but can't construct buildings.
Added an unlockable resort you can open to let villagers visit the islands, including new beach attire and schedules.
Added hidden pages of a lost sailor's journal to uncover his story and learn about the islands.
Added golden walnuts hidden throughout the islands, which can be used to unlock new areas and content.
Added golden coconuts, which Clint can crack open to find rare island items.
Added secrets and puzzles to discover around the island.
Added new enemies:
dwarvish sentry;
false magma cap;
hot head;
lava lurk;
magma sprite;
magma sparker;
magma duggy;
spiker;
stick bug;
tiger slime.
Added new cosmetic critters: crabs, caldera monkeys, overhead parrots, marsupial, and tropical butterflies.
Added new island obelisk building.
New farm features
Added a new beach farm layout.
Added ostrich as a farm animal.
The immovable dressers found in Farmhands’ cabins have been removed.
Added home renovations, which let you further expand and adjust the farmhouse after it's fully upgraded.
Beds are now normal furniture you can pick up, move around, and replace. (You can even have a house with no bed, but your spouse might have something to say about that.)
Once unlocked, the greenhouse can now be moved at Robin's shop.
The default shipping bin can now be moved or demolished at Robin's shop.
Added advanced game options, which can be used to customize a new game:
set seed value used in randomization;
choose default vs randomized community center bundles;
choose default vs randomized mine chests;
make red cabbage seeds guaranteed to sell at least once at the travelling cart in year one, so it's always possible to finish the community center in the first year;
change profit margins and cabin-related options that were previously inaccessible when creating a single-player farm.
can toggle monsters spawning.
You can now apply cosmetic paints to the farmhouse and buildings.
Ducks can now swim in water, and certain coop animals will now follow adults around.
Slimes now drink from slime hutch troughs in random order.
Other new content and features
Added tool and weapon enchanting.
Added ability to combine two rings into one.
Added special orders, more dynamic late-game quests which let you help villagers with their personal projects through a special orders board in town. These can include more varied goals and rewards, temporary world changes (like new enemies for the duration of the quest), permanent changes (e.g., new shop inventory), and post-completion events.
Added a second community upgrade.
Added a more difficult version of the mines and the Skull Cavern, which includes new and more powerful monsters along with better drops. These can be accessed late-game, and can optionally be toggled permanently using the Shrine of Challenge.
Added new enemies which appear in the difficult mines:
shadow sniper;
skeleton mage;
spider (jumps, often found near webs that can trap players and dust sprites);
prismatic slime (quest only);
putrid ghost (causes nauseated debuff);
blue squid;
royal serpent;
slime variants ('cool' and stacked).
Added new fishing TV channel.
Added new crops and trees:
mahogany tree (drops hardwood)
mahogany seed;
fiber seeds;
ginger (forage);
banana;
mango;
pineapple;
taro root (paddy crop);
New palm tree variant;
Qi fruit (available during special Qi quest).
Festival changes:
added new even-numbered year dialogues for Egg Festival;
added shops to the Dance of the Moonlight Jellies, Feast of the Winter Star, Festival of Ice, and Luau;
added new items to various festival shops;
Children now attend festivals.
You can now change your name and gender in the Wizard's basement shrine.
You now have a perfection rating which tracks the percentage of game content you've completed. Reaching full completion lets you buy golden chickens, adds a random Golden Witch event, unlocks access to the Summit with a new event, and adds new bird critters.
You can now further customize sprinklers with attachments:
enricher automatically applies loaded fertilizer while planting seeds nearby;
pressure nozzle increases watering range.
Added new craftable items and machines:
auto-petter auto-pets animals in a coop or barn (this keeps your animals content, but can't replace the full benefit of human touch);
bone mill turns bone items into fertilizer;
coffee maker brews a fresh cup every morning;
cookout kit lets you cook on the go;
dark sign displays an item without consuming it;
deconstructor destroys crafted items, but salvages their most valuable material;
farm computer scans the farm and displays useful information;
geode crusher consumes coal to break open geodes.
heavy tapper works twice as fast as a normal tapper;
hopper auto-loads items placed inside into the machine in front of it;
Junimo chests are linked to a global shared stash;
mini-obelisks let you warp between two obelisks when placed on the farm;
mini-shipping bins is a smaller shipping bin that can be placed outside the farm;
ostrich incubator when placed in a barn, hatches ostrich eggs into baby ostriches;
solar panel slowly generates battery packs when left in the sun;
statue of true perfection produces a prismatic shard each day;
stone chest is a variant of chest crafted with stone instead of wood;
telephone calls stores to check hours and inventory, and occasionally receive random phone calls (no effect on gameplay);
warp totem: island warps to the Fern Islands.
Added new food items:
bug steak;
banana pudding;
ginger;
ginger ale;
mango sticky rice;
piña colada;
poi;
taro root;
tropical curry;
squid ink ravioli (temporarily prevents debuffs).
Added new fertilizers:
deluxe fertilizer increases chance of higher-quality crops;
deluxe retaining soil always keeps soil watered overnight;
hyper speed-gro increases growth rate by at least 33%.
Added new items:
bone fragment;
Fossilized Skull, Spine, Tail, Legs, and Ribs and snake skull, snake vertebrae;
cinder shard;
dragon tooth;
tiger slime egg;
fairy dust can used on a machine to have it finish processing;
golden walnut;
magma cap;
monster musk causes more monsters to spawn;
mummified bat and mummified frog;
ostrich egg;
Qi gem;
Qi seasoning increases quality of cooked recipes;
radioactive ore and radioactive bar;
taro tuber;
horse flute summons your horse when outside;
mushroom tree seed.
Added new fishing tackle:
curiosity lure increases the chance to catch rare fish;
quality bobber increases fish quality;
magic bait catches fish from any season/time/weather for a given location.
Added new quest items:
Advanced TV Remote
Arctic Shard
Ectoplasm
Gourmet Tomato Salt
Pierre's Missing Stocklist
Pirate's Locket
Prismatic Jelly
Stardew Valley Rose
War Momento
Wriggling Worm
Added new rings:
glowstone ring provides both light and increased item collection radius;
hot java ring increases your chance to find coffee drinks when slaying monsters;
immunity band reduces chance of status debuffs by 40%;
lucky ring increases luck by +1;
phoenix ring restores some health after being knocked out once per day.
protection ring keeps you invincible longer after taking damage;
soul sapper ring restores a bit of energy after slaying a monster;
thorns ring damages enemies when they attack you.
Added new hats:
???;
dark cowboy hat;
deluxe pirate hat;
forager's hat;
goggles;
golden helmet;
Mr. Qi's hat;
pink bow;
Qi mask (secret);
radioactive goggles;
star helmet;
sunglasses;
swashbuckler hat;
tiger hat;
warrior helmet.
Added new clothing:
banana shirt;
ginger overalls;
hot pink shirt;
island bikini;
magenta shirt;
tropical sunrise shirt;
yellow suit.
Added new shoes:
cinderclown shoes;
mermaid boots;
dragonscale boots;
crystal shoes.
Added new weapons:
dwarf sword, dwarf hammer, and dwarf dagger;
dragontooth cutlass, dragontooth club, and dragontooth shiv;
infinity blade, infinity dagger, and infinity gavel;
iridium needle;
ossified blade;
some previously inaccessible items have also been made accessible.
Added new fish:
stingray;
lionfish;
blue discus;
legendary fish:
Glacierfish Jr.;
Legend II;
Ms. Angler;
Radioactive Carp;
Son of Crimsonfish.
Added new furniture:
35 paintings (many only found in festival shops or while fishing certain locations);
14 bed variants;
ten rugs:
blossom rug;
funky rug;
icy rug;
large cottage rug;
large green rug;
large red rug;
light green rug;
modern rug;
oceanic rug;
old world rug;
eight 'floor divider' rugs that can be placed between rooms to join visually different floor types;
five fish tanks you can put fish in (including an Easter egg involving hats);
decorative trash can;
gourmand statue;
iridium krobus;
large brown couch;
plain torch and stump torch;
squirrel figurine;
tropical chair.
Added a new 'sconce' furniture type with seven options.
Added new flooring:
rustic plank floor;
stone walkway floor.
Added new debuffs from enemies:
burnt (Speed -2, Defense -3);
darkness (dims lighting, making it harder to see in caves);
frozen (speed -8);
nauseated (prevents you from eating or drinking anything);
weakness (-20 Attack).
Added 17 new hair styles.
Added mail from Krobus with his own stationary.
Added new decorations and tweaks to many maps.
Added new Easter eggs:
Easter egg when you change your name at the Shrine of Illusions to include item spawn codes;
title screen 'happy face' secret;
new lucky purple shorts secret;
new strange capsule secret.
Emily now visits Sandy on her birthday.
Clicking the pigs at the Festival of Ice now plays a pig sound.
Quality of life changes
Added lost & found box in Mayor Lewis' house. This can be used to retrieve items donated to failed special orders, lost quest items and tools, items from offline players, hats from children that have been turned into doves, and items left behind in the Stardew Valley Fair grange display.
You can now sit on chairs (both placed furniture and chairs that are part of the map).
You can now place most furniture outside.
You can now talk to people while mounted on a horse.
You can now donate items of different qualities for the same community bundle ingredient.
You can no longer plant fruit trees on tiles they won't be able to grow on.
Improved game menus and HUD:
The social tab now shows whether you talked to an NPC today.
The cooking tab now shows the recipe for an item when you hover over it.
The cooking tab now fades icons for recipes you know but haven't made yet.
The cooking/crafting tooltips now show the number produced.
The inventory menu's organize button now combines partial item stacks.
The inventory menu for a chest now shows the Community Center button.
The shipment screen now shows the unit price of shipped items instead of displaying the shipped quantity twice.
The quest log now shows an arrow in the morning when you have pending completed quests.
Buff icons now subtly pulse when they're close to expiring.
Improved shop menus:
You can now press `ESC` or controller `B` to move the held item to your inventory (or drop it if you have no more inventory room).
While holding a purchase, the inventory now highlights items you can stack it with.
Improved sprinklers:
Sprinklers can now water slime hutch troughs.
Hoes no longer remove sprinklers.
Improved Journey of the Prairie King:
Progress can now be saved and resumed, so it can be completed in multiple sessions.
You now also replay the original difficulty even if you've already completed it. (Previously it would increase difficulty automatically, which is now a New Game+ mode.)
Improved game options:
added option to choose between multiple fish-bite chime sounds;
added option to mute farm animals and pets;
you can now scale the UI independently of the view zoom;
increased maximum zoom from 120% to 200%.
Improved various items:
The jukebox now has a "Random" setting.
Removing a crystalarium that isn't ready for harvest will now drop the gem that was placed in it.
You can now push chests containing items by holding the interact button on them with no tool equipped (the same way you could previously remove empty chests without using a tool).
Improved inventory sorting:
no longer changes tool order;
now sorts by quality too;
now sorts names in alphabetical instead of reverse alphabetical order.
Improved museum donation interactions:
Clicking an item now grabs one instead of the whole stack.
Pressing back while placing an item now returns to the inventory instead of closing the whole UI.
Other minor improvements.
Improved HUD:
Added a notification when you enter a farm building if an incubator is ready but the building is at max capacity.
The "infestation" indicator in the mines is now drawn alongside the floor number, rather than replacing it.
Balance changes
Combat changes:
Immunity now reduces the chance of status debuffs.
Changed special move cooldowns on daggers (6→3 seconds) and clubs (4→6 seconds).
The dagger special attack now pins the target in place until the last stab (which then knocks them back), so dagger hits are less likely to miss.
Reduced desperado profession's damage bonus from 3x to 2x.
Slightly improved dagger critical hit chance.
Crafting changes:
Changed skull brazier recipe (was 10 hardwood + solar essence + coal; now 10 bone fragments).
Repairing a fence now restores full fence health, instead of half the health of a new fence.
Farming changes:
Lowered the cost of ducks (2000→600g).
Doubled the value of duck feathers.
Slightly increased the duck feather spawn rate.
Fishing changes:
Fishing rod tackle no longer loses endurance when catching junk.
Catching a non-fish item no longer triggers the minigame.
Reaching an effective fishing level of 15+ now increases the rod casting range by one tile.
Mining changes:
Gem nodes now provide mining XP and can drop diamonds.
Gem node drops are no longer limited by mine level.
Item drop changes:
Stumps and hollow logs now have a 10% chance of dropping mahogany seeds.
Any monster in the Secret Woods now has a 10% chance of dropping mahogany seeds.
Skeletons now have 4% chance of dropping a bone sword.
Wilderness golems now drop rice shoots more often.
Some Skull Cavern monsters now have a small chance of dropping red cabbage seeds.
Pure-white slimes now drop diamonds and refined quartz.
Some containers now drop better items after reaching the bottom of the mines at least once.
Different drops now unlock on mine levels 60/80/100 and the first level of the Skull Cavern.
Reduced chance of lead rod drops on mine levels 60–79 (or Skull Cavern level 40+ before the previous fix), and added chance for shadow dagger and wood mallet.
Mine wood barrels can now drop basic retaining soil instead of sap.
Mine frost barrels can now drop quality retaining soil instead of sap.
Reduced chance of frost barrels dropping aquamarine, frozen geode, hardwood, jade, or equipment from 35% to 26%.
Shop changes:
Pierre will now sell his seasonal items year-round once you complete a certain new quest.
Added two more items to the Stardew Valley Fair star token shop.
Coconuts can be purchased from Sandy on Monday. This is now limited to ten per day.
The slingshot and master slingshot are now sold at the Adventurer's Guild.
Reduced workbench price (3000→2000g).
Reduced earth obelisk and water obelisk prices (1000000→500000g).
Machine changes:
Some machines' processing time was previously affected by the time of day. These have been standardized so they're always ready when the morning starts: bee house (every 4 days), mushroom box (every day), strange capsule (3 days), Tapper (depends on input), and worm bin (every morning).
Doubled star token rewards for the slingshot and fishing minigames at the Stardew Valley Fair.
Fertilizer in the greenhouse no longer disappears on season change in some cases.
The random stone owl and strange capsule night events are now much less rare.
Multiplayer changes
Added local split-screen multiplayer mode.
The join co-op screen now remembers the last IP you entered.
Farmhands can now move buildings through Robin's menu. The host can configure how this works (disabled, enabled, or only for a player's own cabin).
Using the return scepter now returns farmhands to their cabin's front door instead of the host's farmhouse.
Added various new chat messages when a player does something.
When viewing a shared event in multiplayer (such as the Community Center event, or Morris' introduction), you are no longer forcibly warped to the event location.
When the host player sees the year 3 event, Grandpa's Theme is now added to all players' jukeboxes even if they weren't in-game at the time.
Interaction changes
Reworked slingshot controls: it now aims at the cursor position, and is fired by holding and releasing the mouse/gamepad fire button. The previous mode (where you'd hold the button and pull back on the cursor to aim) can be re-enabled in the options menu if desired.
To simplify bulk actions like harvesting, holding down a button while moving will no longer repeat weapon special attacks, open/close barn/coop doors, or interact with boulders, chests, furniture, hollow logs, meteorites, shipping bins, or scarecrows.
Constructed shipping bins now have a click-to-ship hitbox that better matches the original map-based shipping bin's hitbox.
Flooring can now be applied by clicking on the tile the farmer is standing on. Previously, flooring had to be applied to a tile next to the farmer.
Purchasing recipes with a full inventory no longer shows a message that the inventory is full.
Clicking an empty tile right above an interactive element (like a machine or chest) now activates the element, similar to clicking below it in previous versions.
Trees chopped from above or below will now take into consideration the player’s horizontal position when falling to the left or right.
Clicking near the bottom-left corner of the screen no longer brings up the chat box.
You can no longer open the quest log by pressing the on-screen journal button if you're currently doing something.
You can now use the "Y" key to answer dialogue boxes for holes and exit ladders in the mines.
Controller improvements:
When buying/betting tokens in the Stardew Valley Festival with a controller, holding the number selection button now causes the amount to increase faster.
Events can now be skipped on the controller even if a dialogue box is on-screen.
Pressing B on a controller while on a specific quest page now returns to the quest list instead of closing the menu.
Pressing B on a controller while an item is held on the crafting menu now snaps to the trash can (similar to the inventory screen).
Other changes
Save names are now based on the farm name instead of the player name. (Saves originally created before 1.5 will continue using the player name.)
Penny and the Dwarf now like artifacts, all other NPCs dislike (instead of hate) them as gifts.
Improved dinosaur sleep sprites.
Characters now face you when you talk to them instead of when the dialogue box closes (in singleplayer).
On the final day of a tracked quest, the timer now says "final day" instead of "1 day" for clarity.
Added many changes for modders; see completed wishlist items and mod migration guide for details.
Cosmetic tweaks to various sprites.
Fixes for multiplayer
Fixed an issue where fences would degrade faster in Multiplayer.
Fixed issue where a farmhand crashing while completing the final bundle could permanently prevent the unlock from properly triggering. It is now unlocked the next time a character enters the area.
Farmhands are now properly positioned under the elevator instead of the ladder when using it to navigate the mines.
Fixed an issue where other farmers’ emotes would not playback properly if you were watching an event.
Fixed a minor issue where multiple players getting the free coffee gift at the Night Market at the same time could prevent anyone from receiving it.
Fixed the note from Grandpa reappearing for farmhands.
Fixed issue where cows in Haley's photoshoot event could be seen sliding around for farmhands. (Non-actor characters in events are now controlled by the host.)
Fixes for player interaction
Fixed rare controller and mouse input drops.
Fixed being unable to remount a horse after dismounting it behind a shipping bin.
Fixed issue where it would sometimes be impossible to name an animal with a controller because the onscreen keyboard would appear and disappear in the same frame.
Fixed character customization screen's hair color slider not properly updating when hair color is randomized.
Fixed some farm tiles incorrectly preventing buildings from being placed on them.
Fixes for visual or cosmetic issues
Adjusted the sorting of item ready indicators for tappers.
Unified when night tiles get applied to fix inconsistencies when windows change from light to dark.
The critters list is now cleared out overnight. This fixes an issue where having a Butterfly Hutch in your house and repeatedly sleeping without leaving would spawn endless butterflies in the house.
Improved various text:
Fixed some localizations using inches for fish measurements to reference centimeters.
Fixed mill description not mentioning rice.
Fixed typos in dialogue and events.
Fixed missing characters in Chinese and Korean fonts.
Fixed credits not showing localizer names correctly if the current language's font doesn't have the needed characters.
Improved many translations.
Fixed various cosmetic/layering issues with character shadows.
Fixed characters in events snapping to strange animation frames when skipping an event.
Fixed various instances where the camera would pan unnecessarily after changing locations.
Fixed greenhouse trees taking on seasonal appearances.
Fixed tooltip for purchasing edible but non-health-restoring items (like crocus) showing price outside of the tooltip.
Fixed a single-frame flicker in Haley’s 10-heart event.
Fixed a single frame flicker of the farm when starting a new game.
Fixed stamina bar showing sweat particles when fishing during the fishing competition.
Fixed the scythe showing the weapon ability cooldown effects.
Fixed the erroneous door tile visible on the south end of the standard farm during winter.
Fixed issue where unlocking multiple community center bundles at once would make the screen pan to the same room multiple times.
Fixed various issues related to the Festival of Ice map, like being able to escape the festival bounds or prematurely end the festival from certain tiles, and minor visual fixes.
Fixed terrain features showing an "interact" cursor when mousing over their tiles during festivals.
Fixed options page scrollbar sometimes going past the end of the scrollbar region.
Fixed various text overflow issues on the options page.
Fixed chests spawned on certain Skull Cavern floors being shifted down by 4 tiles.
Fixed tiling of…
floor tiles in the farmhouse so applied flooring in adjacent rooms appear contiguous instead of having hard edges;
wall tiles in the farmhouse to fix sorting of certain objects that extend outside normal tile boundaries (e.g., grass starter).
the fountain so that it has a more consistent appearance throughout the seasons;
Pierre's stand at the Egg Festival to fix layering issues.
Other bug fixes
Fixed crash when resizing game window in some cases.
Fixed rare crash on launch due to invalid game window size options.
Fixed Iridium Bat kills not counting towards Adventurer's Guild bat eradication goal.
Fixed an issue where the Mermaid Show reward was delayed incorrectly.
Fixed some events showing a dark blue screen after fading out when viewed during rainy days.
Fixed museum-related rarecrows not sold at the Night Market after being unlocked.
Fixed issue where non-wooden gates would revert to wooden gates after saving & loading a game.
Fixed being able to add staircases to the Luau.
Fixed an item duplication exploit related to chest organization.
Fixed a minor desync in character pathfinding that could happen when characters pathed to the JojaMart on modded games.
Fixed Penny walking through walls on rainy days if you've completed the community upgrade.
Fixed Penny's 4-heart event not accessible once you finish the community upgrade.
Fixed fences not collected correctly after a divorce or Penny's 14-heart event.
Fixed characters greeting you when you enter a location when they're not present.
Fixed characters you divorced still greeting you when you enter a location.
Fixed issue where an NPC spouse fails to pathfind when a player/NPC is blocking the front door when they check, causing them to stand in place instead.
Fixed crops sometimes growing a day slower than they should.
Fixed applying flooring for the first time in an upgraded house sometimes causing the flooring in the kitchen to switch to the default wooden flooring.
Fixed issue where riding a horse while travelling from one location to another diagonally would repeatedly warp back and forth between the two locations.
Fixed watered slime hutch troughs emptied when you load a save. (This mainly affects loading a mid-day save on mobile.)
Fixed the community center not properly loading the refurbished map variant on game load. This caused characters like Maru to path incorrectly in them if the player had not visited the Community Center during that playthrough.
Fixed the weekly friendship boost for giving an NPC two gifts not applied if you also gave them a third gift for their birthday.
Fixed overnight lightning not randomized correctly, so either every overnight lightning would strike or none of them would.
Fixed issue where stones, wood, and weeds could spawn on top of terrain features when a new year begins.
Further changes were later released without changing the version number:
21 December 2020 (appended to 1.5.1 post)
Fixed a crash when interacting with the Junimo notes in the Community center when playing in non-English.
22 December 2020 (appended to 1.5.1 post)
Fixed malformed item data causing the game to crash when playing in Turkish.
23 December 2020 (appended to 1.5.1 post)
Players can now choose another player's character in local multiplayer. This allows players continuing multiplayer farms in local multiplayer to resume their old farmers.
Fixed shared events in multiplayer potentially putting players out of bounds.
Fixed the am/pm display not displayed properly in non-English languages.
Various localization fixes and changes.
1.4.5
Stardew Valley 1.4.5 was released on 11 February 2020.

Bug fixes
Fixed an issue on Windows where the game would initialize incorrectly and start without audio.
Fixed an issue where passable objects, such as torches, could block you from attacking enemies that are standing nearby.
You can now reclaim the ancient seed crafting recipe from Gunther if you donated an Ancient Seed artifact and collected only the seed and not the recipe.
Fixed an issue that would allow animals to walk on certain water tiles alongside some bridges.
Wallpapers can no longer be used in place of items to be processed into artisan goods.
Fixed the Lewis statue letter not granting its reward in the Simplified Chinese localization.
1.4.4
Stardew Valley 1.4.4 was released on 31 January 2020.

Changes
Adjusted dropped item pickups so that they're more responsive for clients in multiplayer and will "rubber band back" to their previous locations less frequently.
Adjusted item collection code so that machines tucked in corners can be refilled without using cursor mode.
Fixed Elliott's 14-heart not properly working in non-English languages.
Fixed a data entry issue that caused some fish ponds to use incorrect data.
Fixed the Shrimp Enthusiast Shirt applying the wrong shirt artwork.
Fixed a soft-lock when watching the 2nd Fall movie in a non-English languages.
Fixed the cursor not appearing in the level up profession selector if the Controller Style Menus option is toggled off while using a controller.
Unsuccessfully crafting an unstackable item while already holding an item on your cursor no longer grants you credit for crafting it.
Fixed an issue where garden pots would consume seeds without planting them if they were planted from more than a tile away.
Fixed the color selector sliders on the farmhand creation screen having incorrect navigation on controller.
Fixed the logic for fruit tree obstruction checking the wrong tile.
Fixed the dagger swipe sound effect repeating an extra time in multiplayer if another player is in the same area.
Krobus will no longer get jealous if you gift characters you're dating after he moves in.
Penny now leaves garden pots alone in her 14 heart event.
Fixed an issue that could cause Sam's 6 heart event to soft-lock.
The game now re-issues the player the Qi's Challenge quest if they had previously opened the mail, but dismissed it without accepting the quest.
Items placed in an ex's room are now collected and placed in a chest after divorce.
You can no longer give away quest items or non-giftable items during the Feast of the Winter Star.
Adjusted some NPC gift reactions (Vincent and Jas now hate triple shot espresso, the Dwarf now loves lemon stone, and Sam now likes concession stand Joja Cola).
Adjusted Desert map so that crab pots placed in the water no longer render incorrectly, and objects can no longer be placed on top of the Desert Trader.
Removed catfish from Willy's fishing quests during Winter, as it's impossible to catch one without a rain totem.
Fixed a crash that could occur on the host when a client connects to a game that was set to Friends or Invite Only that is now being hosted on a platform that doesn't support those online modes.
Fixed incorrectly looping ambient noise in the Deep Woods at night.
Fixed an issue where the Japanese localization's dialogue for a spouse watering your crops would incorrectly show both gender variants of the text.
Fixed the Simplified Chinese localization incorrectly showing sunflower seeds as a Fall only crop.
Removed the ‘<‘ from the Simplified Chinese localization of the "Pet loves you" dialogue.
Fixed an issue where Junimos would show an empty text bubble when bringing a bundle to the Junimo hut after completing a bundle in Simplified Chinese or Korean.
Fixed an issue where viewing the Junimo note before learning to read it would cause certain text to permanently display much larger in the Simplified Chinese, Japanese, and Korean localizations.
Filled in some missing characters in the Korean fonts. This fixes some instances where an asterisk appears instead of a Korean character.
Fixed a minor typo in Grandpa's note in the Korean localization.
1.4.3
Stardew Valley 1.4.3 was released on 13 December 2019.

Bug fixes
Fixed an issue where you could collect multiples of a bundles reward in the Community Center if you closed the menu without collecting them.
Fixed an issue where naming your pet the name of an NPC could have your pet appear on the calendar on that NPC’s birthday.
Fixed an item duplication exploit when using the add to existing stacks button on an inventory with a full stack.
Made some fixes to the Turkish localization.
Fixed a bug in the crafting menu that could cause extra resources to be consumed in certain situations.
Adjusted the Four Corners farm map to fix layering issue with buildings.
Fixed a bug where you could enter the Wizard's Tower before unlocking the Community Center.
Taking a map screenshot while the option to show menu backgrounds is on will no longer render the menu in the screenshot.
Fixed an issue causing certain wallpapers to grant a Lost Book when selected in the catalogue.
Fixed an issue where you could get your grange score immediately after asking Lewis to judge your grange during the Stardew Valley Fair.
1.4.2
Stardew Valley 1.4.2 was released on 4 December 2019.

Changes
Reverted placement rules introduced in 1.4.1 which prevented players from placing flooring or torches on their spouse's porch tiles. Instead, spouses now ignore flooring and will "pop off" any torches that are placed on those tiles when they move there in the morning.
Bug fixes
Fixed the crane game crashing when it loads on Mac.
Fixed workbenches not pulling items from chests that are on rugs.
Fixed Robin staying in bed if she was upgrading certain buildings on game load.
Fixed a bug where buying a magic rock candy, exiting to title, and then reloading the game would cause the candy to not re-appear in the shop.
Fixed a crash when mashing the dialogue advance buttons while transitioning between maps during an event.
Fixed another way the club smash could cause the player to get "stuck" holding out a weapon.
Fixed some issues where non-user-initiated mouse movements could cause changes in mouse button states to not register.
Fixed a potential soft-lock if you passed out on another player's bed.
Fixed the screen being partially faded out when Demetrius comes to ask about the farm cave.
Fixed an issue where characters would greet you via speech bubble even if they weren't in the same location (e.g., Elliot welcoming you into his shack even though he's standing at the beach).
Fixed being able to perform certain actions (like using a return scepter) during overnight farm events.
Fixed farmers who are knocked out while holding an item not properly showing the knocked-out animation.
Fixed an issue where the tool being upgraded at Clint's could be set to an invalid value, causing Lewis to incorrectly send you a set of tools every night.
Clicking the emoji menu toggle button on gamepad no longer shows the onscreen keyboard.
Adjusted rumble on third-party controllers. This may not fully solve issues on certain third-party controllers, but will at least prevent states where the rumble is stuck on.
1.4.1
Stardew Valley 1.4.1 (previously known as 1.4.0.1, but renamed for compatibility with SMAPI) was released on 2 December 2019.

New features
Added Gamepad Mode to the options menu. This has three values: "auto" (default) switches between keyboard/mouse depending on the last input; "force on" forces the game to use gamepad logic, similar to earlier versions of Stardew Valley; and "force off" disables the gamepad and can be used if you only play the game using keyboard/mouse.
You can now buy the museum rarecrows from the Night Market after you've unlocked them.
Some non-spouse NPC's now have custom movie ticket acceptance dialogue (in English only).
Balance changes
Explosive ammo now costs 300g each in the Adventurer's Guild, won't appear until you've unlocked the crafting recipe, and now only explodes with a 2-tile radius instead of 3.
You can now only buy one piece of magic rock candy per Thursday at the Desert Trader.
Iridium ore abundance now increases much more slowly beyond level 100 of the Skull Cavern.
Weapon cooldowns now only happen if game time should pass.
Other changes
You can now buy recipes with a full inventory.
Penny's 14-heart event no longer removes placed dressers. Furniture that was supposed to be placed in an occupied tile is now added to the same chests Penny puts your objects in.
Vincent now loves snails.
Adjusted shorts easter egg to give precedence to any normal interactions with the NPCs it affects (gifting, completing a quest, etc).
Slightly optimized debris code.
Bug fixes
Fixed farmhands' separate wallets resetting to 500g if the host was playing on Linux or Mac.
Fixed the incorrect ordering of NPC gift tastes, so tastes should now match 1.3.
Fixed trash bear appearing on festival days (which could cause a potential crash).
Fixed an issue where reclaiming the insect head, Neptune's glaive, forest sword, or carving knife from Marlon would cause Clint to appear to be upgrading that weapon, losing any tool already being upgraded.
Fixed problem harvesting crops with the golden scythe.
Fixed being able to warp into the sewer on your horse, causing you to warp into the void.
Fixed an issue allowing torches and flooring to be placed on the spouses's porch position, so they couldn't come outside.
Fixed the golden scythe still appearing on the reaper after you've already received it.
Fixed a minor issue where players who have connected to a game and are creating a character while an achievement triggers would send a message saying "- has earned the '(Achievement Name)' achievement."
Fixed a hole in the refurbished saloon room, which let players walk out of the map boundaries.
Fixed an issue where a farmhand entering a freshly built cabin could cause the farmhand that owns it to spawn in the upper-left corner of the main farmer's farmhouse.
Fixed fish pond silhouettes being incorrect after clearing the pond in multiplayer.
Fixed a typo causing plant seeds being removed from the inventory when unsuccessfully attempting to plant them outside of the farm.
Fixed pre-1.4 untyped "Honey" items that were misnamed "Wild Honey"; they're now just converted to "Wild Honey" that stacks with other "Wild Honey" items.
Fixed a crash when tree fertilizer recipe is added to a save that already has it.
Fixed the dove subplot enemy leaving visual trails on the host's machine regardless of the location they were in.
Fixed non-synchronization of items recovered from Marlon at the Adventurer's Guild.
Fixed the display name of flounder in Russian being the same as halibut.
Fixed a botched after-movie dialogue from Evelyn.
Fixed the direction of the fold on the Gi clothing items.
Fixed tea saplings not being placeable on certain tiles on the farm.
Fixed a crash when checking the calendar while engaged to another farmer that is currently disconnected from the game.
Fixed problem where you could soft-lock a shop menu in an edge case scenario.
Controller fixes:
Fixed some inconsistencies with cursor placement when item stowing is on.
Fixed an issue where using the trigger buttons to swap pages in the Junimo Bundle menu while holding an item would cause it to be lost.
Fixed an issue in the quest log where if you moved the cursor right from the "back" button when viewing a quest description on the second or higher page of the quest log, the cursor would move to an invalid position.
Highlighting a dropdown menu option in the options screen on the controller now snaps to the drop down button, no longer obscuring the text.
When a dialogue question is asked, the first selectable option is now selected by default in controller mode, regardless of whether the controller-style menus option is enabled.
Corrected the fix for the Stardew Valley Fair festival's petting zoo area appearing incorrectly if certain post-game conditions had been unlocked.
Added a graceful fail state to the function that gets a wedding for the day in case there's a completely invalid farmer ID in the farmers list (potentially from a removed cabin).
Players that could have missed increases to their max health, crafting recipes due to skipping combat skill levels will now earn them on level load.
Pending level-ups are now removed from characters as they are applied, instead of all at once at the end of the night. That ensures that a character who gets disconnected/crashes during a level-up can now reapply their level-ups the next time they are connected.
Adjusted the requirements to be able to respec a skill at the Statue of Uncertainty to allow users who have "missed levels" to reclaim their missed perks levels using it.
Potential fix for switching over to the scythe after using the club slam repeat quirk causing the next used tool to soft-lock the player in place.
Fixed various typos.
Fixed crash if a location no longer exists in the game, for players with residual mod data in their save file.
Fixed the /friendAll debug command granting friendships to NPCs that aren't friendable, which could possibly cause issues on any game mechanics that randomly select a friend (e.g., daily quests).
1.4
Stardew Valley 1.4.0 was released on 26 November 2019.

New content and features
Added movie theater unlocked in late game, with related content and features.
Added 14-heart events for every spouse.
Added new events and dialogue (including a new heart event for Caroline).
Added clothing items equipped on the player (replaces former clothing appearance options).
Added clothes tailoring and dyeing.
Added 24 new hair styles, including bald heads.
Added Four Corners farm map (meant for co-op, divides the land into four areas with their own perks).
Added fish ponds to breed fish and produce items.
Added new items:
181 shirts;
35 hats;
14 pants (including dresses, skirts, and shorts);
2 boots;
38 decorative items obtained in various ways (e.g., new events);
17 new flooring options;
2 new secret notes;
two fish: flounder and midnight carp;
two rings: crabshell ring and napalm ring;
artifact troves (can be broken open by Clint to yield artifacts);
caviar, roe, and aged roe;
dark sword;
deluxe scarecrow (recipe given when you collect all rarecrows, has double the radius);
dinosaur mayonnaise (processed from dinosaur eggs);
golden scythe;
grass starter recipe (purchased from Pierre);
magic rock candy;
mini-jukebox (place anywhere on the farm or in farm buildings to play previously-heard music);
mini-fridges (place inside to extend your fridge capacity);
rice crop;
seafoam pudding (fishing level 9 cooking recipe);
shrimp cocktail (recipe learned from the Queen of Sauce episode on Winter 28 Y2);
squid ink;
sunflower honey (produced by beehouses);
tea bushes, tea leaves and green tea;
training rod (easier fishing but only catches common fish);
tree fertilizer (non-fruit trees grow more quickly);
triple shot espresso;
void ghost pendant;
warp totem: desert;
wilted bouquet (crafted from a bouquet), which lets you break up with NPCs you're dating;
workbench (lets you craft with ingredients in adjacent chests);
wood chipper (breaks hardwood and driftwood into wood).
Added new mine content:
a quarry mineshaft dungeon with new haunted skull and sludge monsters, and a Golden Scythe;
prehistoric floors in the Skull Cavern with a new pepper rex monster;
rare alternative floors in the 1-120 mines after unlocking the quarry similar to the quarry mineshaft dungeon.
Added shed upgrade (doubles the interior size).
Added cat/dog breeds selectable from the new-character customisation menu or the Shrine of Illusions.
Added Krobus as a potential roommate if you're unmarried.
Added a desert trader that sells new items.
Added Trash Bear to clean up trash around town in year 3+.
Added 4 new monster eradication goals & prizes.
Added 4 new museum reward levels (for donating 35, 70, 80, and 90 items).
Added trash can upgrades purchasable from Clint (gives 15-60% of trashed items' value as money).
Added a new sunroom in Pierre and Caroline's house.
Added the ability to perform various emotes through a new menu (default key is Y).
Added a new farm building: desert obelisk.
Added winter flooring sprites.
Added hidden subplot if you've turned children into doves. (Spoilers: check the television on Fall 26, then visit the Witch's Hut for a recurring effect and fish on the Four Corners farm for a one-time effect.)
Added experimental support for letting farmhands move buildings. Use the /movebuildingpermission command to toggle between on (farmhands can move any building), owned (they can move their own cabins or buildings they've built themselves), or off (default).
Added a new trash bin in front of JojaMart.
Added map export feature (except on 32-bit Linux), accessed via a button in the options menu or the /mapscreenshot chat command. Screenshots are saved in the appdata folder on Windows, and ~/.local/share/StardewValley/Screenshots/ on Linux; click a button in the options screen to open it. When using the command, you can optionally specify a filename and percentage size like /mapscreenshot test 25.
Added VSync option. Disabling VSync may improve overall framerate at the expense of frame rate stability.
Added an NPC gift log accessed through the social tab (tracks birthdays, their liked/disliked gifts as you discover them in-game, etc).
Added 'advanced crafting info' option which shows more info on the crafting menu (including number of times crafted and the number of each ingredient available).
Added OST files for new music tracks.
Added new easter egg on the title screen.
Junimo Kart has been completely redone and is now actually fun.
Dressers can now be used to store clothing, hats, shoes, and rings.
When you catch a silver or gold-quality fish, a 'perfect' catch now increases the quality by one. (This is the only way to get iridium-quality fish.)
You can now put hats on your children (once they can walk).
You can now play Elliott's piano.
You can now put gemstones in Junimo huts to affect the color of new Junimos.
Divorced spouses no longer attend your wedding.
Divorced spouses no longer treat their exes normally during Festivals.
Auto-Grabbers now work in the coop too.
Successfully parrying a slime attack now prevents the slimed debuff.
Seaweed can now be foraged along the bottom shore of the tidal pool beach.
The adventurer's guild now sells any boots you already found in mine chests.
You can no longer load saves created in a newer version of the game than you have. (This will only affect future versions of the game.)
Multiplayer changes
Added optional separate money in multiplayer.
Added support for private chat messages.
Added more multiplayer "server messages".
Added a /ping chat command which prints the current ping to the host (for farmhands) or to each farmhand (for the host).
Added a /kick <farmer name> chat command.
Added /ban and /unban chat commands. Bans are per-farm, and the command can be called with a farmer name, user ID, or IP address. in all cases it will ban the user, not the farmhand character.
Added multiplayer synchronization for…
daily luck;
bulletin board quests (in most cases);
trains;
lightning bolts;
mine fog events;
lost book collection;
merchants' limited stock;
drum/flute blocks;
adjustments to the fishing bobber's position while it's midair;
the animation when a player has a fish on the line.
When creating a new multiplayer form, the Starting Cabins option now defaults to 1 instead of None.
Each player now has a separate mailbox and spouse porch area.
Each player can now build a separate cellar.
When a player drops an item in multiplayer, other nearby players now have priority for picking it up.
You can now see other players' scores during certain festivals in Multiplayer.
Quests in multiplayer now set difficulty based on the highest-level player.
In the Skull Cavern, mine shafts now drop players to the same level in multiplayer.
In multiplayer, many random checks now use the team's average luck instead of only the host's luck.
If connecting to a multiplayer server fails, the game will now retry internally before giving up.
The reward for completing the Bulletin Board bundle is now applied to all players in multiplayer.
Moving a Shipping Bin no longer leaves behind its lid for other players on a multiplayer farm.
Quality of life changes
Added ability to rearrange the museum artifacts (without donating a new one).
Added ability to reread received letters anytime via the collections tab.
Added ability to rotate the toolbar (using Tab and Ctrl+Tab by default).
Added ability to fill existing stacks in a chest from your inventory.
Added notification when a tool being upgraded is ready.
Added tabs to the Catalogue and Furniture Catalogue.
Added current Qi coin balance to Calico Jack minigame UI.
Added support on Linux for pasting invite codes via an onscreen button (requires xclip).
Added upcoming weddings to in-game calendar.
All events should now be skippable.
Gates can now be attached to one piece of fencing (instead of needing fences on both sides), which allows for double-width gates.
The hallway to the spouse's room in a two-story farmhouse now matches the bedroom flooring.
Changed interaction cursor when pointing at farm animals you haven't pet today.
Giving datable NPCs a gift no longer makes your spouse jealous unless you're currently dating them.
You can now construct/move farm buildings onto tilled dirt and tree seeds.
Trying to construct/move farm buildings onto an animal now poke them out of the way.
Collapsing in the mines no longer makes you forget levels.
After collapsing in the mines and losing items, a list of lost items is now shown and you can pay Marlon to recover one of them.
You can now remove horse hats (by interacting with the horse while holding another hat).
You can now trash copper pans and slingshots.
You can now buy copper pans from Willy's shop after receiving the first one.
You can now stack craftable items in inventories (like kegs or furnaces).
You can now attach baits, tackles, etc. to your fishing rods directly from a treasure chest.
You can now shift-click items to move them out of the toolbar.
You can now hold down the interact button without retriggering the eat item prompt. That lets players quickly refill rows of kegs/preserves jars without being interrupted by the prompt.
You can now go to sleep while holding an item.
You can now pause Junimo Kart by pressing Enter or P.
You can now play Junimo Kart entirely with the keyboard.
You can no longer place iridium-quality items in casks.
Made it easier to collect milk/wool from farm animals. Animals now have a larger hitbox, and using shears/pail while facing multiple animals now finds the best match instead of the first one.
Interacting with a Mill that only has one type of item in it now automatically collects the item instead of opening a chest menu.
Pointing at an inventory item needed for a bundle now makes the Junimo bundle button pulsate.
Pointing at an item to sell in the shop menus now shows the "Gunther can tell you more" text if the item hasn't been donated yet.
Mushroom tree sprouts are now distinguishable from other trees.
Wild Bait now provides a chance to catch two fish at once.
Pets no longer spawn in positions that block the farmhouse door or corridors.
When exiting a Junimo bundle menu, the cursor highlights the bundle that was exited.
Farm animals standing on crops no longer prevent the crop from being harvested.
A message now appears when fruit tree growth is prevented by a surrounding obstruction.
When an NPC walks over a chest, it will now dump its contents out instead of destroying them.
When viewing a bundle, inventory items for completed slots are now grayed out.
Jumping down a mineshaft just above level 100 will no longer drop you below level 100 in the Skull Cavern.
Players can now "push" through NPCs at festivals, to avoid getting trapped in some cases.
Queen of Sauce reruns will now choose an already-aired recipe that a player doesn't know.
The animation played when finding a new lost book is now only played once per player.
Unclaimed bundle rewards can now be picked up from a Junimo bag in the Community Center.
Wild tree seeds can now be placed in any diggable tile outside of the farm without needing to hoe it first.
When you dismiss the map by clicking on it, you're now returned to the previous menu tab (if any).
Wilted trellis crops no longer block movement.
The Hat Mouse now sells hats you've won in festival competitions.
Moving the cursor over a crab pot while holding the action button no longer picks it up.
Moving the cursor over a farm animal while holding the action button no longer opens the inspection menu (so it's easier to pet animals).
Moving the cursor over a scarecrow while holding the action button no longer checks it (so it's easier to harvest large fields).
Improved the 'Organize Inventory' logic. Now properly handles empty spaces on Linux, and sorts stacks from highest to lowest quantity.
Changed processing time of tapped mushroom trees so that they're harvestable in the morning (instead of midway through the day).
Obelisks now have a 3x2 footprint instead of 3x3. (Their sprites are unaffected.)
Dropping an item when collecting rewards from Gunther now throws the item downwards instead of upwards, to prevent players without magnet rings from dropping items into out-of-reach positions.
Balance changes
Fruit trees no longer need the surrounding tiles to be empty to increase in quality once fully grown.
Fruit trees are no longer blocked from growing by non-colliding objects (notably artifact spots).
Mushroom trees no longer drop wood (and debris chunks are now white instead of brown).
You can now increase friendship by talking with NPCs at festivals.
Trains now drop more items.
Some items no longer appear in random shop stocks: void eggs, void mayonnaise, and sweet gem berries.
The quarry now spawns oak & maple trees.
Charcoal kilns now require 2 copper bars (instead of a gold bar).
Cheese now sells for more.
Cloth now drops more often from mummies.
Dressers now cost more.
Looms can now produce multiple cloths when higher-quality items are input.
Pancakes can no longer be bought from Krobus before winter Y1.
Sturdy ring is now easier to craft.
Journey of the Prairie King has been rebalanced.
Calico Jack and slot machines in the casino now statistically favor the player. (Previously the player was more likely to lose.)
The Forester profession now causes 25% more wood to drop from trees/stumps/logs, instead of raising the value of wood by 50%.
Speed-gro and retaining soil can now be applied to crops anytime.
Basic and quality fertilizers can be applied to seeds (but can't be applied once a seed has sprouted).
Rebalanced the frequency that secret notes are dropped.
Fishing tackle now sells for less once damaged, depending on its remaining durability.
Sweet gem berry can no longer be bought from the traveling cart (you can only buy the seeds).
Bean hotpot now grants max energy +30 and magnetism +32, instead of showing "max energy +2" but granting nothing.
Spring onions quality is now determined at the start of the day.
The Legend can now only be caught once.
Made bottom edge of fishing bobber bar slightly more generous.
The effect of fishing level on fish size no longer caps at 10.
Debris now respawns at the start of spring in Cindersap Forest, Town, and the Railroad.
Reduced cases of items splashing into water when they're visually on dry land.
Lightning rods are now always harvestable immediately the day after being struck.
Wheat now has a 40% chance to also drop hay on harvest.
Wild bait can now be obtained from fishing treasure chests if you know the crafting recipe.
Fixed the burglar's ring not affecting some monster loot items (those added programmatically).
Reduced recipe prices in the Stardrop Saloon.
Improved controller support
Added an on-screen keyboard to type into chat or text fields using the controller.
Added ability to stow an item when playing with the controller, freeing up your hands to interact with NPCs without accidentally gifting them items.
Added a left/right bumper hotkey in inventory menus. when the new 'add to existing stacks' button is available, pressing the hotkey will automatically snap to that button for easier inventory consolidation.
You can now highlight the list of required items in the Junimo bundle screen while using a controller, so you can see a tooltip with the item's description.
Improved controller navigation/use in…
the museum donation screen;
the Load Game and Join/Host Coop Game menus;
the bundle screen (no longer need to scroll all the way to the right to access the second row);
chest and item grab screens;
crafting menu.
Improved switching between keyboard/mouse and controller mode. For example, having a controller plugged in no longer snaps mouse input to buttons.
Improved placement logic with a controller (planting seeds, placing furniture, etc).
You can now direct your fishing casts with a controller.
The buffs display tooltip is now hidden if the mouse cursor isn't visible.
Fixed cursor snapping to upper-left item when clicking the organize items buttons on the controller.
Fixed D-Pad not correctly selecting dialogue options.
Fixed an issue making the animal pregnancy disable option unselectable with a controller.
Fixed navigation of the languages menu using a controller.
Fixed an issue where rearranging artifacts in the museum didn't work with controller-style menus.
Fixed various issues related to selecting dialogue choices with a controller.
Fixed being able to move the cursor on the shipment screen after the screen is dismissed with the OK button on a controller.
Fixed cursor slightly misaligned on the skills screen when you first enter it using a controller.
Fixed various issues related to the display of the cursor in the level up screens with a controller.
Fixed some issues with controller navigation of the items in the wallet section of the skills tab.
Fixed controller navigation of dropdown lists in the options screen.
Fixed an issue where the controller's left thumbstick was moving the mouse cursor around while playing minigames.
Fixed an issue where using the face buttons to aim shots in Journey of the Prairie King on the controller would sometimes cause the shots to go in the wrong direction and cause the player to get stuck shooting.
Fixed chest color picker buttons being selectable if the color picker isn't shown.
Other changes
Various copyediting, improved text, tweaked sprites, and tweaked map tiles.
Made some optimizations that may improve performance on some machines/platforms or in some cases.
Improved many translations and fixed missing font characters in Korean.
Changed midnight from 12:00 to 0:00 in Japanese.
Added an open sprite to the fridge.
Adjusted the mail received after collapsing to more accurately reflect timeline changes in the game.
Adjusted a dialogue option in Penny's 2-heart event to be more considerate of George's perspective.
Removed the Junimo Note/Community Center Button from non-inventory screens.
Improved Elliott's cabin interior design a bit.
Items found in the trash now pop out of the trash instead of going directly into your inventory.
Updated credits.
In single-player, the mines now reset as soon as you leave instead of waiting for the next 10-minute update.
NPCs now destroy trees in their path (and will trample wild tree seeds underfoot).
NPCs now close their eyes and do a sleep pose when they go to bed.
Players now close their eyes when they go to bed.
Penny no longer randomly reveals Pam's taste for alcoholic items.
Fish sold to Willy are now resold in his own shop (fish are no longer sold at Pierre's).
Tweaked hoed dirt color on the beach in fall.
Made David's cage look more appropriate for guinea pigs.
Reduced splash effect of small cosmetic debris to make it easier to distinguish splash of actual items.
Added animation when digging through trash.
Adjusted sound made when picking up forageables, eggs, etc.
Added changes for modders.
Added log for unexpected network disconnects (in a separate DisconnectLogs folder).
The ordering of the items on the collections page is now consistent between languages.
Fixes for gameplay
Dismissing a letter with unclaimed items now automatically picks up the items.
You can no longer activate the Statue of Uncertainty if you haven't met the level requirements.
You no longer take damage from monsters while passing out at 2am.
Fixed various exploits, including…
opening the journal while fishing paused time but still caught fish;
opening the journal while dying skipped the death event and prevented losing items;
you could use an incorrect item in some cases (like using a wallpaper to obtain the galaxy sword, incubate a dinosaur egg, or when crafting);
you could predict the mushroom level pattern in the mines;
you couldn't be damaged while the eat confirmation prompt was up in multiplayer;
the invincibility timer after taking damage didn't decrease in multiplayer if a menu was open;
right-clicking a fishing rod attachment in the inventory reset its durability;
using glitches to leave the spa while in swimming mode would result in infinite energy/health regen;
you could obtain up to 109 statues of perfection by storing each one in a cabin's inventory chest;
items of different qualities could be combined into one stack when buying from Pierre;
you could sell items to Pierre's at an upgraded price (e.g., salmonberries with the Bear's Knowledge perk) and buy them back at their normal price. He now resells them at the same price he paid.
Fixed players getting stuck…
if you cast a fishing rod just after opening a treasure chest in the mines;
in the blocking pose when you use a sword's special ability in rare cases;
on top of a mine ladder if multiple ladders were spawned;
in the traveling merchant's cart when dismounting from a horse in some cases (or getting your horse stuck that way);
on top of Abigail when playing the minigame in her two-heart event.
Fixed rare issue where no ladder would spawn on a mine floor.
Fixed monsters spawning too close to the start of a floor in the mines.
Fixed mummies dealing damage while downed.
Fixed invisible, interactable elevators on treasure floors of the Skull Cavern.
Fixed various issues where using bombs could cause items to spawn at the main player's current location instead of the location where the bomb was placed (e.g., artifacts found via secret notes, fruit tree items, giant crops, mystic rocks, hardwood, crystals, and cave grass).
Fixed issue where weeds could be spawned on the tile directly beneath the elevator in the mines.
Fixed objects on the farm sometimes skipping their daily updates, which could cause issues like crops surviving a day into Winter or batches of crops not maturing at the same rate.
Fixed various cases where an entire stack of held items was incorrectly consumed.
Fixed certain artifacts not spawning as intended.
Fixed cooking ingredients spread between your inventory and fridge not correctly counted together.
Fixed issue where leveling up would incorrectly affect the related skill for the rest of the day (i.e., common trees wouldn't drop seeds after leveling up foraging).
Fixed artifacts appearing on grass after winter turns to spring.
Fixed bug when getting a JojaMart membership shortly after completing the Community Center.
Fixed weed item obtained from breaking a mushroom seed or shaking a mushroom tree.
Fixed Livin' Off the Land announcing the start of blackberry season on the wrong date.
Fixed certain placeable items being placeable on tiles occupied by other furniture.
Fixed a few missing boundary tiles in certain areas, including in the Stardew Valley Fair.
Fixed player's fishing level and bait not taken into account for the wait time if the first nibble was missed.
Fixed Tiller profession bonus sometimes not applied to combined foraged and grown grape stacks.
Fixed Prospector profession not applied to rocks destroyed in the mines.
Fixed forage sometimes spawning out of bounds.
Fixed removing tappers from trees in certain ways making them become un-choppable.
Fixed fishing cast distance not determined when the bobber hits the water (previously set at the end of the cast).
Fixed TV weather forecast not always matching actual weather.
Fixed Queen of Sauce sometimes airing a new recipe on the Wednesday before it's scheduled on the following Sunday.
Fixed Queen of Sauce repeatedly airing the Stir Fry episode at the end of year 2 and the beginning of year 3.
Fixed players playing a minigame at 2am not properly quitting the minigame and passing out.
Fixed players able to continue fishing or charging tools past 2am.
Fixed giant crops growing in a noticeable pattern.
Fixed discrepancy between an item's shown health recovery and the actual recovery when consumed.
Fixed the chicken statue furniture being stackable with the chicken statue artifact.
Fixed issue where players could still take damage and die while warping with an obelisk or return scepter.
Fixed issue where ore/mineral veins destroyed with a bomb outside of the mine would only drop stone.
Fixed issue where going to bed early caused machines to process more quickly overnight. (Machines previously processed 100 minutes per hour slept; they now only do so between 2am and 6am, and the remaining time slept will be processed at the normal daytime rate of 60 mins/hour.)
Fixed issue where harvesting a tapped mushroom tree in winter would cause it to not produce again until mid-Spring, rather than Spring 1.
Fixed issue where snow yams and winter root could be dug up in the desert in winter.
Fixed lopsided bee house flower range.
Fixed some Witch Swamp and Mutant Bug Lair water tiles not correctly marked as water, causing inconsistent fish quality in those areas.
Fixed issue where entering a house the moment an NPC passes through a door would close the door on top of the NPC, causing them to get stuck.
Fixed issue where fruit trees wouldn't grow if there was a monster or other NPC near them overnight.
Fixed issue where closing a mine chest with the OK button while your inventory was full destroyed the item; instead the item is now dropped.
Fixed issue where a player at the Stardew Valley Fair would get their score calculated based on the contents of the Grange upon closing the minigame (instead of when Lewis had actually finished his judging), letting that player have a different score than intended.
Fixed minor issue where zero shots fired at the Stardew Valley Fair slingshot shooting gallery would give a large negative calculated accuracy.
The Cookie recipe will be sold at the Saloon if Evelyn's 4-heart event has been seen but the recipe wasn't obtained.
Fixes for player interaction
You can now collect lost books even if your inventory is full.
Fixed horses being unmountable if they're very close to a pet.
Fixed being able to trash items from the crafting menu even though the trash can is invisible.
Fixed answering dialogues on a small screen causing the cursor to interact with the toolbar.
Fixed interacting with objects in the world while holding an item sometimes causing both the interaction and object to be used at the same time.
Fixed interacting with a fireplace sometimes not toggling it.
Fixed interacting with objects so that objects behind the character are longer interacted when the character is facing upwards.
Fixed interacting with a trash can on horseback simultaneously dismounting the horse and searching the trash (now just dismounts).
Fixed issue where players couldn't harvest or pick up items by clicking and holding the tool button with a melee weapon or scythe in hand.
Fixed issue where attempting to charge an upgraded watering can to the left of a body of water on the farm would prevent the farmer from charging it.
Fixed unable to fill water can from the left side of the water trough in the greenhouse.
Fixed issue where depositing ore into two nearby furnaces could activate both of them.
Fixed large rotated furniture being placeable on top of tables, causing them to disappear.
Fixed issue where players could move while warping out of the Witch's Swamp.
Fixed issue where players couldn't push through farm animals in some cases if they were offset by half a tile.
Fixed issue where interactable furniture like fireplaces couldn't be picked up with left-click when standing close to them and holding a non-tool item.
Fixed issue where it was hard to click on NPCs if you went into a festival while holding a placeable item.
Fixed crawling-stage babies in the crib not being interactable.
Fixed minor issue where you could cause the farmer to stop shaking during a tool charge by pressing a movement key.
Fixed being able to interact with NPCs when your farmer is set to be immobile. (For example, this prevents you from trying to gift your spouse a second gift immediately after kissing them and getting stuck in an erroneous animation frame.)
Fixed opened gates orphaned by destroying the fence post they're attached to not blocking movement.
Fixed wild tree seed placement cursor not accounting for seed-placeable rules.
Fixed crab pot placement cursor always green, even if an invalid placement tile is selected.
Fixed palm trees not shaking and dropping leaf debris when interacted in winter.
Fixed the "Warrior" option not being selectable during Sebastian's 6-heart event in Korean.
Fixed being able to use the dagger while bathing.
Fixed museum reward collection menu not dismissible using the exit hotkey.
Fixed museum donation screen issue where panning the camera would cause the cursor to scroll off of UI elements.
Fixed issue where watering a small tree sapling played a scythe sound.
Fixed issue where hitting a fence that has a torch on it would destroy the torch instead of dropping it.
Fixed invisible blocking tile front of Lewis's house during the Stardew Valley Fair.
Fixed blank or whitespace-only chat messages being sendable.
Fixes for festivals, events, and quests
Dismissing a quest letter no longer discards the quest. (It's now added to your quest log to avoid permanently missing out on quests.)
You can no longer place objects at the beach while the Night Market is occurring.
Removed invisible trees from festivals.
Fixed exploit where you could pause time when the Night Market submarine was ascending/descending to skip the wait time.
Fixed exploit where you could watch the Night Market Mermaid Show while time was paused (the show now pauses too).
Fixed exploit where you could fulfill the requirements for a gathering quest by taking items out of a chest one-by-one.
Fixed players getting stuck on doors or placed objects during cutscenes in some cases.
Fixed players getting stuck in Harvey's 8-heart event if it was triggered when leaving his bedroom.
Fixed players getting stuck in Harvey's 10-heart event if a train came by.
Fixed introductions quest not considering Willy done after you meet him to receive the fishing rod.
Fixed Mr. Qi's Challenge not considered complete if you fulfilled the conditions before getting his letter.
Fixed the egg in Lewis' truck not being accessible during the egg hunt.
Fixed time not passing for machines inside of farm buildings during festivals.
Fixed players getting trapped in the hospital until the festival starts if they were knocked out for the first time on a festival day.
Fixed time passing during festivals not reflecting when the player(s) started the festivals.
Fixed some out-of-season items appearing as targets for "Help Wanted" quests.
Removed strawberry from Summer quests, catfish from Winter quests, and sardine from Summer quests.
Fixed bug limiting which NPC would request gathering, slay monsters, or fishing quests.
Fixed Help Wanted quests not reflecting that they pay 3x the market value, instead of 2x.
Fixed occasional spacing issues with the messages on the daily quest board.
Fixed Robin sometimes thanking you for the wrong item when completing a billboard quest.
Fixed winning festival events not counting towards farm's total earnings.
Fixed Penny's 6-heart event not triggering after purchasing the Community Upgrade.
Fixed Sam's 8-heart event being silent if you skipped his 2-heart event.
Fixed "A Winter Mystery" quest not triggering if exiting the farm from the bottom tile of the exit to the bus stop.
Fixes for shops and shipping
Fixed merchants refilling limited-stock items when you reopen their shops.
Fixed traveling merchant sometimes having the same item for sale for two different prices.
Fixed items bought from shops being sellable at a different price than produced/grown versions.
Fixed issue where honey would sometimes sell for more than expected.
Fixed pressing Alt + Enter while buying from Pierre destroying the held item.
Fixed selling animals not counting towards farm's total earnings.
Fixed issue where you couldn't buy animals while Robin was upgrading the pertinent building.
Fixes for NPCs
Fixed several cases where NPC dialogues were out of sync with the actual state of the game world (e.g., saying the wrong dialogue in bed).
Fixed issue where villagers could get stuck doing their daily schedules late into the night after a festival.
Fixed issue where Vincent could get stuck on a flower barrel during the flower dance.
Fixed issue that prevented some villagers from hanging out with one another in town on certain days.
Fixed various issues related to naming horses.
Fixed various bugs caused by giving a villager's name to a horse, pet, or child.
Fixed friendship-related achievements not properly triggering as soon as the conditions are met.
Fixed various friendship-related bugs and inconsistencies, including 10-heart events being unlockable without a bouquet.
Fixed NPCs reacting incorrectly to certain gifted items.
Fixed issue where gifts couldn't be given to the dwarf if their dialogue was exhausted for the day.
Fixed Abigail visiting the farmer on the same day as her 8-heart event.
Fixed Bouncer just saying "Hi." instead of his unique line.
Fixed Bouncer not accepting the club card if you've already exhausted his dialogue for the day.
Fixed Demetrius plowing through bushes by the fountain in summer.
Fixed Dwarf always responding negatively to items it feels neutral about.
Fixed Dwarf not liking cave carrots, despite having dialogue which suggests otherwise.
Fixed Emily's four-heart event unlockable at night.
Fixed Gus offering Bread, Pizza, Salad, and Spaghetti as dish of the day (he already sells them as part of his normal shop stock).
Fixed Henchman dialogue box showing a friendship jewel.
Fixed Krobus secret note event not triggered if riding a horse.
Fixed Krobus not keeping silent on Fridays when accepting gifts.
Fixed Leah's summer schedule causing her to walk into the water and get stuck there for the rest of the day.
Fixed Penny not having her own introductory line.
Fixed Penny talking about the sound of rain on the roof of her trailer after the community upgrade is built.
Fixed Penny talking about living in a trailer after the community upgrade is built.
Fixed Pierre talking about time off after the Community Center has been restored.
Fixed Shane sending two recipes at 3 hearts. (The second is now sent at 7 hearts as intended.)
Fixed Welwick saying two different things on the same day.
Fixed free gift at the Night Market being available every ten minutes instead of once a day.
Fixed buggy interaction with Mayor Lewis when getting a Joja membership before starting the Community Center.
Fixed townsfolk sending players the wrong cooking recipes for their current friendship level.
Fixed villagers you're already dating still accepting bouquets from you.
Fixed a rare crash when attacking "slimes in love".
Fixed attacking a rock crab with a pickaxe not dealing damage after its shell is broken.
Fixed issue where villagers that respond differently depending on their current location will no longer say those location specific lines when talked to again later.
Fixed spouse continuing their ongoing dialogue after being interrupted with giving you a Stardrop.
Fixed most cases of crawling-stage babies waking up in the crib at the start of the day. (They'll now spend longer trying to find a non-crib position before giving up.)
Fixed NPCs sometimes detecting players rummaging through their trash or private possessions from a different location.
Fixed NPCs saying something upon entering an area (e.g., Pam entering the Saloon) doing so if you're watching an event.
Fixes for multiplayer
Farmhands' spouses now move around, run their daily schedules, and react to their spouses like they should.
Farmhands now return to their own porches after a festival, instead of the main farmer's porch.
Players can no longer give quest items as gifts to other players.
You can now connect to the host via IP while they're in the process of loading the game.
Fixed an issue where if a server was shut down on the same day a remote player had leveled up overnight, the level up would not be applied until the following night upon save load.
Fixed rearranging the museum in multiplayer showing a message that the player donated a new item.
Fixed farmhands not seeing the notification that a train is approaching.
Fixed players stuck if a bundle is completed while they're on a tile that becomes unwalkable after the room gets renovated.
Fixed issue where a spouse could get stuck in a farmhand's cabin after divorce. Save files that already have this issue will be fixed after the first night.
Fixed bundles button visible on the inventory screen for farmhands that had missed a bundle completion cutscene.
Fixed issue where you couldn't interact with something behind another player (e.g., to talk to an NPC).
Fixed farmhands seeing bundles for completed areas when looking at the bundles menu.
Fixed farmhands unable to pick up lost books if the host has a menu open.
Fixed married NPCs saying marriage-specific lines to players who aren't their spouse while they're on their married schedules.
Fixed the door frame from Robin's construction animation not properly removed for remote clients after construction is done.
Fixed messages like the one about spreading weeds only shown for the host player.
Fixed Kent sometimes missing from clients' festivals.
Fixed players that collapse in multiplayer seeing the screen briefly flash, showing them in bed.
Fixed fishing rod cast sound affected by other players' casts.
Fixed fishing rod animation not properly synchronized when clicking and holding to recast.
Fixed issue where Lupini would only stop selling a painting if the host player was the one to buy it.
Fixed issue where horses could lose their hats in multiplayer.
Fixed issue where farmhands couldn't activate the Dark Shrine of Night Terrors.
Fixed issue where monsters wouldn't move while host was watching an event or getting knocked out.
Fixed various issues related to child placement and multiplayer synchronization.
Fixed issue where light sources from disconnected farmhands wouldn't get cleaned up.
Fixed issue where animals in barns built by farmhands in multiplayer were unable to breed.
Fixed issue where completing a Vault bundle wouldn't send a global chat message in multiplayer.
Fixed issue where the Witch event would create a void egg for each logged-in player.
Fixed issue where items shipped, minerals found, recipes cooked, fish caught, and artifacts found during a multiplayer session could be forgotten if a client disconnected before the end of the day.
Fixed several bugs relating to Mummy behavior and multiplayer sync.
Fixed sleep stamina recovery being based on the last player who went to bed (now tracked separately for each player).
Fixed baby slimes in the mines destroying rocks on contact if a non-host player killed the big slime.
Fixed various multiplayer data sync issues.
Fixed time slowing for all players when the host is in the mine (no longer slows at all in multiplayer).
Fixed missing tools in multiplayer not always being recovered.
Fixed various issues related to pets in multiplayer.
Fixed remote players not properly showing jump/jitter animations during emotes or horse mounting/dismounting.
Fixed the host player seeing flashes or feeling controller rumbles from bombs in other locations.
Fixed explosion flashes not showing up on farmhand machines.
Fixed player getting stuck on the "Waiting for players" check after a festival if another player joined at the same time.
Fixed Joja purchase form not reflecting upgrades bought by other players.
Fixed issue where getting killed while paused in multiplayer could leave you in a perpetual getting-knocked-unconscious state; this now unpauses instead.
Fixes for visual or cosmetic issues
Items that come in various colors (like tulips) now show their proper color in the item received pop-up.
The mouse cursor is now hidden in scenes that lock user input.
The lighting in the Secret Woods now changes more consistently with the rest of the world as time passes through the day.
Lit furniture placed on top of tables will now properly light upon nightfall.
Fixed various visual map issues, including…
various tile issues in the Mines and Skull Cavern;
glow from certain lamps in the town interiors tilemap bleeding into adjacent tiles in the tilesheet;
incorrect corner edge tile used inside the walls in mine level 6;
incorrect grass tiling under the fence on the bottom of the mountain path to town, and missing tile on the tree near that location;
incorrect tiles in the Flower Festival;
a missing stone tile under the JojaMart sign in town;
visual issue with the kitchen floor tile;
visual bugs with the eyes of the statue in the secret woods;
visual issues with hat mouse's house;
artwork of the Bulletin Board in the Community Center not lining up with the walls around it;
mismatched walls behind the plant and picture frame in the hallway between Alex and George and Evelyn's rooms;
mismatched wall with the power outlet for George's TV;
look of the carpet under Sam's bed;
incorrect shadowing on some tiles in the mines on floor 7 and 14;
Secret Woods statue eyes staying red after activation until the season changes or you reload the save.
Fixed various text display issues, including…
various typos;
various line wrapping issues in dialogue boxes;
line wrapping issue when leaving the feast of the winter star;
line wrapping issue in tooltips for boots, rings, and melee weapons with long names;
extra space at the bottom of tooltips for edible items that don't grant any health;
sizing issues in carpenter menu for non-English languages;
spacing issues in bulletin board request text;
one of Haley's lines having a blank dialogue page;
certain items with long names causing tooltips to word wrap incorrectly;
stardrop message easter eggs incorrectly appending the favorite thing after the special text.
Fixed various sprite issues, including…
layering issues (e.g., when the farmer is facing upwards while using some tools, or bushes drawn over chests);
character sprite coloration issues;
some monsters having two shadows (affected Ghosts, Dust Sprites, and Bugs);
Bouncer trying to face the player in some cases, resulting in an invalid sprite;
Linus starting some days slightly clipped into a wall;
Maru reverting to her plain clothes after her event in the clinic;
Penny's hair missing some pixels when she's sitting on the bench in town;
player hat rendered incorrectly in the inventory at night time;
player with an item raised above their head rendering with hands lowered in some specific cases;
player sprite rendered incorrectly after collapsing while in a bathing suit;
player sprite facing upwards after interacting with a child or festival NPC from above;
player 'wiggling nose' animation issue when casting or reeling in a fish;
player eye color drawn incorrectly when reeling in a fish;
player sprite flickering to invalid animation frame when tapping a movement key while aiming the fishing rod;
kissing your spouse in multiplayer sometimes showing an incorrect idle frame (sometimes facing the wrong direction);
various issues related to animations played as part of an NPC's daily schedule;
the light halo overlay on outdoor lamps sorting incorrectly at some positions;
health bar not fully consistent with stamina bar.
Fixed Penny washing dishes too far from the sink.
Fixed issue where rebinding keys would cause the game to display a blank options screen instead of properly prompting the player to press a key.
Fixed switching toolbars causing incorrect animations to play in multiplayer.
Fixed various issues related to the frogs that sometimes spawn on rainy days.
Fixed ancient seed not visible in inventory.
Fixed edible items that don't grant energy displaying the poisonous icon in tooltip.
Fixed being able to click title menu buttons before they're visible.
Fixed visual issues when swapping toolbars away or onto light sources.
Fixed some dialogue boxes being positioned incorrectly.
Fixed issue where hovering over the dialogue friendship jewel would show a friendship level tooltip, even if the jewel wasn't currently visible (e.g., when answering a question).
Fixed visual seams appearing in Junimo Kart.
Fixed visual bug in the character's health bar when their health is low.
Fixed screen fading out twice when using Robin's building related functions.
Fixed resizing the window below the minimum size causing black bars on screen.
Fixed resizing the window or adjusting zoom resetting the scrollbar position on the options screen.
Fixed social tab showing one gift given if you gave two gifts that week plus a birthday present.
Fixed minor visual bug when switching between the "Host" and "Join" tabs in the co-op screen.
Fixed non-centered text alignment in the header of Robin's build menu.
Fixed the host player seeing light sources from Ghosts in the mines, even while not in the mines.
Fixed purchasing stacks of player-sold items from Pierre not visibly reducing the stack available.
Fixed lighting in the mine changed as soon as you start going down a ladder, instead of after loading the next level.
Fixed screen briefly fading to black during Grandpa's evaluation.
Fixed players sometimes getting stuck on a black screen during weddings.
Fixed pulling the last piece of hay out of a hopper not making it display as empty.
Fixed several issues with weather debris displaying incorrectly.
Fixed issue where white or black customization colors would cause the HSV sliders to show invalid numbers upon using the Shrine of Illusion.
Fixed visual issues with the cutscenes while riding the bus.
Fixed issue where holding 'up' while taking the bus back from the desert would cause the camera to pan during the cutscene.
Fixed trees planted in the desert showing their snow-covered sprites in winter.
Fixed issue where player animations weren't properly looping during events.
Fixed issue where Journey of the Prairie King showed -1 lives after losing all of your lives.
Fixed issue in Robin's menu where the Deluxe Barn's description overlapped the materials list.
Fixed minigames / cutscenes not always centered when the game is zoomed out.
Fixed the order of recipes in the Collections menu and the kitchen stove menu not matching.
Fixed weather debris clumped up after playing a minigame.
Fixed alignment of several UI elements in Calico Jack minigame.
Fixed falling leaves in the Secret Woods not showing their seasonal variants in fall.
Fixed campfire lighting misaligned.
Fixed map showing the player in the mines when they're in the Skull Cavern.
Fixed menu backgrounds not shown in the Community Center bundles menu.
Fixed the map's location label partly rendered off-screen in some cases.
Fixed white borders sometimes drawn on pieces of debris/dropped items.
Fixed mouse cursor not showing gift icon when gifting items to an NPC you're meeting for the first time.
Fixed mouse cursor showing "talk to" when hovering over NPCs during non-interactable events.
Fixed issue where harvesting from a crab pot while your inventory was full would result in multiple 'inventory full' messages without the red 'X'.
Fixed crab pots positioned/rendered over tiles they should be being drawn behind.
Fixed issue where opening a door would briefly show a ghost door.
Fixed windows in barns, coops, and spouse rooms providing light on rainy days or when it's dark out.
Fixed inconsistent particle effect when you right-click vs left-click to sell in the shop.
Fixed digging up an artifact spot in the rain leaving a dry spot.
Fixed hoeing in the desert when it's raining elsewhere leaving a wet spot.
Fixed outdoor garden pots not showing watered sprite when it's raining.
Fixed the health bar 'bleeding' at low health values if the health bar isn't currently being drawn or if the screen is currently fading.
Fixed double cursor in the Stardew Valley Fair slingshot minigame, and disabled drawing of it when playing with controller.
Other bug fixes
All mine songs now show up in the Jukebox list.
Fixed crash on startup if no audio output device is detected.
Fixed resolution issues for some players.
Fixed music not properly playing at the start of a new day.
Fixed Junimos not behaving properly after completing the community center.
Fixed issue where other players could affect the music that's playing in the mines.
Fixed various bugs caused by simultaneous buffs and debuffs.
Improved confusing error if certain game files are missing.
Fixed issue where players wouldn't get museum achievements until the next time they donated something themselves.
Fixed Master Angler achievement awarded before catching all fish.
Fixed issue where the music in Leah's house didn't stop after leaving her house.
Fixed issue where the wallpaper and flooring would shift rooms as you upgraded your house.
Fixed skipping an event sometimes making the player wait on a black screen for a while.
Fixed placing a bomb and leaving the screen before it explodes causing a buggy sound effect.
Fixed placing a bomb that destroys weeds and leaving the area before the explosion happens still playing the weed destruction sounds.
Fixed options menu being scrollable while a dropdown list is active.
Fixed an issue where a female character's pants could have their color changed to black during a wedding ceremony.
Fixed issue where you'd need to click twice to clear the dialogue that appeared after falling down a mineshaft.
Fixed issue where hotkeys (like opening the inventory) triggered after sending a chat message.
Fixed issue where dialogue couldn't be advanced using keyboard inputs.
Fixed issue where the music would sometimes briefly play again after you had turned the volume down.
Fixed issue where rebinding the menu key closed the options menu.
Fixed Prairie King game over screen only accepting input every 1.5 seconds.
Fixed Prairie King music overlapping if you use the zombie powerup multiple times in quick succession.
Fixed mouse repositioned when clicking HUD zoom buttons, making it harder to zoom in/out multiple times.
Fixed issue where loading a save would play the furnace and fireplace sounds.
Fixed volume levels not properly applied when connecting to a game as a farmhand.
Fixed rare crash or invisible grass caused by grass sizes becoming invalid.
Fixed clicking without dragging with the slingshot consuming ammo but firing nothing.
Fixed crash after eating a Maki Roll while playing in French.
Fixed Prehistoric Tibia and Amphibian Fossil not appearing in the forest (or anywhere) while playing in Spanish.
Fixed Wild Plums listed as forage instead of fruit in non-English languages.
1.3.36
Stardew Valley 1.3.36 was posted to the beta channel on 24 January 2019 and released on 1 March 2019.

Changes
Added French, Korean, Italian, Hungarian, and Turkish language support
Added a new Credits menu to replace the "About" menu on the title screen, and removed the /credits chat command.
Removed unneeded tilesheet files under Content.
Removed translated map files under Content/Maps (translated tilesheets are now loaded automatically).
Centered shed door.
Bug fixes
Fixed bug where music doesn't correctly play in the morning.
Fixed bug where giving a gift to an NPC caused the gift action to happen twice in rapid succession.
Fixed furniture rotation bug for "stools".
Fixed Junimos not disappearing after the final goodbye.
Beta Versions (1.3.35–1.3.36)
1.3.33
Stardew Valley 1.3.33 was posted to the beta channel on 18 December 2018 and released on 8 January 2019.

Changes
Improved performance in locations with lots of light sources (e.g., torches).
Improved performance on farms with lots of animals.
Tweaked new "H" health icon.
Bug fixes
Fixed multiplayer visual glitch when another player uses a tool and then starts moving in a new direction.
Fixed "fishing stance" visual glitches in multiplayer.
1.3.32
Stardew Valley 1.3.32 was released on 19 November 2018. (Versions 1.3.29–1.3.32 were all posted on the beta channel, and are included in 1.3.32.)

Changes
Optimised network performance.
Added more ways for the host to unpause the server (by pressing ESC, B, Back).
Added alternative way to show the chat box (press right stick button on a controller).
Added internal changes for modders (should have no effect on vanilla gameplay).
Bug fixes
Fixed slimes not pouncing correctly.
Fixed items-crafted stat being 0 after loading a file until you craft something again.
Fixed rabbit's foot not affecting the breakup scene in non-English language modes.
Fixed some rare tool-related crashes in multiplayer.
Fixed an audio-related crash often caused when using bombs.
Fixed Junimos dropping crops on the floor instead of collecting them.
Fixed NPCs walking through the saloon doors.
Fixed a few rare-ish crashes that can occur when connecting to another player's game.
Fixed eye color being reset to brown after reloading.
Fixed inability to use rod / slingshot in festival minigames.
Fixed the title menu back button being hidden behind submenus.
Fixed inability to move after receiving a gift at the Feast of the Winter Star.
Fixed crash when saving after the game adds Lewis' shorts to Marnie's house.
Fixed crash viewing the map when another player is in certain events.
Fixed "double sound" when using singing stone.
Fixed a Geneva Convention violation (by replacing red crosses in graphics).
Fixed clicks on the chatbox not being registered when the game is paused.
Fixed players sometimes walking off in a straight line through all terrain when they get disconnected.
Fixed babies sometimes spawning in houses that don't belong to the parents.
Fixed the potential for overnight events to cancel or skip a wedding event.
Fixed a desync that could occur if a player tried to get into the casino after a different player has removed the bouncer.
Fixed players able to simultaneously build overlapping farm buildings.
Fixed only one player being able to get the dark talisman.
Fixed the inability to place donated items on the bottom two rows of the museum.
Fixed farmhands being unable to pick up items they dropped in festivals.
Fixed Pam's upgraded house interior event not happening.
Fixed visual glitches caused by triggering a shared event simultaneously with the return scepter.
Fixed softlock caused by mistaken ability to use daggers during events.
Fixed players all receiving the same personal overnight events on the same day (e.g., spouse asking if you want a baby).
Fixed attempting to demolish cabins of abnormally disconnected farmhands causing the cabin to be destroyed after you leave the buildings menu.
Fixed farmers getting stuck in the fishing casting animation after picking up someone else's rod.
Fixed host sometimes appearing stuck using tool in shared events.
Fixed soft-lock when you play the Journey of the Prairie King past 2am.
Fixed glitched chest lid appearing when you destroy a cabin.
Fixed duplicate songs in the jukebox.
Fixed only one player's glow ring working at a time.
Fixed farmhands not being able to see each others' bundle changes.
Fixed bug causing some players to become married to two other players in 3-4 player farms.
Fixed player sometimes getting stuck in bed after another player got in and then got back out.
Beta Versions (1.3.29–1.3.32)
1.3.28
Stardew Valley 1.3.28 was posted to the beta channel on 10 August 2018 and to the main channel on 14 August 2018.

Fixed bug preventing buildings from being placed where there would be a path/flooring tile in front of the door.
Fixed music not playing at the Luau festival and in town.
Fixed clients occasionally crashing in rainy weather.
Fixed server crash when there are no available network adapters.
Fixed the load menu showing 'no saved games' while searching for files.
Fixed crash that occurred if you collided with a monster on the first frame you entered a new location.
Fixed Robin forgetting that she's meant to upgrade a farmhand cabin if the farmhand disconnects abnormally.
Fixed farmhands not being able to set the next day's weather with rain totems.
Fixed farmhands 'swimming' inside their cabins if they're disconnected while swimming in the spa.
Fixed swimming-related visual bugs in on farmers' faces.
Fixed furniture rotation graphical glitch.
Fixed a crash that occurs if you try to copy an invite code while remotely logged into the machine the game is running on.
Fixed a German localization issue with '%Farm' appearing in text instead of the farm's name.
Fixed spouse NPCs not kissing farmers.
Various internal changes requested on the modding wishlist.
1.3.27
Stardew Valley 1.3.27 was released on 1 August 2018. (Versions 1.3.3–1.3.26 were only posted on the beta channel, and are included in 1.3.27.)

New content
Added multiplayer over GOG, Steam, or LAN. This includes chat with custom emotes, and new cabin buildings.
Added Night Market event.
Added Community Upgrade to carpenter's shop.
Added buildable shipping bins to Carpenter's Shop.
Added Abigail encounter at level 20 in the mines.
Added new heart events for Jas, Linus, Pam, Vincent, and Willy.
Added new heart events when player has given a bouquet to all bachelors or bachelorettes.
Added rare treasure chest rooms in Skull Cavern.
Added new monsters in the Skull Cavern: carbon ghost, iridium bat, and iridium crab.
Added secret notes and related quests.
Added new items: auto-grabber, cactus seeds, garden pot, wood sign and stone sign, solid gold Lewis statue, pearl, wedding ring, new paintings, and decorative items sold at shops and festivals throughout the year.
Added bear's knowledge, special charm, spring onion mastery.
Added Statue Of Uncertainty to change professions.
Added different stationery for letters from Sandy and the Wizard.
Added horse hats.
Balance changes
Increased purchase price of wood, stone, ores, and coal in the year 2+. The gold received for selling them is unchanged.
Reduced price of tub o' flowers from 1000g to 250g, and recipe from 2000g to 1000g.
Breaking small tree stumps now provides +1 foraging XP.
Once the player reaches the mine bottom...
prismatic shards and diamonds may rarely drop from any monster;
gems and purple mushrooms may be found when searching trash bins;
gems and purple mushrooms may be requested in NPC quests;
some monsters will be stronger.
Other changes
Once the player reaches the mine bottom, the Dwarf will attend weddings.
Golden pumpkin is now a universal love (instead of universal hate).
Tweaked several seed packet sprites.
Tweaked Mr. Qi dialogue portrait.
You can now add Mayor Lewis' shorts to the Luau soup.
You can now put fire quartz in the furnace to produce refined quartz.
You can now refill a Watering Can at the kitchen sink.
Fireplaces are now furniture, so you can move them around and buy different fireplaces.
Fruit Trees cannot be planted on top of decorations in the greenhouse border, or in the corners of the Greenhouse.
Replaced gold display on player menu from "g" to "金" in Chinese.
Improve Chinese translations:

Item name changes
Item description changes:

Items Changed
Bug fixes
Fixed crops harvested with a scythe not giving XP.
Fixed bee houses always giving wild honey when used on custom farms.
Fixed seeds planted out of season disappearing.
Fixed player collapse being cancelled when they open the journal.
Fixed animal mood & happiness bugs.
Fixed crystalarium item swap exploit.
Fixed furniture being usable to complete bundles.
Fixed some recipes allowing Milk, but not Large Milk.
Fixed crash that occurred after 596 hours of gameplay.
Fixed staircase being spawned on mine level 120 when a placed object is destroyed.
Several grammar/spelling fixes.
Fixed wheat seeds and bok choy seeds descriptions in Brazilian-Portugese.
Fixed spring sign on bathhouse in Chinese.
Beta Versions (1.3.0–1.3.27)
1.2.33
Stardew Valley 1.2.33 was a small bugfix patch released on 10 July 2017.

Changes
Fixed Linux/Mac builds distributing with MonoGame-built content instead of XNA-built content (which made modding more difficult).
1.2.32
Stardew Valley 1.2.32 was a small bugfix patch released on 10 July 2017.

Bug fixes
Fixed Linux install failing due to broken symlink in 1.2.31.
Fixed save files potentially getting overwritten if you start a new file after using exit to title.
1.2.31
Stardew Valley 1.2.31 was a small bugfix patch released on 7 July 2017.

Bug fixes
Fixed crashes related to use of slot machines.
Fixed some potential sources of unnecessarily increased memory usage.
Fixed some options in dialogue not being usable with a controller.
Localization fixes
Fixed the 'loading...' message on loading screens wrapping incorrectly in some languages.
English: fixed grammar in Luau community soup text.
Portuguese: fixed some dialogue options in Linus' 0 heart event being missing.
Portuguese: fixed the cut-off 'level up' title.
Russian: added more space for the '(single)' text on the social page.
1.2.30
Stardew Valley 1.2.30 was released on 12 May 2017.

Changes
The window mode preference is now shared between all save files.
Bug fixes
Fixed crash when the game switches window mode while loading a save.
1.2.29
Stardew Valley 1.2.29 was released on 02 May 2017. (Versions 1.2.27–1.2.28 were only posted to the Steam beta channel, and are included in 1.2.29.)

Bug fixes
Fixed crashes while loading save files.
Fixed crashes when going fullscreen.
Fixed crashes while saving due to slay-monster quest.
1.2.26
Stardew Valley 1.2.26 was released on 24 April 2017 with in-game support for six new languages. Beta versions were posted to the Steam beta channel starting 07 February 2017.

Changes
Translations for German, Spanish, Brazilian Portuguese, Russian, Japanese and Simplified Chinese.
When using a controller, the cursor will snap between menu buttons by default. If you disable that, the cursor will instead accelerate while moving.
When using a controller, pressing the back button will skip events that are skippable.
"Show sharper digits" on Options menu removed.
Exit to Title has returned.
Added panda hat (TGP only).
Bug fixes
Fixed lighting shader not covering the whole screen on Mac and Linux.
Switching from "Windowed Borderless" to "Fullscreen" should now go straight to fullscreen instead of Windowed mode.
Wallpapers and floors no longer have a tile placement indicator showing a random object.
Increased stability of preference-saving code. This should fix infrequent crashes that require the player to delete startup_preferences.
Fixed a crash that can happen when a pig tries to spawn a truffle but there’s no space for it.
Fixed a couple of rare crashes that could have occurred at any time during the game.
Fixed a typo of the word ‘pronounce’ in the marriage event.
Fixed the player not getting the recipe for Cookies if they skip Evelyn's event.
Fixed farm animals not producing goods at high happiness.
Farming level now affects crop yield prior to level 10.
Beta Versions (1.2.0–1.2.25)
1.11
Stardew Valley 1.11 was released 06 October 2016, with a beta posted to the Steam beta channel on 05 October 2016.

Minor changes
All the new farms now provide some kind of fishing opportunity, although the riverland farm is still superior.
The riverland farm now has the potential to spawn splashing fish nodes and ore panning nodes.
You can place buildings on most grass areas.
On the riverland and forest farm maps, some bushes can be destroyed with an upgraded axe.
Digging spots now appear on the farm, although less frequent as elsewhere. The hill-top quarry also has a chance of spawning them.
The forage berry bushes are now affected by the Botanist perk.
Slime egg prices increased.
Placing a wicked statue in a slime hutch prevents the witch from visiting it.
On the forest farm map, forage items have a chance to spawn on any grassy area, not just in the west.
Spouses will now speak to you when they come home on Friday nights.
Bug fixes
Price of galaxy dagger has been corrected to 35,000g (it was at 350,000g).
The Artisan Perk description has been corrected to reflect the actual bonus (it's 40% now, but the description still says 50%).
Weeds in the Mutant Bug Lair no longer change with the season (and no longer turn to battery packs in the winter).
The Mutant Bug Lair now replenishes itself a bit each day.
Monsters in the Mutant Bug Lair will now always be mutant... not revert to the standard grub/fly after saving and reloading.
Meteorites can no longer land on top of stumps or boulders.
You can once again place buildings in the little-shaded strip right below cliffs.
Fixed some tiles on the farm maps.
Fixed problem with forage spawning under stumps.
Spring onions can be iridium quality with the botanist perk.
Truffles should no longer spawn in the water.
Pets should no longer be able to walk down the cellar stairs into the void.
The Outlaw boss in Journey of the Prairie King will warp back to the center of the map if he happens to run too far off screen in either direction.
Coop animals can now actually produce higher quality produce like they were supposed to.
Can no longer fill your watering can at a well that isn't fully constructed or in construction.
Trees can no longer spread off the map into the void, causing the game to start getting slower with each day. The new patch will retroactively remove these problem trees as well.
You should now properly see the final Joja cutscene, even if you switched to JojaMart after completing most of the Community Center.
Forage items shouldn't spawn in inaccessible places anymore.
Fixed issue where lightning that struck an object on the farm would cause that object to "pop" into the current map when the current map was not the farm.
When you reach level 5 or 10 in a skill, but haven't slept yet, it no longer shows your new profession as "Desperado".
Minor convenience adjustments and bug fixes.
1.1
Stardew Valley 1.1 was released 3 October 2016, with a beta posted to the Steam beta branch on 29 September 2016.

Marriage candidates
Marriage candidates now have an outdoor area on the farm that is unique for most spouses, and sometimes spend time out there, usually doing a unique behavior.
Sam has a little halfpipe and he does skateboard tricks.
Maru has a little gadget that she works on.
Abigail plays her flute.
Leah has a sculpture to carve.
Sebastian works on his bike.
Alex lifts weights.
Penny, Harvey, and Elliott read a book in a little potted plant garden.
Emily meditates in a crystal garden.
Haley takes pictures between two potted palm trees.
Shane has a little chicken hutch, and he stands by it holding his chicken "Charlie".
Shane can be married and has new dialogue, scheduling and heart events. There's a new door for Shane in Marnie's shop which is locked. Shane's "spouse room" is a mess, with a mini-fridge and a muddy path of footprints leading up to it.
Emily can be married and has new dialogue, scheduling and heart events.
Buildings
Robin has a few new buildings available for sale.
shed: an empty room which players can do whatever they like with. They can decorate it the same way as their house.
mill: lets players place wheat in it to make flour, or beets to make sugar. One wheat makes one flour. One beet makes 3 sugars. When they place wheat or beets inside, the flour or sugar will be ready the next morning. The little box on the right side of the mill acts like a chest and it will contain any product that has been milled the previous day.
The wizard now offers new farm buildings after completing a quest line. These buildings are very expensive and intended for end-game. They'll appear instantly after purchase, unlike Robin's buildings which require construction.
Junimo hut: Junimos will come out to harvest any mature crops within a certain distance of the hut. The Junimos will place the crops they harvest in the hut for players to grab at their leisure.
Water obelisk: when interacted with, it warps players to the beach, exactly like the beach warp totem. It's basically an infinite totem that lives on the farm.
Earth obelisk: just like the water obelisk except it warps players to the mountains.
Gold clock: prevents debris from appearing on your farm. Keeps fences from decaying.
Farm maps
There are now five farm maps to choose from when starting a new game. The basic map that exists currently, as well as a new map themed around each "skill". Each special map has a feature that makes it a little different, and each map also comes with unique decorations inside the players house.
Riverlands: lots of water on this map... limiting your farm space. Looks nice. Fishing is actually viable on this farm... In fact, players can catch the same fish that are available in town.
Forest: the forest encroaches on the land, limiting farming space. However, there are renewable stumps on the east edge of the map, and seasonal forage items spawn there as well. Also, there is a new type of "weed" that spawns on the farm, which looks unique and will always drop mixed seeds when cut.
Hill-top: lots of cliffs... and there is a special mining area in the southwest where ore will spawn, as well as unique geode-bearing stones.
Wilderness: lots of space to farm, looks a little more interesting than the basic farm with a large lake in the southwest corner, and a cliff along the east and south. On this map, bats and golems will come out at night. There is a new monster called a wilderness golem which is unique to this map. It behaves just like the stone golem, but has different drops. Its stats scale with player combat level.
Farm
Added coffee beans, which can be used to brew coffee.
Added a new farmhouse upgrade which adds a cellar.
Added casks, which can be used to age alcohol and cheese to higher quality and value. This includes a new iridium quality, which doubles the value of the base item.
Fruit trees can now produce iridium-quality fruit. The fruit trees increase quality by 1 star per year of age after reaching maturity.
Divorce
Players can now divorce their spouse by filing in a little book inside the mayor's house.
After divorce, your spouse moves out and returns to their old life, but any children will stay.
After divorce, ex-spouses are less friendly toward the player and have unique 'rejected' dialogue.
Using the Dark Shrine of Memory in the Witch's Hut will erase the ex-spouses memory, making it seem like you had never been married.
Other new content
Return scepter now sold by Krobus in the sewer for 2,000,000g. This item acts like a permanent warp totem to the farm. You can use it any time to warp back to the farm.
Two new fish can be caught in the wild: slimejack (Mutant Bug Lair) and void salmon (Witch's Swamp).
Inside a new building, the Witch's Hut there are three new shrines:
Dark Shrine of Memory - Will erase a divorced spouse's memory, making it seem like you had never been married.
Dark Shrine of Selfishness - Allows you to turn your children into doves (Gets rid of them) in exchange for a prismatic shard.
Dark Shrine of Night Terrors - Allows you to toggle having monsters spawn on your farm in exchange for a strange bun.
There are two new quests available which unlock the new Wizard farm buildings (available after completing either the Community Center or JojaMart goals).
Dark Talisman - Sends the player to a new area, the Mutant Bug Lair to retrieve a powerful magical artifact.
Goblin Problem - Sends the player to a new area, the Witch's Swamp.
honey can now be placed inside kegs to make mead.
casks can now be crafted to age alcohol and cheese which increases quality.
void mayonnaise can now be crafted from void eggs.
catalogue - Sold by Pierre, this expensive furniture piece allows players to purchase wallpaper and flooring from their home.
furniture catalogue - Sold by Robin. Like the catalogue, this can be placed at the farm and players can interact with it to purchase furniture.
New furniture - anchor, bamboo mat, boarded window, bonsai tree, burlap rug, candle lamp, carved window, ceiling flags, decorative lantern, floor TV, green cottage rug, hanging shield, Junimo plush, l. light string, metal window, miner's crest, monster danglers, monster rug, mystic rug, nautical rug, ornate lamp, ornate window, porthole window, s. pine, small crystal, tree column, woodcut rug, world map.
Galaxy swords, galaxy daggers and galaxy hammers are now purchasable from Marlon once you have obtained a galaxy sword.
Minor changes
New mail messages after the player passes out from exhaustion or dies. They'll sometimes end up at Harvey's clinic after passing out.
Strange bun had its price and cooking ingredients adjusted.
Giving someone a gift on their birthday will never make your spouse jealous.
You can now wallpaper the little hallways in your upgraded house.
When you beat Journey of the Prairie King, you can now start over in a harder mode, keeping your upgrades and coins.
2 new "Lost Books" to collect for the library.
You can now choose to color your chests with one of 20 color options.
NPC's now appreciate quality level in gifts, but it only has an effect on gifts they "like" or "love".
You can now move your buildings via Robin's construction menu.
Krobus now sells void eggs.
Slime balls now have a chance to drop petrified slime.
When paused, the time now blinks from black to gray, to black.
Added a graphics option to display "sharper" stack number digits.
Kegs no longer require clay to craft.
You can once again plant fruit trees around the edge of the greenhouse interior.
After seeing Shane's 8-heart event, each chicken you purchase from Marnie has a 25% chance of being blue. Aside from appearance, the blue chicken is identical to the white chicken.
Sunflower seeds can now be purchased and planted in summer in addition to fall.
Balance changes
All animal products are increased in value by 25% (rounded up to the nearest 5g)
The Rancher profession now increases the value of animal products by 20%, up from 10%
The Artisan profession now increases the value of Artisan goods by 40%, down from 50%
The Blacksmith profession now increases the value of metal bars by 50%, up from 25%
The value of blueberry is now 50g, down from 80g
The value of starfruit is now 750g, down from 800g
The value of cranberry is now 75g, down from 130g
The value of ancient fruit is now 550g, down from 750g
Cranberry sauce has had its value reduced to 120g
Stuffing has had its value reduced to 165g
Cranberry candy has had its value reduced to 175g
Blueberry tart has had its value reduced to 150g
Fruit salad has had its value reduced to 450g
Reduced sell price of cranberry seeds to 60g
Bug fixes
Wild plums are now labeled as fruit.
Grandpa's Shrine should now always properly give the reward for reaching 4 candles.
Fixed issue where gathering an item with the "botanist" profession would fail if the inventory was full, even though the gold-level item was present in the inventory.
Slime charmer ring should now protect against giant slimes.
You can no longer tap a stump.
Fixed Joja Warehouse graphic issue in winter.
"Check action"-mapped keys should now work to attach bait to a rod.
Rain ambient sound should no longer play in Sandy's Oasis under any conditions.
Your baby should now be properly born, even if you pass out in the mines on the eve of the birth.
Moonlight Jellies engagement crash.
Galaxy sword should now be truly unloseable.
You can no longer lose hay to a hopper because you have no silo.
You can no longer plant fruit trees off the farm.
Typo fixes
1.07a
Stardew Valley 1.07a was released on 29 July 2016.

Changes
Added Mac OSX and Linux compatibility.
1.07
Stardew Valley 1.07 was released 04 April 2016, with a beta posted to the Steam beta channel on 31 March 2016.

Gameplay
Spouses now say unique dialogues during festivals (most of the time), rather than the generic handful of dialogues.
Spouse stands next to you at the Dance of the Moonlight Jellies.
In-law dialogue... when you marry someone, their parents/relatives dialogues will change slightly to account for the change.
Sam, Sebastian, and Abigail now go to the saloon on Fridays after you marry them.
Spouses won't leave on rainy days, unless they have to go to work.
Fruit trees produce higher quality fruit as they age. (once per year, up to gold star).
Fruit tree harvesting now involves shaking the tree to drop the fruit.
Lightning strikes now have a unique effect on fruit trees.
Lightning is more likely to strike trees and crops, but lightning rods now have a very good chance of intercepting lightning strikes (if they aren't already processing a lightning bolt).
Charcoal kiln now requires 10 wood to produce 1 coal, down from 20.
Maxed-out friendship levels will no longer decay.
Added another digit to the shipping menu money counters.
Dying in the mines is less harsh: money lost caps at 5000g, rate of item loss reduced, can't lose rings or the galaxy sword.
Your assigned movement keys are now used within Journey of the Prairie King.
You can now retrieve powerups and coins that drop on the edge of the map in Journey of the Prairie King.
The last two hearts are now greyed-out for marriage candidates until you give them the bouquet.
Willy now likes most fish dishes.
Adventurer's Guild now sells monster slayer rewards after you've unlocked them (you still get the free reward).
Hardware mouse cursor option.
Bug fixes
Tools left in chests within farm buildings won't count as "missing".
Poppy properly consumed in poppyseed muffin recipe.
Can no longer incorrectly "consume" trap bobbers (click to make them disappear with strange sound).
Agriculturist profession no longer causes an extra 25% growth rate when speed-gro isn't present. Speed increase effects should now properly apply to very slow-growing crops.
Fixed sunflower seed price at JojaMart.
Chests should no longer appear on top of your in bed after upgrading your house.
Item placement with the gamepad improved, and there is now an option to show an item placement indicator.
Snow yams shouldn't appear in the desert anymore.
Sea cucumber should properly appear in the fishing tab of the Shipping menu.
Farm animals should no longer get stuck on fences placed directly to the right of the barn door.
Various minor bug fixes.
Minor changes/fixes to dialogue.
1.06
Stardew Valley 1.06 was released 20 March 2016.

Changes
Added unique dialogues for all spouses.
Spouses now leave the house on Mondays.
Value of most animal products increased.
Holly is now poisonous.
Missing events problem shouldn't happen anymore.
Minor bug/grammar/graphics fixes.
1.051b
Stardew Valley 1.051b was released 17 March 2016.

Changes
Fixed disappearing item problem. (items can still be destroyed by farm debris).
Kegs now require oak resin to craft.
Bee houses now require maple syrup to craft.
Tortilla price changed from 75g to 50g.
Nautilus shell (artifact) renamed to nautilus fossil.
1.051
Stardew Valley 1.051 was released 12 March 2016.

Changes
Fixed weird rectangle lighting problem.
Flooring can now be removed by bombs.
You can press a "menu" button (Esc or E by default) to close out of yes/no dialogues.
If no other function is mapped to it, the Y key will choose "yes" in a yes/no dialogue.
You can use the trigger buttons on a gamepad to navigate through the Community Center menu.
Minor fixes.
More secrets.
1.05
Stardew Valley 1.05 was released 9 March 2016, with a beta posted to the Steam beta channel on 4 March 2016.

Gameplay changes
Only read if you've gotten to year 3: Grandpa's had a change of heart... he feels he's been a little too harsh with his judgements. He no longer mentions "great honors", and his dialogue is a lot softer. If he's already visited you, check his shrine for a new opportunity...
Restored a "lost" Shane event.
Changed earthquake to Summer 3rd... to make it clear that it's the season change that kills crops.
Increased opportunities for iridium. The chance to find iridium in the Skull Cavern increases significantly every ten levels.
Added a zoom in/out feature to the options tab.
Added volume sliders for ambient sounds and footstep sounds.
Added snow transparency slider.
Added option to turn off flash effects.
Added lighting quality option.
Added quest (Rat Problem) to make it clearer that you have to investigate the Community Center.
Bug fixes
Leah's schedule has been fixed.
Spouses who have jobs won't get stuck in the bus area anymore.
Upgrading a house with crafted flooring should no longer cause a mess.
Restored more advanced NPC end-point behavior.
"Secret" NPC's should no longer show up on calendar until you meet them.
Escargot, chowder, etc. should now properly give fishing buff.
You now truly cannot pass the bouncer.
You can no longer get stuck trying to board the bus.
Fixed issue with invisible trees preventing interaction with tiles.
Dead flowers no longer affect honey.
You can now dance with your spouse at the Flower Dance.
Game should now properly pause when steam overlay is active.
Fixed issue where inactive window was still responding to input.
Fixed fertilizer prices in Pierre's shop.
Fixed Fector's Challenge.
You can now press the toolbar shortcut keys (1, 2, 3, etc. by default) to change the active slot while the inventory menu is up.
Iron ore nodes can no longer be removed, only destroyed.
The dog or cat should no longer sit on chests...
Spouses less likely to run away into the dark abyss.
Naming your child after an NPC should no longer cause issues.
Fixed issue where recipes would sometimes consume more ingredients than they should.
Fixed crashes in certain cutscenes, when certain dialogue options were chosen.
Many small bug and typo fixes.
1.04
Stardew Valley 1.04 was released 1 March 2016.

Gameplay changes
Added a randomize character button to the character creation screen.
Robin now sells crafting recipes for wood floor, stone floor, and stepping stone path.
Added a secret new way to modify a rare item.
Increased grass growth rate.
Increased forage spawn possibilities, and made it much less likely for forage to spawn behind trees.
Reduced value of honey from 200g to 100g.
Raised Clint's ore prices.
Inventory menus now indicate which slot is the "active slot".
Made the meteorite look snazzier.
Bug fixes
Fixed problem with swinging sword while riding a horse.
Fixed strange lighting behavior when holding torches.
Fixed problem where stone fence was spawning debris.
Spouse should no longer get stuck on their way to town.
Wild seeds now produce the proper produce when in the greenhouse.
Secret gift exchange should now work properly.
All scarecrows now give reports on their crow-scaring activity.
Bouncer is now truly impassable.
Trees no longer grow directly in front of warp statues.
Willy's shop no longer counts as water.
The meteorite should no longer appear in the pond or buildings.
If an object is ever directly underneath you, preventing you from moving, right click to remove it.
Mariner and Luremaster professions should now work properly.
Tappers are now properly destroyed by bombs.
Fixed bathing hairstyle inconsistency.
Fixed various item duplication and stacking issues.
Poppyseed muffin now actually looks like a muffin.
Quest items should no longer disappear when you die.
You can no longer give quest items to the wrong person.
The Skull Cavern quest can no longer be completed before receiving the actual journal entry.
1.03
Stardew Valley 1.03 was released 28 February 2016.

Gameplay changes
The cooking menu now looks for items in your refrigerator as well as your inventory.
Scarecrow range reduced to an 8 tiles radius.
The price of mayonnaise and other artisan animal products now increased by the rancher profession.
Once you befriend someone to 2 hearts, their room is permanently unlocked, even if you go below 2 hearts again.
The 'auto run' option is now enabled by default.
Bug fixes
Fixed duplicate item issue in the mines.
Ladders should no longer spawn underneath the player, locking them in place.
Fixed problems with the Community Center menu. You can now throw items down and delete them (Delete key) in the Community Center menu.
Fixed item quality exploit.
You can now throw items down while in the crafting menu.
If you destroy the stable, you can now rebuild it.
Spa won't recharge you while the game is paused (e.g., steam overlay up).
Fixed problems with the Stardew Valley Fair fishing game.
Various stability fixes.
1.02
Stardew Valley 1.02 was released 27 February 2016.

Changes
If you never received your pet, you will now have another opportunity.
When you go to sleep, the game now checks if any of your essential tools are missing. If so, they will appear next to your bed in the morning.
The game now properly saves on level-up nights.
Eating skill food and then going to bed on a level-up night works properly now.
Fixed problem where completing the Crafts Room while standing in certain locations causes your character to get stuck.
Player character should now walk correctly while in a cutscene after drinking coffee.
Removed an item duplication exploit.
Forage items should no longer spawn in the woods above the beach.
Fixed crab pot problem (again).
Fixed exploding armchair bug.
Relaxing in the spa with your menu up no longer restores energy.
Removed Leah's doppelganger.
Debris should no longer spawn in the pathway between farm & forest.
Fixed disappearing tapper problem.
Fixed a few minor graphics problems & dialogue typos.
Other minor issues (spoilers).
Tools being upgraded no longer erroneously considered "missing".
Clay duplication bug fixed.
Pet cutscene won't refer to the "cat" as a "dog" anymore.
Leah's 10-heart event fixed.
Pepper Popper recipe now requires cheese.
1.01
Stardew Valley 1.01 was released 26 February 2016.

Changes
Fixed random crash when going to sleep after getting your pet.
Sound effect volume now properly applied on load.
The error item should no longer appear for sale in the saloon.
Z key is now bind-able.
No longer possible to exit the Community Center menus while holding an item.
Finding your first artifact from a geode no longer destroys remaining held geodes.
Mature wild crops no longer disappear on day of load.
Crab pots can now be placed and removed without issue.
Fixed crash when inspecting chests in the mines.
You can no longer place chests in the mines.
Tree seeds no longer incorrectly show a "Wrong Season" message.
Fixed some map issues.
1.0
Stardew Valley 1.0 was released on 26 February 2016.

## Document 17
**Source**: https://alanwake.fandom.com/wiki/Alan_Wake_2

Alan Wake 2
Why the hell did you kill Casey? What the hell were you thinking, man?
This article or a section of this article will contain full, or partial plot spoilers of an Alan Wake game or any other piece of media related to the franchise.
You have been warned...

"This story... is a monster. And monsters wear many faces."
― Alan Wake

Alan Wake 2 (stylized as Alan Wake II) is a survival-horror video game that released on 27 October 2023 on digital storefronts for the PlayStation 5, Xbox Series X|S and PC through the Epic Games Store. It is the sequel to 2010's Alan Wake. The game had an expansion DLC released on June 8, 2024 called Night Springs and a second expansion DLC, The Lake House, is slated to be released sometime later. The game has four difficulties: Story, Normal, Hard, and Nightmare, the fourth of which is only available in "The Final Draft" mode. The Final Draft is a New Game Plus mode for Alan Wake 2, featuring new Manuscript pages, other new collectibles, a new expanded ending, and other changes to the game's story. "The Final Draft" was released on December 11, 2023.

Patch notes for Alan Wake 2 updates can be found here.


Contents
1	Synopsis
2	Plot
3	Chapter List
3.1	The Final Draft
3.2	Expansion 1: Night Springs
4	Gameplay
5	Development
5.1	Initial development
5.2	Remedy Connected Universe
5.3	Official development
6	Reception
7	Trivia
8	Gallery
8.1	Official Images
8.2	Concept art
8.3	Concept art (earlier iteration)
9	Videos
10	Sources
Synopsis
Quote1 A string of ritualistic murders threatens Bright Falls, a small-town community surrounded by Pacific Northwest wilderness. Saga Anderson, an accomplished FBI agent with a reputation for solving impossible cases arrives to investigate the murders. Anderson’s case spirals into a nightmare when she discovers pages of a horror story that starts to come true around her.

Alan Wake, a lost writer trapped in a nightmare beyond our world, writes a dark story in an attempt to shape the reality around him and escape his prison. With a dark horror hunting him, Wake is trying to retain his sanity and beat the devil at his own game.

Anderson and Wake are two heroes on two desperate journeys in two separate realities, connected at heart in ways neither of them can understand: reflecting each other, echoing each other, and affecting the worlds around them.

Fueled by the horror story, supernatural darkness invades Bright Falls, corrupting the locals and threatening the loved ones of both Anderson and Wake. Light is their weapon—and their safe haven — against the darkness they face. Trapped in a sinister horror story where there are only victims and monsters, can they break out to be the heroes they need to be? Quote2
― Epic Games Store page description
Plot
See also: Alan Wake, Alan Wake's American Nightmare, and Control
In 2023, thirteen years after the events of Alan Wake, a naked man emerges from the dark shores of Cauldron Lake, experiencing visions of a man violently screaming before he is found and has his heart cut out by a group of men wearing deer masks.

FBI Special Agent Saga Anderson and her partner Alex Casey are dispatched to the town of Bright Falls, Washington to investigate a series of ritualistic murders. They investigate the latest victim, the naked man, who is revealed as former FBI Agent Robert Nightingale. It is believed he was murdered by a group calling themselves the "Cult of the Tree". In addition to Nightingale's corpse, Saga finds a mysterious manuscript page that seems to predict the future. While in the town, they encounter Sheriff Tim Breaker, who promises to assist their investigation, as well as waitress Rose Marigold, who recognizes Saga and acts like Saga was a local of the area, despite this being her first visit to the town. She also claims Saga's daughter Logan drowned several years ago, despite being alive in Virginia with her father. At the morgue, Saga then performs an autopsy on Nightingale's corpse, but it suddenly reanimates, in search of the "Clicker", and escapes the morgue after Breaker mysteriously vanishes.

As they pursue Nightingale to Cauldron Lake, Saga uses her psychic powers to investigate the scene. Casey reveals he had investigated a murder cult in New York City dedicated to bringing back the missing author Alan Wake by reenacting the murders described in his books, and that Nightingale came to Bright Falls to pursue Alan thirteen years prior. Saga encounters Nightingale, now converted into what the manuscript called a "Taken", and is forced to kill him. Saga then finds a very-shaken Alan Wake washed up on the shore of the lake and takes him into custody while also discovering evidence that an organization called the Federal Bureau of Control has a presence in Bright Falls. Saga and Casey take Alan back to the Elderwood Palace Lodge in their field office where he recounts how he escaped from a dream-like dimension called the Dark Place.

While trapped in the Dark Place, Alan continually tried to find a way to escape. After appearing in a mysterious talk show called "In Between With Mr. Door", Alan found an Angel Lamp once belonging to Thomas Zane and connected to the Clicker that, in combination with his writing ability, allowed him to manipulate the Dark Place to better navigate it. Alan began navigating a dark, twisted version of New York City, following the trail of Alex Casey's investigation of the "Cult of the Word" led by Alan's evil doppelganger Scratch, who survived his erasure from existence, which brought him through the various scenes of the murders committed by the cult. Along the way, Alan also encountered Breaker, who was searching for the talk show host, Warlin Door, believing him to be responsible for trapping him in the Dark Place. Alan also occasionally made brief contact with Saga, the two of them trading vital information when they could. After believing he had killed Tom Zane, who had gone insane from his captivity inside the Dark Place, Alan was contacted by an alternative version of himself, explaining that his repeated attempts to escape the Dark Place are causing him to experience time loops.

Back in the present, Alan explains that he wrote a new novel, "Return", that helped him escape the Dark Place. However, Scratch re-edited the manuscript into a horror story now taking effect in reality. Alan warns that Scratch is searching for the Clicker, which is the key he needs to free the malevolent Dark Presence completely, but also the key to permanently defeating it. When one of the manuscript pages mentioning the Cult of the Tree possesses the Clicker, Saga decides to follow its trail in Watery and realizes that "Return" has rewritten her past so that her daughter Logan drowned in an accident. Angered that Alan wrote her and Logan into his story, Saga recovers the Clicker, but before she can get it to Alan, agents from the FBC led by Agent Kiran Estevez arrive and apprehend him as well as the Cult leaders, revealed to be town entrepreneurs Ilmo and Jaakko Koskela.

With no other options, Saga goes to the Valhalla Nursing Home and tracks down Odin and Tor Anderson, who know more about the Clicker. As she communicates with them and rescues Tor from a Taken Cynthia Weaver, she learns that Odin and Tor are actually her grand-uncle and grandfather, respectively, and she inherited their seer abilities, allowing her to discern the changes to reality "Return" is causing. Odin and Tor also explain that the Clicker does not do anything by itself, but instead dramatically enhances the creative power of the person using it, which is why it is important to Alan and Scratch. Saga then heads back to Bright Falls to get the Clicker to Alan, but finds out that the Alan who escaped Cauldron Lake was actually Scratch. With his identity now exposed, Scratch kills Jaakko and escapes from captivity, attempting to take the Clicker from Saga. He is temporarily thwarted and banished by the FBC.

Ilmo reveals that he and Jakko formed the cult in order to scare townsfolk away from the dangers of the lake, while they perform their ritual killings on whatever Taken emerges from it, such as Nightingale. Realizing that Alan is still trapped in the Dark Place, Saga enlists the help of Casey, Odin, Tor, and Estevez to carry out a ritual to summon him to the real world. Meanwhile, Alan continues to try and find a way out of the Dark Place, eventually making his way to his old apartment. There, he discovers his wife Alice had been tormented with visions of Scratch, eventually leading to her apparent suicide. In anger, Alan kills who he believes is Scratch, but is actually a version of himself attempting to fix Scratch's ending of "Return", perpetuating the loop.

Back in the real world, the summoning ritual fails to summon Alan in the current time and instead was responsible for his initial appearance earlier in the story. Both Saga and Alan come to the realization that Alan and Scratch were always the same person, with Scratch being Alan, who is possessed by the Dark Presence at the end of every loop, and thus indirectly responsible for Alice's death. Scratch arrives at the summoning site and Saga is able to banish him from Alan's body, only for Scratch to possess Casey instead, steal the Clicker, and throw Saga into the Dark Place.

With Scratch in possession of the Clicker, Alan concludes that the only way to stop him now is to find the manuscript and write a completely new ending for "Return". He returns to his writing room and tries to work out how to write a perfect ending that saves everybody while staying consistent with the horror genre. Meanwhile, trapped in her mind place, Saga fights off the Dark Presence's attempt to overwhelm her with her own negative emotions and self-doubt. Now in the Dark Place proper, she reunites with Breaker, who remains there in his search for Door, heavily implied to be Saga's missing father. She then receives aid from an anonymous woman who directs her to the Clicker and a Bullet of Light. Saga takes the two items and escapes back to the real world by mimicking Door's actions on a manuscript page given to her by Breaker. With the Clicker, Alan is able to banish Scratch from Casey's body. Scratch returns to possessing Alan, and Saga shoots him with the Bullet of Light, seemingly killing him and Scratch. As Casey recovers from his possession, Saga tries to call Logan to confirm her safety, but the scene cuts short before any answer can be heard.

In a post-credits scene, a recording left behind by Alice reveals that she had managed to fully regain her memories of what happened to Alan after consulting with the FBC at the Oldest House. She had tricked Alan into thinking she committed suicide by choosing to return the Dark Place as part of a plan to help him eventually escape, explaining that the only way he can escape the loops is through "ascension." Alan then revives from his gunshot wound and says, "It's not a loop, it's a spiral."

In the "Final Draft" ending, Alan realizes that the Bullet of Light was meant to cleanse a part of himself the Dark Presence used to create Scratch, finally killing his doppelgänger for good while finishing the spiral and freeing Alan from the loop. Saga's call connects, confirming Logan's survival, and Alan revives soon after to the surprise of her and Casey, declaring himself the master of not just two worlds, but many.

Chapter List
The chapters/parts listed here are played in the following order:
Prologue: The Cult
Return 1: Invitation
Return 2: The Heart
Initiation 1: Late Night
Initiation 2: Casey
Initiation 3: Haunting
Players have the choice to play the following of Alan and Saga's chronological chapters/parts in any order they wish:
Return 3: Local Girl
Return 4: No Chance
Return 5: Old Gods
Return 6: Scratch
Initiation 4: We Sing
Initiation 5: Room 665
Initiation 6: Return
Initiation 7: Masks
Initiation 8: Zane's Film
The chapters/parts listed here are past the point of no return and are played in the following order:
Return 7: Summoning
Initiation 9: Gone
Return 8: Deerfest
Return 9: Come Home
The Final Draft
Remedy released a New Game Plus update to the game on December 11th, 2023 named "The Final Draft".

Expansion 1: Night Springs
Set as "episodes" of the Night Springs TV show, these can be played in any order the player wishes.

Number One Fan
North Star
Time Breaker
Gameplay
Similar to the original, the game is a third-person shooter, with players using light to burn away the darkness of the enemy and various weapons to fight against the dark forces as well as various cult members. Unlike the first game, which was an action-adventure game, Alan Wake 2 emphasizes survival-horror gameplay. Players have an inventory with limited space, where they will need to conserve their ammo and healing items. Health items themselves consist of med kits and painkillers, with Safe Havens only healing the player to take them out of a "critical state." Players also encounter various puzzles and locked boxes that they'll need to solve in order to obtain upgraded gear.

The game features two distinct campaigns, one where you play as the titular Alan Wake, and one where you play a new protagonist, Saga Anderson. The two campaigns blend together, eventually allowing you to switch between the two at various points, using a dark puddle found in certain Break Rooms if the player wishes, with the two stories both foreshadowing and echoing each other. Eventually though, the player will be required to complete both stories before progressing past a point of no return.

Saga’s story takes place in the Pacific Northwest, consisting of three hubs: the small town of Bright Falls, the stunning primordial forest surrounding the mysterious Cauldron Lake, and the run-down town of Watery. Alan's story takes place solely within the Dark Place in a warped version of New York City, with his reality shifting and looping. Similarly to the episodic nature of the original, the narrative is divided into chapters, which each having their own accompanying end song. Between chapters, players are returned to the hubs and are allowed to explore or move to the next chapter at their own pace.

Whilst Saga's story involves a lot of talking to various townsfolk around the area in order to progress in her environment, Alan uses an Angel Lamp to allow him to change a scene by transferring light from one area of New York to another. Both characters have their own "mind palaces" to help progress their stories, with Alan having his Writer's Room to help change the story and Saga having her Mind Place to help her with her investigations, both of which can be accessed at the press of a button.

Development
Initial development
Throughout 2011 and 2012, several hints had been dropped of a potential sequel to Alan Wake. These hints include when "Alan Wake 2" was shown on the Artist Althea Suarez Gata's CV, only for it to be removed on the very same day. Whilst Alan Wake's American Nightmare (though the name was unknown at the time) was revealed not long after this hiccup, fans had been trying to find more evidence of a direct sequel. In Alan Wake's American Nightmare, the credits to the game also then indicated that "Alan Wake's journey through the night will continue".

Also in 2012, Sam Lake tweeted a link to a "Blogspot" called "This House of Dreams." At first, the site seemed like a mere blog for someone refurbishing a house, but one such blog talks about a dream the blogger had about a man "wearing a funny jacket with old-fashioned elbow patches" and that he wanted "to turn all the lights on." This tweet came just days before E3 2012, a gaming expo that reveals and shows brand new content of upcoming releases. People also found that the domain "alanwake2.com" was also reserved by Remedy Entertainment.

At the Xbox Event on May 21, 2013, Remedy revealed Quantum Break, which would be an exclusive to the newest Xbox console at the time, Xbox One. On February 2016, it was confirmed that it would also come to PC. Fans were disappointed that Alan Wake 2 wasn't revealed, but some still supported Remedy in their new franchise. A day after the Quantum Break announcement, Sam Lake took to YouTube to talk to the fans about why Alan Wake 2 wasn't announced. He revealed that the time just wasn't right yet, but mentioned he had not given up on the franchise.

In April 2015, Remedy announced that Alan Wake 2 had previously gone into the early stage of development shortly after Alan Wake was released, where a video of prototype demo was also released. While in the stage of showing this demo to publishers, Remedy went into conversations with Microsoft and the project was put on hold indefinitely while Quantum Break went into development. The sequel would have introduced new features, many of which were used in Alan Wake's American Nightmare. When asked about the possibility of an Alan Wake sequel being released in the future, Sam Lake replied, "It's hard to guess," but that he would "love to do that".

Remedy Connected Universe
Easter eggs in Remedy's 2019 game Control revealed that the game shared the same universe as Alan Wake. Two typewritten pages found within the game (and which were said to have been written by Alan Wake himself) heavily imply that almost ten years had passed since Alan's experience in Bright Falls, and that it was not an isolated event, but rather what the Federal Bureau of Control classifies as an "Altered World Event" (AWE). In this way, Control revealed additional information about the events involving the Dark Presence, especially given the nature of its own primary enemy, the Hiss.

Furthermore, the second DLC for Control, AWE, was released in August 2020. While the letters can simply stand for "Altered World Event," they also resemble Alan's own name. In addition to this, the top half of the cover art depicted a flashlight-wielding person in a dark forest, while the bottom half depicted a second figure surrounded by red, which figures prominently with the Hiss in Control.

In an interview given on May 14, 2020 with VG24/7, Sam Lake commented on this, explaining, "Through AWE you’ll learn more about the Bureau’s involvement, research, and interest in Alan Wake and the events that took place 10 years ago,” Lake said. “We’re really happy to give fans of the original game a bit more of Alan Wake-related content."[1] This suggested a deeper connection, possibly even a future crossover, between the events of Control and Alan Wake.

The plot of AWE confirmed this, tying up some loose ends from the previous Alan Wake entries while also setting up details which would come in a sequel work. In the ending of AWE, an alarm sounds in the Federal Bureau of Control that another AWE appears to be happening again in Bright Falls. This, along with Alan's narration, seemed to indicate Remedy's next game could be a follow up to Alan Wake.

Official development
In March 2020, Remedy signed a deal with Epic Games to publish two single-player games under Epic's new publishing initiative. The games were said to be part of "the same franchise". In March 2021, Remedy CEO Tero Virtala confirmed that they were indeed working on two unannounced project with Epic Games that are part of the same franchise, one smaller scale and one AAA in size. In April 2021, GamesBeat reporter Jeff Grubb told viewers that "I've heard that Remedy is going to be making Alan Wake 2," as part of the Remedy-Epic deal. Grubb went on to say that the game "should kind of be the follow-up that fans of that series want," but that there's little extra information and no word on an official announcement.

On the 7 September 2021, Alan Wake Remastered was revealed by Sam Lake, of which some people believed to have been the smaller project mentioned in March 2021, and the other AAA from the same franchise was to be Alan Wake 2. With the reveal of Alan Wake Remastered, which indicated Remedy are trying to generate interest in the franchise, a sequel was looking more and more likely.

At The Game Awards 2021, Alan Wake 2 was officially announced for 2023 and would be Remedy's first survival-horror video game. Like Quantum Break and Control, it was announced that Alan Wake 2 would use the Northlight engine and be a third-person game. On a later interview with IGN, Sam Lake revealed that the game would have a Mature 17+ age rating.

On May 24, 2023, Sony hosted a PlayStation Showcase livestream, in which a gameplay trailer for Alan Wake 2 was revealed, with a release date of October 17, 2023. It was revealed that players would control two protagonists within their own campaigns, Alan Wake himself and a new protagonist, Saga Anderson. At Summer Game Fest on June 8, 2023, Sam Lake shared further information on the ways Alan and Saga's campaigns would be connected to each other. Additionally, more gameplay and combat mechanics were shown.

On August 17, 2023, the game was delayed by 10 days to October 27, 2023 to make way for various other games also releasing in October. At Gamescom 2023, Alan Wake's side of the game in the Dark Place was focused on in a new trailer, which was later followed by a lengthy Alan-centric gameplay featured behind closed doors.

Reception
Alan Wake 2 received near universal acclaim from video game critics. Itr received five nominations at the 2023 Golden Joystick Awards and won the Critic's Choice Award. It was nominated for eight awards at The Game Awards 2023, and won for Best Game Direction, Best Narrative, and Best Art Direction.

The game went on to win more awards in Finland and around the world.

Trivia
Ilkka Villi and Matthew Porretta both reprise their role as Alan Wake in the sequel. James McCaffrey reprises his role as Alex Casey, who he previously voiced in the manuscript pages of The Sudden Stop.
Brett Madden, who played Alice Wake in the first game, sadly passed away in September 2020. She was memorialized in the credits of the game. Alice was recast in the sequel, now played by Christina Cole.
While the first game was an action-adventure game that implemented horror elements, Alan Wake 2 is a full-blown survival-horror game.
Unlike the first game that was published by Microsoft Studios, the sequel is published by Epic Games Publishing.
The game was initially a digital-only release due to various shifts towards a digital-only market. This was also done to keep the price of the game down at launch. However despite initially saying there were no plans for a physical release, in June 2024 along with a trailer and release date announcement of the first DLC it was revealed that a physical version would be released that October, a year after the digital release. Both a physical version of the digital deluxe version (inclusive of the DLC) and a limited run collector's edition were announced.
The second entry in Remedy's Max Payne series, Max Payne 2: The Fall of Max Payne, also had two playable protagonists (Max Payne and Mona Sax).

## Document 18
**Source**: https://www.polygon.com/23691206/best-fantasy-books-sci-fi-2023

The best sci-fi and fantasy books of 2023
It’s been a stellar year in speculative fiction

By Nicole Clark, Sadie Gennis, and Polygon Staff  Updated Dec 8, 2023, 10:00am EST  34 Comments / 34 New
If you buy something from a Polygon link, Vox Media may earn a commission. See our ethics statement.

It’s been another banner year for science fiction and fantasy books. Many of our favorites once again blur the line between sci-fi and fantasy, but this year was a particular standout for books blurring the line between SFF and other genres. This includes everything from historical fiction — both speculative histories and Westerns — to fable retellings to intergenerational sagas in translation.

Though we seem to have crested the wave of pandemic novels, that sense of dread and discoloration has lingered, written into novels of new forms. There’s a preponderance of post-post-apocalyptic science fiction unpacking lofty ideas like sentience and humanity, often set on different planets or among the stars. It has also been a standout year for supernatural horrors and thrillers, particularly ones that mix queer longing with a dose of body horror. Last but not least, it’s been a great year for kissing books set in fantastical worlds.

RELATED

Looking for more recs? Here are our favorite books of 2022
So jump in and take your pick. Whichever direction you head in, it will be sure to grip you — and make you think. This list is in reverse chronological order, so the newest releases are listed first. We updated this list throughout 2023, sometimes retroactively adding in entries that we missed from earlier in the year. We’ve also included our favorite runners-up.

HONORABLE MENTIONS
Emily Wilde’s Encyclopaedia of Faeries by Heather Fawcett, Victory City by Salman Rushdie, The Crane Husband by Kelly Barnhill, The Mimicking of Known Successes by Malka Older, Monstrilio by Gerardo Sámano Córdova, White Cat, Black Dog by Kelly Link, Divine Rivals by Rebecca Ross, Our Hideous Progeny by C.E. McGill, The Cheat Code (Wisdom Revolution #3) by Misba, The Deep Sky by Yume Kitasei, Silver Nitrate by Silvia Moreno-Garcia, Vampires of El Norte by Isabel Cañas, Prophet by Sin Blaché and Helen Macdonald, Terrace Story by Hilary Leichter, Her Radiant Curse by Elizabeth Lim, Starling House by Alix E. Harrow, System Collapse (The Murderbot Diaries #7) by Martha Wells, Dark Heir (Dark Rise #2) by C.S. Pacat

Cover image for Ed Park’s Same Bed Different Dreams, a split image between what looks like Earth and Mars.
Image: Random House
SAME BED DIFFERENT DREAMS BY ED PARK
Same Bed Different Dreams is a remarkable achievement, and not for the faint of heart. Through three storylines, the book creates a kind of speculative history of Korea, with an emphasis on World War II and Japan’s colonial rule and aftermath (and, crucially, the United States’ involvement). One story thread builds out a hefty alternative history of the Korean Provisional Government’s role and reach. Another story thread focuses on a Black Korean War vet who wrote a sci-fi epic series called 2333, which is later adapted into a video game. And yet another story thread has a more futuristic flavor, focusing on a has-been writer who now works for a tech company called GLOAT. These threads periodically intersect — for example, GLOAT ends up owning the rights to 2333, and turns it into a kind of edutainment.

If it sounds like there’s a lot going on, it’s because there is. And it’s made even denser by the author’s Pynchonian sense of humor. Some of its best moments are utterly weird or feel like the writer was smirking — like a character’s dog who can’t stop “archiving” by burying found manuscript pages, the fact that GLOAT employees truly don’t know what the acronym stands for, or the idea that Marilyn Monroe is a member of the Korean Provisional Government. These absurd bits only make it harder to comb apart what’s real and what’s Ed Park’s “alternate history” in sections with realistic-sounding combinations of fact and fiction.

It’s got the same ambitious patchwork as Jennifer Egan’s The Candy House and Namwali Serpell’s The Old Drift. Critics have compared it to everything from David Mitchell’s Cloud Atlas to David Foster Wallace’s Infinite Jest. There’s also, of course, books within the book. It’s a fever dream of a thing, and one I’d heartily recommend, but perhaps with a notebook in hand or some sticky notes to help track the references. (Or perhaps, as I did, just letting the wave of information roll over you, until you’re left with a vast impression and a desire to reread.) —Nicole Clark

Cover image for Kylie Lee Baker’s The Scarlet Alchemist, featuring a woman in a red outfit with a large crown set against a dark skyline.
Image: Inkyard Press
THE SCARLET ALCHEMIST (THE SCARLET ALCHEMIST #1) BY KYLIE LEE BAKER
Do not go into The Scarlet Alchemist expecting typical YA fare. What Kylie Lee Baker delivers is a story of visceral brutality, interlaced with elements of Chinese history and thoughtful meditations on family, race, and belonging. It’s a book that can turn your stomach as easily as it can break your heart.

Set in an alternate Tang dynasty, the novel follows Zilan, a profoundly talented young alchemist who travels to the capital in hopes of landing a coveted position in the royal service. But being a poor, half Scotian girl means the odds are stacked inordinately high against her in the imperial service exams — and that’s before her skills with the illegal art of resurrection catch the prince’s attention and pull her into a dangerous political game. While the premise seems familiar (underdog competes in trials, falls into star-crossed romance), Baker’s skills with immersive world-building, knotty characters, and genuinely gruesome horror make The Scarlet Alchemist a dazzling and singular tale that left me rushing to read her back catalog. —Sadie Gennis

Cover image of C Pam Zhang’s Land of Milk and Honey, featuring rollicking hills of white, blue, and yellow.
Image: Riverhead
LAND OF MILK AND HONEY BY C PAM ZHANG
After I read How Much of These Hills is Gold in 2020, C Pam Zhang became an instant must-read author in my household. Land of Milk and Honey is entirely unlike her debut — where her debut’s language was sparse and pointed, this book is florid and indulgent — though similar in the extent to which it transported me somewhere entirely new, and more than a little threatening.

In Land of Milk and Honey the climate apocalypse has rendered fresh produce, at scale, a thing of the past — which is to say a provision of the extremely rich. The protagonist, listless and hungry, applies for a job as a private chef for a mysterious family in the Italian Alps (those who live around it call it “​​la terra di latte e miele”). While there, she unravels the family’s true intentions, while making them delicious meals from rare ingredients.

Zhang sensuously describes all pleasures of the tongue, moving from descriptions of lapping of culinary delicacies to the folds of the flesh. Food feels hyperreal, with an emphasis on the texture and taste of every ingredient — and sometimes the cruelty of that ingredient’s procurement. The same can be said of its scenes depicting queer intimacy; that texture and taste take precedent, and the cruelties of human emotion, too. Even after I finished, I was hungry for more. —N. Clark

Cover image for Megan Kamalei Kakimoto’s Every Drop is a Man’s Nightmare, featuring a red and yellow flower against a painted backdrop.
Image: Bloomsbury
EVERY DROP IS A MAN’S NIGHTMARE BY MEGAN KAMALEI KAKIMOTO
This short story collection initially caught my attention with its cover, which depicts a woman springing up from the center of a corpse flower, like a stalk standing against the wind. Each story weaves together Hawaiian mythology and the everyday lives of the Hawaiian and mixed-race Japanese women who live there.

These stories range from fabulism to science fiction, all speculative fiction in their own way. In one story, a woman’s encounter with a wild pig ends up foreshadowing a complicated pregnancy later in her life. In another story, a Brazilian waxing company allows people to pay for hairless skin by giving up personality traits. In another story, the narrator falls for a woman who lives with her family — in one of numerous queer stories in the collection — but has to cope with that woman’s decision to return to “what remains of Kaua’i” and join their protests.

The author’s own words, published in The Guardian, sum it up best: “There is a mythical idealisation of the islands of Hawaii as paradise, peace in the tropics; some even call it a modern utopia. Yet this flattening of Hawaii to a postcard image divests our homeland of its culture and colour, reducing us to a place and history that is easily digestible. But we are not easily digestible, and our stories are not meant to be easy for you.” —N. Clark

Cover image for Shelley Parker-Chan’s He Who Drowned the World, a painted image of ships on a yellow sea, with the moon looming over them.
Image: Tor
HE WHO DROWNED THE WORLD (THE RADIANT EMPEROR #2) BY SHELLEY PARKER-CHAN
An alternate history of the founding of the Ming dynasty, He Who Drowned the World shifts between four tragically ambitious figures willing to pay any price to materialize their destiny, whether that’s revenge on the empire or crowning themselves the ruler of it. They pursue these goals with unshakeable inertia, doing endlessly cruel and sadistic actions with only the occasional doubts as to whether happiness could be possible if they chose a different path.

This is a relentlessly brutal sequel, and there’s a hopelessness that weighs heavy throughout the book. But Parker-Chan’s penetrating ability to bring empathy and nuance into even the darkest corners of humanity sparks an undeniable connection with these characters, whose self-destructive natures would otherwise be too hard to bear witness to. He Who Drowned the World is a dark and difficult read, yet Parker-Chan’s prose is so brilliant, her character work so complex, that I still found myself sad to leave this world behind. —SG

Cover image for M.A. Carricks’s Labyrinth’s Heart, featuring a mask-wearing figure with purple wings sprouting out of the top of the mask.
Image: Orbit
LABYRINTH’S HEART (ROOK & ROSE #3) BY M.A. CARRICK
One of my favorite fantasy series of the past five years, Rook & Rose is an intricately layered trilogy where there are so many secrets, schemes, and conspiracies that at times it’s admittedly difficult to keep track of them all. Because of that, there were a lot of loose ends to tie up in the anticipated conclusion, Labyrinth’s Heart. (Ren alone was juggling four different identities at the novel’s start.) So imagine my surprise when I discovered M.A. Carrick not only managed to leave no question unanswered by the series’ end, but wrapped up even the most complicated storylines in big, bright bows.

There are elements of Labyrinth’s Heart that feel like they were precisely crafted to cater to fans, but here’s the thing: I don’t really care. Carrick created such a lush world populated by lovable characters, an interesting magic system, and a lived-in cultural history that I was just happy to be back in Nadežra after a two-year wait. While things may have been tied up a bit too neatly for my usual tastes, that didn’t stop me from whipping through pages and smiling the whole way through. Sometimes it’s nice to simply soak in a happy ending rather than bathe in the bittersweet. —SG

Cover art for Kiersten White’s Mister Magic, which features a melting television against a pink background.
Image: Del Rey Books
MISTER MAGIC BY KIERSTEN WHITE
The latest fantasy-with-an-irresistible-pop-premise from the author of Hide, Mister Magic revolves around a children’s TV show no viewer can forget … or prove it ever existed in the first place. There are no official records of it, no YouTube videos or merchandise or passed-around VHS tapes, and any discussion of it on the internet rapidly disappears. But the people who remember seeing it are convinced the special effects were remarkably vivid and realistic. They agree the central concept is unnerving: a creepy magician-figure leading a group of children in imagination-games aimed at teaching some decidedly non-standard lessons about embracing conformity and meekness. And they’re all sure that something horrible happened while they were watching, though they can’t agree on what.

A reunion between five of the former child cast members, taking place 30 years after the show ended, slowly unravels its mysteries, which are even weirder than the description above suggests. Mister Magic is a startling dark fantasy with a lot of foreboding, foreshadowing, and eerie twists. At heart, though, it’s also an incisive story about the kinds of people who revel in control over other people’s lives, and about what an act of rebellion imagination can be. —Tasha Robinson

Cover image for Rebekah Bergman’s The Museum of Human History, featuring a painted image of a naked figure with a red cloud over the top of their head.
Image: Tin House
THE MUSEUM OF HUMAN HISTORY BY REBEKAH BERGMAN
A poetic reflection on memory, loss, and connection, The Museum of Human History is a stunning debut reminiscent of the work of Emily St. John Mandel. Slipping backward and forward in time, this introspective mosaic weaves between an identical twin whose sister fell asleep at age 8 and has never aged in the 25 years since, a museum director who questions his place within the family legacy, a widower who lost his most cherished memories as a result of an anti-aging treatment, and others equally struggling with the passage of time. There is a lyrical detachment in Bergman’s prose that leaves you feeling like you’re watching events unfold through a pane of thick glass, never fully able to connect with the characters, yet you remain helplessly transfixed by the haunting cycle they’re caught in. It’s an incredibly melancholy book, but the kind of aching sadness you’re happy to sink into. —SG

Cover image for Sara Hashem’s The Jasad Heir, featuring what looks like statues of a snake,, a bull, and a griffin.
Image: Orbit Books
THE JASAD HEIR (THE SCORCHED THRONE #1) BY SARA HASHEM
“Arin of Nizahl was maddeningly elegant. I wanted to cut him open and compare our bones to understand why his gave him grace and mine gave me back pain.” This was the line that absolutely sold me on The Jasad Heir, an irresistible enemies-to-lovers fantasy that reminded me why I’ll never quit this genre.

Headstrong Sylvia is the presumed dead heir of Jasad, a kingdom that was destroyed by the neighboring Nizahl and saw its citizens’ innate magic outlawed. Sylvia managed to carve out a relatively normal life for herself as a chemist’s apprentice, but everything falls apart after she accidentally reveals her magic to the heir of Nizahl. Using her life as leverage, the calculating Arin strikes a deal with Sylvia to help him capture a group of Jasadi rebels and act as his champion in a series of deadly trials. It’s a familiar setup, but one impeccably done by Hashem, who delivers sharp political intrigue, sparkling banter, and touching friendships on top of Sylvia and Arin’s simmering romance. —SG

Cover image for Kritika H. Rao’s The Surviving Sky, featuring a floating island overgrowing with buildings and plant life, above a stormy planet.
Image: Titan Books
THE SURVIVING SKY (THE RAGES TRILOGY #1) BY KRITIKA H. RAO
After I finished The Surviving Sky, I wouldn’t shut up about it and tried (not always successfully) to get everyone I know to read it. So let me try once more, and maybe with less yelling this time:

With the planet’s surface made unlivable by catastrophic storms, the remains of humanity survive on floating cities constructed of and powered by plants that only a select group of people, known as architects, can control. An archeologist without the ability to traject plants, Ahilya has dedicated her life to finding a way to unshackle humanity’s survival from the architects’ powers and return to the surface. It’s not hard to see why this mission causes friction in her marriage to Iravan, one of the most powerful architects in their city, and one with an arrogance to match his revered status. Though estranged, Ahilya and Iravan come together to help clear his name after he’s accused of pushing his powers dangerously far, an accusation, which if proved true, carries dire consequences for the architect.

But the deeper they look into trajection and its risks, the more Ahilya and Iravan realize they don’t actually know much about where their people – and their powers – came from. And as the floating cities begin to sink toward the earthrages below, the race to save their civilization may also be the end of society as it stands, as Ahilya and Iravan uncover long-buried truths that previous generations worked hard to keep hidden.

So did I do it? Did I convince you to read this Hindu philosophy-inspired debut with some of the most inventive world-building and one of the most complex romances I’ve read in years? Please say yes. You’ll be doing us both a favor. —SG

Cover image for Alexander Darwin’s The Combat Codes, which features a metallic dragon against a black background.
Image: Orbit
THE COMBAT CODES AND GRIEVAR’S BLOOD (THE COMBAT CODES SAGA #1-2) BY ALEXANDER DARWIN
In the world of The Combat Codes, war no longer exists as it used to. Neither does justice — both concepts have been replaced by proxies who fight on behalf of nations or individuals, solving disputes with their fists.

Alexander Darwin’s debut novel effectively builds a world around this core concept, bringing it to life with compelling characters and locations (including a classic “magical school for gifted youngsters” situation). The Combat Codes follows Cego, a young abandoned boy skilled at fighting, and Murray, a washed-up former fighter now tasked with scouting the next generation of combatants, whose discovery of Cego changes his entire world.

Darwin is also a Brazilian jiu-jitsu practitioner and teacher, and uses that experience in the books’ excellent fight sequences. His evocative and visceral descriptions not only deliver excitement and suspense in this underdog story; they build your understanding of the characters through how they fight. The Combat Codes and its equally fun sequel, Grievar’s Blood, which adds new exciting characters and points-of-view, are the first two parts of a planned trilogy, and I can’t wait for the conclusion next year. —Pete Volk

Cover image for Katie Williams’ My Murder, showing a woman’s face peering outside of red vertical lines.
Image: Riverhead Books
MY MURDER BY KATIE WILLIAMS
Fans of Sarah Gailey’s The Echo Wife won’t want to miss My Murder, which shares some key elements and themes with Gailey’s novel while also taking them in a unique direction. In a near-future with only a few light sci-fi elements, Lou has been resurrected along with a handful of other women murdered by a single serial killer. The politics of resurrection in her world are complicated, and few people qualify. That leaves her and her fellow victims (whose therapy circle recalls Grady Hendrix’s The Final Girl Support Group) a bit at sea as they try to come to terms with their deaths, which none of them can recall, and their new lives as celebrities for all the wrong reasons.

Like The Echo Wife, My Murder ends up thoughtfully exploring issues around women subjected to violent men — not just the personal and internal response, but the society that shapes that violence, and responds to it in ways that raise endless questions. The victims all respond to their deaths differently, questioning their culpability and the possible failures that might have made them targets, and navigating their families’ unpredictable responses to their revival. There’s one big mystery at the heart of My Murder, and a whole lot of abrupt and compelling surprises. But at the core, it’s a sci-fi twist on the survivor story, letting some very different people explore what it means to be victimized, and how to reclaim the lives that have been abruptly handed back to them. —TR

Cover image for Ann Leckie’s Translation State, a minimalist drawing with red, orange, and green, a silhouette of a person, and circular lines.
Image: Orbit
TRANSLATION STATE BY ANN LECKIE
Set in the same universe as Leckie’s Imperial Radch trilogy, Translation State follows Enae, who leaves hir long-standing isolation for what was supposed to be an interstellar goose chase. After hir demanding grandmaman dies, Enae is given a diplomat title and assigned to investigate a missing Presgr translator no one expects to be found (but that the government still wants the goodwill for pretending to look for). Only, Enae doesn’t just pretend to look; sie discovers sie has quite the knack for investigating the 200-year-old cold case.

This is how hir path crosses that of Reet, an adopted maintenance worker whose mysterious origins and unsettling impulses might be explained by being the child of the fugitive translator, if you ask Enae, or the last descendant of a lost sovereign line, if you ask one particularly zealous diaspora social group. Rounding out the POV characters is Qven, a young Presgr terrified of their species’ ritual of merging with an elder, a rite of passage which will see Qven’s selfhood entirely dissolved. Enae, Reet, and Qven’s explorations of their own identities wind up having interplanetary consequences, but it’s the way Leckie gives weight to the small moments, both personal and shared, that make this book sing.

Though I’m sure there are layers that only those familiar with the Imperial Radch trilogy will notice and appreciate, the standalone Translation State and its rich exploration of self-identification and personhood serve as a fantastic introduction to Leckie’s world. So don’t hesitate to jump into Translation State if you’re – like me – new to Radch and simply drawn to a thrilling mystery where the most intimate emotions can fuel a universal upheaval. —SG

Cover image for Rita Chang-Eppig’s Deep as the Sky, Red as the Sea, with facial features set against a crashing wave.
Image: Bloomsbury Publishing
DEEP AS THE SKY, RED AS THE SEA BY RITA CHANG-EPPIG
I still remember standing in my local bookstore, struck by the cover of this book, and reading the summary. It had me at “Chinese pirate queen.”

In Deep as the Sky, Red as the Sea, Chang-Eppig writes a historical fantasy about Shek Yeung, a fearsome Chinese pirate who must navigate her fleet after the death of her powerful husband. She marries her late husband’s second-in-command, with the promise of bearing an heir, in order to retain power over the fleet — and stay a major player as the Chinese Emperor seeks to rid the waters of piracy.

The book isn’t paced like a thriller, so don’t make the mistake of assuming so when you start it. It’s equal parts historical exposition, strategy, and warfare — and it especially excels in its characterization of a complicated woman forced to make difficult decisions and sacrifices in order to protect her power. Fantasy can put its villains and heroes on pedestals, but Deep as the Sky, Red as the Sea never errs in its very human portrayal of Shek Yeung, and how deftly she must play this game of political chess for survival. I was riveted. —N. Clark

Cover art for Emma Törzs’ Ink Blood Sister Scribe, featuring a dripping pen growing out of the bottom of a tree against a purple background.
Image: William Morrow
INK BLOOD SISTER SCRIBE BY EMMA TÖRZS
There’s nothing cozier than a magical book about the magic of books — though this tale bends a little darker, and tells a story about witchcraft and complicated family dynamics. In Ink Blood Sister Scribe, two estranged sisters come together to solve the mystery of their family, and prevent further tragedies. In this world, blood can be concocted into ink — wielded by scribes for the creation of books with arcane powers — though the creation of such books drains a scribe’s health. When others read these books, they create magic; willing flowers to bloom, or making magical carpets that can fly in the air.

Ink Blood Sister Scribe is the perfect sister thriller to read in one sitting. It doesn’t reinvent the wheel, but it doesn’t need to — it simply delivers on a wonderfully entertaining premise. —N. Clark

Cover art for Martha Wells’ Witch King, featuring a person running across the cover while wearing a cloak and dress fitting for a fantasy setting.
Image: Tor
WITCH KING BY MARTHA WELLS
In an era where a lot of fantasy fans value quick or cozy reads, Martha Wells’ Witch King feels like a gauntlet thrown at readers’ feet. It’s a complex, meaty fantasy that opens well into what a more linear book would consider the third act, as Kai, the witch king of the title, is exhumed from a watery grave and starts exploring who betrayed him and trapped him there. Readers have to learn everything about Kai’s world as his story unfolds in multiple intertwined timelines. That includes figuring out what a “witch king” is, unwrapping the layers of what Kai actually is and why it matters. It also means being introduced to a wide variety of allies and enemies while alternately flashing back to how he met them, and slowly coming to understand the dense political machinations that shaped all their lives in the past and present.

As with Wells’ Murderbot books and her Books of the Raksura series in particular, part of the draw here is a powerful, skilled protagonist whose biggest struggles are often internal. Kai has a lot of intense emotional responses to the world, but lacks the tools to understand what to do with those feelings, or who to trust with them. Wells packs Witch King with a lot of audacious, expansive world-building for a standalone novel (albeit one that could easily invite sequels or prequels), but what makes Witch King an enjoyable read instead of a frustrating one is the way all the book’s complications and surprises are filtered through Kai’s vivid inner life, giving readers something to hold onto as they’re untangling the puzzlebox aspects of this cleverly structured novel. —TR

Cover image for Justin Lee Anderson’s The Lost War, featuring five figures walking through white grass after emerging from a dark green forest. Three of the figures wear green cloaks, while two wear white.
Image: Orbit
THE LOST WAR (THE EIDYN SAGA #1) BY JUSTIN LEE ANDERSON
Originally self-published in 2019, The Lost War is a traditional fantasy adventure that follows a rag-tag group of strangers on a mission across a war-torn country, fighting monsters and uncovering mysteries along the way. Despite the strong buzz leading up to the novel’s expanded publication by Orbit this year, I found myself hesitant to pick it up since it seemed so similar to many books I’ve read before. But while it’s true The Lost War doesn’t rewrite the genre – it’s filled with well-worn tropes and classic adventurer archetypes – Anderson’s skillful execution left me completely charmed. There is a real Dungeons and Dragons feel to The Lost War, and though the characters are familiar (the honorable paladin, the hard-drinking haunted soldier), Anderson does a fantastic job developing unique dynamics between the party members that vault the book beyond the sum of its parts. And it all builds up to a massive twist at the end that completely upends your understanding of what you’ve read and any previous expectations for where the second book will go. The delightfully unexpected ending once again has the fantasy community buzzing ahead of Anderson’s next release – only this time I’m right there with them. —SG

Cover image for Moniquill Blackgoose’s To Shape a Dragon’s Breath, a red cover with flowers and a dragon’s head/mask on it.
Image: Del Rey
TO SHAPE A DRAGON’S BREATH (NAMPESHIWEISIT #1) BY MONIQUILL BLACKGOOSE
To Shape a Dragon’s Breath’s description hooked me immediately: It’s got dragons, a magic school, and a strong teenage main character. Moniquill Blackgoose has taken several different fantasy tropes and created a fantasy novel that’s unlike anything I’ve read; To Shape a Dragon’s Breath is set in an evolving steampunk world as Anglish settlers push the Indigenous Masquapaug people out of their land and onto a remote island. Dragons had long been important cultural touchstones to the Indigenous people, but colonization has, too, pushed them away. To Shape a Dragon’s Breath begins as 15-year-old Anequs finds a dragon egg — the first to be spotted in the area in generations. Anequs is named a Nampeshiweisit, or a dragon rider, as the community helps raise and hatch the dragon’s egg.

The colonizing nation quickly finds out and forces Anequs and her dragon into the Anglish dragon school; if she resists, the dragon will be eliminated. To Shape a Dragon’s Breath is about the growing relationship between her and her dragon Kasaqua, but also about her resistance to the Anglish traditions relating to dragons. The Anglish treat dragons as something to be conquered — they use them as tools and weapons, whereas the Indigenous people have historically partnered with dragons for a relationship built on both tradition and respect.

That partnership means Anequs now has the power to take on colonialism and racism in a new way. Where To Shape a Dragon’s Breath really shines is in that growing relationship between Anequs and Kasaqua; the partnership — and power for both that comes with it — is in stark contrast to the Anglish ways. Bonus: To Shape a Dragon’s Breath has well-written, complex bisexual and neurodivergent characters, too. —Nicole Carpenter

Cover image for Melvin Burgess’s Loki, a black cover with a black snake wrapped around gold letters with the title.
Image: Pegasus
LOKI BY MELVIN BURGESS
Melvin Burgess has spent a career writing confrontationally frank children’s literature like Junk, his 1990s book about heroin-addicted teenagers. His first adult book, published at age 69, is a blistering, transgressive, and hugely entertaining reframing of the Norse myths, as told by the most unreliable narrator imaginable: Loki himself, the god of tricks, inventions, and political intrigue. But what does reliable mean, anyway, in the mutable world of myth? Burgess paints Loki (or rather, has him paint himself, as he addresses the reader directly in first person) as an eternal outsider, shaking his head sagely at the follies of the gods, and challenging their might-is-right order. But of course, that’s what he’d want us to think. Burgess’ best trick, though, is the way he rolls together the deeply weird, muddy, shape-shifting mystery of the tales themselves with a bracing modernity in characterization and language, somehow without one clashing with the other. In doing so he brings the wild, ancient power of the Norse myths to vivid life. —Oli Welsh

Cover image for Nana Kwame Adjei-Brenyah’s Chain-Gang All-Stars, featuring a scythe chopping through the words with a bright yellow background.
Image: Pantheon Books
CHAIN-GANG ALL-STARS BY NANA KWAME ADJEI-BRENYAH
In Chain-Gang All-Stars, prison inmates fight to the death in a series of gladiatorial matches — and all of it is televised to a hungry audience. It’s a program called CAPE, the Criminal Action Penal Entertainment, which promises freedom to inmates who survive three years of its brutality. The average life expectancy for anyone who enters is three months. Within this system, Loretta Thurwar and Hammara Stacker (called Hurricane Staxxx by her fans) emerge as two frontrunners.

This National Book Award finalist takes on the viciousness of the carceral system, with more than a bit of The Hunger Games’ DNA sprinkled in. “Hard action” fans salivate over matches, a self-obsessed announcer resents the fact that contestants don’t offer more banter, and the women who top the leaderboards become sex symbols in pop culture. But where other fight-to-the-death dystopias — among the greats, like Battle Royale or Lord of the Flies — spin a more fantastical yarn, Chain-Gang All-Stars is aimed right at the heart of the all-too-real cruelties of our existing for-profit penal system.

Early in the book, Thurwar kills a 16-year-old boy in a gladiator match. Fans in the stands lament not the death of the boy, but the idea that the fight wasn’t entertaining because it wasn’t a fair matchup. In a footnote, Adjei-Brenyah writes of George Stinney Jr., a 14-year-old Black boy who was convicted for murder and executed in 1944. Chain-Gang All-Stars also illustrates the ways in which imprisonment is simply “slavery by another name,” showing all manner of menial labor the contestants are forced to perform. In 2022, the ACLU reported that inmates made between 13 and 52 cents an hour, and sometimes nothing.

Critics have said this book is an “act of protest” but that it doesn’t “straightforwardly preach,” or that it’s more entertaining than “an attempt to convince its readers of the case for prison abolition has any right to be.” I understand why you’d want to say this book is “fun” despite an abolitionist message, especially in a political climate where radical writing is often appreciated only as a teaching tool. But I think that kind of delineation undercuts Adjei-Brenyah’s talent as a novelist, and his skill in heightening the real as a form of storytelling. I’d call it thrilling, over calling it fun. And the fact that it is thrilling is inextricable from its openly abolitionist values — it’s the very knowledge of real life that Adjei-Brenyah wields to craft suspense. —N. Clark

Cover image for Rebecca Yarros’ Fourth Wing, which features a circle image behind black text, with clouds and some flying creatures.
Image: Entangled
FOURTH WING BY REBECCA YARROS
This action-packed, fantasy romance feels like a grown up version of all of my favorite young adult books. It’s got all of the fun nostalgic tropes — a magical school, deadly trials, dragon riding, and a love triangle between the main character, a golden retriever love interest, and a misunderstood emo rival — but it’s also extremely horny, as all fun fantasy romance must be.

Violet Sorrengail is thrown into a series of trials in order to prove whether she can be a dragon rider. There are a few problems with this: she trained as a scribe, never thought she’d be thrust into danger, and she also must deal with Xaden Riorson, her sworn enemy (wink). She also manages a joint condition, which leaves her in chronic pain — a fact the book handles gracefully. In one of my favorite climactic moments of the book, Violet is given a mobility device to help her with her trials; those close to her remind her that it doesn’t diminish her power, but is a tool like any other, and one that allows her to flourish. I’m thrilled to read the next installment, when it comes out in November. —N. Clark

Cover art for Adrian Tchaikovsky’s Lords of Uncreation, which shows a spaceship approaching what looks like a space battle next to a planet, with exploding orbs in space and a lot of spaceships in the distance.
Image: Orbit
LORDS OF UNCREATION (THE FINAL ARCHITECTURE #3) BY ADRIAN TCHAIKOVSKY
Reading the Final Architecture series, I had to accept long ago that I would never fully grasp the nuances of some of its central concepts, even if I understood them on an instinctual level.

This acceptance set me up well for Lords of Uncreation, which revolves around concepts that even the characters find impossible to understand, and whose minds may literally break if they try to. Like looking directly into the sun, confronting the blurred space between the real and unreal (as well as the eldritch terrors that lurk within) poses a grave threat to those doing so head-on – at least to anyone other than weary intermediary Idris Tellemier, whose risk is merely reduced rather than eliminated. But the characters Adrian Tchaikovsky has populated this world with are so grounded, so emotionally rich, and so vibrant that the details of the brain-bending threats lurking within unspace become secondary to their impact on the lives of and relationships between the Vulture God’s crew.

This is not to say that Tchaikovsky does not deliver an incredibly satisfying conclusion to the mysteries of unspace (he does!). But what I’ll remember most is how he crafted the perfect emotional resolution to this intellectually intricate tale that left me in tears and has stayed with me since. —SG

Lead art for Justin Cronin’s The Ferryman, which pictures a cloudy sky over the horizon, as a single sail boat sits on the water.
Image: Ballantine Books
THE FERRYMAN BY JUSTIN CRONIN
Proctor Bennett is a ferryman, whose duty is to guide unhappy citizens from the utopian Propersa to the Nursery, where they retire their old selves before returning in younger bodies with no memories of their former lives. But when Proctor is assigned to retire his own father, the troubling encounter sends him careening off the path of conformity. He begins questioning prescribed truths and confronting the darker side of Prospera, which runs off the work of a disenfranchised support staff whose discontent is building towards a revolution that pulls Proctor into its orbit.

Though this premise may feel familiar, The Ferryman is anything but. This tightly-wound, atmospheric thriller weaves together layers of knotted mystery with Proctor’s haunting POV as he grapples with his relationship to grief, happiness, family, and identity. It’s a sharply complex mystery with a cinematic quality to it. Throughout reading, I couldn’t help but fan-cast who would star in a Christopher Nolan adaptation of it. But even if you aren’t an Inception fan, it’ll be easy to become immersed in The Ferryman’s distinct dystopian world. —SG

Cover image for Emily Tesh’s Some Desperate Glory, featuring a woman walking confidently in front of a wall opening to reveal a planetary body.
Image: Tor
SOME DESPERATE GLORY BY EMILY TESH
Around September, as the pile of unpainted plastic miniatures here in my home office began to get particularly deep, I suddenly ran out of Warhammer 40,000 Black Library audiobooks by Games Workshop that I was the least bit interested in listening to. That’s when I stumbled upon Some Desperate Glory by Emily Tesh. Billed as a space opera told from the perspective of one of humanity’s last genetically engineered super soldiers, I fell for the premise hook, line, and sinker. Then, about 50 pages in, I let it sucker-punch me right in the gut.

With Some Desperate Glory, Tesh has envisioned a deeply affecting reality where the children of a subjugated, war-torn race slowly come to realize that they have been lied to — manipulated into an amoral war of vengeance without end. Tesh shows incredible restraint throughout, reeling out a thick and binding thread of painful realizations from deep within the main character, Kyr. After grappling with my personal love for the grim darkness of the far future for quite a few years now, this book helped me come to terms with how much I despise those tropes even as I find myself drawn toward them time and time again.

Some Desperate Glory is, in my opinion, required reading for anyone who has ever painted a Space Marine in earnest – and a new fixture in the canon of queer science fiction. —Charlie Hall

Cover image for Jade Song’s Chlorine, featuring a large fin in the ocean waves.
Image: William Morrow & Company
CHLORINE BY JADE SONG
I think I have been waiting my whole life for this book — for someone to write adolescence like the body horror it is, with all of the cultural specificity of being a Chinese American girl, simply bursting at the seams with sapphic longing. Chlorine stars Ren Yu, a swimmer who believes that she is a mermaid. But she is tethered to land by her human ambition: By the parents who constantly push her to achieve, and by a swim coach who pays inappropriate attention to her — pushing her to swim faster times, while also making her feel uncomfortable in her skin.

Ren’s steadfast belief in being a mermaid feels both like a flight of fancy, and increasingly like a means of dissociating from the horrors of everyday life. Being a young girl is hard enough without having to contend with the high expectations of parents, the predation of adult men, and the casual racism of peers. Jade Song’s writing is gruesomely lyrical, contrasting the sublime with the deeply disturbing. There were several points where this book almost made me throw up, and I mean that as a high compliment. —N. Clark

A Black woman stands alone in a field, her face covered by shadow, in the cover art for Lone Women by Victor LaValle.
Image: One World
LONE WOMEN BY VICTOR LAVALLE
Adelaide Henry is traveling to Montana, where she plans on making a new life as a homesteader — leaving the flames of her California home, and the bodies of her parents, behind. But she has a heavy weight to carry. She lugs an enormous steam trunk wherever she goes; whenever the trunk opens, people around her die. In 1915, Montana is in the middle of a homestead boom, and though Adelaide aims to make a new start, not everyone is welcoming to a Black woman traveling alone.

Victor LaValle mixes horror and fantasy in this expertly paced tale. It’s satisfyingly bloody, while making incisive commentary on the price of being an outsider. The Western genre has long fixated on the white imagination, perhaps occasionally making space for the early struggle of the suffragettes. But LaValle’s vision of history emphasizes just how powerful white women are in upholding the interests of their white husbands, and how far these women will go to protect the societal structures that put them in proximity to power. Lone Women also examines how shame, and the family unit, ultimately uphold these unspoken rules — ostracizing those who might otherwise find community support.

This book was so good that I am now reading my way through every interview LaValle has given on the Lone Women press circuit, too, and then reading every book he references. What a gift! —N. Clark

Cover image of Nathan Ballingrud’s The Strange, depicting a diner on Mars.
Image: Gallery/Saga Press
THE STRANGE BY NATHAN BALLINGRUD
Nathan Ballingrud’s debut novel was added to my TBR pile after seeing it marketed as a blend of Ray Bradbury’s The Martian Chronicles and Charles Portis’ True Grit. I’m always dubious about marketing comparisons, but was thrilled when The Strange delivered on this high promise.

In an alternate history where humanity colonized Mars in the early 1900s, the red planet has lost all communication with Earth, leaving the fate of 14-year-old Annabelle Crisp’s mother unknown. When a thief steals Annabelle’s sole voice recording of her mom, she and her beloved Kitchen Engine, Watson, set off into the desert to retrieve what’s hers and see justice served. The longer Annabelle’s adventure goes on, the more she loses perspective and drifts away from righteousness in dogged pursuit of her own selfish desires. Struggling to comprehend that the world can’t be divided into binaries like right or wrong and black or white, Annabelle converts her fear into anger, lashing out and harming those around her, including those providing aid.

Annabelle can be vengeful and cruel, and though I often disagreed with her choices, Ballingrud makes it impossible not to understand and empathize with her. Annabelle Crisp isn’t a hero and she isn’t a villain, but she is an outstanding protagonist in a wonderfully original sci-fi tale. —SG

Cover image for Moses Ose Utomi’s The Lies of the Ajungo, featuring a figure walking upside down on mounds of sand as a castle lurks in front.
Image: Tor
THE LIES OF THE AJUNGO (THE FOREVER DESERT #1) BY MOSES OSE UTOMI
In his debut novella, Moses Ose Utomi wields his precise prose to tell a dark, visceral fable about a young boy from the City of Lies, a metropolis reliant on the brutal Ajungo Empire for their supply of water. But the cost of this trade is high: At 13, every child of the City of Lies has their tongue cut out and sent to the Ajungo.

Even with this gruesome tithe, the Ajungo send barely enough water for the population to survive, and far from what they’d need to do so comfortably, let alone thrive. Shortly before his thirteenth birthday, the brave Tutu sets out on a dangerous journey to save his mother and the city by finding their own water supply. As Tutu explores the outside world for the first time, his perception of truth and history is challenged, and he comes to understand how the decisions and deceptions of those in power rewrite the past and shape the future to uphold those with privilege and foster compliance in those who don’t. —SG

Cover image for Edward Ashton’s Antimatter Blues, A Mickey7 Novel. It features an astronaut from behind on a rocky planet, looking out at another planet in the distance.
Image: St. Martin’s Press
ANTIMATTER BLUES BY EDWARD ASHTON
Edward Ashton’s sequel to Mickey 7, the 2022 novel Parasite director Bong Joon-ho is adapting as a movie starring Robert Pattinson, takes up two years after the first book left off, with “Expendable”-status planetary colonist Mickey still on the outs with the leadership of his struggling colony after a gutsy bluff he made to ensure his own survival. The sixth clone of the original Mickey, who accepted life as a disposable body for suicide missions in exchange for a ticket to space, Mickey 7 has walked off that job. His ongoing draw on the colony’s resources is only tolerated because he’s exaggerated his diplomatic connections with the local aliens. Then the base commander orders him to do something impossible, or the entire colony will die.

Antimatter Blues is knottier than the first book in the series, with more to take in about the ethics of survival and humanity’s predisposition toward xenophobia and selfish, self-serving behavior. It sure isn’t a pleasant book to read: A lot of Mickey’s co-colonists are bigots, most of them are indifferent to anyone else’s suffering, and at times, the book reads as though Earth deliberately sent all the worst people into space, the better to be free of them. Even Mickey himself is, at absolute minimum, generally more focused on his own safety and comfort than on the horrific results of some of his choices. But as soon as he’s placed in what seems like an unsurvivable situation, that dynamic leads to high drama, and Antimatter Blues becomes a breathless book rocketing to a surprising conclusion. Prepare to feel sorry for various alien races who have to deal with icky humanity. —TR

Cover image for Samantha Shannon’s A Day of Fallen Night, a colorful image with a a dragon swirling around it
Image: Bloomsbury
A DAY OF FALLEN NIGHT (THE ROOTS OF CHAOS #0) BY SAMANTHA SHANNON
Samantha Shannon’s A Day of Fallen Night is her second book in the Roots of Chaos series, but a prequel to The Priory of the Orange Tree. Like The Priory of the Orange Tree, A Day of Fallen Night is an epic, far-flung fantasy novel set in a world of magic and dragons. A Day of Fallen Night is set hundreds of years before The Priory of the Orange Tree, and follows several of the original book’s ancestors as the world fears the return of an evil wyrm, the Nameless One. You don’t have to have read The Priory of the Orange Tree to enjoy A Day of Fallen Night; in fact, it’s likely a good place to start if you’ve been interested in reading Shannon’s original, massive fantasy book. Of course, this is a slow-burn 800-page book that precedes another 800-page book, so it’s definitely a time investment regardless of the path.

Though A Day of Fallen Night deals with a world-shaping, cataclysmic threat and widespread political machinations, the book is rooted within four characters from around the book’s world: Sabran, Glorian, Dumai, and Tunuva Melim. The stories of these characters intertwine as their regional beliefs tied to wyrms and dragons conflict, muddying up the necessary collaboration in fighting off the looming threat. In between all that catastrophe, Shannon gives the women of the book rich stories of personal relationships, sacrifice, and conflicting feelings. Motherhood and bodily autonomy are also strong themes throughout the book; both Sabran and Glorian (mother and daughter) have their bodily autonomy tied to the fate of their region.

It’s not easy to describe A Day of Fallen Night in a short blurb — it does so many things and goes so many places. Shannon’s created a series that has the scale of The Lord of the Rings, wrapped up in a world of queer, female power. The Roots of Chaos, as a whole, is one of my favorite fantasy series ever. —N. Carpenter

Cover image for Mariana Enriquez’s Our Share of Night, featuring a red hand with long yellow fingernails.
Image: Hogarth Press
OUR SHARE OF NIGHT BY MARIANA ENRÍQUEZ
This literary tome defies categorization, so I’ll paint a scene instead: A father (Juan) whisks his son (Gaspar) away on a trip. Juan is mercurial; at turns terrifying and violent, at turns bewilderingly tender, nearly infinite in love. But he is a closed book. And if you think you’ve seen his hands elongate, spindly fingers yielding to piercing claws — well no, you didn’t.

Slow, dreadful, and razor-sharp, Our Share of Night charts a family’s desperate attempt at escaping the clutches of a death cult in Argentina. Its members seek the secrets of immortality, and many are willing to pay any price to obtain it. Set in 1981, the novel’s supernatural terrors intertwine with those of the Dirty War, the authoritarian violence offering cover for the cult to operate uninhibited.

I will read anything Mariana Enríquez writes next, it’s an absolute joy to experience her work. —N. Clark

Cover image for Annalee Newitz’s The Terraformers, which features a futuristic cityscape with lush greenery.
Image: Tor Books
THE TERRAFORMERS BY ANNALEE NEWITZ
The Terraformers concerns itself with one question: As a species evolves, what behaviors stick around? Set more than 50,000 years in the future (yes, you read that number right), The Terraformers details the process of terraforming and developing a privatized planet into a tourism joint for the super rich. Technology has advanced in barely fathomable ways, allowing, for instance, the extension of human-level intelligence to animals and robots. But some aspects of society might seem familiar: Real estate developers who jack up rent with no warning? Local governments that abhor public transit? That every video call still has one person who can’t get the camera to work?

Equal parts prescient and absurd, The Terraformers splits its story over three novellas, each 700 years apart. One of those stars a sentient train who teams up with an investigative journalist ... who also happens to be a cat ... who’s also trying to prove this ostensibly privatized planet is in fact public land. Written by a leading science journalist of our era (author Annalee Newitz is the founder of io9 and has written for basically every major science publication under our sun), The Terraformers is unexpectedly one of the most accurate representations of the journalistic process I’ve ever read. And it all culminates in an undeniable stance: That capitalistic power must still be held in check by the truth. Even 50,000 years in the future, a free press is among society’s most essential facets. The more things change... —Ari Notis

The cover image of Adrian Tchaikovsky’s Children of Memory, which depicts a spaceship approaching a large orange planet.
Image: Orbit
CHILDREN OF MEMORY (CHILDREN OF TIME #3) BY ADRIAN TCHAIKOVSKY
Adrian Tchaikovsky’s highly anticipated third book in the Children of Time trilogy once again delves into some of science fiction’s headiest topics. There are parallels to earlier installments — Tchaikovsky once again uses another hyper-intelligent animal species to examine the idea of what being “alive” really means. But he also takes readers somewhere completely and utterly new, outside the scope of the previous titles, and incredibly difficult to describe without spoiling the premise entirely.

All I can say is hold on for the ride. This is an author who dives head first into Asimov-esque ideas, and who is willing to take the plot in fanciful directions. I still can’t believe that I have recommended a book about sentient spider colonies to so many friends, but here we are. This finale is worth your time. —N. Clark

## Document 19
**Source**: https://arxiv.org/pdf/2404.10981

A Survey on Retrieval-Augmented Text Generation for Large Language
Models
Yizheng Huang
York University
hyz@yorku.ca
Jimmy X. Huang
York University
jhuang@yorku.ca
Abstract
Retrieval-Augmented Generation (RAG)
merges retrieval methods with deep learning
advancements to address the static limitations
of large language models (LLMs) by enabling
the dynamic integration of up-to-date external
information. This methodology, focusing
primarily on the text domain, provides a
cost-effective solution to the generation of
plausible but incorrect responses by LLMs,
thereby enhancing the accuracy and reliability
of their outputs through the use of real-world
data. As RAG grows in complexity and
incorporates multiple concepts that can
influence its performance, this paper organizes
the RAG paradigm into four categories:
pre-retrieval, retrieval, post-retrieval, and
generation, offering a detailed perspective
from the retrieval viewpoint. It outlines
RAG’s evolution and discusses the field’s
progression through the analysis of significant
studies. Additionally, the paper introduces
evaluation methods for RAG, addressing
the challenges faced and proposing future
research directions. By offering an organized
framework and categorization, the study
aims to consolidate existing research on
RAG, clarify its technological underpinnings,
and highlight its potential to broaden the
adaptability and applications of LLMs.
1 Introduction
The advent of ChatGPT has significantly impacted
both academia and industry due to its interactive
capabilities and widespread application, establishing itself as a leading artificial intelligence tool
(Laskar et al., 2023; Jahan et al., 2023; Huang
and Huang, 2024). At the core of ChatGPT is the
large language model (LLM) GPT-4, as detailed by
(OpenAI et al., 2023), which has seen numerous
enhancements to its predecessors, showcasing exceptional abilities in a variety of Natural Language
Processing (NLP) tasks (Laskar et al., 2020). Despite these advancements, the adoption of LLMs
Figure 1: An example of RAG benefits ChatGPT resolves questions that cannot be answered beyond the
scope of the training data and generates correct results.
has highlighted several critical issues primarily due
to their reliance on extensive datasets. This reliance
restricts their ability to incorporate new information post-training, leading to three primary challenges. First, the focus on broad and general data
to maximize accessibility and applicability results
in subpar performance in specialized areas. Second,
the rapid creation of online data, combined with the
significant resources required for data annotation
and model training, hinders LLMs’ ability to stay
updated. Third, LLMs are susceptible to generating convincing yet inaccurate responses, known as
“hallucinations”, which can mislead users.
Addressing these challenges is crucial for LLMs
to be effectively utilized across various domains. A
promising solution is the integration of RetrievalAugmented Generation (RAG) technology, which
supplements models by fetching external data in
response to queries, thus ensuring more accurate
and current outputs. Figure 1 illustrates how RAG
can enable ChatGPT to provide precise answers
beyond its initial training data.
Since its introduction by Lewis et al. (Lewis
et al., 2020b) in 2020, RAG technology has undergone significant advancements, particularly influenced by ChatGPT’s success. However, there is a
noticeable gap in the literature regarding a thorough
analysis of RAG’s mechanisms and the progress
made by subsequent studies. Furthermore, the field
is characterized by diverse research focuses and the
use of ambiguous terminology for similar methods,
leading to confusion. This paper aims to clarify these aspects by offering a structured overview of
RAG, categorizing various methods, and delivering an in-depth understanding of this research area.
This survey will primarily focus on textual applications of RAG, reflecting the current emphasis of
research efforts in this area.
RAG combines retrieval methods and advanced
deep learning to address two main questions: effectively retrieving relevant information and generating accurate responses. The workflow of RAG
is outlined in Section 2, categorizing the methodologies into pre-retrieval, retrieval, post-retrieval,
and generation phases. These sections, from 3 to
6, provide an in-depth analysis of the technologies
within these phases. Section 7 offers summaries of
the reviewed studies, along with the retrievers and
generators utilized. Section 8 details the evaluation
methodologies for RAG. Section 9 explores future
research directions, concentrating on text-based
studies and extending to image and multimodal
data considerations. The conclusion is presented in
Section 10.
The contributions of this paper are threefold:
This paper offers a comprehensive framework for
understanding the RAG domain, identifying areas
for improvement and challenges for future research.
It provides a detailed analysis of RAG’s core technologies, examining their strengths in addressing
retrieval and generation. Additionally, it introduces
the evaluation methods used in RAG research, highlighting current challenges and suggesting promising directions for future studies.
2 RAG Framework
The hallucinations are largely attributed to LLMs’
inability to access up-to-date information. This
limitation stems from the models’ reliance on their
training datasets. RAG proposes a solution to this
issue by supplementing the LLM’s training data
with current information from external sources
through a retrieval model, thereby enabling the generation of accurate responses. RAG presents a more
cost-effective alternative to the extensive training
and fine-tuning processes typically required for
LLMs. It allows for the dynamic incorporation
of fresh information via traditional retrieval methods or pre-trained LMs, without the need to directly
integrate this new data into the LLM. This feature
makes RAG both flexible and scalable, facilitating its application across different LLMs for various purposes. The information retrieved through
RAG is derived from real-world data, authored
by humans, which not only simplifies the generation process but also increases the reliability of
the generated responses. Figure 2 represents the
unified RAG framework with basic workflow and
paradigm.
Research by Khandelwal et al. (Khandelwal
et al., 2020) demonstrates that accessing relevant
information from the training dataset itself can significantly improve LLM performance, highlighting the effectiveness of RAG. Over time, RAG
has evolved from a means of providing supplementary information to enabling multiple interactions
between the retrieval and generation components.
This involves conducting several rounds of retrieval
to refine the accuracy of the information retrieved
and iteratively improve the quality of the generated output. Platforms such as LangChain1
and
LlamaIndex2 have modularized the RAG approach,
enhancing its adaptability and expanding its range
of applications. Despite these platforms employing
diverse methodologies to tackle different aspects of
RAG—from multiple search iterations to iterative
generation—they maintain adherence to the fundamental RAG workflow. This consistency is crucial
for understanding their operation and pinpointing
opportunities for further development.
2.1 Basic RAG Workflow
The foundational workflow of RAG begins with the
creation of an index comprising external sources.
This index serves as the basis for retrieving relevant
information through a retriever model based on a
specific query. The final step involves a generator
model, which combines the retrieved information
with the query to produce the desired output.
2.1.1 Indexing
Efficient retrieval begins with comprehensive indexing, where data preparation is key. This stage
involves text normalization processes such as tokenization, stemming, and the removal of stop words
to enhance the text’s suitability for indexing (Manning et al., 2008). Text segments are then organized
into sentences or paragraphs to facilitate more focused searches, allowing for the pinpointing of segments containing pertinent keywords. The integration of deep learning has revolutionized indexing
through the use of pretrained LMs for generating
semantic vector representations of texts. These vectors are stored, enabling rapid and precise retrieval from extensive data collections, significantly
enhancing retrieval efficiency.
2.1.2 Retrieval
While traditional retrieval methods, such as the
BM25 algorithm (Hancock-Beaulieu et al., 1996),
focus on term frequency and presence for document
ranking, they often overlook the semantic information of queries. Current strategies leverage pretrained LMs like BERT (Devlin et al., 2019), which
capture the semantic essence of queries more effectively. These models improve search accuracy by
considering synonyms and the structure of phrases,
thereby refining document ranking through the detection of semantic similarities. This is typically
achieved by measuring vector distances between
documents and queries, combining traditional retrieval metrics with semantic understanding to yield
search results that are both relevant and aligned
with user intent.
2.1.3 Generation
The generation phase is tasked with producing text
that is both relevant to the query and reflective of
the information found in the retrieved documents.
The usual method involves concatenating the query
with the retrieved information, which is then fed
into an LLM for text generation (Li et al., 2022).
Although ensuring the generated text’s alignment
and accuracy with the retrieved content presents
challenges, it is also essential to strike a balance between adhering closely to the source material and
infusing the output with creativity. The generated
text should accurately convey the information from
the retrieved documents and align with the query’s
intent, while also offering the flexibility to introduce new insights or perspectives not explicitly
contained within the retrieved data.
2.2 RAG Paradigm
The RAG paradigm organizes research within
the domain, offering a straightforward yet robust
framework to enhance LLM performance. Central to RAG is its search mechanism, crucial for
generating high-quality outcomes. Therefore, this
paradigm is structured into four main phases from
a retrieval perspective: pre-retrieval, retrieval, postretrieval, and generation. Both single-hop and
multi-hop retrieval approaches, encompassing iterative retrieve-generate cycles, follow this four-phase
structure. Figure 3 is the taxonomy tree of RAG’s
core techniques.
2.2.1 Pre-Retrieval
The pre-retrieval phase of retrieval-augmented generation lays the foundation for successful data and
query preparation, ensuring efficient information
retrieval. This phase includes essential tasks to
prepare for effective data access.
Indexing The process starts with indexing, which
establishes an organized system to enable fast and
accurate retrieval of information. The specificity
of indexing depends on the task and data type.
For example, sentence-level indexing is beneficial
for question-answering systems to precisely locate
answers, while document-level indexing is more
appropriate for summarizing documents to understand their main concepts and ideas.
Query Manipulation After indexing, query manipulation is performed to adjust user queries for
a better match with the indexed data. This involves query reformulation (Jansen et al., 2009;
Yu et al., 2020), which rewrites the query to align
more closely with the user’s intention; query expansion (Huang et al., 2013), which extends the query
to capture more relevant results through synonyms
or related terms; and query normalization, which
resolves differences in spelling or terminology for
consistent query matching.
Data Modification Data modification is also critical in enhancing retrieval efficiency. This step
includes preprocessing techniques like removing
irrelevant or redundant information to improve the
quality of results and enriching the data with additional information such as metadata to boost the
relevance and diversity of the retrieved content
(Bevilacqua et al., 2022a).
2.2.2 Retrieval
Search & Ranking The retrieval stage is the
combination of search and ranking. It focuses on
selecting and prioritizing documents from a dataset
to enhance the quality of the generation model’s
outputs. This stage employs search algorithms to
navigate through the indexed data, finding documents that match a user’s query. After identifying
relevant documents, the process of initially ranking
these documents starts to sort them according to
their relevance to the query.
2.2.3 Post-Retrieval
The post-retrieval phase serves to refine the initially
retrieved documents to improve the quality of text
generation. This phase consists of re-ranking and
filtering, each aimed at optimizing the document
selection for the final generation task.
Re-Ranking In the re-ranking step, the documents previously retrieved are reassessed, scored,
and reorganized. The objective is to more accurately highlight the documents most relevant to
the query and diminish the importance of the less
relevant ones. This step involves incorporating additional metrics and external knowledge sources
to enhance precision. In this context, pre-trained
models with superior accuracy but lower efficiency
can be effectively employed due to the limited set
of candidate documents available (Huang and Hu,
2009).
Filtering Filtering aims to remove documents
that fail to meet specified quality or relevance
standards. This can be done through several approaches, such as establishing a minimum relevance score threshold to exclude documents below
a certain relevance level. Furthermore, the use of
feedback from users or prior relevance evaluations
assists in adjusting the filtering process, guaranteeing that only the most relevant documents are
retained for text generation (Khattab and Zaharia,
2020; Huang and Huang, 2023).
2.2.4 Generation
The generation stage is a crucial component of the
RAG process, responsible for leveraging retrieved
information to enhance the quality of the generated
response. This stage encompasses several sub-steps
aimed at producing content that is readable, engaging, and informative.
Enhancing At the heart of the generation phase
is the enhancement step, where the objective is
to merge the retrieved information with the user’s
query to create a coherent and relevant response.
This includes the process of elaboration, adding
extra details to the retrieved content to enrich it. Efforts are focused on improving the output’s quality
by increasing its clarity, coherence, and stylistic
appeal through methods such as rephrasing and
restructuring. Information from various sources
is combined to offer a comprehensive perspective,
and verification is conducted to ensure the accuracy
and relevance of the content.
Customization Customization is an optional
step, involving the adjustment of content to align
with the user’s specific preferences or the context
of the request. This tailoring includes adapting the
content to meet the needs of the target audience or
the format in which it will be presented and condensing the information to succinctly convey the
essence of the content. The process also entails
creating summaries or abstracts that emphasize the
key points or arguments, ensuring the output is both
informative and concise.
3 Pre-Retrieval
3.1 Indexing
The integration of the k-nearest neighbor (kNN)
algorithm with pre-trained neural LMs, as demonstrated in kNN-LMs (Khandelwal et al., 2020), represents significant progress in language modeling. This method employs a datastore created from collections of texts, enabling the dynamic retrieval of
contextually relevant examples to improve perplexity without necessitating additional training.
Known for its efficiency, FAISS (Johnson et al.,
2021) has been adopted in many studies for indexing purposes (Khandelwal et al., 2020; Lewis et al.,
2020b; Khattab et al., 2022). Some research integrates enhancements like the Hierarchical Navigable Small World (HNSW) approximation (Malkov
and Yashunin, 2020) to achieve faster retrieval
(Lewis et al., 2020b). In addition, alternative tools
like utilizing the Bing API 3
for indexing based
on actual user search histories as outlined in Webgpt (Nakano et al., 2021), illustrate the variety of
indexing techniques under investigation.
Furthermore, MEMWALKER (Chen et al.,
2023a) introduces an innovative method to overcome the limitations of context window size in
LLMs by creating a memory tree from the input
text. This tree is formed by initially segmenting
the text into smaller pieces and then summarizing these segments into a hierarchical structure of
summary nodes, facilitating efficient indexing and
management of large volumes of information.
3.2 Query Manipulation
Studies such as FiD (Izacard and Grave, 2021),
COK(Li et al., 2023), and Query2doc (Wang et al.,
2023a) emphasize the significance of creating new
queries or refining existing ones to achieve more
3
https://www.microsoft.com/en-us/bing/apis/bing-websearch-api
pertinent retrieval results. These research efforts
highlight the necessity of efficiently gathering evidence from multiple passages and tailoring queries
to suit various knowledge sources, whether structured or unstructured. Techniques ranging from the
creation of pseudo-documents to enhance queries
have shown to bolster retrieval performance across
diverse information retrieval datasets.
Further exploration into query manipulation has
been conducted by Step-Back (Zheng et al., 2023)
and PROMPTAGATOR (Dai et al., 2023), which
focus on abstracting high-level concepts or utilizing LLMs for prompt-based query generation.
These strategies strive to better align queries with
the retrieval system’s functionality by rephrasing
tasks into more generalized versions or crafting
task-specific queries from limited examples. Such
methodologies enhance the consistency between
queries and indexed data, facilitating the retrieval
of more pertinent and insightful information.
Moreover, KnowledGPT (Wang et al., 2023b)
and Rewrite-Retrieve-Read (Ma et al., 2023) introduce approaches for query manipulation through
“program of thought” prompting and innovative
query rewriting techniques. KnowledGPT innovates by generating code to interface with knowledge bases, converting user queries into structured
search commands. In contrast, Rewrite-RetrieveRead utilizes a trainable compact LM for query
reformulation, adjusting them to more effectively
reflect the user’s intent and context.
Lastly, FLARE (Jiang et al., 2023) presents a
strategy based on confidence for query formulation, which focuses on crafting queries that precisely
reflect the information needs. This method incorporates the use of generated sentences or fragments
thereof as a foundation for search queries. By opting to directly use sentences, obscuring tokens of
low confidence, or formulating explicit questions,
this approach aims to boost the efficiency of the
retrieval process, ensuring that the retrieved information faithfully satisfies the requirements of the
generation process.
3.3 Data Modification
RA-DIT (Lin et al., 2023b) and RECITE (Sun et al.,
2023) emphasize enhancements through internal
data modifications. RA-DIT distinguishes between
fine-tuning datasets for LLMs and retrievers, aiming to bolster the LLM’s contextual comprehension
and the retriever’s ability to align with queries. RECITE, on the other hand, utilizes passage hints and
synthetic question-passage pairs to increase the
variety and relevance of its generated recitations
and responses. This approach seeks to broaden the
model’s knowledge base and improve its response
accuracy.
UPRISE (Cheng et al., 2023a) and GENREAD
(Yu et al., 2023a) target the refinement of external
data. UPRISE converts raw task data into a structured format and refines the selection of prompts
to enhance retrieval outcomes. In contrast, the
Clustering-Based Prompts method employed by
GENREAD generates documents from questions
and clusters them to eliminate irrelevant data, enriching the input with varied contextual insights.
This technique aims to improve the performance of
the generative model by providing it with a richer
set of information.
Furthermore, KnowledGPT (Wang et al., 2023b)
is dedicated to augmenting raw text data with structured, semantically rich information through entity
linking. This enrichment process not only structures the data more cohesively and makes it more
amenable to queries but also boosts the model’s
retrieval efficiency. It leverages precise, linked
knowledge to enhance the model’s understanding and its ability to generate relevant responses,
thereby improving its overall performance.
4 Retrieval
4.1 Search & Ranking
Atlas (Izacard et al., 2023) investigates few-shot
learning approaches, including Attention Distillation and Perplexity Distillation, to steer the retriever toward retrieving more relevant documents.
IRCOT (Trivedi et al., 2023) integrates retrieval
with reasoning to improve the effectiveness of retrieval. SURGE (Kang et al., 2023) employs a
subgraph retriever to extract relevant subgraphs
from a knowledge graph, while AAR (Yu et al.,
2023b) modifies search preferences to help LLMs
in fetching pertinent documents.
PRCA (Yang et al., 2023a) focuses on employing domain-specific abstractive summarization to
extract relevant and context-rich information from
documents, using a supervised learning strategy
to prioritize content crucial for accurate query responses. Meanwhile, MEMWALKER (Chen et al.,
2023a) leverages an internal search and ranking
mechanism in the constructed memory tree to identify pertinent information for long-context question
answering. Additionally, the Confidence-based Active Retrieval approach of FLARE (Jiang et al.,
2023) dynamically triggers information retrieval
based on the confidence levels of generated sentences, utilizing the insight that low-confidence
tokens signal a need for external knowledge.
5 Post-Retrieval
5.1 Re-Ranking
Re2G (Glass et al., 2022) introduces a sequencepair classification approach for re-ranking, utilizing a BERT transformer to simultaneously analyze
the query and passage. This interaction model, employing cross-attention between sequences, offers a
contrast to the representation model typically used
in initial retrieval phases. PROMPTAGATOR (Dai
et al., 2023) also employs a cross-attention model
for re-scoring. Its “Lift Yourself Up” strategy iteratively selects the best candidate from a pool for
further generation rounds, progressively improving
content quality via self-generated content.
Re-ranking is also a significant focus of InContext RALM (Ram et al., 2023). Two approaches to reranking are explored: zero-shot
reranking using language models and predictive
reranking through trained models. This step is
aimed at refining the selection of documents based
on their expected utility for improving language
model performance. ITER-RETGEN (Shao et al.,
2023), in particular, leverages knowledge distillation from the re-ranker to the dense retriever, finetuning retrieval efforts based on relevance signals
from LLM outputs. This optimization of the retrieval model aims to more accurately capture query
nuances, thereby improving document selection.
DKS-RAC (Huang et al., 2023) presents the
Dense Knowledge Similarity (DKS) for aligning
the knowledge between answers and retrieved passages at the sequence level. This approach is categorized under re-ranking due to its direct impact on
passage selection based on knowledge similarity,
refining the match between queries and documents.
FiD-light (Hofstätter et al., 2023) introduces a
listwise autoregressive re-ranking method that employs source pointers to optimize the ranking order.
This method maintains a link between the generated text and source passages, enabling a more
structured generation process. By incorporating
textual citations within the model’s output as pointers to relevant information sources, this approach
facilitates an organized retrieval and generation
process, enhancing the overall coherence and relevance of the generated content.
5.2 Filtering
COK (Li et al., 2023) presents the Progressive Rationale Correction technique, aimed at iteratively
refining rationales with retrieved knowledge. This
method constitutes a continuous optimization process, significantly enhancing the relevance and
quality of information used in content generation.
Self-RAG (Asai et al., 2023) introduces a selfreflection mechanism to efficiently filter out irrelevant content. By employing critique tokens, this
approach evaluates the relevance, supportiveness,
and utility of retrieved passages, ensuring the integration of only high-quality information into the
content generation process.
Additionally, FiD-TF (Berchansky et al., 2023)
and RECOMP (Xu et al., 2023) are dedicated to the
removal of irrelevant or redundant tokens and information from retrieved documents. FiD-TF employs
a dynamic mechanism to identify and eliminate unnecessary tokens, enhancing the efficiency of information processing. RECOMP, on the other hand,
compresses documents into concise summaries, focusing on selecting only the most pertinent content
for the generation process. These methods streamline the content generation workflow by ensuring
that only relevant and supportive information is
utilized, thereby improving the overall quality and
relevance of the generated content.
6 Generation
6.1 Enhancing
DSP (Khattab et al., 2022) introduces a framework
designed to generate multiple retrieval queries to
summarize and answer questions, drawing upon information aggregated from various passages. This
framework employs CombSUM (Fox and Shaw,
1994) to calculate a cumulative probability score
for passages across different retrieval lists, facilitating the compilation of a comprehensive response
from multiple sources.
PRCA (Yang et al., 2023a) outlines a RewardDriven Stage, wherein the distilled context is refined based on feedback from the generator. Utilizing reinforcement learning, this stage adjusts
the parameters of PRCA according to the rewards
received for providing relevant context. The objective is to fine-tune the extracted context to meet
the specific requirements of the generator, thereby
optimizing the generation process.
REPLUG (Shi et al., 2023) proposes a method
for prepending retrieved documents to the input
context before the final prediction by the black-box
LM. It introduces an ensemble strategy to encode
retrieved documents in parallel, overcoming the
limitations of LM context length and enhancing
accuracy through the allocation of increased computational resources. This approach improves the
generation process by ensuring that the LM has
access to a broader range of relevant information.
RECITE (Sun et al., 2023) implements a selfconsistency technique, which involves generating
multiple recitations independently and employing
a plurality/majority vote system to determine the
most appropriate answer. This method is designed
to increase the reliability and accuracy of the answers, thereby improving the quality and credibility
of the output.
6.2 Customization
The PKG framework, introduced by (Luo et al.,
2023), represents an approach to customizing the
output of LMs. By generating background knowledge internally using a pre-trained model, PKG
eliminates the need for traditional external retrieval
processes. This method directly integrates domainor task-specific knowledge into the generation step,
significantly enhancing the LM’s capacity to produce responses that are specifically tailored to the
given context or requirements.
Self-RAG (Asai et al., 2023) offers a strategy that incorporates reflection tokens within a customizable decoding algorithm. This technique permits dynamic adjustment of the model’s retrieval
and generation behaviors based on the specific task,
facilitating more versatile response generation. Depending on the requirements, this approach can be
tuned for accuracy or creativity, providing flexibility in generating outputs that meet diverse needs.
SURGE (Kang et al., 2023) achieves customization through the application of graph-text contrastive learning. This method ensures that the
generated dialogue responses are in tight alignment
with the knowledge contained in the retrieved subgraph, yielding responses that are specific, relevant,
and deeply rooted in the dialogue context. By maintaining consistency between the retrieved knowledge and the generated text, SURGE is capable
of producing outputs that precisely reflect the detailed knowledge of the subgraph, enhancing the
relevance and specificity of the responses.
7 Comparisons of RAG
7.1 The Comprehensive Summary of RAG
Table 1 presents a detailed analysis of the RAG
studies discussed in this paper. The analysis shows
that the majority of these studies have utilized external data sources to enrich the content of LLMs.
A preference for multiple-hop over single-hop retrieval was noted, indicating that iterative search
rounds generally yield superior results. In other
words, most methods employ dense retrieval to secure higher quality candidate documents. Compared to modifying datasets in the pre-retrieval
stage, more studies focus on manipulating the query
to improve retrieval performance. Additionally,
there is a significant emphasis on optimizing the
retrieval phase, highlighting its crucial role in the
research. However, there seems to be a scarcity
of studies concentrating on customization in the
generation stage, pointing to this as a potential area
for future exploration. Overall, while the goal of
RAG is to enhance the response quality of LLMs,
greater efforts have been directed towards improving retrieval aspects.
7.2 Retriever and Generator
In RAG, the retriever and the generator are the
primary components. Table 2 summarizes the retrievers and generators used in the studies discussed
in this paper. It is clear from the table that while
most generators utilize advanced language models,
a significant number of retrievers still employ the
traditional BM25 due to its efficiency. The method
of retrieval is a crucial aspect in RAG, highlighting the importance of exploring ways to enhance
retrieval performance without compromising efficiency. Similarly, not many studies have adopted
powerful LLMs such as LLaMA2, GPT-3.5, or
GPT-4 as their generators. LLMs like T5 remain
popular, yet fundamental models like BERT and
Transformers are rarely used in 2023. Compared
to generators, it is evident that not many IR-based
LLMs are used in retrievers, indicating a promising
direction for developing such models in the future.
8 Evaluation in RAG
To understand the effectiveness of LMs in generating more accurate, relevant, and robust responses
by leveraging external knowledge, the evaluation
of RAG systems has become a significant research
area. With the popularity of dialogue-based interactions, recent works have been focused on assessing
the performance of RAG models on such downstream tasks using established metrics like Exact
Match (EM) and F1 scores. Furthermore, a wide
array of datasets has been utilized for this purpose,
including TriviaQA (Joshi et al., 2017), HotpotQA
(Yang et al., 2018), FEVER (Thorne et al., 2018),
Natural Questions (Kwiatkowski et al., 2019), Wizard of Wikipedia (Dinan et al., 2019), and T-REX
(ElSahar et al., 2018).
However, evaluation solely from the perspective of downstream tasks falls short in addressing
the evolving needs of RAG development. Recent
research has introduced various frameworks and
benchmarks that aim to evaluate these systems
across multiple dimensions, including the quality
of the generated text, the relevance of retrieved
documents, and the model’s resilience to misinformation, as shown in Table 3. These evaluations focus on assessing specific capabilities such as noise
robustness, negative prompting, information integration, and counterfactual robustness, highlighting the complex challenges faced by RAG systems
in practical applications. The continuous development of evaluation frameworks and metrics is
crucial for advancing the field, broadening the applicability of RAG systems, and ensuring they meet
the demands of a complex and evolving information landscape.
8.1 Retrieval-based Aspect
In information retrieval, the quality of search results is typically evaluated using standard metrics
such as Mean Average Precision (MAP), Precision,
Reciprocal Rank, and Normalized Discounted Cumulative Gain (NDCG) (Radlinski and Craswell,
2010; Reimers and Gurevych, 2019; Nogueira et al.,
2019). These metrics primarily assess the relevance
of retrieved documents to a given query.
Retrieval-based Metrics in RAG focus on the effectiveness of retrieving relevant information to
support generation tasks. These include Accuracy, which measures the precision of retrieved
documents in providing correct information for answering queries, and Rejection Rate (Chen et al.,
2023b), assessing a system’s ability to decline answering when no relevant information is found.
Additionally, Error Detection Rate (Chen et al.,
2023b) evaluates the model’s capability to identify
and disregard incorrect or misleading information
from retrieved documents. Context Relevance is
another essential metric, assessing the pertinence
of the retrieved documents to the query. It’s vital to
ensure the information used to generate responses
is directly related to the query’s context. Faithfulness (Shahul et al., 2023) measures the accuracy
with which the generated content reflects the information in the retrieved documents, ensuring that
the generation process with no misinformation.
8.2 Generation-based Aspect
Evaluating the quality of text produced by LLMs
involves analyzing their performance on various
downstream tasks using standard metrics. These
metrics assess linguistic quality, coherence, accuracy, and the extent to which the generated text
reflects ground-truth data. Linguistic quality and
coherence are evaluated through metrics such as
BLEU (Papineni et al., 2002), which measures fluency and similarity to human-produced text, and
ROUGE-L (Lin, 2004), which quantifies the overlap with reference summaries to gauge the text’s
capacity to encapsulate main ideas and phrases.
Accuracy and overlap with ground-truth data are
gauged using metrics like EM and F1 Score, which
respectively determine the percentage of answers
that are entirely correct and offer a balanced assessment of precision and recall in retrieving relevant
answers while minimizing inaccuracies.
Beyond these standard metrics, the evaluation
may also incorporate task-specific criteria and
novel metrics tailored to particular applications.
For instance, in dialogue generation, perplexity
and entropy are used to evaluate response diversity and naturalness. Additionally, metrics such as
Misleading Rate and Mistake Reappearance Rate
(Liu et al., 2023) gauge a model’s ability to avoid
misinformation and inaccuracies. Other specialized metrics include Answer Relevance (Shahul
et al., 2023), assessing the precision of responses
to queries; Kendall’s tau (Saad-Falcon et al., 2023),
for evaluating the accuracy of RAG system rankings; Micro-F1 (Saad-Falcon et al., 2023), which
fine-tunes accuracy evaluation in tasks with multiple correct answers; and Prediction Accuracy, directly measuring the alignment of generated answers with expected responses, thereby offering a
direct insight into a system’s effectiveness in generating accurate content.
9 Future Directions
9.1 Retrieval Quality
The integration of RAG into LLMs faces significant
hurdles due to the vast amounts of unreliable information on the internet, including fake news. This
presents a challenge for accurately retrieving useful
knowledge, leading to the unreliable generation of
responses by LLMs. As a result, LLMs may generate content based on incorrect information, undermining their reliability. Recent research efforts
are directed towards enhancing retrieval methods
to improve the efficiency, scalability, and effectiveness of LLMs in generating accurate and reliable
responses.
Differentiable Search Indices (Tay et al., 2022)
and (Bevilacqua et al., 2022b) developed differentiable search indices that integrate the retrieval
process within a Transformer model, enabling direct mapping of text queries to document identifiers.
These approaches offer superior performance and
potential for more efficient and scalable retrieval.
Generative Models for Search GERE (Chen
et al., 2022a) can directly generate document titles
and evidence sentences for fact-verification tasks.
PARADE (Li et al., 2024) is a method for document
reranking that aggregates passage representations
into a unified document relevance score. Both of
them demonstrate significant improvements in retrieval quality over traditional methods.
Fine-tuning Pre-trained Language Models
RankT5 (Zhuang et al., 2023) is a model that finetunes the T5 framework specifically for text ranking. It leverages ranking losses to optimize performance metrics and exhibits promising zero-shot
performance on out-of-domain data.
Noise Power (Cuconasu et al., 2024) provide a
comprehensive analysis of the impact of IR components on RAG systems, revealing that the inclusion
of irrelevant documents can significantly improve
accuracy. It challenges conventional retrieval strategies and underscores the potential for developing
specialized approaches that integrate retrieval with
language generation models.
9.2 Multimodal RAG
The multimodal RAG domain has experienced significant growth, highlighting a pivotal advancement
at the confluence of text and visual comprehension.
The introduction of MuRAG (Chen et al., 2022b)
marked a breakthrough by amalgamating textual
and visual information for language generation, establishing a new standard for multimodal datasets.
This model showcased the efficacy of utilizing a
multimodal memory system to boost the accuracy
in question-answering and reasoning tasks.
After MuRAG, studies such as REVEAL (Hu
et al., 2023) and Re-Imagen (Chen et al., 2023c)
have focused on enhancing visual question answering and text-to-image generation. They achieved
this through the incorporation of dynamic retrieval
mechanisms and the improvement of image fidelity,
respectively. These advancements laid the groundwork for further models by researchers like Sarto
et al. (Sarto et al., 2022) for image captioning,
and Yuan et al. (Yuan et al., 2023) for text-to-audio
generation, broadening the scope of RAG’s application across different modalities and improving the
quality and realism of the generated outputs. Furthermore, Re-ViLM (Yang et al., 2023b) refined
image captioning capabilities through a retrievalaugmented visual language model. By fine-tuning
model parameters and implementing innovative filtering strategies, it has made strides in producing
more precise and contextually appropriate captions.
By tapping into external resources, these models
have provided significant enhancements over traditional benchmarks, highlighting the advantage of
integrating diverse sources of knowledge.
10 Conclusions
In this paper, we have presented a comprehensive framework for understanding the RAG domain, highlighting its significance in enhancing
the capabilities of LLMs. Through a structured
overview of RAG, categorizing various methods,
and an in-depth analysis of its core technologies
and evaluation methods, this study illuminates the
path for future research. It identifies crucial areas
for improvement and outlines potential directions
for advancing RAG applications, especially in textual contexts. This survey aims to elucidate the
core concepts of the RAG field from a retrieval
perspective, and it is intended to facilitate further
exploration and innovation in the accurate retrieval
and generation of information.
11 Limitations
This survey comprehensively examines existing
RAG models, summarizing their core techniques
into four main steps from a retrieval perspective. It
recognizes that some methods may encompass multiple steps and that decoupling these steps could
potentially obscure their intrinsic connections. Nevertheless, the primary objective is to simplify the
complexity of the approach, clearly delineating the
specific problems it addresses. This allows for a
clearer identification of areas ripe for further optimization and improvement. Despite the thorough investigation, the rapid evolution of the field and
page limits mean that certain aspects might not
have been fully analyzed and explored, or recent
developments could have been missed. While the
paper references evaluation methods that can aid
in the development of RAG, it also acknowledges
mature tools like LangChain and LlamaIndex as
useful resources. However, the focus of this survey
is not on detailing the evaluation pipeline or how
these tools are specifically used, but rather on illustrating how evaluation aspects can support the
advancement of RAG. This choice highlights an
area for future work, emphasizing the importance
of methodological clarity and the application of
evaluation tools in refining and enhancing RAG
models.
Acknowledgements
This work was supported by the Natural Sciences
and Engineering Research Council (NSERC) of
Canada and the York Research Chairs (YRC) program.
Acknowledgements
This work was supported by the Natural Sciences
and Engineering Research Council (NSERC) of
Canada and the York Research Chairs (YRC) program.
References
Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, and
Hannaneh Hajishirzi. 2023. Self-RAG: Learning
to Retrieve, Generate, and Critique through SelfReflection. arXiv, abs/2310.11511.
Moshe Berchansky, Peter Izsak, Avi Caciularu, Ido
Dagan, and Moshe Wasserblat. 2023. Optimizing
Retrieval-augmented Reader Models via Token Elimination. In Proceedings of the 2023 Conference on
Empirical Methods in Natural Language Processing,
pages 1506–1524. Association for Computational
Linguistics.
Michele Bevilacqua, Giuseppe Ottaviano, Patrick S. H.
Lewis, Scott Yih, Sebastian Riedel, and Fabio Petroni.
2022a. Autoregressive search engines: Generating
substrings as document identifiers. In Advances in
Neural Information Processing Systems 35: Annual
Conference on Neural Information Processing Systems 2022, NeurIPS 2022, New Orleans, LA, USA,
November 28 - December 9, 2022.
Michele Bevilacqua, Giuseppe Ottaviano, Patrick S. H.
Lewis, Scott Yih, Sebastian Riedel, and Fabio Petroni.
2022b. Autoregressive Search Engines: Generating Substrings as Document Identifiers. In Conference on Neural Information Processing Systems
(NeurIPS).
Sid Black, Gao Leo, Phil Wang, Connor Leahy,
and Stella Biderman. 2021. GPT-Neo: Large
Scale Autoregressive Language Modeling with MeshTensorflow.
Sebastian Borgeaud, Arthur Mensch, Jordan Hoffmann,
Trevor Cai, Eliza Rutherford, Katie Millican, George
van den Driessche, Jean-Baptiste Lespiau, Bogdan
Damoc, Aidan Clark, Diego de Las Casas, Aurelia
Guy, Jacob Menick, Roman Ring, Tom Hennigan,
Saffron Huang, Loren Maggiore, Chris Jones, Albin Cassirer, Andy Brock, Michela Paganini, Geoffrey Irving, Oriol Vinyals, Simon Osindero, Karen
Simonyan, Jack W. Rae, Erich Elsen, and Laurent
Sifre. 2022. Improving Language Models by Retrieving from Trillions of Tokens. In International Conference on Machine Learning (ICML), pages 2206–
2240.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,
Clemens Winter, Christopher Hesse, Mark Chen, Eric
Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess,
Jack Clark, Christopher Berner, Sam McCandlish,
Alec Radford, Ilya Sutskever, and Dario Amodei.
2020. Language Models are Few-Shot Learners. In
Conference on Neural Information Processing Systems (NeurIPS), volume abs/2005.14165.
Howard Chen, Ramakanth Pasunuru, Jason Weston, and
Asli Celikyilmaz. 2023a. Walking Down the Memory
Maze: Beyond Context Limit through Interactive
Reading. arXiv, abs/2310.05029.
Jiangui Chen, Ruqing Zhang, Jiafeng Guo, Yixing Fan,
and Xueqi Cheng. 2022a. Gere: Generative Evidence
Retrieval for Fact Verification. In Proceedings of
the 45th International ACM SIGIR Conference on
Research and Development in Information Retrieval.
ACM.
Jiawei Chen, Hongyu Lin, Xianpei Han, and Le Sun.
2023b. Benchmarking large language models in retrieval-augmented generation. arXiv,
abs/2309.01431.
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming
Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph,
Greg Brockman, and others. 2021. Evaluating
large language models trained on code. arXiv,
abs/2107.03374.
Wenhu Chen, Hexiang Hu, Xi Chen, Pat Verga,
and William Cohen. 2022b. Murag: Multimodal
Retrieval-Augmented Generator for Open Question
Answering over Images and Text. In Proceedings
of the 2022 Conference on Empirical Methods in
Natural Language Processing (EMNLP).
Wenhu Chen, Hexiang Hu, Chitwan Saharia, and
William W. Cohen. 2023c. Re-Imagen: RetrievalAugmented Text-to-Image Generator. In International Conference on Learning Representations
(ICLR).
Zhihong Chen, Feng Jiang, Junying Chen, Tiannan
Wang, Fei Yu, Guiming Chen, Hongbo Zhang, Juhao
Liang, Chen Zhang, Zhiyi Zhang, and others. 2023d.
Phoenix: Democratizing chatgpt across languages.
arXiv, abs/2304.10453.
Daixuan Cheng, Shaohan Huang, Junyu Bi, Yuefeng
Zhan, Jianfeng Liu, Yujing Wang, Hao Sun, Furu
Wei, Weiwei Deng, and Qi Zhang. 2023a. Uprise:
Universal Prompt Retrieval for Improving Zero-Shot
Evaluation. In Proceedings of the 2023 Conference
on Empirical Methods in Natural Language Processing, pages 12318–12337. Association for Computational Linguistics.
Xin Cheng, Di Luo, Xiuying Chen, Lemao Liu,
Dongyan Zhao, and Rui Yan. 2023b. Lift Yourself Up: Retrieval-augmented Text Generation with
Self-Memory. In Thirty-seventh Conference on
Neural Information Processing Systems, volume
abs/2305.02437.
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin,
Maarten Bosma, Gaurav Mishra, Adam Roberts,
Paul Barham, Hyung Won Chung, Charles Sutton,
Sebastian Gehrmann, Parker Schuh, Kensen Shi,
Sasha Tsvyashchenko, Joshua Maynez, Abhishek
Rao, Parker Barnes, Yi Tay, Noam Shazeer, Vinodkumar Prabhakaran, Emily Reif, Nan Du, Ben
Hutchinson, Reiner Pope, James Bradbury, Jacob
Austin, Michael Isard, Guy Gur-Ari, Pengcheng Yin,
Toju Duke, Anselm Levskaya, Sanjay Ghemawat,
Sunipa Dev, Henryk Michalewski, Xavier Garcia,
Vedant Misra, Kevin Robinson, Liam Fedus, Denny
Zhou, Daphne Ippolito, David Luan, Hyeontaek Lim,
Barret Zoph, Alexander Spiridonov, Ryan Sepassi,
David Dohan, Shivani Agrawal, Mark Omernick, Andrew M. Dai, Thanumalayan Sankaranarayana Pillai, Marie Pellat, Aitor Lewkowycz, Erica Moreira,
Rewon Child, Oleksandr Polozov, Katherine Lee,
Zongwei Zhou, Xuezhi Wang, Brennan Saeta, Mark
Diaz, Orhan Firat, Michele Catasta, Jason Wei, Kathy
Meier-Hellstern, Douglas Eck, Jeff Dean, Slav Petrov,
and Noah Fiedel. 2023. Palm: Scaling Language
Modeling with Pathways. Journal of Machine Learning Research (JMLR), 24:240:1–240:113.
Hyung Won Chung, Le Hou, S. Longpre, Barret
Zoph, Yi Tay, W. Fedus, Eric Li, Xuezhi Wang,
Mostafa Dehghani, Siddhartha Brahma, Albert Webson, S. Gu, Zhuyun Dai, Mirac Suzgun, Xinyun Chen,
Aakanksha Chowdhery, Dasha Valter, Sharan Narang,
Gaurav Mishra, Adams Wei Yu, Vincent Zhao, Yanping Huang, Andrew M. Dai, Hongkun Yu, Slav
Petrov, E. Chi, J. Dean, Jacob Devlin, Adam Roberts,
Denny Zhou, Quoc V. Le, and Jason Wei. 2022. Scaling Instruction-Finetuned Language Models. arXiv,
abs/2210.11416.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. 2020. Unsupervised
Cross-lingual Representation Learning at Scale. In
Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 8440–
8451. Association for Computational Linguistics.
Florin Cuconasu, Giovanni Trappolini, Federico Siciliano, Simone Filice, Cesare Campagnano, Yoelle
Maarek, Nicola Tonellotto, and Fabrizio Silvestri.
2024. The Power of Noise: Redefining Retrieval for
RAG Systems. arXiv, abs/2401.14887.
Zhuyun Dai, Vincent Y. Zhao, Ji Ma, Yi Luan, Jianmo
Ni, Jing Lu, Anton Bakalov, Kelvin Guu, Keith B.
Hall, and Ming-Wei Chang. 2023. Promptagator:
Few-shot Dense Retrieval From 8 Examples. In International Conference on Learning Representations
(ICLR).
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. Bert: Pre-training of Deep
Bidirectional Transformers for Language Understanding. In Proceedings of the 2019 Conference of the
North, pages 4171–4186. Association for Computational Linguistics.
Emily Dinan, Stephen Roller, Kurt Shuster, Angela
Fan, Michael Auli, and Jason Weston. 2019. Wizard
of Wikipedia: Knowledge-Powered Conversational
Agents. In International Conference on Learning
Representations (ICLR).
Zhengxiao Du, Yujie Qian, Xiao Liu, Ming Ding,
Jiezhong Qiu, Zhilin Yang, and Jie Tang. 2022. Glm:
General Language Model Pretraining with Autoregressive Blank Infilling. In Proceedings of the 60th
Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers). Association for
Computational Linguistics.
Hady ElSahar, Pavlos Vougiouklis, Arslen Remaci,
Christophe Gravier, Jonathon S. Hare, Frédérique
Laforest, and Elena Simperl. 2018. T-REx: A Large
Scale Alignment of Natural Language with Knowledge Base Triples. In International Conference on
Language Resources and Evaluation (LREC).
Zhangyin Feng, Xiaocheng Feng, Dezhi Zhao, Maojin Yang, and Bing Qin. 2023. Retrieval-generation
synergy augmented large language models. arXiv,
abs/2310.05149.
Edward A. Fox and Joseph A. Shaw. 1994. Combination of multiple searches. In TREC-2: Text retrieval
conference, 500215, pages 105–108.
Tianyu Gao, Xingcheng Yao, and Danqi Chen. 2021.
Simcse: Simple Contrastive Learning of Sentence
Embeddings. In Proceedings of the 2021 Conference on Empirical Methods in Natural Language
Processing, pages 6894–6910. Association for Computational Linguistics.
Michael Glass, Gaetano Rossiello, Md Faisal Mahbub
Chowdhury, Ankita Naik, Pengshan Cai, and Alfio
Gliozzo. 2022. Re2g: Retrieve, Rerank, Generate.
In Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies,
pages 2701–2715. Association for Computational
Linguistics.
Simon Gottschalk and Elena Demidova. 2018. EventKG: A Multilingual Event-Centric Temporal Knowledge Graph. Springer International Publishing.
Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat,
and Ming-Wei Chang. 2020. Retrieval Augmented
Language Model Pre-Training. In International Conference on Machine Learning (ICML), pages 3929–
3938.
William L. Hamilton. 2020. Graph representation learning. Springer International Publishing.
Micheline Hancock-Beaulieu, Mike Gatford, Xiangji
Huang, Stephen E. Robertson, Steve Walker, and
P. W. Williams. 1996. Okapi at TREC-5. In Proceedings of The Fifth Text REtrieval Conference, TREC
1996, Gaithersburg, Maryland, USA, November 20-
22, 1996, volume 500-238 of NIST Special Publication. National Institute of Standards and Technology
(NIST).
Sebastian Hofstätter, Jiecao Chen, Karthik Raman, and
Hamed Zamani. 2023. Fid-light: Efficient and effective retrieval-augmented text generation. In Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information
Retrieval, pages 1437–1447.
Ziniu Hu, Ahmet Iscen, Chen Sun, Zirui Wang,
Kai-Wei Chang, Yizhou Sun, Cordelia Schmid,
David A. Ross, and Alireza Fathi. 2023. Reveal:
Retrieval-Augmented Visual-Language Pre-Training
with Multi-Source Multimodal Knowledge Memory. In 2023 IEEE/CVF Conference on Computer
Vision and Pattern Recognition (CVPR), pages 23369–
23379. IEEE.
Jie Huang, Hanyin Shao, Kevin Chen-Chuan Chang,
Jinjun Xiong, and Wen-mei Hwu. 2022. Understanding Jargon: Combining Extraction and Generation
for Definition Modeling. In Proceedings of the 2022
Conference on Empirical Methods in Natural Language Processing. Association for Computational
Linguistics.
Jimmy Xiangji Huang, Jun Miao, and Ben He. 2013.
High performance query expansion using adaptive
co-training. Inf. Process. Manag., 49(2):441–453.
Wenyu Huang, Mirella Lapata, Pavlos Vougiouklis,
Nikos Papasarantopoulos, and Jeff Z Pan. 2023. Retrieval Augmented Generation with Rich Answer Encoding. Proc. of IJCNLP-AACL, 2023.
Xiangji Huang and Qinmin Hu. 2009. A bayesian learning approach to promoting diversity in ranking for
biomedical information retrieval. In Proceedings of
the 32nd Annual International ACM SIGIR Conference on Research and Development in Information
Retrieval, SIGIR 2009, Boston, MA, USA, July 19-23,
2009, pages 307–314. ACM.
Yizheng Huang and Jimmy Huang. 2024. Exploring
chatgpt for next-generation information retrieval: Opportunities and challenges. CoRR, abs/2402.11203.
Yizheng Huang and Jimmy X. Huang. 2023. Diversified
prior knowledge enhanced general language model
for biomedical information retrieval. In ECAI 2023 -
26th European Conference on Artificial Intelligence,
September 30 - October 4, 2023, Kraków, Poland - Including 12th Conference on Prestigious Applications
of Intelligent Systems (PAIS 2023), volume 372 of
Frontiers in Artificial Intelligence and Applications,
pages 1109–1115. IOS Press.
Gautier Izacard, Mathilde Caron, Lucas Hosseini, Sebastian Riedel, Piotr Bojanowski, Armand Joulin, and
Edouard Grave. 2022. Unsupervised Dense Information Retrieval with Contrastive Learning. Transactions on Machine Learning Research (TMLR), 2022.
Gautier Izacard and Edouard Grave. 2021. Leveraging
Passage Retrieval with Generative Models for Open
Domain Question Answering. In Proceedings of the
16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume,
pages 874–880. Association for Computational Linguistics.
Gautier Izacard, Patrick S. H. Lewis, Maria Lomeli,
Lucas Hosseini, Fabio Petroni, Timo Schick, Jane
Dwivedi-Yu, Armand Joulin, Sebastian Riedel, and
Edouard Grave. 2023. Atlas: Few-shot Learning with
Retrieval Augmented Language Models. Journal
of Machine Learning Research (JMLR), 24:251:1–
251:43.
Israt Jahan, Md. Tahmid Rahman Laskar, Chun Peng,
and Jimmy Xiangji Huang. 2023. Evaluation of
chatgpt on biomedical tasks: A zero-shot comparison with fine-tuned generative transformers. CoRR,
abs/2306.04504.
Bernard J. Jansen, Danielle L. Booth, and Amanda
Spink. 2009. Patterns of query reformulation during web searching. J. Assoc. Inf. Sci. Technol.,
60(7):1358–1371.
Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu,
Dan Su, Yan Xu, Etsuko Ishii, Yejin Bang, Andrea
Madotto, and Pascale Fung. 2023. Survey of hallucination in natural language generation. ACM Comput.
Surv., 55(12):248:1–248:38.
Zhengbao Jiang, Frank F. Xu, Luyu Gao, Zhiqing Sun,
Qian Liu, Jane Dwivedi-Yu, Yiming Yang, Jamie
Callan, and Graham Neubig. 2023. Active Retrieval
Augmented Generation. In Conference on Empirical
Methods in Natural Language Processing (EMNLP),
pages 7969–7992.
Jeff Johnson, Matthijs Douze, and Hervé Jégou. 2021.
Billion-scale similarity search with gpus. IEEE
Transactions on Big Data, 7(3):535–547.
Mandar Joshi, Eunsol Choi, Daniel Weld, and Luke
Zettlemoyer. 2017. Triviaqa: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension. In Proceedings of the 55th Annual Meeting
of the Association for Computational Linguistics (Volume 1: Long Papers), pages 1601–1611. Association
for Computational Linguistics.
Minki Kang, Jin Myung Kwak, Jinheon Baek,
and Sung Ju Hwang. 2023. Knowledge
Graph-Augmented Language Models for
Knowledge-Grounded Dialogue Generation.
arXiv, abs/2305.18846.
Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick
S. H. Lewis, Ledell Wu, Sergey Edunov, Danqi Chen,
and Wen-tau Yih. 2020. Dense Passage Retrieval for
Open-Domain Question Answering. In Conference
on Empirical Methods in Natural Language Processing (EMNLP), pages 6769–6781.
Urvashi Khandelwal, Omer Levy, Dan Jurafsky, Luke
Zettlemoyer, and Mike Lewis. 2020. Generalization
through Memorization: Nearest Neighbor Language
Models. In International Conference on Learning
Representations (ICLR).
O. Khattab, Keshav Santhanam, Xiang Lisa Li, David
Leo Wright Hall, Percy Liang, Christopher Potts,
and M. Zaharia. 2022. Demonstrate-Search-Predict:
Composing retrieval and language models for
knowledge-intensive NLP. arXiv, abs/2212.14024.
Omar Khattab and Matei Zaharia. 2020. Colbert - Efficient and Effective Passage Search via Contextualized Late Interaction over BERT. In Proceedings of
the 43rd International ACM SIGIR Conference on
Research and Development in Information Retrieval,
pages 39–48. ACM.
Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti,
Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, Kristina Toutanova, Llion Jones, Matthew
Kelcey, Ming-Wei Chang, Andrew M. Dai, Jakob
Uszkoreit, Quoc Le, and Slav Petrov. 2019. Natural
Questions: A Benchmark for Question Answering
Research. Transactions of the Association for Computational Linguistics, 7:453–466.
Md. Tahmid Rahman Laskar, M. Saiful Bari, Mizanur
Rahman, Md Amran Hossen Bhuiyan, Shafiq Joty,
and Jimmy Xiangji Huang. 2023. A systematic study
and comprehensive evaluation of chatgpt on benchmark datasets. CoRR, abs/2305.18486.
Md. Tahmid Rahman Laskar, Enamul Hoque, and
Jimmy X. Huang. 2020. Query focused abstractive
summarization via incorporating query relevance and
transfer learning with transformer models. In Advances in Artificial Intelligence - 33rd Canadian Conference on Artificial Intelligence, Canadian AI 2020,
Ottawa, ON, Canada, May 13-15, 2020, Proceedings,
volume 12109 of Lecture Notes in Computer Science,
pages 342–348. Springer.
Mike Lewis, Yinhan Liu, Naman Goyal, Marjan
Ghazvininejad, Abdelrahman Mohamed, Omer Levy,
Veselin Stoyanov, and Luke Zettlemoyer. 2020a.
Bart: Denoising Sequence-to-Sequence Pre-training
for Natural Language Generation, Translation, and
Comprehension. In Proceedings of the 58th Annual
Meeting of the Association for Computational Linguistics, pages 7871–7880. Association for Computational Linguistics.
Patrick S. H. Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman
Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih,
Tim Rocktäschel, Sebastian Riedel, and Douwe
Kiela. 2020b. Retrieval-Augmented Generation for
Knowledge-Intensive NLP Tasks. In Conference on
Neural Information Processing Systems (NeurIPS).
Canjia Li, Andrew Yates, Sean MacAvaney, Ben He,
and Yingfei Sun. 2024. Parade: Passage Representation Aggregation forDocument Reranking. ACM
Transactions on Information Systems, 42(2):1–26.
Huayang Li, Yixuan Su, Deng Cai, Yan Wang, and
Lemao Liu. 2022. A Survey on Retrieval-Augmented
Text Generation. arXiv, abs/2202.01110.
Xingxuan Li, Ruochen Zhao, Yew Ken Chia, Bosheng
Ding, Shafiq R. Joty, Soujanya Poria, and Lidong
Bing. 2023. Chain-of-Knowledge: Grounding Large
Language Models via Dynamic Knowledge Adapting
over Heterogeneous Sources. arXiv.
Chin-Yew Lin. 2004. ROUGE: A package for automatic evaluation of summaries. In Text Summarization Branches Out, pages 74–81, Barcelona, Spain.
Association for Computational Linguistics.
Sheng-Chieh Lin, Akari Asai, Minghan Li, Barlas
Oguz, Jimmy Lin, Yashar Mehdad, Wen-tau Yih,
and Xilun Chen. 2023a. How to Train Your Dragon:
Diverse Augmentation Towards Generalizable Dense
Retrieval. In Findings of the Association for Computational Linguistics: EMNLP 2023, pages 6385–
6400. Association for Computational Linguistics.
Xi Victoria Lin, Xilun Chen, Mingda Chen, Weijia Shi,
Maria Lomeli, Rich James, Pedro Rodriguez, Jacob
Kahn, Gergely Szilvasy, Mike Lewis, and others.
2023b. Ra-dit: Retrieval-augmented dual instruction tuning. arXiv, abs/2310.01352.
Xi Victoria Lin, Todor Mihaylov, Mikel Artetxe, Tianlu
Wang, Shuohui Chen, Daniel Simig, Myle Ott, Naman Goyal, Shruti Bhosale, Jingfei Du, Ramakanth
Pasunuru, Sam Shleifer, Punit Singh Koura, Vishrav
Chaudhary, Brian O’Horo, Jeff Wang, Luke Zettlemoyer, Zornitsa Kozareva, Mona Diab, Veselin Stoyanov, and Xian Li. 2022. Few-shot Learning with
Multilingual Generative Language Models. In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing. Association for
Computational Linguistics.
Yi Liu, Lianzhe Huang, Shicheng Li, Sishuo Chen,
Hao Zhou, Fandong Meng, Jie Zhou, and Xu Sun.
2023. Recall: A Benchmark for LLMs Robustness
against External Counterfactual Knowledge. arXiv,
abs/2311.08147.
Ziyang Luo, Can Xu, Pu Zhao, Xiubo Geng, Chongyang
Tao, Jing Ma, Qingwei Lin, and Daxin Jiang. 2023.
Augmented Large Language Models with Parametric
Knowledge Guiding. arXiv, abs/2305.04757.
Xinbei Ma, Yeyun Gong, Pengcheng He, Hai Zhao,
and Nan Duan. 2023. Query Rewriting in RetrievalAugmented Large Language Models. In Proceedings
of the 2023 Conference on Empirical Methods in
Natural Language Processing, pages 5303–5315. Association for Computational Linguistics.
Yu A. Malkov and D. A. Yashunin. 2020. Efficient
and robust approximate nearest neighbor search using hierarchical navigable small world graphs. IEEE
Transactions on Pattern Analysis and Machine Intelligence, 42(4):824–836.
Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schütze. 2008. Introduction to Information Retrieval. Cambridge University Press.
Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff
Wu, Long Ouyang, Christina Kim, Christopher
Hesse, Shantanu Jain, Vineet Kosaraju, William
Saunders, and others. 2021. Webgpt: Browserassisted question-answering with human feedback.
arXiv, abs/2112.09332.
Jianmo Ni, Chen Qu, Jing Lu, Zhuyun Dai, Gustavo Hernandez Abrego, Ji Ma, Vincent Zhao, Yi Luan,
Keith Hall, Ming-Wei Chang, and Yinfei Yang. 2022.
Large Dual Encoders Are Generalizable Retrievers.
In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pages
9844–9855. Association for Computational Linguistics.
Rodrigo Nogueira, Wei Yang, Kyunghyun Cho, and
Jimmy Lin. 2019. Multi-stage document ranking
with BERT. CoRR, abs/1910.14424.
OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal,
Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, Red Avila, Igor Babuschkin,
Suchir Balaji, Valerie Balcom, Paul Baltescu, Haiming Bao, Mo Bavarian, Jeff Belgum, Irwan Bello,
Jake Berdine, Gabriel Bernadett-Shapiro, Christopher Berner, Lenny Bogdonoff, Oleg Boiko, Madelaine Boyd, Anna-Luisa Brakman, Greg Brockman,
Tim Brooks, Miles Brundage, Kevin Button, Trevor
Cai, Rosie Campbell, Andrew Cann, Brittany Carey,
Chelsea Carlson, Rory Carmichael, Brooke Chan,
Che Chang, Fotis Chantzis, Derek Chen, Sully Chen,
Ruby Chen, Jason Chen, Mark Chen, Ben Chess,
Chester Cho, Casey Chu, Hyung Won Chung, Dave
Cummings, Jeremiah Currier, Yunxing Dai, Cory
Decareaux, Thomas Degry, Noah Deutsch, Damien
Deville, Arka Dhar, David Dohan, Steve Dowling,
Sheila Dunning, Adrien Ecoffet, Atty Eleti, Tyna
Eloundou, David Farhi, Liam Fedus, Niko Felix,
Simón Posada Fishman, Juston Forte, Isabella Fulford, Leo Gao, Elie Georges, Christian Gibson, Vik
Goel, Tarun Gogineni, Gabriel Goh, Rapha GontijoLopes, Jonathan Gordon, Morgan Grafstein, Scott
Gray, Ryan Greene, Joshua Gross, Shixiang Shane
Gu, Yufei Guo, Chris Hallacy, Jesse Han, Jeff Harris,
Yuchen He, Mike Heaton, Johannes Heidecke, Chris
Hesse, Alan Hickey, Wade Hickey, Peter Hoeschele,
Brandon Houghton, Kenny Hsu, Shengli Hu, Xin
Hu, Joost Huizinga, Shantanu Jain, Shawn Jain,
Joanne Jang, Angela Jiang, Roger Jiang, Haozhun
Jin, Denny Jin, Shino Jomoto, Billie Jonn, Heewoo
Jun, Tomer Kaftan, Łukasz Kaiser, Ali Kamali, Ingmar Kanitscheider, Nitish Shirish Keskar, Tabarak
Khan, Logan Kilpatrick, Jong Wook Kim, Christina
Kim, Yongjik Kim, Hendrik Kirchner, Jamie Kiros,
Matt Knight, Daniel Kokotajlo, Łukasz Kondraciuk,
Andrew Kondrich, Aris Konstantinidis, Kyle Kosic,
Gretchen Krueger, Vishal Kuo, Michael Lampe, Ikai
Lan, Teddy Lee, Jan Leike, Jade Leung, Daniel Levy,
Chak Ming Li, Rachel Lim, Molly Lin, Stephanie
Lin, Mateusz Litwin, Theresa Lopez, Ryan Lowe,
Patricia Lue, Anna Makanju, Kim Malfacini, Sam
Manning, Todor Markov, Yaniv Markovski, Bianca
Martin, Katie Mayer, Andrew Mayne, Bob McGrew,
Scott Mayer McKinney, Christine McLeavey, Paul
McMillan, Jake McNeil, and others. 2023. Gpt-4
Technical Report. PREPRINT.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll L. Wainwright, Pamela Mishkin, Chong
Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray,
John Schulman, Jacob Hilton, Fraser Kelton, Luke
Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul F. Christiano, Jan Leike, and Ryan Lowe.
2022. Training language models to follow instructions with human feedback. In Conference on Neural
Information Processing Systems (NeurIPS).
Kishore Papineni, Salim Roukos, Todd Ward, and WeiJing Zhu. 2002. Bleu: a method for automatic evaluation of machine translation. In Proceedings of the
40th Annual Meeting on Association for Computational Linguistics, ACL ’02, page 311–318, USA.
Association for Computational Linguistics.
Baolin Peng, Chunyuan Li, Pengcheng He, Michel Galley, and Jianfeng Gao. 2023. Instruction tuning with
gpt-4. arXiv.
Fabio Petroni, Aleksandra Piktus, Angela Fan, Patrick
Lewis, Majid Yazdani, Nicola De Cao, James Thorne,
Yacine Jernite, Vladimir Karpukhin, Jean Maillard,
Vassilis Plachouras, Tim Rocktäschel, and Sebastian
Riedel. 2021. Kilt: a Benchmark for Knowledge Intensive Language Tasks. In Proceedings of the 2021
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies, pages 2523–2544. Association for Computational Linguistics.
Filip Radlinski and Nick Craswell. 2010. Comparing
the sensitivity of information retrieval metrics. In
Proceedings of the 33rd International ACM SIGIR
Conference on Research and Development in Information Retrieval, SIGIR ’10, page 667–674, New
York, NY, USA. Association for Computing Machinery.
Colin Raffel, Noam M. Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi
Zhou, Wei Li, and Peter J. Liu. 2020. Exploring
the Limits of Transfer Learning with a Unified Textto-Text Transformer. Journal of Machine Learning
Research (JMLR), 21:140:1–140:67.
Ori Ram, Yoav Levine, Itay Dalmedigos, Dor Muhlgay,
Amnon Shashua, Kevin Leyton-Brown, and Yoav
Shoham. 2023. In-Context Retrieval-Augmented
Language Models. Transactions of the Association
for Computational Linguistics, 11:1316–1331.
Ori Ram, Gal Shachaf, Omer Levy, Jonathan Berant,
and Amir Globerson. 2022. Learning to Retrieve
Passages without Supervision. In Proceedings of the
2022 Conference of the North American Chapter of
the Association for Computational Linguistics: Human Language Technologies. Association for Computational Linguistics.
Nils Reimers and Iryna Gurevych. 2019. SentenceBERT: Sentence Embeddings using Siamese BERTNetworks. In Proceedings of the 2019 Conference on
Empirical Methods in Natural Language Processing
and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages
3980–3990. Association for Computational Linguistics.
Stephen Robertson and Hugo Zaragoza. 2009. The
Probabilistic Relevance Framework: Bm25 and Beyond. Foundations and Trends® in Information Retrieval, 3(4):333–389.
Jon Saad-Falcon, O. Khattab, Christopher Potts, and
Matei Zaharia. 2023. Ares: An Automated Evaluation Framework for Retrieval-Augmented Generation
Systems. arXiv, abs/2311.09476.
Sara Sarto, Marcella Cornia, Lorenzo Baraldi, and Rita
Cucchiara. 2022. Retrieval-Augmented Transformer
for Image Captioning. In International Conference
on Content-based Multimedia Indexing. ACM.
ES Shahul, Jithin James, Luis Espinosa Anke, and
S. Schockaert. 2023. Ragas: Automated Evaluation of Retrieval Augmented Generation. arXiv,
abs/2309.15217.
Zhihong Shao, Yeyun Gong, Yelong Shen, Minlie
Huang, Nan Duan, and Weizhu Chen. 2023. Enhancing Retrieval-Augmented Large Language Models
with Iterative Retrieval-Generation Synergy. In Findings of the Association for Computational Linguistics: EMNLP 2023, pages 9248–9274. Association
for Computational Linguistics.
Weijia Shi, Sewon Min, Michihiro Yasunaga, Minjoon
Seo, Rich James, Mike Lewis, Luke Zettlemoyer, and
Wen-tau Yih. 2023. Replug: Retrieval-augmented
black-box language models. arXiv, abs/2301.12652.
Zhiqing Sun, Xuezhi Wang, Yi Tay, Yiming Yang, and
Denny Zhou. 2023. Recitation-Augmented Language Models. In International Conference on Learning Representations (ICLR).
Yi Tay, Mostafa Dehghani, Vinh Q. Tran, Xavier Garcia,
Jason Wei, Xuezhi Wang, Hyung Won Chung, Dara
Bahri, Tal Schuster, Huaixiu Steven Zheng, Denny
Zhou, Neil Houlsby, and Donald Metzler. 2023. Ul2:
Unifying Language Learning Paradigms. In International Conference on Learning Representations
(ICLR).
Yi Tay, Vinh Tran, Mostafa Dehghani, Jianmo Ni, Dara
Bahri, Harsh Mehta, Zhen Qin, Kai Hui, Zhe Zhao,
Jai Prakash Gupta, Tal Schuster, William W. Cohen,
and Donald Metzler. 2022. Transformer Memory
as a Differentiable Search Index. In Conference on
Neural Information Processing Systems (NeurIPS).
James Thorne, Andreas Vlachos, Christos
Christodoulopoulos, and Arpit Mittal. 2018.
Fever: a Large-scale Dataset for Fact Extraction
and VERification. In Proceedings of the 2018
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies, Volume 1 (Long Papers),
pages 809–819. Association for Computational
Linguistics.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothee Lacroix,
Baptiste Roziere, Naman Goyal, Eric Hambro, Faisal
Azhar, and others. 2023a. Llama: Open and efficient
foundation language models. arXiv, abs/2302.13971.
Hugo Touvron, Louis Martin, Kevin Stone, Peter
Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava,
Shruti Bhosale, and others. 2023b. Llama 2: Open
foundation and fine-tuned chat models. arxiv,
abs/2307.09288.
Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot,
and Ashish Sabharwal. 2023. Interleaving Retrieval
with Chain-of-Thought Reasoning for KnowledgeIntensive Multi-Step Questions. In Proceedings of
the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pages 10014–10037. Association for Computational
Linguistics.
Ashish Vaswani, Noam M. Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz
Kaiser, and Illia Polosukhin. 2017. Attention is All
you Need. In Neural Information Processing Systems, pages 5998–6008.
Alex Wang, Yada Pruksachatkun, Nikita Nangia, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy,
and Samuel R. Bowman. 2019. Superglue: A Stickier Benchmark for General-Purpose Language Understanding Systems. In Conference on Neural Information Processing Systems (NeurIPS), pages 3261–
3275.
Ben Wang and Aran Komatsuzaki. 2021. GPT-J6B: A 6 Billion Parameter Autoregressive Language Model. https://github.com/kingoflolz/
mesh-transformer-jax.
Liang Wang, Nan Yang, and Furu Wei. 2023a.
Query2doc: Query Expansion with Large Language
Models. In Proceedings of the 2023 Conference on
Empirical Methods in Natural Language Processing,
pages 9414–9423. Association for Computational
Linguistics.
Xintao Wang, Qian Yang, Yongting Qiu, Jiaqing Liang,
Qi He, Zhouhong Gu, Yanghua Xiao, and W. Wang.
2023b. Knowledgpt: Enhancing Large Language
Models with Retrieval and Storage Access on Knowledge Bases. arXiv, abs/2308.11761.
BigScience Workshop, Teven Le Scao, Angela Fan,
Christopher Akiki, Ellie Pavlick, Suzana Ilic, Daniel
Hesslow, Roman Castagné, Alexandra Sasha Luccioni, François Yvon, and others. 2022. Bloom: A
176b-parameter open-access multilingual language
model. arXiv, abs/2211.05100.
Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang,
Jialin Liu, Paul N. Bennett, Junaid Ahmed, and
Arnold Overwijk. 2021. Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text
Retrieval. In International Conference on Learning
Representations (ICLR).
Fangyuan Xu, Weijia Shi, and Eunsol Choi. 2023. Recomp: Improving Retrieval-Augmented LMs with
Compression and Selective Augmentation. arXiv,
abs/2310.04408.
Haoyan Yang, Zhitao Li, Yong Zhang, Jianzong Wang,
Ning Cheng, Ming Li, and Jing Xiao. 2023a. Prca:
Fitting Black-Box Large Language Models for Retrieval Question Answering via Pluggable RewardDriven Contextual Adapter. In Proceedings of the
2023 Conference on Empirical Methods in Natural
Language Processing, pages 5364–5375. Association
for Computational Linguistics.
Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio,
William Cohen, Ruslan Salakhutdinov, and Christopher D. Manning. 2018. Hotpotqa: A Dataset for
Diverse, Explainable Multi-hop Question Answering.
In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing, pages
2369–2380. Association for Computational Linguistics.
Zhuolin Yang, Wei Ping, Zihan Liu, Vijay Korthikanti,
Weili Nie, De-An Huang, Linxi Fan, Zhiding Yu,
Shiyi Lan, Bo Li, Mohammad Shoeybi, Ming-Yu
Liu, Yuke Zhu, Bryan Catanzaro, Chaowei Xiao, and
Anima Anandkumar. 2023b. Re-ViLM: RetrievalAugmented Visual Language Model for Zero and
Few-Shot Image Captioning. In Findings of the Association for Computational Linguistics: EMNLP 2023,
pages 11844–11857. Association for Computational
Linguistics.
Shi Yu, Jiahua Liu, Jingqin Yang, Chenyan Xiong,
Paul N. Bennett, Jianfeng Gao, and Zhiyuan Liu.
2020. Few-shot generative conversational query
rewriting. In Proceedings of the 43rd International
ACM SIGIR conference on research and development
in Information Retrieval, SIGIR 2020, Virtual Event,
China, July 25-30, 2020, pages 1933–1936. ACM.
Wenhao Yu, Dan Iter, Shuohang Wang, Yichong Xu,
Mingxuan Ju, Soumya Sanyal, Chenguang Zhu,
Michael Zeng, and Meng Jiang. 2023a. Generate
rather than Retrieve: Large Language Models are
Strong Context Generators. In International Conference on Learning Representations (ICLR).
Wenhao Yu, Chenguang Zhu, Zaitang Li, Zhiting Hu,
Qingyun Wang, Heng Ji, and Meng Jiang. 2022. A
survey of knowledge-enhanced text generation. ACM
Comput. Surv., 54(11s):227:1–227:38.
Zichun Yu, Chenyan Xiong, Shi Yu, and Zhiyuan Liu.
2023b. Augmentation-Adapted Retriever Improves
Generalization of Language Models as Generic PlugIn. In Proceedings of the 61st Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), pages 2421–2436. Association for
Computational Linguistics.
Yi Yuan, Haohe Liu, Xubo Liu, Qiushi Huang, Mark D
Plumbley, and Wenwu Wang. 2023. RetrievalAugmented Text-to-Audio Generation. arXiv,
abs/2309.08051.
Susan Zhang, Stephen Roller, Naman Goyal, Mikel
Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona Diab, Xian Li, Xi Victoria Lin, and others.
2022. Opt: Open pre-trained transformer language
models. arXiv, abs/2205.01068.
Huaixiu Steven Zheng, Swaroop Mishra, Xinyun Chen,
Heng-Tze Cheng, E. Chi, Quoc V. Le, and Denny
Zhou. 2023. Take a Step Back: Evoking Reasoning
via Abstraction in Large Language Models. arXiv,
abs/2310.06117.
Honglei Zhuang, Zhen Qin, Rolf Jagerman, Kai Hui,
Ji Ma, Jing Lu, Jianmo Ni, Xuanhui Wang, and
Michael Bendersky. 2023. Rankt5: Fine-Tuning T5
for Text Ranking with Ranking Losses. In Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information
Retrieval. ACM.

