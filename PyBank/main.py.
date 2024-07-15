import csv

with open('Resources/budget_data.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    next(csv_reader, None)

    # Initialize variables
    total = 0
    total_months = 0
    previous_value = None
    changes = []
    max_increase = None
    max_increase_month = None
    max_decrease = None
    max_decrease_month = None

    # Iterate over the rows in the CSV file
    for row in csv_reader:
        # Extract month and convert the relevant cell to a float or int
        month = row[0]
        value = int(row[1]) 
        total += value
        total_months += 1
            
        # Calculate the change if not the first month
        if previous_value is not None:
            change = value - previous_value
            changes.append(change)
            
            # Track maximum increase and decrease
            if max_increase is None or change > max_increase:
                max_increase = change
                max_increase_month = month
            if max_decrease is None or change < max_decrease:
                max_decrease = change
                max_decrease_month = month
            
        # Update the previous value
        previous_value = value
      
    # Calculate the average change
    average_change = round(sum(changes) / len(changes,),2) if changes else 0

    # Output results
    print("Financial Analysis")
    print("Total Months:", total_months)
    print("Total: $", total)
    print("Average Change: $", average_change)
    print("Greatest Increase in Profits:", max_increase_month, "($", max_increase, ")")
    print("Greatest Decrease in Profits:", max_decrease_month, "($", max_decrease, ")")
