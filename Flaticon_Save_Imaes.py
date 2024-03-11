import datetime
import requests
from bs4 import BeautifulSoup
import  os
import logging
from selenium import webdriver

#logging.basicConfig(filename=f'logfile{str(datetime.datetime.date(datetime.datetime.now()))}',level=logging.NOTSET,format='%(asctime)s %(Name)s %(levelname)s %(Message)s')

class flaticon():
    def __init__(self,search_input):
        self.__search_input = search_input

    def save_images(self,local_system_folder):
        if '/' in local_system_folder:
            local_system_folder.replace('/',r'\\')
        else:
            local_system_folder
        directory = os.makedirs(local_system_folder + '\\' + str(datetime.datetime.now().date()) + '_' + self.__search_input,exist_ok=True)
        directory_Name = local_system_folder + '\\' + str(datetime.datetime.now().date()) + '_' + self.__search_input + '\\'
     #get image data from website
        get_response = requests.get(f'https://www.flaticon.com/search?word={self.__search_input}')
        soup = BeautifulSoup(get_response.text,'html.parser')
        image_tags = soup.find_all('img')


    #Save image in folder
        for sno,img in enumerate(image_tags):
            image_extension = img['src'][-(len(img['src'])-(img['src'].find('.',img['src'].find('.com')+1)+1)):]
            image_name = f"{sno}.{image_extension}"
            img_path= os.path.join(directory_Name, image_name)
            save_images = open(img_path,'wb')
            save_images.write(img['src'])
            #save_images.closed
            #print(img['src'],' ' ,img['src'][-(len(img['src'])-(img['src'].find('.',img['src'].find('.com')+1)+1)):])



t1 = flaticon('invoice')
print(t1.save_images('D:\Python_Beginner\Data'))



