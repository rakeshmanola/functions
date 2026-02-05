from google.cloud import storage
import pandas as pd
import io
import os
import psycopg2
from google.cloud import storage
from google.cloud import bigquery
from google.cloud import secretmanager

def csv_to_parquet(event, context):
    file_name = event["name"]

    if not file_name.endswith(".csv"):
        return

    client = storage.Client()

    # ✅ Source bucket: manola11
    src_bucket = client.bucket("manola11")
    src_blob = src_bucket.blob(file_name)

    df = pd.read_csv(io.BytesIO(src_blob.download_as_bytes()), dtype=str)

    buffer = io.BytesIO()
    df.to_parquet(buffer, engine="pyarrow", index=False)
    buffer.seek(0)

    # ✅ Target bucket: manola12
    tgt_bucket = client.bucket("manola12")
    tgt_bucket.blob(file_name.replace(".csv", ".parquet")) \
        .upload_from_file(buffer)

    print(f"Converted {file_name} → Parquet")
