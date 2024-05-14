import os
import pandas as pd
import requests
from io import BytesIO
from PIL import Image

BASE_DIR = "/home/den/Documents/nexign_ITMO/chicagoParsing/"
# Read XLSX file using pandas
file_path = BASE_DIR + 'links_to_chicago_imgs.xlsx' 
df = pd.read_excel(file_path, sheet_name='Лист1')

# Create output directory if not exists
output_directory = BASE_DIR +'chicago/'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Iterate through each row and download images
for index, row in df.iterrows():
    try:
        photo_link = row['Ссылка на фото'] 
        print(photo_link)
        response = requests.get(photo_link)
        
        # Save image
        img = Image.open(BytesIO(response.content))
        img.save(os.path.join(output_directory, f"{index}.jpg"))  # Save image with row index as filename
        print(f"Image {index} saved successfully.")
    except Exception as e:
        print(f"Error while processing image {index}: {e}!!")