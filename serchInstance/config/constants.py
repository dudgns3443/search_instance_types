BUCKET_NAME = 'your-s3-bucket'
DB_FILE_NAME = 'mydatabase.db'
LOCAL_DB_PATH = '/tmp/mydatabase.db'

class Constants:
    @property
    def BUCKET_NAME(self):
        return "your-api-key"
    
    @property
    def DB_FILE_NAME(self):
        return 'mydatabase.db'
    
    @property
    def LOCAL_DB_PATH(self):
        return '/tmp/mydatabase.db'

