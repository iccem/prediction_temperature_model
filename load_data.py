import requests

class LoadData:
    def get_data_url(url):
        if url == '':
            file_name = url.split('/')[-1]
            
            with open(file_name, 'wb') as file:
                r = requests.get(url)
                file.write(r.content)
        return file_name
