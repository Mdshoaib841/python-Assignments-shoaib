def read_employee(filename):
    try:
        with open(filename, "r") as file:
            line = file.readlines()
        return line
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return []


def validate(file_data):
    invalid_rows = []
    valid_rows = []

    for line in file_data[1:]:  # skip header
        row = line.strip()
        if not row:
            continue

        try:
            EmployeeID, EmployeeName, Department, Rating = row.split(",")
        except ValueError:
            invalid_rows.append(f'"{row}" -> Wrong number of fields')
            continue

        if not EmployeeID.strip().isdigit():
            invalid_rows.append(f'"{row}" -> EmployeeID is not numeric')
            continue

        if EmployeeName.strip() == "":
            invalid_rows.append(f'"{row}" -> EmployeeName cannot be empty')
            continue

        if Department.strip() == "":
            invalid_rows.append(f'"{row}" -> Department cannot be empty')
            continue

        try:
            r = float(Rating)
            if not (1.0 <= r <= 5.0):
                invalid_rows.append(f'"{row}" -> Rating must be between 1.0 and 5.0')
                continue
        except ValueError:
            invalid_rows.append(f'"{row}" -> Rating is not a valid float')
            continue

        valid_rows.append(row)

    return valid_rows, invalid_rows


def print_invalid_rows(invalid_rows):
    with open("error_log.txt", "w") as log:
        for item in invalid_rows:
            log.write(f"Invalid row: {item}\n")
    print("error_log.txt has been created for invalid rows.")


def print_valid_rows(valid_rows):
    if not valid_rows:
        print("No valid data found!")
        return

    total_valid = len(valid_rows)

    dept_rating = {}
    highest_rating = 0
    top_emp = None

    for row in valid_rows:
        EmployeeID, EmployeeName, Department, Rating = row.split(",")
        Rating = float(Rating)

        if Rating > highest_rating:
            highest_rating = Rating
            top_emp = (EmployeeName.strip(), Department.strip(), Rating)

        if Department in dept_rating:
            dept_rating[Department].append(Rating)
        else:
            dept_rating[Department] = [Rating]  # store as list

    with open("performance_summary.txt", "w") as file:
        file.write("--- VALID ROWS ---\n")
        file.write(f"Total Valid Employees: {total_valid}\n\n")

        file.write("Average Rating by Department:\n")
        for Department, ratings in dept_rating.items():
            avg = sum(ratings) / len(ratings)
            file.write(f"{Department}: {avg:.2f}\n")

        file.write("\n" + "*" * 34 + "\n")
        file.write("Top Performer:\n")
        file.write(f"Employee Name : {top_emp[0]}\n")
        file.write(f"Department: {top_emp[1]}\n")
        file.write(f"Rating :{top_emp[2]}\n")
    print("profile_summary.txt has been created for Valid rows.")


# -MAIN PROGRAM -

input_file = input("Enter file name to read: ")
file_data = read_employee(input_file)

if not file_data:
    print("No file to process. Exiting...")
else:
    valid_rows, invalid_rows = validate(file_data)

    if invalid_rows:
        print_invalid_rows(invalid_rows)

    if valid_rows:
        print_valid_rows(valid_rows)
