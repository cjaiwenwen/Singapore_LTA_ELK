import json
import os
import sys
import re
from datetime import date
import shutil


def listfile(path):
    filelist = os.listdir(path)
    return filelist


def readfile(file):
    with open(file) as f:
        d = json.load(f)
    return d


def main(path):
    filelist = listfile(path)
    fp = open("/home/cjaiwenwen/content1.txt", 'a')
    for filename in filelist:
        file = path + '/' + filename
        newfile = "/home/cjaiwenwen/PycharmProjects/chenjun" + '/' + 'processed' + '/' + filename
        content = readfile(file)
        resp_dump = json.dumps(content)
        resp_dict = json.loads(resp_dump)
        a = resp_dict['value']
        for item in a:
            Longitude = str(item['Longitude'])
            Latitude = str(item['Latitude'])
            Type = str(item['Type'])
            Type = Type.replace(" ","_")
            Message = item['Message']
            Message = str(Message).replace(' ','_')
            currentdate = re.findall('\(\d+/\d+\)',Message)
            currentdate = str(currentdate).strip('['']')[2:-2]
            currentdate = currentdate + '/' + str(date.today().year)
            #currentdate = currentdate + '/' + "2016"
            currentyear = str(date.today().year)
            currentmonth = currentdate.split("/")[1]
            time = re.findall('(\w+:\d+)',Message)
            time = str(time).strip('['']')[1:-1]
            hour = time.split(":")[0]
            sys.stdout = fp
            print currentdate, currentyear, currentmonth, time, hour, Longitude, Latitude, Type
        os.chdir(path)
        shutil.move(file, newfile)
    fp.close()


if __name__ == '__main__':
    path = "/home/cjaiwenwen/PycharmProjects/chenjun/LTA"
    main(path)