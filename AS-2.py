# =====================================================
# Session 2 Assignment
# Control Flow & Error Handling
# =====================================================

# ==========================================
# TASK A
# ==========================================

print("TASK 1")
print("This program will enter a number to determine:")
print("- Positive, Negative, or Zero")
print("- Even or Odd")
print()

try:
    number = int(input("Enter a number: "))

    # Check positive, negative, or zero
    if number > 0:
        print("Number is Positive")
    elif number < 0:
        print("Number is Negative")
    else:
        print("Number is Zero")

    # Check even or odd
    if number % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")

except ValueError:
    print("Invalid input! Please enter a valid number.")

print("\n" + "=" * 50 + "\n")


# ==========================================
# TASK B
# ==========================================

print("TASK 2")
print("This program will:")
print("- Enter up to 5 numbers")
print("- Calculate the Sum")
print("- Count Positive Numbers")
print("- Count Negative Numbers")
print("- Stop if you enter 0")
print("- Skip invalid inputs")
print()

total = 0
positive_count = 0
negative_count = 0

for i in range(1, 6):

    try:
        number = float(input(f"Enter number {i}: "))

        # Stop if user enters 0
        if number == 0:
            print("Stopped early because you entered 0.")
            break

        # Add to total
        total += number

        # Count positives and negatives
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1

    except ValueError:
        print("Invalid input! Skipping...")
        continue

print("\nSummary:")
print(f"Sum = {total}")
print(f"Positive numbers = {positive_count}")
print(f"Negative numbers = {negative_count}")

print("\n" + "=" * 50 + "\n")



# ==========================================
# TASK C
# ==========================================

print("TASK 3")
print("This program analyzes exam scores and classifies them.")
print("Please enter 6 exam scores.")
print()

scores = []

# Get 6 scores from the user
for i in range(1, 7):

    while True:
        try:
            score = int(input(f"Enter score {i}: "))

            # Validate score range
            if score < 0 or score > 100:
                print("Score must be between 0 and 100.")
                continue

            scores.append(score)
            break

        except ValueError:
            print("Invalid input! Please enter a number.")

excellent = 0
good = 0
average = 0
poor = 0

print("\nScore Classification:")

for score in scores:

    if score >= 90:
        print(f"Score {score}: Excellent")
        excellent += 1

    elif score >= 75:
        print(f"Score {score}: Good")
        good += 1

    elif score >= 60:
        print(f"Score {score}: Average")
        average += 1

    else:
        print(f"Score {score}: Poor")
        poor += 1

print("\nSummary:")
print(f"Excellent: {excellent}")
print(f"Good: {good}")
print(f"Average: {average}")
print(f"Poor: {poor}") 


# ==========================================
# BONUS CHALLENGE
# ==========================================
print()
print("BONUS CHALLENGE")
print("Enter numbers separated by commas. ex (10.20,-30,30,0)")
print("The program will count positive, negative, and zero values.")
print()

positive = 0
negative = 0
zero = 0

while True:

    data = input("Enter numbers separated by commas: ")

    if data.strip() == "":
        print("Input cannot be empty. Try again.")
        continue

    entries = data.split(",")

    for item in entries:

        item = item.strip()

        try:
            number = float(item)

            if number > 0:
                positive += 1

            elif number < 0:
                negative += 1

            else:
                zero += 1

        except ValueError:
            print(f"Invalid entry '{item}'. Skipping...")
            continue

    break

print("\nSummary:")
print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Zero: {zero}")
print()
 
