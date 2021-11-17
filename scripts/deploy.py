# deploy.py
print("line 0")
import brownie
from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIROMENTS,
)

DECIMALS = 18
STARTING_PRICE = 2000
print("line 1")


def deploy_fund_me():
    account = get_account()
    print("line2")
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
        print("line 3")
    else:
        deploy_mocks()
        print("line 4")
        price_feed_address = MockV3Aggregator[-1].address


    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()
