from art import logo

print(logo)

bids = {}

def print_winner():
  highest_bidder = {'name': 'none', 'bid': 0}
  for bid in bids:
    if bids[bid] > highest_bidder['bid']:
      highest_bidder['name'] = bid
      highest_bidder['bid'] = bids[bid]

  print(f"The winner is {highest_bidder['name']} with a bid of     {highest_bidder['bid']}")

def add_bid():
  bidder_name = input("What is your name?")
  bidder_bid = int(input("What is your bid?"))  
  bids[bidder_name] = bidder_bid
  bid_again = input("Any other bids?")
  if bid_again == "Y":
    add_bid()
  else:
    print_winner()
add_bid()


