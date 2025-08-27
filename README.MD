# Week 5 Python Assignment

## Overview
This assignment demonstrates the use of Python classes, inheritance, encapsulation, and object-oriented programming concepts through a superhero-themed example.

## Files
- `class.py`: Contains the implementation of the `SuperHero` and `OtherTwin` classes, along with example usage.

## Classes
### SuperHero
Represents a superhero with the following features:
- Attributes: `name`, `real_name`, `power_level`, `custom_color`, `nemesis`, `special_abilities` (public), and `__secret_mission` (private)
- Methods:
  - `fight_crime()`: Prints a message and increases power level based on current value
  - `train()`: Increases power level
  - `reveal_identity()`: Prints the real name
  - `set_secret_mission(mission)`: Sets a private mission
  - `get_secret_mission()`: Returns the private mission

### OtherTwin (inherits from SuperHero)
- Overrides `fight_crime()` to provide a custom message and power increase
- Adds:
  - `super_power()`: Prints a unique super power
  - `secret()`: Sets a humorous secret mission

## Example Usage
The script creates two objects:
- `codeman` (SuperHero)
- `twin` (OtherTwin)

It demonstrates their methods and prints the secret mission of the twin.

## How to Run
1. Make sure you have Python 3 installed.
2. Run the script:
   ```powershell
   python class.py
   ```

## Output Example
```
CodeMan says: 'Yo, you're good!' 💥
CodeTwin prefers debugging over fighting. 🐛🔧
CodeTwin's super power: Debugging anything, even your mood swings 😅
Twin's secret mission: Rob a house... or maybe just rob bugs from your code 🕵️‍♂️
```

---
Feel free to modify the classes or add new superheroes!
