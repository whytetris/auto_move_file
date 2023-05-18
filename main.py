import shutil
import os
import re
import time


config_path = []
with open("config.txt", "r") as file:
    for line in file:
        dic = {"input_path":line.split(";")[0], "output_path":line.split(";")[1],"ext_path":line.split(";")[2]}
        config_path.append(dic)

while True:
    for j in config_path:
        input_path = j.get("input_path")
        output_path = j.get("output_path")
        extension = j.get("ext_path")
        for file_name in os.listdir(input_path):
            if file_name.endswith(extension):
                src_path = os.path.join(input_path, file_name)
                dst_path = os.path.join(output_path, file_name)
                shutil.move(src_path, dst_path)
    time.sleep(60)