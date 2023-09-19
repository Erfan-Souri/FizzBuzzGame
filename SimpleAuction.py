# The auction
# You can type in as many persons and their bids to this program, and program picks the highest bidder
# and shows their name using python dictionaries

bidders = {}


def add_bidder(bidder_name, bidder_bid):
    bidders[bidder_name] = bidder_bid


last_person = False
while not last_person:
    name = input("Please enter your name:\n")
    bid = int(input("Please enter your bid:\n"))
    add_bidder(bidder_name=name, bidder_bid=bid)
    more_people = input("Are there any more people? type 'yes' or 'no'")
    if more_people == "no" or more_people == "n":
        last_person = True

winner_bid = 0
winner_name = ""
for person in bidders:
    if bidders[person] > winner_bid:
        winner_bid = bidders[person]
        winner_name = person

print(bidders)
print(f"The winner is {winner_name} with {winner_bid}$")
