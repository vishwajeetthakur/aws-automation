import boto3 
import sys
import argparse
import secrets
import string

def get_random_password(password_length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(password_length):
        secrete = secrets.choice(chars)
        password += secrete

    return password


def create_iam_user(iam, username, password=None, attach_policy= None):
    try: 
        iam.get_user(
            UserName= username
        )
        print(f"user '{username}' already exists")

    except iam.exceptions.NoSuchEntityException as e:
        try:
            if password is None:
                password = get_random_password()

            iam.create_user(
                UserName = username,
            )

            iam.create_login_profile(
                UserName = username,
                Password = password,
                PasswordResetRequired = True|False
            )

            if attach_policy is None: # deault s3 read only policy
                iam.attach_user_policy(
                    UserName = username,
                    PolicyArn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
                )
                print("s3 read only policy attached")


            print(f"user '{username}' created")
            print(f"Password is '{password}'")

        except Exception as e:
            print(f"Tried creating iam user '{username}' but : {e}")
    
    except Exception as e:
        print("New exception")
        print(e)


if __name__ == '__main__':

    iam = boto3.client('iam') 
    parser = argparse.ArgumentParser(description="use it bro")
    parser.add_argument("-u", "--username", help = "The name of IAM user, user want to create")
    parser.add_argument("-p", "--password", help = "The password for the IAM user(default is to generate the random password)")
    parser.add_argument("-pol", "--attach_policy", help = "Atach iam policy to user")
    parser.add_argument("-f", "--filename", help = "Atach iam policy to user")
    

    args = parser.parse_args()
    
    if not any(vars(args).values()):
        parser.print_help()
        sys.exit()

    if args.filename:
        with open(args.filename, 'r') as file:
            usernames = file.read().splitlines() 
        print(usernames)

        for username in usernames:
            create_iam_user(iam, username) 

    else:
        create_iam_user(iam, args.username, args.password, args.attach_policy) 

    print("****** Script Ended *******")