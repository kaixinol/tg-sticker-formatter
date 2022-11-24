from argparse import RawTextHelpFormatter, ArgumentParser
from sys import argv
from PIL import Image
from math import sqrt
from os.path import isdir
parser = ArgumentParser(
    description='A resize tool that convert images (gif and webp, jpg, png) that do not meet Telegram Sticker requirements into acceptable images or video streams(webm) of 512x512 size.\n\tGithub: \033[4;5mhttps://github.com/kaixinol/tg-sticker-formatter\033[0m',
    epilog='''
Example:
\tmain.py -i input_folder -o output_folder --multhread 10
\tmain.py -i input_file -o output_file --align left
''', formatter_class=RawTextHelpFormatter)
parser.add_argument('-i', metavar='INPUT', type=str, required=True,
                    help="The file or folder path that needs to be converted")
parser.add_argument('-o', metavar='OUTPUT', default='/',
                    help="saved location after conversion")
parser.add_argument('-f', '--force', action='store_true', default=False,
                    help='whether to forcibly zoom if the image size is too small \033[31mdefault is disabled\033[0m')
parser.add_argument('-thread', '--multithread', metavar='THREAD', default=2, type=int,
                    help='The number of concurrent tasks. \033[31mdefault is 2\033[0m')
parser.add_argument('--makeicon', metavar='FILE', type=str)
if len(argv) == 1:
    parser.print_help()
    exit(0)
args = parser.parse_args()
work = list()

def resize_gif
def resize_pic(image):
    def default(image_pil):
        ratio_w = 512 / image_pil.width
        ratio_h = 512 / image_pil.height
        if ratio_w < ratio_h:
          resize_width = 512
          resize_height = round(ratio_w * image_pil.height)
        else:
          resize_width = round(ratio_h * image_pil.width)
          resize_height = 512
        image_resize = image_pil.resize(
         (resize_width, resize_height), Image.Resampling.LANCZOS)
        return image_resize

    def small(image_pil):
        if image_pil.width> image_pil.height:
            salt = sqrt(512/(image_pil.width))
        else:
            salt = sqrt(512/(image_pil.height))
        salt *= int(pow(salt*salt, 1/3))
        resize_w = int(image_pil.width*salt)
        resize_h = int(image_pil.height*salt)
        image_resize = image_pil.resize(
        (resize_w, resize_h), Image.Resampling.LANCZOS)
        background = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
        offset = (round((512-resize_w)/2),
              round((512-resize_h)/2))
        background.paste(image_resize, offset,mask=background)
        return background

    pic=Image.open(image, 'r')
    if args.force or not (image.width < 200 or 200 > image.height):
        return default(pic)
    else:
        return small(pic)
def get_task():
    if isdir(args.i):

for file in onlyfiles:
    if file[file.find('.'):].lower() in ['.webp', '.png', '.jpg']:
        image = Image.open(os.getcwd()+'/Input/'+file, 'r')
        # special process for very small picture
        if image.width < 200 or 200 > image.height:
            smallPicResize(image).save(os.getcwd()+'/Output/' +
                                       file[:file.find('.')]+'.png', quality=100)
            logger.info('\033[92m[small pic]\033[39m'+file)
        else:
            resize(image, 512, 512).save(os.getcwd()+'/Output/' +
                                         file[:file.find('.')]+'.png', quality=100)
            logger.info(file)
    elif file[file.find('.'):].lower() == '.gif':
        image = Image.open(os.getcwd()+'/Input/'+file, 'r')
        b1 = os.getcwd()+'/Output/'+file[:file.find('.')]
        b2 = os.getcwd()+'/Input/'+file
        logger.info(file)
        if image.height > image.width:
            subprocess.check_output(
                f'ffmpeg -i {b2} -c:v libvpx-vp9 -r 30 -loglevel quiet -vf scale=-1:512 {b1}.webm')
        elif image.width > image.height:
            subprocess.check_output(
                f'ffmpeg -i {b2} -c:v libvpx-vp9 -r 30 -loglevel quiet -vf scale=512:-1 {b1}.webm')
        else:
            subprocess.check_output(
                f'ffmpeg -i {b2} -c:v libvpx-vp9 -r 30 -loglevel quiet -vf scale=512:512 {b1}.webm')
    else:
        logger.warning(f'ignore: {file}')
