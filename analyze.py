# Place code below to do the analysis part of the assignment.

import csv
import os

platform_agnostic_file_path = os.path.join('data', 'clean_data.csv')
csv_reader = csv.DictReader(open(platform_agnostic_file_path, 'r'))
averages_list = []

# Convert the CSV values to a list for easier processing
data = list(csv_reader)

#Calculate the number of remainder years for decades
remainder = len(data)%10

# build a list to store the year
year = []
new_year = []
for value in data:
    year += [value['Year']]
for i in range(0, len(year), 10):
    new_year += [year[i]]



# Iterate through each column in the CSV file
for column_name in csv_reader.fieldnames[1:-1]:
    # Calculate the average of every 10 values in one column without overlapping
    values_to_add = [float(row[column_name]) for row in data]
    column_averages = []

    for i in range(0, len(values_to_add) - remainder, 10):
        avg = sum(values_to_add[i:i+10]) / min(10, len(values_to_add) - i)
        column_averages.append(float(format(avg, '.2f')))

        # Build a dictionary to store the result
        dic = {}
        for i in range(len(column_averages)):
            dic[f"{new_year[i]}s"] = column_averages[i]

 
    averages_list.append({column_name: column_averages})

# Calculate the annual average
first_12_rows = averages_list[:12]  # Select the first 12 rows

annual_decades = []

for i in range(len(column_averages)):
    column_sum = 0
    for element in first_12_rows:
        for value in element.values():
            column_sum += value[i]
    annual_decades.append(float(format(column_sum/12, '.2f')))
dic2 = {}
for i in range(len(column_averages)):
    dic2[f"{new_year[i]}s"] = annual_decades[i]

# print the annual mean
print('Average Temperature Difference by Decade (deg-F)\n')
print(f"Annual Average: {dic2}\n")



# Print the averages for each column in list format
for column_data in averages_list:
    for column_name, column_avg in column_data.items():
        print(f"Averages for {column_name}: {dic}\n")