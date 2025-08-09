print("Python is working for me in VS code")

# test_full_setup.py

# 1. Basic print
print("✅ Python is working in VS Code!")

# 2. Simple math
a = 10
b = 5
print(f"{a} + {b} = {a + b}")

# 3. Import a standard library module
import datetime
print("Current date & time:", datetime.datetime.now())

# 4. File write & read
with open("sample.txt", "w") as f:
    f.write("Hello from Python!")

with open("sample.txt", "r") as f:
    print("File contents:", f.read())
