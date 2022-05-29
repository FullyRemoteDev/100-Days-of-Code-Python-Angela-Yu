import os
import art

bid_details = {}
bidder_name = ''
bidder_bid = 0
winning_bidder = ''
winning_bid = 0

user_choice = 'yes'
bids_continue = True

print(art.logo)

while bids_continue:
    bidder_name = input("What is your name?: ")
    bidder_bid = int(input("What is your bid?: $"))

    bid_details[bidder_name] = bidder_bid

    user_choice = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if user_choice == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        bids_continue = True
    elif user_choice == 'no':
        bids_continue = False


for name in bid_details:
    if bid_details[name] > winning_bid:
        winning_bid = bid_details[name]
        winning_bidder = name
print(
    f"\nThe winner is {winning_bidder} with a bid of ${winning_bid}\n")
