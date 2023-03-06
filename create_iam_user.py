import boto3 

iam = boto3.client('iam')

try:
    response = iam.create_user(
        UserName='vicky'
    )
    print("User is created sucessfully ")
except iam.exceptions.EntityAlreadyExistsException as e:
    print("EntityAlreadyExistsException ", e)

print("****** Script Ended *******")