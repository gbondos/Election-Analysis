# Open the data
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

import datetime
now = datetime.datetime.now()
print(f"The time right now is {now} o'clock!")


"""
Direct path method
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

"""

"""
Indirect path method

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)
"""
"""
import os
import csv 

file_to_save = os.path.join("Analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe \nDenver \nJefferson \n")
"""

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    print(election_data)

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data) # file reader is an iterator
    # Print the header row.
    headers = next(file_reader)
    print(headers)
    # for row in file_reader:
    #     print(row)