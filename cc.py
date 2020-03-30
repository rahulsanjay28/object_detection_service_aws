import sys
import boto3
from botocore.exceptions import ClientError
import threading
import os
import json

# ec2 = boto3.client('ec2', region_name="us-east-1")
sqs = boto3.client('sqs')
s3 = boto3.client('s3')

# response = ec2.start_instances(InstanceIds=['i-0f31382883b78fe95'], DryRun=False)
# response = ec2.stop_instances(InstanceIds=['i-0f31382883b78fe95'], DryRun=False)

# get all the instance id's
# response = ec2.describe_instances()
# print(len(response['Reservations']))
# for instance in response['Reservations']:
#     if("stopped" in instance['Instances'][0]['State']['Name']):
#         print(instance['Instances'][0]['InstanceId'], instance['Instances'][0]['State']['Name'])
        # start_response = ec2.start_instances(InstanceIds=[instance['Instances'][0]['InstanceId']], DryRun=False)

# ec2 = boto3.resource('ec2')
# for instance in ec2.instances.all():
#     print (instance.id , instance.state['Name'])

# instance_id = sys.argv[2]
# action = sys.argv[1].upper()
#
#
#
# if action == 'ON':
#     # Do a dryrun first to verify permissions
#     try:
#         ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
#     except ClientError as e:
#         if 'DryRunOperation' not in str(e):
#             raise
#
#     # Dry run succeeded, run start_instances without dryrun
#     try:
#         response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
#         print(response)
#     except ClientError as e:
#         print(e)
# else:
#     # Do a dryrun first to verify permissions
#     try:
#         ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
#     except ClientError as e:
#         if 'DryRunOperation' not in str(e):
#             raise
#
#     # Dry run succeeded, call stop_instances without dryrun
#     try:
#         response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
#         print(response)
#     except ClientError as e:
#         print(e)


response = sqs.get_queue_url(QueueName='object_detection_requests_queue')
print(response['QueueUrl'])
queue_url = response['QueueUrl']

# Create SQS client
for i in range(50):
    # # Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=0,
        MessageAttributes={
            'key': {
                'DataType': 'String',
                'StringValue': 'rahul_sanjay'
            }
        },
        MessageBody=(
            'video.h264'
        )
    )
#
# print(response['MessageId'])

# while True:
#     # Receive message from SQS queue
#     response = sqs.receive_message(
#         QueueUrl=queue_url,
#         AttributeNames=[
#             'SentTimestamp'
#         ],
#         MaxNumberOfMessages=1,
#         MessageAttributeNames=[
#             'All'
#         ],
#         VisibilityTimeout=0,
#         WaitTimeSeconds=0
#     )
#     if 'Messages' in response:
#         message = response['Messages'][0]
#         receipt_handle = message['ReceiptHandle']
#         body = message['Body']
#         # Delete received message from queue
#         sqs.delete_message(
#             QueueUrl=queue_url,
#             ReceiptHandle=receipt_handle
#         )
#         print('Received and deleted message: %s' % body)
#     else:
#         print("No messages in the queue, will wait for some_time and check again")
#         break

# Retrieve the list of existing buckets
# response = s3.list_buckets()
#
# # Output the bucket names
# print('Existing buckets:')
# for bucket in response['Buckets']:
#     print(f'  {bucket["Name"]}')


# def upload_file(file_name, bucket, object_name=None):
#     """Upload a file to an S3 bucket
#
#     :param file_name: File to upload
#     :param bucket: Bucket to upload to
#     :param object_name: S3 object name. If not specified then file_name is used
#     :return: True if file was uploaded, else False
#     """
#
#     # If S3 object_name was not specified, use file_name
#     if object_name is None:
#         object_name = file_name
#
#     # Upload the file
#     s3_client = boto3.client('s3')
#     try:
#         response = s3_client.upload_file(file_name, bucket, object_name)
#     except ClientError as e:
#         logging.error(e)
#         return False
#     return True
#
class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()

# s3.upload_file(
#     'video.h264', 'videosnotprocessed', "video.h264",
#     Callback=ProgressPercentage('video.h264')
# )

# s3.download_file('cc-object-detection-results', "video", 'sample.mp4')

# obj = s3.get_object(Bucket = 'cc-object-detection-results',Key = 'sample.mp4')
# print(obj['Body'].read())
# if obj['Body'].read() == 'Person':
#     print("it is a person")


# ec2_resource = boto3.resource('ec2')
# instances = ec2_resource.create_instances(ImageId="ami-01f07d71075cbfa31", MinCount=1, MaxCount=1,
#                                  InstanceType="t2.micro", KeyName="aws_key_pair", SecurityGroups=["launch-wizard-15"])
# print(instances)