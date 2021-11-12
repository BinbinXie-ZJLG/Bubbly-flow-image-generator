import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image
import os
import random
# os.environ["CUDA_VISIBLE_DEVICES"] = "3"

def detect_img(yolo):
    while True:
        filepath = input('Input filepath:')
        _img_path=os.listdir(filepath)
        random.shuffle(_img_path)
        i=0
        for img_path in _img_path:     
            i=i+1
            img_name=os.path.splitext(img_path)[0]
            try:
                print(filepath+img_path)
                image = Image.open(filepath+img_path)
            except:
                print('Open Error! Try again!')
                continue
            else:
                r_image = yolo.detect_image(img_name,image)
                r_image.save('result/'+img_name+'.jpg',quality=95)
                # r_image.show()
            if i==100:
                break
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    parser.add_argument(
        '--model', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )

    parser.add_argument(
        '--image', default='picture', action="store_true",
        help='Image detection mode, will ignore all positional arguments'
    )
    '''
    Command line positional arguments -- for video detection mode
    '''
    parser.add_argument(
        "--input", nargs='?', type=str,required=False,default='picture',
        help = "Video input path"
    )

    parser.add_argument(
        "--output", nargs='?', type=str, default="output",
        help = "[Optional] Video output path"
    )

    FLAGS = parser.parse_args()

    if FLAGS.image:
        """
        Image detection mode, disregard any remaining command line arguments
        """
        print("Image detection mode")
        if "input" in FLAGS:
            print(" Ignoring remaining command line arguments: " + FLAGS.input + "," + FLAGS.output)
        detect_img(YOLO(**vars(FLAGS)))
    elif "input" in FLAGS:
        detect_video(YOLO(**vars(FLAGS)), FLAGS.input, FLAGS.output)
    else:
        print("Must specify at least video_input_path.  See usage with --help.")
