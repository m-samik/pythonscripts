import json
import os

from pyfiglet import Figlet

f = Figlet(font='bubble')
print (f.renderText('AWS  CLI'))


# Launching Instance

aws_cng = input("Is Your AWS CLI already Setup ? (y/n) :")

if aws_cng == "n" :
	os.system("aws configure")
	os.system("python3 aws_cli.py")
elif aws_cng == "y" :
	name=input("Enter Name For Your Instance : ")
	vol = int(input("Enter Volume for Your Instance (in GiB) : "))
	os.system("tput setaf 3")

	print("\t\t Configuration Started Please Wait ... ")

	os.system("tput setaf 7 ")


	os.system("aws ec2 run-instances --image-id ami-0ad704c126371a549 --instance-type t2.micro  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value= %s }]'  --key-name myawskey  > instance.json"%(name))

	file_in = open("instance.json")
	data_in = json.load(file_in)
	data_in = data_in['Instances']
	for i in data_in:
	    instance_id=i["InstanceId"]
	    region = i["Placement"]['AvailabilityZone']
	    
	os.system("rm -f instance.json")
	os.system("tput setaf 2")

	print("Lauching Instance Done ====> \t\t\t 100%")

	os.system("tput setaf 7")

	# Creating Volume

	os.system(f"aws ec2 create-volume --volume-type gp2   --availability-zone {region} --size {vol}  > c_volume.json")
	 
	file_vol = open("c_volume.json")
	data_vol = json.load(file_vol)
	volumeid = data_vol['VolumeId']


	os.system("rm -f c_volume.json")

	os.system("tput setaf 2 ")

	print("Creating Volume Done ====> \t\t\t 100%")
	os.system("tput setaf 7")

	os.system("sleep 30")
	# Attaching the Volume

	os.system("aws ec2 attach-volume --instance-id {0} --volume-id {1} --device /dev/sdf > output.json".format(instance_id,volumeid))


	os.system("tput setaf 2")
	print("Attching Volume Done ====> \t\t\t 100%")
	os.system("tput setaf 7")

	os.system("aws ec2 describe-instances --instance-ids {0} > ec2_info.json".format(instance_id))



	os.system("tput setaf 1")
	print("The Instance Information is Stored in ec2_info.json ")
	os.system("tput setaf 7")

	print("Volume id is " , volumeid)


	print ("Instance id is " , instance_id)

