def read_expensive(filename):
    try:
        with open(filename,'r') as file:
            line=file.readlines()
        return line
    except FileNotFoundError:
        print(f"errror:file{filename} not found")
        return []

def calculate_summary(lines):
    total_amount=0
    Category_summary={}
    Date_summary={}
    for line in lines[1:]:
        try:
            Date, Category, Amount=line.strip().split(',')
            Amount=int(Amount)
            total_amount+=Amount
            if Category in Category_summary:
                Category_summary[Category]+=Amount
            else:
                Category_summary[Category]=Amount    
            if Date in Date_summary:
                Date_summary[Date]+=Amount
            else:
                Date_summary[Date]=Amount    
        except ValueError:  
            print(f"Skipping malformed line: {line.strip()}")   
    return total_amount,Category_summary,Date_summary  


#------testing file-----------
input_file=input("enter file name:")
output_file=input("enter file name to create an output file:")
file=read_expensive(input_file)
if file:
    total,calculate_summary,Date_summary=calculate_summary(file)
    print("================= Expense Summary =================")
    print(f"Total Monthly Expenses:${total}\n")
    print("Category wise breakdown:")
    for cat,amt in calculate_summary.items():
        print(f"{cat}:{amt}")
    # for date,amt in Date_summary.items():
    #     print(f"{date}:{amt}")
    highest_day = max(Date_summary, key=Date_summary.get)
    print(f"Highest Spending Day: {highest_day} (₹{Date_summary[highest_day]})")    


#Write results to output file
    with open(output_file,'w',encoding='utf-8') as out:
        out.write("================= Expense Summary =================\n")
        out.write(f"Source File: {input_file}\n")
        out.write(f"Total Monthly Expenses:${total}\n")
        out.write("Category wise breakdown:\n")
        for cat,amt in calculate_summary.items():
         out.write(f"{cat}:{amt}\n")
        out.write(f"\nHighest Spending Day: {highest_day} (₹{Date_summary[highest_day]})\n")
    print(f"\n✅ Report successfully saved to '{output_file}'")