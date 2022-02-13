import os
from os import path
from bing_image_downloader import downloader


def loader(query):
    downloader.download(query=str(query), limit=30, output_dir='/Users/Tom/PycharmProjects/Spot')

path = '/Users/Tom/PycharmProjects/Spot/person, human'
files = os.listdir(path)

def rename(cls):
    i = 1
    for index, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, cls + str(i) + '.jpg'))
        i = i+1
