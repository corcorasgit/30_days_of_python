# 30_days_of_python
30 days of python course by cfe -- Justin Mitchel on Udemy
just stating now


<span style="color:red">
<h2>Strings</h2>
</span>

| Navigation  | Description |  
| :----------: | :--------- | 
| h  | move cursor right |
| l  | move cursor left |

Welcome to Python 3 Basics: Strings, Variables, and Integers
🧠 Lesson 1: What Is a Variable?
Think of a variable as a labeled box in your brain. You can put something in it, give it a name, and use it later.

📦 Variable = Box
🏷️ Name = Label
🎁 Value = What’s inside

```
# Here's how you create a variable in Python:
name = "Alice"
```

🧪 Try It:

python
Copy
Edit
city = "New York"
print(city)
🧠 Lesson 2: Strings (Text in Quotes)
A string is a fancy name for text — anything between quotes:

python
Copy
Edit
greeting = "Hello, world!"
You can use:

Double quotes: "Hello"

Single quotes: 'Hi there'

🧪 Try It:

python
Copy
Edit
message = "Python is fun!"
print(message)
You can even join strings together:

python
Copy
Edit
first = "Python"
second = "Rocks"
result = first + " " + second
print(result)
👀 Output:

nginx
Copy
Edit
Python Rocks
🧠 Lesson 3: Integers (Whole Numbers)
An integer (or int) is just a whole number — no quotes, no decimal points:

python
Copy
Edit
age = 25
print(age)
You can do math with integers:

python
Copy
Edit
x = 10
y = 5
print(x + y)  # Adds them
print(x * y)  # Multiplies them
print(x - y)  # Subtracts
print(x / y)  # Divides (returns a float)
🛠️ Tip: Check What Type It Is
Want to check what kind of data something is? Use type():

python
Copy
Edit
print(type("Hello"))  # string
print(type(42))       # integer
🔄 Recap Time
Concept	Example	What It Is
Variable	name = "Sam"	A box storing a value
String	"hello" or 'hi'	Text inside quotes
Integer	age = 30	Whole number

🧩 Mini Challenge
Can you write a small program that:

Stores your name and age.

Prints a greeting like:
"Hello Alice, you are 30 years old!"

💡Hint: Use string + to join things, and remember to convert numbers to strings using str()!

python
Copy
Edit
name = "Alice"
age = 30
print("Hello " + name + ", you are " + str(age) + " years old!")


<span style="color:red">
<h2>Lists</h2>
</span>


👨‍🏫 Python 3 Lesson: Lists – The Swiss Army Knife of Data!
🧠 What’s a List?
Imagine a list as a row of boxes 📦📦📦, each one holding a value — maybe numbers, strings, or even other lists! And yes — just like real-life lists — you can add, remove, sort, and access things in them.

python
Copy
Edit
# A list of fruits
fruits = ["apple", "banana", "cherry"]
📦 fruits is a list that contains three strings.

🧪 Let’s Peek Inside
python
Copy
Edit
print(fruits)
Output:

css
Copy
Edit
['apple', 'banana', 'cherry']
🎯 Accessing Items in a List (Indexing)
Python starts counting from 0. So:

python
Copy
Edit
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # cherry
✍️ Changing a Value
Want to change "banana" to "orange"?

python
Copy
Edit
fruits[1] = "orange"
print(fruits)
# ['apple', 'orange', 'cherry']
➕ Adding Items to a List
python
Copy
Edit
fruits.append("grape")  # adds to the end
print(fruits)
Or add it at a specific spot:

python
Copy
Edit
fruits.insert(1, "mango")  # inserts at index 1
print(fruits)
❌ Removing Items
python
Copy
Edit
fruits.remove("cherry")  # removes by value
print(fruits)
Or remove the last item:

python
Copy
Edit
fruits.pop()
print(fruits)
🧹 Clear the Whole List
python
Copy
Edit
fruits.clear()
print(fruits)  # []
🔁 Looping Through a List
python
Copy
Edit
colors = ["red", "green", "blue"]

for color in colors:
    print("Color is:", color)
Output:

csharp
Copy
Edit
Color is: red  
Color is: green  
Color is: blue  
📏 Length of a List
python
Copy
Edit
print(len(colors))  # 3
🧩 Mini Practice: Your Favorite Things
Try writing a small program that:

Creates a list of 3 of your favorite foods.

