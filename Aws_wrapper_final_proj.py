import boto3

def show_buckets(s3_obj):
    for bucket in s3_obj.buckets.all():
        print(bucket.name)
def file_upload(s3_obj,bucket_name,file_path,key_name):
    file_data = open(file_path,'rb') # b used binary format data used for upload
    s3_obj.Bucket(bucket_name).put_object(Key=key_name,Body=file_data)
    file_data.close()
    print("file uploaded successfully")

def list_file(s3_obj,bucket_name):
    print(f"These are the files in {bucket_name} :")
    for object in s3_obj.Bucket(bucket_name).objects.all():
        print(object.key)
def create_bucket(s3_obj, bucket_name):
    s3_obj.create_bucket(Bucket=bucket_name,CreateBucketConfiguration= {'LocationConstraint':'us-west-1'})
    print(f"{bucket_name} is created successfully")
