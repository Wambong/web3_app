
from django.http import JsonResponse
from asgiref.sync import async_to_sync
from django.shortcuts import render
from .forms import AddressForm, AddressesForm, TopNForm, TokenAddressForm, TopNFormInfo
from .utils import get_balance, get_balances, get_token_info,  get_top_token_holders, get_top_token_holders_with_transactions

def get_balance_view(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            balance = get_balance(address)
            return render(request, 'balance.html', {'form': form, 'balance': balance})
    else:
        form = AddressForm()
    return render(request, 'balance.html', {'form': form})

def get_balance_batch_view(request):
    if request.method == 'POST':
        form = AddressesForm(request.POST)
        if form.is_valid():
            addresses = form.cleaned_data['addresses'].split()
            balances = get_balances(addresses)
            return render(request, 'balances.html', {'form': form, 'balances': zip(addresses, balances)})
    else:
        form = AddressesForm()
    return render(request, 'balances.html', {'form': form})

def get_token_info_view(request):
    if request.method == 'POST':
        form = TokenAddressForm(request.POST)
        if form.is_valid():
            token_address = form.cleaned_data['token_address']
            token_info = get_token_info(token_address)
            return render(request, 'token_info.html', {'form': form, 'token_info': token_info})
    else:
        form = TokenAddressForm()
    return render(request, 'token_info.html', {'form': form})


KNOWN_ADDRESSES = [
    "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619",
    "0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0",
    "0x51f1774249Fc2B0C2603542Ac6184Ae1d048351d",
    '0x4830AF4aB9cd9E381602aE50f71AE481a7727f7C',
    "0x54bA15efe1b6D886bA4Cd5C5837240675BD0D43a",
    "0xb91dd8225Db88dE4E3CD7B7eC538677A2c1Be8Cb",
    "0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359",
    "0xc2132d05d31c914a87c6611c10748aeb04b58e8f",

]
def top_token_holders_view(request):
    top_holders = []
    if request.method == 'POST':
        form = TopNForm(request.POST)
        if form.is_valid():
            top_n = form.cleaned_data['n']
            top_holders = get_top_token_holders(KNOWN_ADDRESSES)[:top_n]
            return render(request, 'top_token_holders.html', {'form': form, 'top_holders': top_holders})
    else:
        form = TopNForm()
    return render(request, 'top_token_holders.html', {'form': form})


def top_token_holders_info(request):
    top_holders = []
    if request.method == 'POST':
        form = TopNFormInfo(request.POST)
        if form.is_valid():
            top_n = form.cleaned_data['n']
            top_holders = get_top_token_holders_with_transactions(KNOWN_ADDRESSES)[:top_n]
            return render(request, 'top_token_holders_info.html', {'form': form, 'top_holders': top_holders})
    else:
        form = TopNForm()
    return render(request, 'top_token_holders_info.html', {'form': form})