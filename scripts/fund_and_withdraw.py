from brownie import FundMe
from scripts.helpful_scripts import get_account, deploy_mocks
from scripts.deploy import deploy_fund_me


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print("current entrance fee is:", (entrance_fee))
    print("funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("withdrawing")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()