# 1. Batch input data: A list of transaction amounts received today
transactions = [149.75, 42.00, 310.50, 18.25, 89.90]

# 2. Pipeline metrics accumulators
total_gross = 0.0
total_fees = 0.0
total_payout = 0.0


print("-- Processing Batch Transactions ---")

for idx, amount in enumerate(transactions, start=1):
    fee = amount * 0.05
    net = amount - fee
    
    # Accumulate running totals
    total_gross += amount
    total_fees += fee
    total_payout += net
    
    print(f"Txn #{idx}: Gross=${amount:6.2f} | Fee=${fee:5.2f} | Net=${net:6.2f}")
    
# 4. Final batch summary
print("--------------------------------")
print(f"Total Transactions Processed: {len(transactions)}")
print(f"Total Gross Volume:           ${total_gross:.2f}")
print(f"Total Fees Collected:         ${total_fees:.2f}")
print(f"Total Net Payouts:            ${total_payout:.2f}")
