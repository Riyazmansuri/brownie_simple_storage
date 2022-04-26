from distutils.command.config import config
from lib2to3.pgen2.literals import simple_escapes
from brownie import SimpleStorage, accounts
from eth_account import Account


def test_deploy():
    # Arrange
    # account = accounts[0]
    Account = get_account()
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    starting_value = simple_storage.store(expected, {"from": account})
    # assert
    assert expected == simple_storage.retrieve()
