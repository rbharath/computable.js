# Demonstrates how adding validated data to a client is in fact an act of mining that adds tokens to Client wallet

import datamined as dm


data = "ATTAGGACATTTATA"
private_key = "LKSDOP*FU(F*UE(WFJEWFF"

# Create a data validator.
validator = dm.valid.NaiveGenomicValidator()
# Check whether data is valid
assert validator.is_valid(data)

# Create an introductory wallet 
wallet = dm.coins.ExampleWallet()
assert wallet.token_count() == 0

# Now that we know that the validator vouches for the data, we store on the
# client. The act of storing generates coins.
client = dm.data.InsecureFileClient(private_key, wallet)
ledger = client.store(data, validator)
assert client.get_wallet().token_count() > 0
