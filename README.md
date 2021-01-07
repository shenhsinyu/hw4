# image super resolution

## enviornment
- tensorflow
- ubuntu 18.04

## data
- create a dir name `data` and put the training data in here.
- If you want to generate more data for data augmentation, run `python3 augmentation.py --dataset="your dataset dir" --augment_level="you can choose 4/8"`.

## train
- First, go to `arg.py` to set the parameter you want, like scale, lr, number of filter... and start training.

## inference
- After training, you must use the same parameter to test the model, run `python3 sr.py --file="your image path"` and you can get upscale image for the low resolution image in the output dir.
- It will genertate 6 images for each lr image, the image named result is the upscale one.

## result
low resolution image 

![image](https://github.com/shenhsinyu/hw4/blob/main/00-lr.png)


high resolution image (x3)

![image](https://github.com/shenhsinyu/hw4/blob/main/00.png)

## reference
- https://github.com/jiny2001/dcscn-super-resolution


