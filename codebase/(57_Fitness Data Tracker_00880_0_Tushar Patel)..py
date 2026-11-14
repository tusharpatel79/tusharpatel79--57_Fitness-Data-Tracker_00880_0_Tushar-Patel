
steps_list = []
calories_list = []

daily_goal = 10000


def add_record():
    try:
        steps = int(input("Enter steps walked: "))
        calories = int(input("Enter calories burned: "))

        if steps < 0:
            print("Invalid steps. Enter a non-negative whole number.")
            print("Record not saved.")
            return

        if calories < 0:
            print("Invalid calories. Enter a non-negative whole number.")
            print("Record not saved.")
            return

        steps_list.append(steps)
        calories_list.append(calories)

        day = len(steps_list)
        percentage = (steps / daily_goal) * 100

        if steps >= daily_goal:
            goal = "Yes"
        else:
            goal = "No"

        print("Record saved for Day", day,
              ". Goal achieved:", goal,
              f"({percentage:.2f}% of goal)")

    except ValueError:
        print("Invalid input. Please enter whole numbers.")
        print("Record not saved.")


def calculate_average():
    if len(steps_list) == 0:
        return 0

    total = sum(steps_list)
    average = total / len(steps_list)

    return average


def calculate_total_calories():
    return sum(calories_list)


def find_best_day():
    if len(steps_list) == 0:
        return 0, 0

    highest_steps = max(steps_list)
    best_day = steps_list.index(highest_steps) + 1

    return best_day, highest_steps


def show_summary():
    if len(steps_list) == 0:
        print("No fitness records available.")
        return

    average = calculate_average()
    total_calories = calculate_total_calories()
    best_day, highest_steps = find_best_day()

    goal_days = 0

    for steps in steps_list:
        if steps >= daily_goal:
            goal_days += 1

    total_days = len(steps_list)

    print("\n----- Weekly Fitness Summary -----")
    print(f"Average steps: {average:.2f} | Total calories: {total_calories} | Best day: Day {best_day} ({highest_steps} steps) | Goal days: {goal_days}/{total_days}")


def calculate_bmi():
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Invalid weight or height.")
            return

        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"BMI: {bmi:.2f} | Category: {category}")

    except ValueError:
        print("Please enter valid numeric values.")


def show_chart():
    if len(steps_list) == 0:
        print("No records available to display chart.")
        return

    try:
        import matplotlib.pyplot as plt

        days = []

        for i in range(len(steps_list)):
            days.append("Day " + str(i + 1))

        plt.bar(days, steps_list, label="Daily Steps")
        plt.axhline(y=daily_goal, color="red",
                    linestyle="--", label="10000 Step Goal")

        plt.title("Daily Steps")
        plt.xlabel("Days")
        plt.ylabel("Number of Steps")
        plt.legend()
        plt.tight_layout()
        plt.show()

    except ImportError:
        print("Matplotlib is not installed.")
        print("Install it using: python3 -m pip install matplotlib")


while True:

    print("===== FITNESS DATA TRACKER =====")
    print("1. Add Record")
    print("2. Weekly Summary")
    print("3. Calculate BMI")
    print("4. Show Steps Chart")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_record()

    elif choice == "2":
        show_summary()

    elif choice == "3":
        calculate_bmi()

    elif choice == "4":
        show_chart()

    elif choice == "5":
        print("Thank you for using Fitness Data Tracker!")
        break

    else:
        print("Invalid choice. Please select from 1 to 5.")
