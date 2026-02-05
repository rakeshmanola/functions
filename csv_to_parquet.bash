#!/bin/bash
set -e

gcloud functions deploy csv_to_parquet_101 \
  --gen2 \
  --region=us-central1 \
  --runtime=python310 \
  --entry-point=csv_to_parquet \
  --service-account=function1@project6174.iam.gserviceaccount.com \
  --trigger-bucket=manola11 \
  --memory=1024MB

