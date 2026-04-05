# Expression Calculator (Python)

A command-line calculator that evaluates mathematical expressions with:
- Operator precedence (BODMAS)
- Parentheses support
- Decimal numbers
- Modulo operations

## Features
- Supports +, -, *, /, %
- Handles nested parentheses
- Input validation (invalid characters, wrong expressions)
- Division by zero handling

## Example

Input:
2*(3+4)

Output:
14

## How it works
1. Tokenizes input string
2. Evaluates inner parentheses first
3. Applies operator precedence
4. Returns final result

## Run the project

python calculator.py