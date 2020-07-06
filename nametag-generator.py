import glob
from PIL import Image, ImageDraw, ImageFont, PdfImagePlugin, _imaging ## was from PIL
from math import ceil
import os

badge_loc = 'border.png' # badge template
filename = 'namesShort.txt' # text file with names
dpi = 300

#Settings
usingTableNumbers = False # Toggle table numbers / dateStamp
color = (0, 82, 16) # Font color
dateStamp = 'July 25 - 2020'
fontStyle = "Cookie-Regular.ttf" # Font - Put within font folder
#/Settings

fontStyle = "./fonts/" + fontStyle # adds font folder prefix

total = 0
count = 0
size = (int(8.5*dpi), int(11*dpi)) # Size of paper to print (8.5x11)

numNames = sum(1 for line in open(filename))
numPages = int(ceil(float(numNames)/6))

pg = 0
for line in open(filename):

    if usingTableNumbers:
        try:
            firstname, lastname, tableNumber = line.split(' ')
        except ValueError:
            print("ERROR: Incorrect number of fields for an entry in: " + filename)
            print("\t ** Assure all attendees have table numbers ** ")
            exit(1)
    else:
        try:
            firstname, lastname = line.split(' ')
        except ValueError:
            print("ERROR: Incorrect number of fields for an entry in: " + filename)
            print("\t ** Assure no attendees have table numbers ** ")
            exit(1)


    badge = Image.open(badge_loc)
    width, height = badge.size

    draw = ImageDraw.Draw(badge)
    font = ImageFont.truetype(fontStyle, 75)

    if usingTableNumbers:
        msg = tableNumber
        if len(msg) <= 3: # only add table to numbers, not named tables
            msg = "table " + msg
    else:
        msg = dateStamp

    w,h = draw.textsize(msg, font = font)
    draw.text(((width-w)/2, 20), msg, fill = color, font=font)

    font = ImageFont.truetype(fontStyle,200)

    w, h = draw.textsize(firstname, font=font)
    draw.text(((width - w)/2, (height-h)/3), firstname, fill = color, font=font)

    w, h = draw.textsize(lastname, font=font)

    # Make font smaller for long last names
    if w >= 1400:
            font = ImageFont.truetype(fontStyle,75)
            w, h = draw.textsize(lastname, font = font)
    elif w >= 1100:
            font = ImageFont.truetype(fontStyle,100)
            w, h = draw.textsize(lastname, font = font)
    elif w >= 900:
            font = ImageFont.truetype(fontStyle,150)
            w, h = draw.textsize(lastname, font = font)
    elif w >= 750:
            font = ImageFont.truetype(fontStyle,175)
            w, h = draw.textsize(lastname, font = font)



    draw.text(((width - w)/2, (height-h)/2+(height/8)), lastname, fill = color, font=font)


    if count == 0 :
            blank_image = Image.new("RGB", size, "White")
            blank_image.paste(badge, (0,0))
    elif count == 1:
            blank_image.paste(badge, (width, 0))
    elif count == 2:
            blank_image.paste(badge, (0, height))
    elif count == 3:
            blank_image.paste(badge, (width, height))
    elif count == 4:
            blank_image.paste(badge, (0, height*2))
    elif count == 5:
            blank_image.paste(badge, (width, (height*2)))
            fname = "./results/"+str(pg)+".png"
            blank_image.save(fname,'png')



    if pg == numPages - 1 and count == (numNames%6)-1:
            fname = "./results/"+str(pg)+".png"
            blank_image.save(fname,'png')

    if count == 5:
            pg += 1
            count = -1

    count += 1
    total += 1

print("DONE: Created " + str(total) + " nametags")
