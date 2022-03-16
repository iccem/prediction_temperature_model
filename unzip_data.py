import gzip
import shutil

class UnGZIP:
    def read_compressed_file(self, file_content):
        name = file_content.split('.')
        new_file_name = name[0]+'.'+name[1]
        
        with gzip.open(file_content, 'rb') as f:
            with open(new_file_name, 'wb') as ff:
                shutil.copyfileobj(f, ff)
