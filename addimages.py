import pandas as pd
import os
import shutil
df=pd.read_csv("C:/Users/Anshul Ranjan/Downloads/test.csv")
df_category_range=df['fabric'].unique()
df_category_range = df_category_range.tolist()
geo_list = df[df['fabric'] == 'georgette']
data = geo_list['image_path']
image_path_column = 'image_path'
destination_folder = 'C:/Users/Anshul Ranjan/Downloads/CCBD/cotton'
for index, row in data.iterrows():
    image_path = row[image_path_column]
    filename = os.path.basename(image_path)
    destination_path = os.path.join(destination_folder, filename)
    shutil.copy(image_path, destination_path)
