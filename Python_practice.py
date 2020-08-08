print("Hello World")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

my_votes = 3330
total_votes = 15590
percentage_votes = (my_votes / total_votes) * 100
message = (f"You received {my_votes:,} votes. "
            f"the total number of votes in the election was {total_votes:,}. "
            f"You had {my_votes/total_votes*100:.2f}% of the votes"
)
print(message)
print(f"I received {my_votes/total_votes*100}% of the total votes. ")