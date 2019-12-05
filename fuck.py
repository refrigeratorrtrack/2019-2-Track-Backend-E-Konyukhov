import boto3


def main():
    #


if __name__ == "__main__":
    session = boto3.session.Session()
    s3_client = session.client(service_name='s3',
                                endpoint_url='http://hb.bizmrg.com',
                                aws_access_key_id='',
                                aws_secret_access_key='')

    s3_client.put_object(Bucket='track', Key='1234.txt', Body='Hello!')

    print("Success!")
