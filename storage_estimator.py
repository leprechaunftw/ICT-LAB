storage_gb = float(input("Enter storage in GB: "))
if storage_gb < 0: print("Storage cannot be negative.")
storage_mb = storage_gb * 1024
print("Storage in MB:", storage_mb)