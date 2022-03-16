import load_data
import unzip_data

url = 'http://93.90.217.252/download/files.synop/27/27612.01.01.2016.18.10.2021.1.0.0.ru.utf8.00000000.xls.gz'


if __name__ == 'main.py':
    load = load_data.LoadData()
    ungz = unzip_data.UnGZIP()
    gz_file = load.get_data_url(url)
    content_file = ungz.read_compressed_file()