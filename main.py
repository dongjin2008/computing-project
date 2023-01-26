from image_convert import ImageConvert
from num_convert import NumConvert
from unit_convert import UnitConvert
from video_downloader import VidDownloader

print(
"""
1. Image converter        
2. Number converter
3. Unit converter
4. Video converter\n
""")

UI = input("Enter the number: ")

if UI == "1":
    image_type = input("output file type(jpg, png, webp, svg): ")
    ImageConvert(Type=image_type)

elif UI == "2":
    num_input = input("Input number type(dec, hex, oct, bin): ")
    num_output = input("Output number type(dec, hex, oct, bin): ")
    print(NumConvert(Input=num_input, Output=num_output))

elif UI == "3":
    unit_input = input("Input unit type: ")
    unit_output = input("Output unit type: ")
    print(UnitConvert(Input=unit_input, Output=unit_output))

elif UI == "4":
    VidDownloader()