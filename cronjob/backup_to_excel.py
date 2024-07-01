import os
import pymongo
import pandas as pd

# MongoDB connection
mongo_uri = os.getenv('mongodb+srv://emymatista:wjJZE0fNMwij2gk2@cluster2.hkghaqf.mongodb.net/pedidos?retryWrites=true&w=majority')
client = pymongo.MongoClient(mongo_uri)
db = client.get_database()

# Fetch data
collection_name = "pedidos"  # Replace with your collection name
collection = db[collection_name]
data = list(collection.find())

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to Excel
output_dir = os.getenv('C:\\Users\\emyma\\OneDrive\\Documentos\\web_practices\\backups', '/usr/share/mongodump/')
output_file = os.path.join(output_dir, f"mongodb_backup_{pd.Timestamp.now().strftime('%d%m%Y-%H%M%S')}.xlsx")
df.to_excel(output_file, index=False)

# Log backup information
backup_log = {
    "backup_file": output_file,
    "timestamp": pd.Timestamp.now()
}
backup_collection = db["backup_logs"]
backup_collection.insert_one(backup_log)

print(f"Backup saved to {output_file} and logged in the database.")
