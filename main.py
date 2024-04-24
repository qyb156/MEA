import os
import json

from PIL import Image

def open_image(file_path):
    try:
        img = Image.open(file_path)
        img.show()  # 显示图像
    except Exception as e:
        print("Error:", e)
import csv

# Data to be written to CSV
data = [
    ['Name', 'Age', 'Location'],
    ['John', 25, 'New York'],
    ['Alice', 30, 'Los Angeles'],
    ['Bob', 35, 'Chicago']
]

# Name of the CSV file
csv_file = 'output.csv'
#
# # Writing to CSV file
# with open(csv_file, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['ok'])
#     writer.writerow(['ok'])
#
#
# exit()

def write_content(content='',filename='negative_content.txt'):
  """将内容写入指定文件。
  Args:
    文件名: 要写入的文件的名称。
    内容: 要写入文件的内容。
  """
  with open(filename, 'a', encoding='utf-8') as f:
    f.write(content+"\n")

def read_json_files(folder_path):
    # 获取目录下所有文件
    files = os.listdir(folder_path)

    # 循环处理每个文件
    count_all=0
    count_negative = 0
    for file_name in files:
        # 检查文件是否为JSON文件
        if file_name.endswith('.json'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                count_all+=1
                # 这里可以对每个JSON文件的内容进行处理

                if data["review_total_score"]<5:
                    # print(data)
                    cur_data=str(count_negative)+' -- '+data['review_title']+'--'+data['review_data']
                    print(cur_data)  # 举例输出
                    # write_content(content=cur_data)
                    # Writing to CSV file
                    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerow([cur_data])

                    # print("总评分:", data["review_total_score"])
                    count_negative+=1
                    # print("img_path:", data["img_path"])
                    for img in data["img_path"]:
                        # print(img)
                        # 指定jpg文件路径
                        file_path = img
                        # open_image(file_path)

    print("符合条件的总数是:",count_all,"符合条件的negative总数是:",count_negative,",用于训练数据集的negative是：",count_negative*0.8)




# 将jsonData文件夹路径传递给函数
folder_path = 'jsonData'
read_json_files(folder_path)
