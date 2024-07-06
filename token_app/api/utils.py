import json
from web3 import Web3
import  requests
import aiohttp
import asyncio
from datetime import datetime
infura_url = "https://polygon-mainnet.infura.io/v3/36eb0f9e8c6042aea22b536a751369af"
web3 = Web3(Web3.HTTPProvider(infura_url))

POLYGONSCAN_API_KEY = '5NZNFGTD7CYA5H6MARNNDGR7RDD2812UTD'
TOKEN_ADDRESS = "0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0"
# Convert to checksum format
TOKEN_ADDRESS = Web3.to_checksum_address(TOKEN_ADDRESS)

TOKEN_ABI = json.loads('''[
    {
        "constant": true,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "name",
        "outputs": [{"name": "", "type": "string"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "symbol",
        "outputs": [{"name": "", "type": "string"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
]''')


contract = web3.eth.contract(address=TOKEN_ADDRESS, abi=TOKEN_ABI)

def get_balance(address):
    address = Web3.to_checksum_address(address)
    balance = contract.functions.balanceOf(address).call()
    return balance / 10**18

def get_balances(addresses):
    addresses = [Web3.to_checksum_address(address) for address in addresses]
    balances = [get_balance(address) for address in addresses]
    return balances

def get_token_info(token_address):
    checksum_address = Web3.to_checksum_address(token_address)
    token_contract = web3.eth.contract(address=checksum_address, abi=TOKEN_ABI)
    name = token_contract.functions.name().call()
    symbol = token_contract.functions.symbol().call()
    total_supply = token_contract.functions.totalSupply().call() / 10**18
    return {"name": name, "symbol": symbol, "totalSupply": total_supply}


def get_token_balance(address):
    url = f"https://api.polygonscan.com/api"
    params = {
        'module': 'account',
        'action': 'tokenbalance',
        'contractaddress': TOKEN_ADDRESS,
        'address': address,
        'tag': 'latest',
        'apikey': POLYGONSCAN_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == '1':  # API call success
        balance = int(data['result']) / (10 ** 18)
        return balance
    else:
        print("Error:", data['message'])
        return 0


def get_top_token_holders(addresses):
    holders = []
    for address in addresses:
        balance = get_token_balance(address)
        holders.append((address, balance))
    holders.sort(key=lambda x: x[1], reverse=True)
    return holders


def get_last_transaction_date(address):
    url = f"https://api.polygonscan.com/api"
    params = {
        'module': 'account',
        'action': 'tokentx',
        'contractaddress': TOKEN_ADDRESS,
        'address': address,
        'page': 1,
        'offset': 1,
        'sort': 'desc',
        'apikey': POLYGONSCAN_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == '1' and data['result']:
        last_tx = data['result'][0]
        timestamp = int(last_tx['timeStamp'])
        date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        return date
    else:
        # print("Error:", data['message'] if 'message' in data else 'No transactions found')
        return "No transactions found"


def get_top_token_holders_with_transactions(addresses):
    holders = []
    for address in addresses:
        balance = get_token_balance(address)
        last_tx_date = get_last_transaction_date(address)
        holders.append((address, balance, last_tx_date))
    holders.sort(key=lambda x: x[1], reverse=True)
    return holders

# async def get_token_balance_info(session, address):
#     url = f"https://api.polygonscan.com/api"
#     params = {
#         'module': 'account',
#         'action': 'tokenbalance',
#         'contractaddress': TOKEN_ADDRESS,
#         'address': address,
#         'tag': 'latest',
#         'apikey': POLYGONSCAN_API_KEY
#     }
#
#     async with session.get(url, params=params) as response:
#         data = await response.json()
#         if data['status'] == '1':  # API call success
#             balance = int(data['result']) / (10 ** 18)
#             return balance
#         else:
#             print("Error:", data['message'])
#             return 0
# async def get_last_transaction_date(session, address):
#     url = f"https://api.polygonscan.com/api"
#     params = {
#         'module': 'account',
#         'action': 'tokentx',
#         'contractaddress': TOKEN_ADDRESS,
#         'address': address,
#         'page': 1,
#         'offset': 1,
#         'sort': 'desc',
#         'apikey': POLYGONSCAN_API_KEY
#     }
#
#     async with session.get(url, params=params) as response:
#         data = await response.json()
#         if data['status'] == '1' and data['result']:
#             last_tx = data['result'][0]
#             timestamp = int(last_tx['timeStamp'])
#             date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
#             return date
#         else:
#             print("Error:", data['message'] if 'message' in data else 'No transactions found')
#             return "No transactions found"
#
#
# async def get_top_token_holders_with_transactions(addresses):
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for address in addresses:
#             balance_task = get_token_balance_info(session, address)
#             tx_date_task = get_last_transaction_date(session, address)
#             tasks.append(asyncio.gather(balance_task, tx_date_task))
#
#         results = await asyncio.gather(*tasks)
#
#         holders = [(address, result[0], result[1]) for address, result in zip(addresses, results)]
#         holders.sort(key=lambda x: x[1], reverse=True)
#         return holders