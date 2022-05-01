from art import logo

print(logo)
next_bidder = True
bids = {}

while next_bidder:
    name = input("Inform name of the bidder: ")
    price = float(input("Whats the offer? $"))
    bids[name] = price

    another_bidder = input("Another person to make a bid? Yes or no? ").lower()
    if another_bidder == "no":
        next_bidder = False
    else:
        print("\n"*80)


def highest_bidder(bids_):
    bidder_name, higher_bid = "", 0
    for key in bids_:
        value = bids_[key]
        if value > higher_bid:
            higher_bid, bidder_name = value, key
    print(f"\n\nThe winner is {bidder_name} with the bid of ${higher_bid}")


# Simpler way
high_bidder = max(bids, key=bids.get)
print(f"\n\nThe winner is {high_bidder} with the bid of ${bids[high_bidder]}")

# Function way
highest_bidder(bids)
