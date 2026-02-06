# Password Strength Validator with SQLite

A secure, modular password strength checker written in Python.  
It evaluates passwords based on length, character variety, and whether they match or contain commonly used weak passwords stored in a local SQLite database.

## Features

- **Basic checks**:
  - Minimum length (configurable, default: 10 characters)
  - At least one digit
  - Optional: uppercase, lowercase, special characters
 
## Technologies

- **Python** 3.8+
- No external packages required

## Future Improvements
- Load weak passwords from rockyou.txt or HaveIBeenPwned-style list.
- Add substring/partial-match checking
- Numerical scoring system 
