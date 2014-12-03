How Humans Sketch (CS-706 Project)
============================================

How to Use
-------

To Train:
```sh
python learn.py -d TRAINING_DATA_FOLDER
```
where TRAINING_DATA_FOLDER is the folder which has all the sketches for Training Purpose in folders with name as the category name

i.e
```sh
TRAINING_DATA_FOLDER
|_ Category_1
  |_ Img_01
  |_ Img_02
  |_ Img_03    
|_ Category_2
  |_ Img_01
  |_ Img_02
  |_ Img_03
```

To Test:
```sh
python entry.py -c TRAINING_DATA_FOLDER/codebook.file -m TRAINING_DATA_FOLDER/trainingdata.svm.model -l TRAINING_DATA_FOLDER/label_mapping.txt -p TRAINING_DATA_FOLDER/trainingdata.svm.prediction 
```

Resources
------
* http://cybertron.cg.tu-berlin.de/eitz/projects/classifysketch/
* http://cybertron.cg.tu-berlin.de/eitz/pdf/2012_siggraph_classifysketch.pdf
* http://www.csie.ntu.edu.tw/~cjlin/libsvm/
* http://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf
*  http://olivier.chapelle.cc/pub/tnn99.pdf
* https://github.com/shackenberg/Minimal-Bag-of-Visual-Words-Image-Classifier
* http://www.vlfeat.org/api/sift.html
* https://copilosk.fbk.eu/images/f/f6/Sift.pdf
* http://www.python-course.eu/python_tkinter.php

Authors
------
* Mohnish Bhatt
* Navin Pai
* Prashant Nagansure
* Vishesh Jain
