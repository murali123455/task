from flask import Flask, jsonify
import boto3

app = Flask(__name__)

# S3 Client Setup
s3 = boto3.client('s3')
BUCKET_NAME = 'muraliklr'  # Replace with your S3 bucket name

# Default Route
@app.route('/')
def home():
    return "Welcome to the S3 Bucket Content Listing Service!"

# List Bucket Content Route
@app.route('/list-bucket-content', defaults={'path': ''}, methods=['GET'])
@app.route('/list-bucket-content/<path:path>', methods=['GET'])
def list_bucket_content(path):
    prefix = f"{path}/" if path else ""
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=prefix, Delimiter='/')
        content = []

        if 'CommonPrefixes' in response:
            content.extend([p['Prefix'].rstrip('/') for p in response['CommonPrefixes']])
        if 'Contents' in response:
            content.extend([o['Key'].replace(prefix, '').rstrip('/') for o in response['Contents']])

        return jsonify({"content": list(filter(None, content))})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
