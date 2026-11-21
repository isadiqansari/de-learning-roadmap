# 1. Storing incoming raw transaction data
customer_name = "Alex Johnson"
transaction_id = 10492
amount = 149.75
is_verified = True

# 2. Transforming data: Calculate a 5% processing fee and the final payout
fee = amount * 0.05
net_payout = amount - fee

# 3. Outputting formatted summary
print("--- Transaction Summary ---")
print(f"Customer:    {customer_name}")
print(f"Order ID:    {transaction_id}")
print(f"Gross:       ${amount}")
print(f"Fee (5%):    ${fee:.2f}")
print(f"Net Payout:  ${net_payout:.2f}")
print(f"Status:      {'Verified' if is_verified else 'Pending'}")