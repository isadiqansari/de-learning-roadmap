# 1. Define a reusable transformation fuction
def calculate_payout(gross_amount, fee_rate=0.05):
    """Takes a gross dollar amount and returns net payout after platform fees."""
    fee = round(gross_amount * fee_rate, 2)
    net = round(gross_amount - fee, 2)
    return net

# 2. Define a reusable validation function
def is_valid_transaction(record):
    """Returns True if the record meets data quality rules, otherwise False."""
    if record["status"] != "completed":
        return False
    if record["amount"] <= 0:
        return False
    return True

# 3. inbound raw batch data
incoming_feed = [
    {"txn_id": "TXN_201", "customer": "Dana", "amount": 250.00, "status": "completed"},
    {"txn_id": "TXN_202", "customer": "Liam", "amount": 0.00,   "status": "completed"},
    {"txn_id": "TXN_203", "customer": "Maya", "amount": 180.50, "status": "failed"},
    {"txn_id": "TXN_204", "customer": "Noah", "amount": 420.00, "status": "completed"}
]

# 4. Pipeline Execution
clean_payouts = []

print("--- Running Function Pipleine ---")
for txn in incoming_feed:
    if not is_valid_transaction(txn):
        print(f"Rejected: {txn['txn_id']} (Failed validation)")
        continue
    
    # Use the reusable function
    payout = calculate_payout(txn["amount"])
    clean_payouts.append({"txn_id": txn["txn_id"], "payout": payout})
    print(f"Approved: {txn['txn_id']} -> Clean Payout: ${payout:.2f}")
    
print("--------------------------------")
print(f"Total Ready for Payout: {len(clean_payouts)}")
print(clean_payouts)