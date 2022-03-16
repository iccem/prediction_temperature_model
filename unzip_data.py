import gzip

class UnGZIP:
    def read_compressed_file(filename, file_content):
        with gzip.open(filename, 'rb') as f:
            file_content = f.read()
            return file_content