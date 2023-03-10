# Clean Code

Best practices for writing better and cleaner code
Following the course by Maximilian Schwarzmueller: [Clean Code](https://www.udemy.com/course/writing-clean-code/)

# Dev notes

## What is Clean Code?

- Code that is easy to read and understand
  - Should be readable and meaningful
  - Should reduce cognitive load
  - Should be concise and to the point

## About the code cotained in this repo

- Short examples of concepts, most of them are demostrative and not executable

## Clean Code vs. Patterns and Principles

- Clean code is readable and easy to understand and Patterns and principles ensures a maintainable and extensible code
- These concepts are different but can be related

## Clean Code vs. Clean Architecture

- Clean code focuses on how to write the code and architecture where to write it
- Clean code focuses on a single problem or file and Clean Architecture focuses on the project as a whole

## Clean Code Key-pain points

- Naming: Variables, functions and classes

### Structure and Comments

- Code formatting
- Good and bad comments

### Functions

- Length
- Parameters

### Conditioning and Error Handling

- Deep Nesting
- Missing Error Handling

### Classes and Data Structures

- Missing distinction
- Bloated classes

## Naming: Why names matter

- represents what the code does in one single name (should be like that)
- well-named pieces allow readers to understand what is it about without the need of reading it entirely

### Rules, Concepts and Bad Names

- Should be meaningful

#### Variables and constants

- Given that they are data containers, its name should be the entity that it contains

#### Functions

- Given that they are commands or calculated values, its name must signify what the function executes

#### Classes

- Given that they are "factories" for new objects the should be nouns or short phrases

### Examples

- in Naming/ folder

## Name Casing

1. snake_case (Python ===> variables, functions, methods)
2. camelCase (Java, JavaScript ===> variables, functions, methods)
3. PascalCase (Python, Java, JavaScript ===> classes)
4. kebab-case (HTML ===> custom HTML elements)

## 1. Naming: Variables, functions and classes

- if it is an object: describe the value

- if it is a number or string: describe the value

- if it is a boolean: should be a question that can be answered as true or false, avoid redundancy

### don't use

- Slangs, unclear abbreviations, disinformation

## 2. Code Structure, Comments and Formatting

** if the code is clean, the comments aren't necessary, with special execeptions **

- Good comments are for example, legal information, a warning and an explanation for what is targeted in a given regex expression, or a TODO note

### Vertical Formatting

- Code should be readable like an essay - top to bottom without too many jumps
- Consider splitting files with multiple concepts (e.g. classes) into multiple files
- Different concepts should be separated by spacing

### Formatting with language-specific considerations

- order and execution depends on the language ability to hoist or not (e.g. Python vs. JavaScript)

## 3. Functions

- limit the number of parameters, use dictionaries or objects as value containers
- single responsability
- don't mix levels of abstraction in a single function
- DRY and avoid unexpected side effects

## 4. Control Stuctures

- prefer positive wording
- avoid deep nesting, use guards and fail fast, or extract control structures into separate functions
- consider polymorphism and factory functions to avoid code duplication
- use real errors instead of synthetic errors replicated with satatements

## 5. Clases, Objects, Data Containers

### Difference between objects and data structures

Objects: hides its internals and exposes a group of methods (API), contains business logic, abstractions over concretions
Data containers: internals are available publicly, does not have API (methods), store and transport data, concretions only

### Why the difference matters?

Becuase if we mix the concepts we end up writting dirty code.

### Classes and Polymorphism

The ability of an object to take different forms

### Cohesion

How much the class methods use the class properties

Aim for highly conhesive classes.
If we have a class which methods don't use any class property, we have a data structure with utility methods, which is fina if that is the intention

### The Law of Demeter

Code in a method may only access direct internals (properties and methods) of:

- the object it belongs to
- objects that are stored in properties of that object
- objects which are received as method parameters
- objects which are created in the method

```js
this.customer.lastPurchase.date; // don't depend on the internals of strangers
```

### SOLID principles

- Single Responsability
- Open-Closed (open for extension but closed for modification)
- Liskov Substitution (objects should replaceable with instances of their subclases without altering the behavior)
- Interface Segregation (many client-specific interfaces are better than one general purpose interface)
- Dependency Inversion (you should depend upon abstractions and not concretions)
