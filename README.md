# image super resolution

## enviornment
- tensorflow
- ubuntu 18.04

## data
- create a dir name `data` and put the training data in here.
- If you want to generate more data for data augmentation, run `image.py` to get more data.

## train
- First, go to `arg.py` to set the parameter you want, like scale, lr, number of filter...
- Then run `python3 train.py` and start training.

## inference
- After training, you must use the same parameter to test the model, run `python3 sr.py --file="your image path"` and you can get upscale image for the low resolution image in the output dir.
- It will genertate 6 image for each lr image, the image named result is the upscale one.

## reference
- https://github.com/jiny2001/dcscn-super-resolution


