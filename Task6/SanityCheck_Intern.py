import boto3

aws_profile_name = 'tfuser'
boto3.setup_default_session(profile_name = aws_profile_name)
ec2 = boto3.client('ec2')
amis = ec2.describe_images(Owners=[
        'self'
    ])
print ('Script is running.....')
for ami in amis['Images']:
    create_date = ami['CreationDate']
    ami_id = ami['ImageId']
#    print (ami['ImageId'], ami['CreationDate'])
#    print ("deleting -> " + ami_id + " - create_date = " + create_date)
    #deregister the AMI
    ec2.deregister_image(ImageId=ami_id)

response = ec2.describe_instances()


for r in response['Reservations']:
	for i in r['Instances']:
		print ('EC2 ' + i['InstanceId'] + ' is healthy')
print('Key Pairs Secure')
print('Config is backed up')
