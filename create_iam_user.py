import boto3 

def create_iam_user(iam, username):
    try: 
        iam.get_user(
            UserName= username
        )
        print(f"user '{username}' already exists")

    except iam.exceptions.NoSuchEntityException as e:
        try:
            iam.create_user(
                UserName = username
            )
            print(f"user created named '{username}'")
        except Exception as e:
            print("Tried creating iam user '{username}' but : ",e)
    
    except Exception as e:
        print("New exception")
        print(e)

if __name__ == '__main__':

    iam = boto3.client('iam') 
    username = input("Enter IAM username : ")
    create_iam_user(iam, username)

    print("****** Script Ended *******")