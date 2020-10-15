from distutils.spawn import find_executable
from operator import attrgetter
from os.path import basename

# external packs
from boto3 import session


class AmazonApi(object):
    def __init__(self, bucket_name, folder_name="", region_name='us-east-1'):

        # self.session = session.Session(region_name=region_name)
        # self.client = self.session.client('s3')
        # self.s3 = self.session.resource('s3')

        # self.session = Session(
        #     aws_access_key_id=PUBLIC_KEY,
        #     aws_secret_access_key=ACCESS_KEY,
        #     region_name=region_name
        # )

        # self.s3 = self.session.resource('s3')

        self.session.client('s3', aws_access_key_id=PUBLIC_KEY,
                            aws_secret_access_key=SECRET_KEY)

        self.bucket_name = bucket_name
        self.folder_name = folder_name
        self.bucket = self.s3.Bucket(self.bucket_name)

    bucket_name = property(attrgetter('_bucket_name'))

    @bucket_name.setter
    def bucket_name(self, d):
        """ Validate incoming format
        """
        if not find_executable("aws"):
            raise Exception(
                "missing aws cli (cmd line tools), ensure the aws cli is installed and configured")
        if not self.bucket_exists(d):
            raise Exception("bucket does not exists '{0}'".format(d))
        # noinspection PyAttributeOutsideInit
        self._bucket_name = d

    def bucket_exists(self, bucket_name):
        return self.s3.Bucket(bucket_name).creation_date

    def push_file(self, file, permission='public-read'):
        data = open(file, 'rb')
        key_text = "{0}/{1}".format(self.folder_name, basename(file))

        # push file to bucket
        self.bucket.put_object(Key=key_text, Body=data, ACL=permission)

        if not check_if_s3_file_exists(key_text, self.bucket):
            raise Exception("file upload unsuccessful '{0}'".format(key_text))

        return self.get_url(key_text)

    def get_url(self, key_name):
        url = self.client.generate_presigned_url('get_object', Params={'Bucket': self.bucket_name,
                                                                       'Key': key_name}, ExpiresIn=604800)
        return url

    def download_file(self, key, output_path):
        self.s3.Bucket(self.bucket_name).download_file(key, output_path)
