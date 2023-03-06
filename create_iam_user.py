import boto3 

iam = boto3.client('iam')

try: 
    iam.get_user(
        UserName='vicky'
    )
    print(f"user already exists")
except iam.exceptions.NoSuchEntityException as e:
    try:
        iam.create_user(
            UserName = "vicky"
        )
        print(f"user created")
    except Exception as e:
        print("some other exception details : ",e)


print("****** Script Ended *******")