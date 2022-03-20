import wget

class LoadData:
    def get_data_url(self, url, file_content):
        wget.download(url, file_content)

