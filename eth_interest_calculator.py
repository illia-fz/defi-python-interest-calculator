# eth_interest_calculator.py
# Example DeFi script calculating compound interest and connecting to Ethereum via Web3
from web3 import Web3

def calculate_interest(principal: float, rate: float, years: int) -> float:
    """
    Calculates compound interest for a principal amount given a rate and number of years.
    :param principal: initial amount of Ether
    :param rate: annual interest rate (e.g. 0.05 for 5%)
    :param years: number of years
    :return: future value of the principal
    """
    return principal * (1 + rate) ** years

# Example usage
if __name__ == "__main__":
    # Connect to Ethereum (placeholder URL)
    provider_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
    web3 = Web3(Web3.HTTPProvider(provider_url))
    print("Connected to Ethereum:", web3.is_connected())
    
    principal_eth = 1.0  # 1 Ether
    annual_rate = 0.05   # 5% annual interest
    years = 2
    future_value = calculate_interest(principal_eth, annual_rate, years)
    print(f"Future value after {years} years: {future_value} ETH")