Adds one more.

Prints each food with a message like: "I love pizza!"

python
Copy
Edit
foods = ["pizza", "sushi", "tacos"]
foods.append("ice cream")

for food in foods:
    print("I love " + food + "!")
🔍 Bonus Tip: Mixing Data Types
A list can hold anything:

python
Copy
Edit
random_things = ["Python", 3.14, 42, True]
🧠 Recap Table
Operation	Code Example	Description
Create a list	my_list = [1, 2, 3]	A list of integers
Access item	my_list[0]	First item
Change item	my_list[1] = 5	Change second item
Add to end	my_list.append(4)	Add new item at end
Insert at position	my_list.insert(1, "hello")	Add at specific index
Remove item	my_list.remove(2)	Remove by value
Pop last item	my_list.pop()	Removes last item
Loop through list	for item in my_list:	Looping




<span style="color:red">
<h2>dictionaries</h2>
</span>




ChatGPT said:
Alright, Python apprentice! 🧙‍♂️
Now that you’ve mastered lists, it’s time to unlock one of Python’s most powerful tools:

👨‍🏫 Python 3 Lesson: Dictionaries – Your Pocket Database!
🧠 What Is a Dictionary?
A dictionary is like a real dictionary 📖.
You look up a word (key) and get a definition (value).

In Python, it works the same way:

python
Copy
Edit
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
🔑 name, age, and city are keys
📦 "Alice", 30, and "New York" are values

🔍 Accessing Data
python
Copy
Edit
print(person["name"])  # Alice
print(person["age"])   # 30
🚨 If you ask for a key that doesn’t exist, Python gets upset!

✅ Use .get() to play it safe:

python
Copy
Edit
print(person.get("hobby"))  # None (doesn't crash)
✍️ Changing & Adding Values
python
Copy
Edit
person["age"] = 31           # Update
person["hobby"] = "reading"  # Add
print(person)
❌ Removing Entries
python
Copy
Edit
del person["city"]  # Bye bye New York
Or:

python
Copy
Edit
person.pop("age")
🔁 Looping Through a Dictionary
🗝️ Keys only:
python
Copy
Edit
for key in person:
    print(key)
📦 Keys and Values:
python
Copy
Edit
for key, value in person.items():
    print(key + ": " + str(value))
📏 How Many Entries?
python
Copy
Edit
print(len(person))  # Number of key-value pairs
🧪 Real-Life Example
Let’s say you want to store a student's info:

python
Copy
Edit
student = {
    "name": "James",
    "grade": "A",
    "subjects": ["Math", "Science", "History"]
}

print(student["subjects"][1])  # Science
Yes! A dictionary can hold lists, other dictionaries, even functions. It’s a flexible beast! 🐍

🧩 Mini Challenge
Write a dictionary to represent a book, with:

title

author

year

Then print a message like:
"The book '1984' was written by George Orwell in 1949."

python
Copy
Edit
book = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949
}

print("The book '" + book["title"] + "' was written by " + book["author"] + " in " + str(book["year"]) + ".")
🧠 Recap Table
Concept	Code Example	Description
Create dictionary	d = {"a": 1, "b": 2}	Key-value pairs
Access value	d["a"]	Get value for key "a"
Safe access	d.get("c")	Returns None if missing
Add or change	d["b"] = 3	Update value or add new key
Delete	del d["a"]	Removes the key and its value
Loop through	for k, v in d.items():	Loop through key & value






<span style="color:red">
<h2>tuples</h2>
</span>

👨‍🏫 Python 3 Lesson: Tuples – The Unchangeable List
🧠 What Is a Tuple?
A tuple is just like a list, but there’s one big difference:

👉 Tuples cannot be changed after you create them.
They are immutable (fancy word for "frozen").

📦 Why Use Tuples?
You want a fixed collection of items.

Tuples are faster and use less memory.

Python won’t let you change them by accident.

🛠️ Creating a Tuple
python
Copy
Edit
colors = ("red", "green", "blue")
✅ Use parentheses () instead of square brackets [].

🧪 Accessing Tuple Elements
Just like a list — by index!

python
Copy
Edit
print(colors[0])  # red
print(colors[2])  # blue
❌ Trying to Change It?
python
Copy
Edit
colors[1] = "yellow"
❌ Boom! Python will throw an error:

