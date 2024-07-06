# import requests
# from web3 import Web3
# import json
# url = "https://raw.githubusercontent.com/maticnetwork/polygon-token-list/main/src/tokens/polygonTokens.json"
# response = requests.get(url)
# tokens_data = json.loads(response.text)
# for token in tokens_data:
#     print(f"Token Name: {token['name']}, Address: {token['address']}")
#
# #
# # def get_token_balance(w3, token_address, owner_address):
# #     # ABI for ERC20 standard functions
# #     erc20_abi = {
# #         "constant": True,
# #         "inputs": [{"name": "_owner", "type": "address"}],
# #         "name": "balanceOf",
# #         "outputs": [{"name": "", "type": "uint256"}],
# #         "payable": False,
# #         "stateMutability": "view",
# #         "type": "function"
# #     }
# #
# #     # Create contract instance
# #     checksum_address = Web3.to_checksum_address(token_address)
# #     contract = w3.eth.contract(address=checksum_address, abi=[erc20_abi])
# #
# #     # Call balanceOf function
# #     checksum_owner_address = Web3.to_checksum_address(owner_address)
# #     balance = contract.functions.balanceOf(checksum_owner_address).call()
# #
# #     return balance
# #
# #
# # # Initialize Web3 with Infura provider
# # w3 = Web3(Web3.HTTPProvider('https://polygon-mainnet.infura.io/v3/36eb0f9e8c6042aea22b536a751369af'))
# #
# # # URL of the JSON file containing the token list
# # url = "https://raw.githubusercontent.com/maticnetwork/polygon-token-list/main/src/tokens/polygonTokens.json"
# #
# # # Send a GET request to the URL
# # response = requests.get(url)
# #
# # # Parse the JSON content of the response
# # tokens_data = json.loads(response.text)
# #
# # # Replace with the actual owner address
# # owner_address = '0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0'
# #
# # # Fetch and print balances for each token
# # for token in tokens_data:
# #     balance = get_token_balance(w3, token['address'], owner_address)
# #     if balance > 0:
# #         print(f"Balance of {token['name']} ({token['address']}) for {owner_address}: {balance} tokens")

import re

def is_valid_polygon_address(address):
    pattern = r'^0x[a-fA-F0-9]{40}$'
    return bool(re.match(pattern, address))

# Test the function with a valid Polygon MATIC address
print(is_valid_polygon_address("0x6e910B4503B5C2576b1395ed3461c58721C09195"))  # Should return True
