#!/bin/bash

# Define paths
folder_name="dependencies"
zip_name="aws_lambda_artifact.zip"
app_name="main.py"


pip3 install -t $folder_name -r requirements.txt
(cd $folder_name; zip ../$zip_name -r .)
zip $zip_name -u $app_name

echo "Packing completed."