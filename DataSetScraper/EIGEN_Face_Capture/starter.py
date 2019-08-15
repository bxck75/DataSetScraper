import argparse,os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",help = "path to input image")
ap.add_argument("-f", "--folder",help = "path to input folder")
ap.add_argument("-s", "--size", default=1024,help = "Size to resize ")
args = vars(ap.parse_args())

if args['image']:
    print('detecting on image')
    os.system('python capture_all_faces.py -i ' + args['image'] + ' -s '+ args['size'])
if args['folder']:
    print('detecting on folder')
    os.system('for i in `ls ' + args['folder'] + '`;do python capture_all_faces.py -i ' + args['folder'] + '/$i -s ' + args['size'] + '; done')
