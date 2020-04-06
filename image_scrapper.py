# import necessary dependencies
import urllib
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os
from string import ascii_lowercase

def download_images():
    # create lits which will store parent urls
    ikea_tv_media_storage_list =[]
    ikea_table_list =[]
    ikea_chair_list =[]
    ikea_wardrobes_list =[]

    # store all the urls for all the images
    url_list = []

    # get the required urs for tv, table, chair and wardrobes
    tv_media_storage_url = "https://www.ikea.com/in/en/cat/tv-media-furniture-10475"
    ikea_tv_media_storage_list.append(tv_media_storage_url)

    table_01_url = "https://www.ikea.com/in/en/cat/dining-tables-21825"
    ikea_table_list.append(table_01_url)
    table_02_url = "https://www.ikea.com/in/en/cat/coffee-side-tables-10705"
    ikea_table_list.append(table_02_url)
    table_03_url = "https://www.ikea.com/in/en/cat/bar-tables-20862"
    ikea_table_list.append(table_03_url)
    table_04_url = "https://www.ikea.com/in/en/cat/dining-tables-21965"
    ikea_table_list.append(table_04_url)

    chair_01_url = "https://www.ikea.com/in/en/cat/armchairs-chaise-longues-16239" 
    ikea_chair_list.append(chair_01_url)
    chair_02_url = "https://www.ikea.com/in/en/cat/cafe-chairs-19144"
    ikea_chair_list.append(chair_02_url)
    chair_03_url = "https://www.ikea.com/in/en/cat/dining-chairs-25219"
    ikea_chair_list.append(chair_03_url)
    chair_04_url = "https://www.ikea.com/in/en/cat/office-chairs-20652"
    ikea_chair_list.append(chair_04_url)
    chair_05_url = "https://www.ikea.com/in/en/cat/bar-chairs-20864/"
    ikea_chair_list.append(chair_05_url)

    wardrobes_01_url = "https://www.ikea.com/in/en/cat/pax-wardrobes-without-doors-19110"
    ikea_wardrobes_list.append(wardrobes_01_url)
    wardrobes_02_url = "https://www.ikea.com/in/en/cat/pax-frames-for-hinge-doors-19106"
    ikea_wardrobes_list.append(wardrobes_02_url)
    wardrobes_03_url = "https://www.ikea.com/in/en/cat/pax-frames-for-sliding-doors-20087"
    ikea_wardrobes_list.append(wardrobes_03_url)

    # add the tv, table, chair, wardrobes to the url_list 
    url_list.append(ikea_tv_media_storage_list)
    url_list.append(ikea_table_list)
    url_list.append(ikea_chair_list)
    url_list.append(ikea_wardrobes_list)

    # create the directory to store images 
    class_dict = {0:"tv_storage",
                 1:"table",
                 2:"chair",
                 3:"wardrobes"}
    path_list = []
    curr_dir = os.getcwd()
    # create a path for dataset dir
    dataset_dir = curr_dir + '/dataset'
    for i in range(len(class_dict)):
        folder_name = class_dict[i]
        # folders where image are/will saved
        path = os.path.join(dataset_dir,folder_name)
        #print(path)
        if not os.path.exists(path):
            os.makedirs(path)
            path_list.append(path)
        else:    
            path_list.append(path)

    # store the images into respective folders
    image_url_list = []

    class_dict = {0:"tv_storage",
                 1:"table",
                 2:"chair",
                 3:"wardrobes"}

    for i in range(len(url_list)):
        folder_name = class_dict[i] 
        image_name = class_dict[i]
        for url_link in url_list[i]:
            image_count=0
            temp_link = url_link
            uClient = uReq(temp_link)
            page_html = uClient.read()
            uClient.close()
            page_soup = soup(page_html, "html.parser")
            containers = page_soup.findAll("div", {"class":"product-compact"})
            for container in containers:
                image_url = container.div.a.div.div.div.img["src"]
                image_url_list.append(image_url)

                #filename =  "/resources/datasets/" + image_name + str(image_count)
                #print(filename)
                file_name = image_name + str(image_count) + ".jpeg"
                save_path = os.path.join(path_list[i], file_name)
                #filename = image_name + str(image_count)
                try:
                    with open(save_path, 'wb+') as image_file:
                        #print(image_url)
                        image_file.write(urllib.request.urlopen(image_url).read())
                        image_file.close()
                except OSError as e:
                    pass
                image_count=image_count+1