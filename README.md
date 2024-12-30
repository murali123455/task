1. Frist we have to install python,pip,flask,boto3

2.In aws we have to create one s3 bucket 
3.After creating s3 bucket we have to create  I am user in aws 
4.After that we have to create one access key and secret key

# Configure your AWS credentials 
$set AWS_ACCESS_KEY = "<Your AWS Access Key>"
$set AWS_SECRET_KEY = "<Your AWS Secret Key>"
$set AWS_REGION = "<Your AWS Region>"


After we have run main file called web_2
step1:using $python web_2
step2:http://192.168.68.152:5000/list-bucket-content
step3:http://192.168.68.152:5000/list-bucket-content/dir1
step4:http://192.168.68.152:5000/list-bucket-content/dir2
