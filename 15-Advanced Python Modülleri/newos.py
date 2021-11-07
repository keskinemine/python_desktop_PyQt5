import  os
import datetime

result = dir(os)
result = os.name



# **** dizin değiştirme
# os.chdir('/Users/eminekeskin/Desktop')
# os.chdir('../..')

# ***Klasor oluşturma
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasör/yeniklasör")

os.rmdir("newdirectory")

# ***listeleme
# result = os.listdir()
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)


# ***etkin dizi öğrenme

# result = os.getcwd()



# result = os.stat("date.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) #oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime) #son erişilma tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime) #değiştirme tarihi







print(result)