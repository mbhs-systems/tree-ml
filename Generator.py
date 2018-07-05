import random
import os
import urllib

if not os.path.exists('training'):
    os.makedirs('training')
if not os.path.exists('test'):
    os.makedirs('test')

#training data

for i in range(10):
    #tiling_resolution = random.randint(0, 11)
    tiling_resolution = 11
    column_num = 320
    row_num = 640
    #column_num = random.randint(200, 400)
    #row_num = random.randint(400, 800)
    url = str("https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/Landsat_WELD_NDVI_Global_Monthly/default/2010-04-01/31.25m/"
              + str(tiling_resolution) + "/" + str(column_num) + "/" + str(row_num) + ".jpg")
    urllib.urlretrieve(url, str(i) + ".jpg")
    os.rename("/Users/ryancho/Documents/Github/systemsCNN/"+str(i)+".jpg", "/Users/ryancho/Documents/Github/systemsCNN/training/"+str(i)+".jpg")

or i in range(10):
    #tiling_resolution = random.randint(0, 11)
    tiling_resolution = 11
    column_num = 320
    row_num = 640
    #column_num = random.randint(200, 400)
    #row_num = random.randint(400, 800)
    url = str("https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/Landsat_WELD_NDVI_Global_Monthly/default/2010-04-01/31.25m/"
              + str(tiling_resolution) + "/" + str(column_num) + "/" + str(row_num) + ".jpg")
    urllib.urlretrieve(url, str(i) + ".jpg")
    os.rename("/Users/ryancho/Documents/Github/systemsCNN/"+str(i)+".jpg", "/Users/ryancho/Documents/Github/systemsCNN/test/"+str(i)+".jpg")
