# Place code below to do the munging part of this assignment.

# Read the raw data file 
import os
platform_agnostic_file_path = os.path.join('data', 'GLB.Ts+dSST.txt')
with open(platform_agnostic_file_path, 'r')as file:
    lines = file.readlines()


# List to store the cleaned data
clean_data = []


# Finding the header row of the table
for line in lines:
    if line.startswith(' ') or line == '\n':
        continue
    line = line.strip()

    # Using ',' to replace space in the header row to make it clear in csv format
    tokens = [token for token in line.split() if token] 
    line = ",".join(tokens)

    # Adding header row in clean_data as header row
    clean_data.append(line)
    break


for line in lines:

    # Moving the line with notes and repeated header row
    if line[0].isnumeric():

        # Handle the missing data by deleting the whole row, 
        # since the number of the data with missing value is relatively smaller 
        # than the number of the whole data
        if '*' not in line:

            # Convert temperature anomalies to Farenheit (deviding 100 and then multiply that result by 1.8(=9/5))
            temp = line.split()
            
            # Build a string to store cleaned value
            temp_new = ''

            for i in range(len(temp)):

                # handle all data exclude year
                if i in range(1, len(temp)-1):
            
                    new = ((float(temp[i]))/100)*1.8
                    
                    # format the data 
                    temp[i]  = str(format(new, ".1f"))

                    # Using ',' to split data which can make data more clear in csv format
                    temp_new += (temp[i] +',')
                
                # handle year
                else:
                    # Using ',' to split data which can make data more clear in csv format
                    temp_new += (temp[i] +',')


            clean_data.append(temp_new)

# Save the data in clean_data.csv in data file
with open('/Users/quanquanxie/Documents/GitHub/2-data-munging-Victoriaxqq/data/clean_data.csv', 'w') as f:
    f.write('\n'.join(clean_data))





