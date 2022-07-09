import requests
from PIL import Image, ImageOps, ImageFilter
import math
import pytesseract

def captcha_url(num_of_digits, image_url):
    
    rel_tol = 0.13
    captcha_result = ''
    
    while ( len(captcha_result) != num_of_digits ) :
        # 1. download image from image_url
        image = requests.get(image_url)
        with open('image_download.png', 'wb') as file:
            file.write(image.content)
    
        # 2. convert from "P" mode to "RGB" mode
        image = Image.open('image_download.png')
        image = image.convert('RGB')
        image_data = image.load()
        height,width = image.size
    
        # 3. get rid of background * by color
        for loop1 in range(height):
            for loop2 in range(width):
                r,g,b = image_data[loop1,loop2]
                if math.isclose( r, 202, rel_tol=rel_tol) and math.isclose( g, 216, rel_tol=rel_tol) and math.isclose( b, 198, rel_tol=rel_tol) :
                        image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 186, rel_tol=rel_tol) and math.isclose( g, 171, rel_tol=rel_tol) and math.isclose( b, 160, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 216, rel_tol=rel_tol) and math.isclose( g, 225, rel_tol=rel_tol) and math.isclose( b, 249, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 238, rel_tol=rel_tol) and math.isclose( g, 193, rel_tol=rel_tol) and math.isclose( b, 200, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 194, rel_tol=rel_tol) and math.isclose( g, 180, rel_tol=rel_tol) and math.isclose( b, 192, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 227, rel_tol=rel_tol) and math.isclose( g, 248, rel_tol=rel_tol) and math.isclose( b, 172, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 217, rel_tol=rel_tol) and math.isclose( g, 170, rel_tol=rel_tol) and math.isclose( b, 196, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 242, rel_tol=rel_tol) and math.isclose( g, 194, rel_tol=rel_tol) and math.isclose( b, 175, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 226, rel_tol=rel_tol) and math.isclose( g, 238, rel_tol=rel_tol) and math.isclose( b, 211, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 241, rel_tol=rel_tol) and math.isclose( g, 197, rel_tol=rel_tol) and math.isclose( b, 234, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 241, rel_tol=rel_tol) and math.isclose( g, 225, rel_tol=rel_tol) and math.isclose( b, 234, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 174, rel_tol=rel_tol) and math.isclose( g, 205, rel_tol=rel_tol) and math.isclose( b, 171, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 211, rel_tol=rel_tol) and math.isclose( g, 166, rel_tol=rel_tol) and math.isclose( b, 236, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 172, rel_tol=rel_tol) and math.isclose( g, 173, rel_tol=rel_tol) and math.isclose( b, 204, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 172, rel_tol=rel_tol) and math.isclose( g, 168, rel_tol=rel_tol) and math.isclose( b, 177, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 179, rel_tol=rel_tol) and math.isclose( g, 222, rel_tol=rel_tol) and math.isclose( b, 251, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 185, rel_tol=rel_tol) and math.isclose( g, 247, rel_tol=rel_tol) and math.isclose( b, 172, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 196, rel_tol=rel_tol) and math.isclose( g, 239, rel_tol=rel_tol) and math.isclose( b, 213, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 227, rel_tol=rel_tol) and math.isclose( g, 164, rel_tol=rel_tol) and math.isclose( b, 235, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 185, rel_tol=rel_tol) and math.isclose( g, 237, rel_tol=rel_tol) and math.isclose( b, 213, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 241, rel_tol=rel_tol) and math.isclose( g, 177, rel_tol=rel_tol) and math.isclose( b, 174, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 245, rel_tol=rel_tol) and math.isclose( g, 172, rel_tol=rel_tol) and math.isclose( b, 214, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 204, rel_tol=rel_tol) and math.isclose( g, 209, rel_tol=rel_tol) and math.isclose( b, 224, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
                if math.isclose( r, 180, rel_tol=rel_tol) and math.isclose( g, 174, rel_tol=rel_tol) and math.isclose( b, 255, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
    
        # 4. convert to "L" mode (gray)
        image = image.convert("L") 
        # 5. resize the image (make the resolution higher)
        image = image.resize((400, 150))
        # 6. add border to prevent chopped at edge
        image = ImageOps.expand(image, border = 30, fill = 255)
        # 7. smoothen image
        image = image.filter(ImageFilter.SMOOTH_MORE)
        # 8. convert to black-white image
        image = image.point(lambda x: 0 if x<170 else 255, '1')
        
        image.save('image_processed.png')
    
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 9. sent to tesseract (by pytesseract)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        captcha_result = pytesseract.image_to_string('image_processed.png', lang='num', config="-c tessedit_char_whitelist=0123456789 --psm 7 8")
        captcha_result = captcha_result.replace(" ", "")
        captcha_result = captcha_result.replace("\n", "")

    # 10. return result
    return captcha_result
    
    
    





def captcha_file(image_screenshot_path):
    
    rel_tol = 0.13
    captcha_result = ''
    
    
    

    # 1. download image from image_url
    

    # 2. convert from "P" mode to "RGB" mode
    image = Image.open(image_screenshot_path)
    image = image.convert('RGB')
    image_data = image.load()
    height,width = image.size

    # 3. get rid of background * by color
    for loop1 in range(height):
        for loop2 in range(width):
            r,g,b = image_data[loop1,loop2]
            if math.isclose( r, 202, rel_tol=rel_tol) and math.isclose( g, 216, rel_tol=rel_tol) and math.isclose( b, 198, rel_tol=rel_tol) :
                    image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 186, rel_tol=rel_tol) and math.isclose( g, 171, rel_tol=rel_tol) and math.isclose( b, 160, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 216, rel_tol=rel_tol) and math.isclose( g, 225, rel_tol=rel_tol) and math.isclose( b, 249, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 238, rel_tol=rel_tol) and math.isclose( g, 193, rel_tol=rel_tol) and math.isclose( b, 200, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 194, rel_tol=rel_tol) and math.isclose( g, 180, rel_tol=rel_tol) and math.isclose( b, 192, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 227, rel_tol=rel_tol) and math.isclose( g, 248, rel_tol=rel_tol) and math.isclose( b, 172, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 217, rel_tol=rel_tol) and math.isclose( g, 170, rel_tol=rel_tol) and math.isclose( b, 196, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 242, rel_tol=rel_tol) and math.isclose( g, 194, rel_tol=rel_tol) and math.isclose( b, 175, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 226, rel_tol=rel_tol) and math.isclose( g, 238, rel_tol=rel_tol) and math.isclose( b, 211, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 241, rel_tol=rel_tol) and math.isclose( g, 197, rel_tol=rel_tol) and math.isclose( b, 234, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 241, rel_tol=rel_tol) and math.isclose( g, 225, rel_tol=rel_tol) and math.isclose( b, 234, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 174, rel_tol=rel_tol) and math.isclose( g, 205, rel_tol=rel_tol) and math.isclose( b, 171, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 211, rel_tol=rel_tol) and math.isclose( g, 166, rel_tol=rel_tol) and math.isclose( b, 236, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 172, rel_tol=rel_tol) and math.isclose( g, 173, rel_tol=rel_tol) and math.isclose( b, 204, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 172, rel_tol=rel_tol) and math.isclose( g, 168, rel_tol=rel_tol) and math.isclose( b, 177, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 179, rel_tol=rel_tol) and math.isclose( g, 222, rel_tol=rel_tol) and math.isclose( b, 251, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 185, rel_tol=rel_tol) and math.isclose( g, 247, rel_tol=rel_tol) and math.isclose( b, 172, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 196, rel_tol=rel_tol) and math.isclose( g, 239, rel_tol=rel_tol) and math.isclose( b, 213, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 227, rel_tol=rel_tol) and math.isclose( g, 164, rel_tol=rel_tol) and math.isclose( b, 235, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 185, rel_tol=rel_tol) and math.isclose( g, 237, rel_tol=rel_tol) and math.isclose( b, 213, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 241, rel_tol=rel_tol) and math.isclose( g, 177, rel_tol=rel_tol) and math.isclose( b, 174, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 245, rel_tol=rel_tol) and math.isclose( g, 172, rel_tol=rel_tol) and math.isclose( b, 214, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 204, rel_tol=rel_tol) and math.isclose( g, 209, rel_tol=rel_tol) and math.isclose( b, 224, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255
            if math.isclose( r, 180, rel_tol=rel_tol) and math.isclose( g, 174, rel_tol=rel_tol) and math.isclose( b, 255, rel_tol=rel_tol) :
                image_data[loop1,loop2] = 255,255,255,255

    # 4. convert to "L" mode (gray)
    image = image.convert("L") 
    # 5. resize the image (make the resolution higher)
    image = image.resize((400, 150))
    # 6. add border to prevent chopped at edge
    image = ImageOps.expand(image, border = 30, fill = 255)
    # 7. smoothen image
    image = image.filter(ImageFilter.SMOOTH_MORE)
    # 8. convert to black-white image
    image = image.point(lambda x: 0 if x<170 else 255, '1')
    
    image.save('image_screenshot_processed.png')

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # 9. sent to tesseract (by pytesseract)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    captcha_result = pytesseract.image_to_string('image_screenshot_processed.png', lang='num', config="-c tessedit_char_whitelist=0123456789 --psm 7 8")
    captcha_result = captcha_result.replace(" ", "")
    captcha_result = captcha_result.replace("\n", "")


    # 10. return result
    return captcha_result