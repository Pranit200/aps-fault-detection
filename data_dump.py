import pymongo
import pandas as pd 
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"

DATABASE_NAME="aps"
COLLECTION_NAME="sensors"


if __name__ =="__main__":
    df= pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

# Convert dataframe into json so that we can dump these records into mongo db
df.reset_index(drop=True,inplace=True) # generally index starts from 1 so we resets it and inplace = true means dataframe is overwritten in same memory location it doesnot create any new location

json_record = list(json.loads(df.T.to_json()).values())
print(json_record[0])

# insert converted record to mongodb
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

