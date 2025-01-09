# Example dataset: wealth data for citizens
citizens_wealth = {
    "Alice": {"bank_account": 1500, "investments": 10000, "properties": 30000},
    "Bob": {"bank_account": 2000, "investments": 15000, "properties": 25000},
    "Charlie": {"bank_account": 3000, "investments": 5000, "properties": 10000},
}

def find_wealthiest_citizen(wealth_data):
    wealthiest_citizen = None
    max_wealth = 0
    
    for citizen, categories in wealth_data.items():
        total_wealth = sum(categories.values())  # Calculate total wealth for the citizen
        if total_wealth > max_wealth:
            max_wealth = total_wealth
            wealthiest_citizen = citizen
    
    return wealthiest_citizen, max_wealth

# Find and display the wealthiest citizen
wealthiest, wealth = find_wealthiest_citizen(citizens_wealth)
print(f"The wealthiest citizen is {wealthiest} with a total wealth of R {wealth}.")
