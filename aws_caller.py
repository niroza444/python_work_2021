import boto3
from Aws_wrapper_final_proj import show_buckets,file_upload,list_file,create_bucket
s3_obj = boto3.resource('s3')
file_path = 'my_new_file.txt'
key = "my_new_file.txt"
show_buckets(s3_obj)

file_upload(s3_obj,'nir444pythonbucket',file_path,key)
list_file(s3_obj,'nir444pythonbucket')

create_bucket(s3_obj,'nir444pythonbucketnew')