from PIL.ExifTags import TAGS
from PIL import Image
import piexif

import tag_list
import edit

print("write name of file")
name=str(input())

im = Image.open(name)
exif=im._getexif()

while True:
    if exif:
        print()
    else:
        print("not have exifinfo")
        break
    print("1: display exifinfo(all)")
    print("2: display exifinfo(for each tag)")
    print("3: edit exifinfo")
    print("4: delete exifinfo")
    print("5: finish")

    sel=int(input())
    print()

    if (sel==1):
        for id,v in exif.items():
            print(TAGS.get(id),":",v)

    if (sel==2):
        print("search word")
        search=str(input())
        tag_list.tags(search)
        print("input id")
        num=int(input())
        for id,v in exif.items():
            if(id==num):
                print(TAGS.get(id),":",v)

    if (sel==3):
        print("input edit tag")
        tag=str(input())
        if tag=='GPS':
            edit.edit_gps(name)
        else:
            edit.edit(name,tag)

    if (sel==4):
        piexif.remove(name)
        print("erase completed")

    if (sel==5):
        break
