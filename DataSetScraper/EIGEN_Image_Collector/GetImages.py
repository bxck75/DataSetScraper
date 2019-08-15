import os,sys,errno

Cproof = os.system('apt list | grep "chromedriver"')
Gproof = os.system('pip list | grep "google_images_download"')
GDproof = os.system('pip list | grep "gallery-dl"')

# Install if needed
# if Cproof == '':
    # Google image chromium installer
# os.system('apt install chromedriver && pip install selenium chromium')

from selenium import webdriver   
# os.system('chromium --no-sandbox &&')    
driver_loc=os.system('which chromedriver')
sys.path.insert(0,driver_loc)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome(options=chrome_options)

import time
print ("Start : %s" % time.ctime())
time.sleep( 1 )
print ("End : %s" % time.ctime())

# if Gproof == '':
    # google_images_download installer
# os.system('pip install google_images_download')
# if GDproof == '':
    # Gallery-dl installer
# os.system('pip install gallery-dl')

def check_file_count(path):
    # set to neg 1 for iteration correction
    G, F = -1, -1
    for file in os.listdir(path):
        #check file iterations
        if 'G_ripped' in file:
            G += 1
        if 'F_ripped' in file:
            F += 1
    # if nothing is found set to 0
    if G == -1:
        G = 0
    if F == -1:
        F = 0
    # return G and F
    return G, F    

# keyword to search images on
Search=sys.argv[1]
Search = Search.replace(' ','+')



# Set max nr of images to fetch
max_img=int(sys.argv[2])


# Google image run
print('googleimagesdownload --keywords '+ str(Search) +' --limit '+ str(max_img) +' --chromedriver "chromedriver"')
os.system('googleimagesdownload --keywords '+ str(Search) +' --limit '+ str(max_img) +' --chromedriver "chromedriver"')
# googleimagesdownload --keywords 'ms13 portrait' --limit 1000 -cd '/usr/bin/chromedriver'

gallery_out_path='gallery-dl/'
gallery_dump_path=gallery_out_path+'flickr/search/'+str(Search).replace('+',' ')+'/'
google_out_path='downloads/'+str(Search)+'/'
final_out_path='ripped_images/'+str(Search)+'/'

G, F = -1, -1
try:
    os.makedirs(final_out_path)
except OSError as e:
    if e.errno != errno.EEXIST:   
        raise
    else:
        print('Counting files....')
        G, F = check_file_count(final_out_path)

# Gallery image run
print('gallery-dl --dest '+gallery_out_path+' --range 1-'+str(max_img)+' https://www.flickr.com/search/?text='+ Search)
os.system('gallery-dl --dest '+gallery_out_path+' --range 1-'+str(max_img)+' https://www.flickr.com/search/?text='+ Search)

# iterate G's
oldg = G
countg = oldg
for files in os.listdir(google_out_path):
    if files.split('.')[len(files.split('.'))-1] == 'jpg' or files.split('.')[len(files.split('.'))-1] == 'jpeg':
        os.rename(google_out_path+files, final_out_path+'G_ripped_'+str(files.split('.')[len(files.split('.'))-2])+'_'+str(countg)+".jpg") 
        countg+=1

# iterate F's
oldf = F
countf = oldf
for files in os.listdir(gallery_dump_path):
    if files.split('.')[len(files.split('.'))-1] == 'jpg' or files.split('.')[len(files.split('.'))-1] == 'jpeg':
        os.rename(gallery_dump_path+files, final_out_path+'F_ripped_'+str(files.split('.')[len(files.split('.'))-2])+'_'+str(countf)+".jpg") 
        countf+=1
        

print("Ripped : "+str(countg)+' GoogleImage files in total. And '+str(countg - oldg)+' In this session')
print("Ripped : "+str(countf)+' Flickr files in total. And '+str(countf - oldf)+' In this session')
# Removing download folders
os.system('sudo rm -r ./gallery-dl ./downloads')
# print(os.listdir(final_out_path))