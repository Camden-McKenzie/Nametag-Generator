# Name Tag Creator

## Author
Camden McKenzie | Jul 6, 2020 | Based on [allisontharp's BadgeGenerator](https://gist.github.com/allisontharp/c48714fe0e7c6f158d4d3ca517ac4c84)

## Running


```
## Run from within folder ##
% source env/bin/activate

% python3 nametag-generator.py
```

## Settings

**usingTableNumbers**
- Toggle if using table numbers in names file

**color**
- Font color

**dateStamp**
- If not ``usingTableNumbers``, then add date stamp here

**fontStyle**
- Choose a font from the font folder by name here

## Names file format

Format names.txt:
> John Smith 2

For John Smith at table 2

or leave off the 2 to use date stamp

> John Smith

Becomes -> John Smith (Jan 1, 2000)

## Border

Add a png named ``border.png``, this will become the border/background for your nametabs
