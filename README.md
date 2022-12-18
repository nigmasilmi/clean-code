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
