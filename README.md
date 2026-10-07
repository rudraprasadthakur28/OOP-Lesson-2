# Python OOP Lesson 2

This repository contains my practice for OOP Lesson 2 in Python.

The lesson focuses on working with multiple methods, withdrawal operations, and understanding the difference between class attributes and instance attributes.

## Topics Covered

- Withdrawal Method
- Multiple Methods
- Class Attributes
- Instance Attributes
- Class vs Instance
- Objects and Methods

## Withdrawal Practice

This section contains practice for creating a withdrawal method inside a class.

The method performs a withdrawal operation and updates the object's balance.

Example:

```python
class BankAccount:
    def withdraw(self, amount):
        # Withdrawal logic
        pass
```

## Multiple Methods Practice

A class can contain multiple methods, with each method performing a different operation.

Example:

```python
class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
```

## Class vs Instance

### Class Attribute

A class attribute is shared by all objects of a class.

```python
class Student:
    school = "ABC School"
```

### Instance Attribute

An instance attribute belongs to a particular object.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

## Practice Sections

- Withdrawal Method Practice
- Multiple Methods Practice
- Class Attribute Practice
- Instance Attribute Practice
- Class vs Instance Practice

## Learning Goal

The goal of this lesson is to understand how multiple methods work inside a class and clearly distinguish between class attributes and instance attributes.

## Status

Completed as part of my Python OOP learning journey.