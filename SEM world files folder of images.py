# import the modules
import os
from os import listdir
import tkinter
import tkinter.filedialog
import tifffile

folder_dir = tkinter.filedialog.askdirectory(title="Select directory of SEM tiles unstitched")

for images in os.listdir(folder_dir):
 
    # check if the image ends with png
    if (images.endswith(".tif")):
        print(images)
        img = folder_dir+'/'+images
        with tifffile.TiffFile(folder_dir+'/'+images) as tif:
            PixelWidth=tif.fei_metadata['Scan']['PixelWidth']*1e3
            PixelHeight=tif.fei_metadata['Scan']['PixelHeight']*1e3
            HorFieldsize=tif.fei_metadata['EScan']['HorFieldsize']*1e3
            VerFieldsize=tif.fei_metadata['EScan']['VerFieldsize']*1e3
            StageX=tif.fei_metadata['EBeam']['StageX']*1e3
            print(StageX)
            StageY=tif.fei_metadata['EBeam']['StageY']*1e3
            ResolutionX=tif.fei_metadata['Image']['ResolutionX']
            ResolutionY=tif.fei_metadata['Image']['ResolutionY']
            MagCanvasRealWidth=tif.fei_metadata['Image']['MagCanvasRealWidth']
        TLx=StageX-((ResolutionX/2)*PixelWidth)
        print(TLx)
        TLy=StageY+((ResolutionY/2)*PixelHeight)
        f = open(img.split(".tif")[0]+".tfw", "w")
        if PixelWidth==PixelHeight:
            print("Pixel sizes xy match")
        else:
            print("Pixel sizes xy do not match")
        f.write(str(PixelWidth))
        f.write("\n")
        f.write("0")
        f.write("\n")
        f.write("0")
        f.write("\n")
        lineA="-"+str(PixelWidth)
        f.write(lineA)
        f.write("\n")
        f.write(str(TLx))
        f.write("\n")
        f.write(str(TLy))
        f.close()