php
Copy
Edit
TypeError: 'tuple' object does not support item assignment
📏 Tuple Length
python
Copy
Edit
print(len(colors))  # 3
🔁 Looping Through a Tuple
python
Copy
Edit
for color in colors:
    print("Color:", color)
💡 One-Item Tuples
Watch out! This isn’t a tuple:

python
Copy
Edit
not_a_tuple = ("hello")
print(type(not_a_tuple))  # str ❌
✅ This is a tuple:

python
Copy
Edit
single = ("hello",)
print(type(single))  # tuple ✅
You must include the comma when making a tuple with only one item.

🔄 Tuple Packing and Unpacking
Packing: Bundle multiple values into one tuple:

python
Copy
Edit
person = ("Alice", 30, "New York")
Unpacking: Assign values from a tuple into variables:

python
Copy
Edit
name, age, city = person
print(name)  # Alice
print(age)   # 30
print(city)  # New York
🧩 Mini Practice
Create a tuple with your favorite 3 movies and print them one by one using a loop:

python
Copy
Edit
movies = ("Inception", "Interstellar", "The Matrix")

for movie in movies:
    print("I love", movie)
🧠 Recap Table
Concept	Code Example	Description
Create tuple	t = (1, 2, 3)	Tuple with 3 elements
Access item	t[0]	First item
Length	len(t)	Number of elements
Loop through tuple	for item in t:	Read every element
Unpacking	a, b = (10, 20)	Assign tuple to multiple vars
Immutable	t[0] = 5	❌ Not allowed
Single-item tuple	t = ("hi",)	Must have comma

Tuples are perfect for:

Coordinates: (x, y)

Dates: (year, month, day)

Fixed settings or constants





<span style="color:red">
<h2>loops</h2>
</span>

🧠 What Is a Loop?
A loop lets your program do something over and over again until you tell it to stop.

It’s like saying:

"For every student in the class, say hello."
or
"While I’m hungry, keep eating."

Python has two main loop types:

🔁 1. for Loop
🔄 2. while Loop
🔁 for Loop – Looping Over a Collection
Use for when you know how many things you’re looping through.

✅ Example 1: Looping Over a List
python
Copy
Edit
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("I like", fruit)
Output:

css
Copy
Edit
I like apple  
I like banana  
I like cherry
✅ Example 2: Using range()
python
Copy
Edit
for number in range(5):
    print(number)
Output:

Copy
Edit
0  
1  
2  
3  
4
💡 range(5) gives you numbers from 0 to 4

🧮 Bonus: range(start, stop, step)
python
Copy
Edit
for i in range(1, 10, 2):
    print(i)
Output:

Copy
Edit
1  
3  
5  
7  
9
🔄 while Loop – Loop Until a Condition Fails
Use while when you don’t know how many times you’ll loop, just that you’ll loop until something happens.

✅ Example: Count Until 5
python
Copy
Edit
count = 0

while count < 5:
    print("Counting:", count)
    count += 1  # Same as: count = count + 1
Output:

makefile
Copy
Edit
Counting: 0  
Counting: 1  
Counting: 2  
Counting: 3  
Counting: 4
🛑 Break and Continue
🧨 break – Stop the loop
python
Copy
Edit
for number in range(10):
    if number == 5:
        break
    print(number)
Output:

Copy
Edit
0  
1  
2  
3  
4
⏭️ continue – Skip one round
python
Copy
Edit
for number in range(5):
    if number == 2:
        continue
    print(number)
Output:

Copy
Edit
0  
1  
3  
4
🧩 Mini Challenge: Loop Practice
Task:
Use a for loop to print numbers 1 through 10.

Use a while loop to count down from 5 to 1.

python
Copy
Edit
# For loop
for i in range(1, 11):
    print(i)

# While loop
count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1
🧠 Recap Table
Loop Type	Syntax Example	When to Use
for	for item in list:	Loop over items in a collection
range()	for i in range(5):	Loop fixed number of times
while	while condition:	Loop until something changes
break	if something: break	Stop loop early
continue	if something: continue	Skip current loop step

Loops are the heart of automation — you'll use them every day in Python.
Want to practice with nested loops, real-world projects, or a mini quiz? Just say the word and we’ll level up! 🧠🔥










<span style="color:red">
<h2>dictionaries</h2>
</span>

<span style="color:red">
<h2>dictionaries</h2>
</span>




