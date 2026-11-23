# 1. Real world dataset: A list of transaction dictionaries (simulating API / DB rows)
transactions_stream = [
    {"txn_id": "TXN_101", "customer": "Alex", "amount": 149.75, "status": "completed"},
    {"txn_id": "TXN_102", "customer": "Sam",  "amount": -10.00, "status": "failed"},
    {"txn_id": "TXN_103", "customer": "Sara", "amount": 310.50, "status": "completed"},
    {"txn_id": "TXN_104", "customer": "John", "amount": 89.90, "status": "completed"}
]

total_volume = 0.0
valid_records = []

print("--- Ingesting & Validating Records ---")

# 2. Iterate through each dictionary record
for record in transactions_stream:
    # Filter: Skip failed transactions or bad data
    if record["status"] != "completed" or record["amount"] <= 0:
        print(f"Skipping Invalid Record -> ID: {record['txn_id']} | Reson : {record['status']}")
        continue
    
    # Extract fields and transform
    amount = record["amount"]
    fee = round(amount * 0.05, 2)
    payout = round(amount - fee, 2)
    
    total_volume += payout
    
    # Store enriched data into a list
    valid_records.append(
        {
            "txt_id": record["txn_id"],
            "customer": record["customer"],
            "net_payout": payout
        }
    )
    
    print(f"Processed {record['txn_id']} for {record['customer']}: Payout = ${payout:.2f}")
    
# 3. Summary
print("--------------------------------")
print(f"Valid Records Transformed: {len(valid_records)}")
print(f"Total Disbursed Volume: ${total_volume:.2f}")
print("Enriched Dataset for DB Load:")
print(valid_records)
