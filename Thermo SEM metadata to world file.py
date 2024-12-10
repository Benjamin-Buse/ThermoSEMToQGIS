#from PIL import Image
#from PIL.TiffTags import TAGS
import tkinter
import tkinter.filedialog
import tifffile
img = tkinter.filedialog.askopenfile(title="Select Thermo SEM Image")
with tifffile.TiffFile(img.name) as tif:
    PixelWidth=tif.fei_metadata['Scan']['PixelWidth']*1e3
    PixelHeight=tif.fei_metadata['Scan']['PixelHeight']*1e3
    HorFieldsize=tif.fei_metadata['EScan']['HorFieldsize']
    VerFieldsize=tif.fei_metadata['EScan']['VerFieldsize']
    StageX=tif.fei_metadata['EBeam']['StageX']
    StageY=tif.fei_metadata['EBeam']['StageY']
    ResolutionX=tif.fei_metadata['Image']['ResolutionX']
    ResolutionY=tif.fei_metadata['Image']['ResolutionY']
    MagCanvasRealWidth=tif.fei_metadata['Image']['MagCanvasRealWidth']
TLx=StageX-((ResolutionX/2)*PixelWidth)
TLy=StageY-((ResolutionY/2)*PixelHeight)
f = open(img.name.split(".tif")[0]+".tfw", "w")
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