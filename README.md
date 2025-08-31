# Python Learning Repository

This repository contains a comprehensive collection of Python scripts organized by programming concepts and practical examples. The scripts cover fundamental programming concepts, AWS automation with boto3, and JSON parsing techniques.

## 📁 Repository Structure

### 🔧 AWS Automation (boto3/)
Scripts demonstrating AWS automation using the boto3 library.

- **`boto.py`** - Basic S3 bucket listing example with region configuration
- **`boto2.py`** - Enhanced AWS S3 operations and bucket management

### 🔄 For Loops (ForLoop/)
Examples demonstrating different ways to use for loops in Python.

- **`ForLoop.py`** - Basic for loop through a list of fruits
- **`ForLoop2.py`** - For loop with range() function
- **`ForLoop3.py`** - For loop with enumerate() for index and value
- **`ForLoop4.py`** - Nested for loops and loop control
- **`ForLoop5.py`** - Looping through dictionaries using .items() method

### 🔀 If-Else Conditions (If-Else-Conditions/)
Conditional programming examples with if-else statements.

- **`CheckOddEvenNumber.py`** - Determine if a number is odd or even using modulo operator
- **`CheckPositiveNumber.py`** - Check if a number is positive, negative, or zero
- **`InCondition.py`** - Using 'in' operator for membership testing
- **`InputAndCheckPositiveNumber.py`** - User input validation for positive numbers
- **`PrintMessageForDifferentRole.py`** - Role-based message printing using conditions

### 📊 JSON Parsing (JSON-Parsing/)
Comprehensive examples of JSON data handling and parsing.

- **`json-parsing.py`** - Basic JSON string parsing into Python dictionary
- **`json-parsing2.py`** - Working with JSON arrays and nested structures
- **`json-parsing3.py`** - JSON file reading and parsing
- **`json-parsing4.py`** - Creating and writing JSON data
- **`json-parsing5.py`** - Complex AWS EC2 JSON response parsing
- **`json-parsing6.py`** - JSON data validation and error handling

### 🔁 While Loops (WhileLoop/)
Examples of while loop usage and control flow.

- **`WhileLoop.py`** - Basic while loop with counter (includes infinite loop example)
- **`WhileLoop2.py`** - While loop with user input validation
- **`WhileLoop3.py`** - While loop with break and continue statements

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- boto3 library (for AWS automation scripts)
- AWS credentials configured (for boto3 scripts)

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd python

# Install required dependencies
pip install boto3
```

### Running the Scripts
Each script can be run independently:
```bash
# Example: Run a for loop script
python ForLoop/ForLoop.py

# Example: Run an AWS automation script
python boto3/boto.py

# Example: Run a JSON parsing script
python JSON-Parsing/json-parsing.py
```

## 📚 Learning Path

This repository is organized to follow a logical learning progression:

1. **Start with basic loops** (ForLoop/) to understand iteration
2. **Learn conditional logic** (If-Else-Conditions/) for decision making
3. **Master while loops** (WhileLoop/) for more complex control flow
4. **Practice JSON parsing** (JSON-Parsing/) for data handling
5. **Apply concepts to AWS automation** (boto3/) for real-world applications

## 🎯 Use Cases

- **Learning Python fundamentals** - Basic programming concepts
- **AWS automation** - Cloud infrastructure management
- **Data processing** - JSON data manipulation and parsing
- **Automation scripts** - Practical examples for real-world scenarios

## 📝 Notes

- All scripts include detailed comments explaining the concepts
- AWS scripts require proper credentials and permissions
- Some scripts demonstrate both correct and incorrect practices for learning purposes
- The repository serves as both a learning resource and a reference for common Python patterns

## 🤝 Contributing

Feel free to add more examples or improve existing scripts. Please ensure all new scripts include proper documentation and comments.

## 📄 License

This repository is for educational purposes. Use the scripts responsibly and in accordance with AWS best practices.
