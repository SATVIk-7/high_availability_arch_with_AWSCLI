import os
import subprocess
print("\t\t\t\t       Welcome to task-6")
print("\t\t\t\tNamaste Performing task-6 demo")
while True:
	print("1)configuring AWS")
	print("2)Creating Key-pair")
	print("3)Creating Security_Group")
	print("4)Launching-Instance")
	print("5)Creating Volume")
	print("6)Attaching Volume")
	print("7)Creating Bucket")
	print("8)Uploading Data")
	print("9)Creating Cloud-front")
	
	cmd = int(input("\t\tEnter requirement :"))
	if cmd==1:
		print("please press the enter button to configure")
		os.system("aws configure")
	elif cmd==2:
		mykeyname = input("Enter Your Key Name: ")
		subprocess.getoutput("aws ec2 create-key-pair --key-name {}  --query KeyMaterial --output text > MyKeyPair.pem".format(mykeyname))
		print("Your key stored inside MyKeyPair.yml")
				
	elif cmd==3:
		
		subprocess.getoutput("aws ec2  create-security-group --group-name task6firewall --description created-using-cli  --query GroupId --output text  >> storetem.txt")
		subprocess.getoutput("aws ec2 authorize-security-group-ingress --group-name task6firewall  --ip-permissions  IpProtocol=tcp,FromPort=0,ToPort=63000,IpRanges=[{CidrIp=0.0.0.0/0}]")
		print("created security group and allowed all traffic")

	elif cmd==4:
		sgid = input("Enter security group id: ")
		keyname = input("Enter key name: ")
		subprocess.getoutput("aws ec2  run-instances --image-id ami-0e306788ff2473ccb --count 1 --instance-type t2.micro --key-name {} --security-group-ids {}  --subnet-id subnet-baa0cbf6 --query Instances[*].InstanceId --output text >> storetem.txt".format(keyname,sgid))
		print(" instance created step completed")

	elif cmd==5:
		os.system("aws ec2 create-volume --availability-zone ap-south-1b --size 1 --volume-type gp2 --query VolumeId  --output text >> storetem.txt")
		print(" creating volume completed")

	elif cmd==6:
		ins_id = input("Enter instance id stored in storetem.txt: ")
		vol_id = input("Enter volume id stored in storetem.txt: ")
		subprocess.getoutput("aws ec2 attach-volume --instance-id {}  --volume-id  {} --device /dev/sdb".format(ins_id,vol_id))	
		print("volume attached")

	elif cmd==7:		
		buk_name = input("Enter your bucket name: ")
		subprocess.getoutput("aws s3api create-bucket --bucket {} --acl public-read --region ap-south-1 --create-bucket-configuration  LocationConstraint=ap-south-1".format(buk_name))
		print("bucket created and ready to store the objects")		

	elif cmd==8:
		buc_up = input("Enter bucket name to upload data: ")
		img_location = input("Enter static object location: ")
		obj_name = input("Enter object name to make public: ")
		subprocess.getoutput("aws s3api put-object --bucket {} --key {} --body {} --acl public-read-write".format(buc_up,obj_name,img_location))
		subprocess.getoutput("aws s3api put-object-acl --bucket {} --key {} --acl public-read".format(buc_up,obj_name))
		print("object uploaded")

	elif cmd==9:
		print("Create cloud-front")
		origin_name = input("Enter origin domain name must be formatted like bucketname.s3.amazomaws.com : ") 
		subprocess.getoutput("aws cloudfront create-distribution --origin-domain-name {}".format(origin_name))

	else:
		print("Try giving option available in your screen")


		





	
	