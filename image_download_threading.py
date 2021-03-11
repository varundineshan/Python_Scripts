#importing required modules
import requests
import time
import concurrent.futures
#funtion to download single image file
def single_file_download(image_url):
    filename = image_url.split("/")[-1]
    blocks = requests.get(image_url).content
    with open(filename+'.jpg', 'wb') as door:
        response = requests.get(image_url, stream=True)
        door.write(blocks)
        print('downloaded-->'+filename)

#initializing list with urls of the image to be downloaded
image_list=['https://images.unsplash.com/photo-1504208434309-cb69f4fe52b0',

'https://images.unsplash.com/photo-1485833077593-4278bba3f11f',

'https://images.unsplash.com/photo-1593179357196-ea11a2e7c119',

'https://images.unsplash.com/photo-1526515579900-98518e7862cc',

'https://images.unsplash.com/photo-1582376432754-b63cc6a9b8c3',

'https://images.unsplash.com/photo-1567608198472-6796ad9466a2',

'https://images.unsplash.com/photo-1487213802982-74d73802997c',

'https://images.unsplash.com/photo-1552762578-220c07490ea1',

'https://images.unsplash.com/photo-1569691105751-88df003de7a4',

'https://images.unsplash.com/photo-1590691566903-692bf5ca7493',

'https://images.unsplash.com/photo-1497206365907-f5e630693df0',

'https://images.unsplash.com/photo-1469765904976-5f3afbf59dfb']
#downloading single image.
single_file_download(image_list[1])

#downloading multiple images sequentially.
start=time.perf_counter()
for image in image_list:
    single_file_download(image)
end=time.perf_counter()
print('Elapsed time for sequential download:'+str(end-start))

start=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    for image in image_list:
        executor.submit(single_file_download,image)
end=time.perf_counter()
print('Elapsed time for threaded download :'+str(end-start))

