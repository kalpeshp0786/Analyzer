# NumPy Analyzer

## Project Overview

NumPy Analyzer is a Python project developed using Object-Oriented Programming (OOP) and the NumPy library. It allows users to create NumPy arrays and perform different mathematical, array manipulation, searching, sorting, filtering, and statistical operations through a menu-driven program.

The program supports 1D, 2D, and 3D arrays and provides different operations to analyze numerical data.

## Project Objectives

- To understand NumPy arrays.
- To learn Object-Oriented Programming in Python.
- To perform mathematical operations on arrays.
- To understand indexing and slicing.
- To combine and split arrays.
- To search, sort, and filter array values.
- To calculate statistical values.
- To use properties, getters, setters, class methods, and static methods.

## Features

### 1. Create a NumPy Array

The program allows users to create three types of arrays:

- 1D Array
- 2D Array
- 3D Array

Users enter the required dimensions and numerical values to create an array.

### 2. Indexing and Slicing

- Select an element using its index.
- Extract a range of elements from a 1D array.
- Select specific rows and columns from a 2D array.
- Use a custom range parser to convert range text into Python slice objects.

### 3. Mathematical Operations

The program supports the following operations:

- Addition
- Subtraction
- Multiplication
- Division
- Dot Product
- Matrix Multiplication

These operations are performed using NumPy functions.

### 4. Combine and Split Arrays

- Combine arrays using vertical stacking.
- Split an array into multiple sections.
- Display each split array separately.

### 5. Search, Sort, and Filter

**Search:** Find the locations of a specified value in an array.

**Sort:** Sort array values along the last axis.

**Filter:** Filter values using comparison conditions such as:

- `> 20`
- `< 50`
- `>= 30`
- `<= 100`
- `!= 10`
- `== 25`
- `= 25`

### 6. Statistical Operations

The program calculates the following statistical values:

- Sum
- Mean
- Median
- Standard Deviation
- Variance
- Minimum Value
- Maximum Value
- Percentile

## OOP Concepts Used

### Class and Object

The `DataAnalytics` class contains methods for performing operations on NumPy arrays.

An object is created in the `main()` function:

```python
analyzer = DataAnalytics()
```

### Encapsulation

The array is stored in a private attribute:

```python
self.__data
```

The `data` property provides access to the array and allows users to update it.

### Constructor

The `__init__()` method initializes the array and increments the total analyzer count.

### Property and Setter

The `@property` decorator is used to access the array, while `@data.setter` is used to update it.

### Private Method

The `__validate_data()` method checks whether an array has been created before an operation is performed.

### Class Variable and Class Method

The class variable `total_analyzers_created` counts the number of `DataAnalytics` objects created.

The `get_instance_count()` class method returns this count.

### Static Method

The `parse_range()` static method converts range text into a Python slice object.

## Technologies Used

- Python
- NumPy
- Object-Oriented Programming

## Requirements

Python must be installed on your computer.

The NumPy library is required to run this project.

Install NumPy using:

```bash
pip install numpy
```

## Project Structure

```text
NumPy-Analyzer/
│
├── numpy_analyzer.py
└── README.md
```

The Python filename `numpy_analyzer.py` is a suggested filename. Save your project code using this name or update the run command to match your actual filename.

## How to Run the Project

### Step 1: Install NumPy

Open the terminal and run:

```bash
pip install numpy
```

### Step 2: Save the Python Code

Save the provided code in a Python file, for example:

```text
numpy_analyzer.py
```

### Step 3: Run the Program

Open the terminal in the project folder and execute:

```bash
python numpy_analyzer.py
```

### Step 4: Select an Operation

The main menu displays these options:

```text
Main Menu
1. Create a Numpy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
```

Enter the option number to perform the required operation.

## Input Details

| Operation | Required Input |
|---|---|
| Create 1D Array | Number of elements and values |
| Create 2D Array | Rows, columns, and values |
| Create 3D Array | Dimensions and values |
| Indexing | Comma-separated indices |
| Slicing | Start and end ranges |
| Mathematical Operations | Values for the second array |
| Combine Arrays | Values for the second array |
| Split Array | Number of sections |
| Search | Value to search |
| Sort | No additional input |
| Filter | Comparison condition |
| Percentile | Percentile between 0 and 100 |

## Learning Outcomes

After completing this project, I learned:

- How to create and manipulate NumPy arrays.
- How to work with 1D, 2D, and 3D arrays.
- How to perform mathematical operations using NumPy.
- How to use indexing and slicing.
- How to combine and split arrays.
- How to search, sort, and filter numerical values.
- How to calculate statistical values.
- How to use encapsulation and properties in Python.
- How to implement class methods and static methods.
- How to build a menu-driven Python application.

## Conclusion

NumPy Analyzer is a menu-driven Python project that demonstrates the use of NumPy and Object-Oriented Programming. It provides practical experience with array creation, mathematical calculations, array manipulation, searching, sorting, filtering, and statistical analysis.

This project helps develop a better understanding of Python programming and numerical data analysis.

## Author

Meet Prajapati