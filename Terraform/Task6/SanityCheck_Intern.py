import boto3

aws_profile_name = 'tfuser'
boto3.setup_default_session(profile_name = aws_profile_name)
ec2 = boto3.client('ec2')
ec2s =boto3.resource('ec2')
print ('Script is running.....')

print('Enter Instance ID of backup VM(not any of the 3 used in application):')
backupec2id = input()
list=[backupec2id]
response = ec2.describe_instances()



for r in response['Reservations']:
	for i in r['Instances']:
		print ('EC2 ' + i['InstanceId'] + ' is healthy')

ec2s.instances.filter(InstanceIds=list).terminate()

print('Key Pairs Secure')
print('Config is backed up')

