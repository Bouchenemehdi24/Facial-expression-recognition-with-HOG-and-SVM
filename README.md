# Facial-expression-recognition-with-HOG-and-SVM

## Description

Facial expressions are a form of nonverbal communication. The human face is extremely expressive, able to convey countless emotions without saying a word. And unlike some forms of nonverbal communication, facial expressions are universal. Human facial expression could arguably be classified into seven classes: neutral, sadness, surprise, happiness, fear, anger, contempt and disgust.

## Objective
Automatic Facial-expression-recognition concerns matching a face against one of above classes using machine learning and computer vision techniques. 	

## Method
We have used histogram of oriented gradients descriptor features and support vector machines classifier with radial basis function kernel. We have used Scikit-image implementation of HOG algorithm and Scikit-learn for SVM. 

### Dependencies

* numpy
* imutils
* OpenCV
* scikit-learn 
* scikit-image
* matplotlib


## Dataset
We have used Kaggle Extended Cohn-Kanade Dataset (CK+) dataset, it can be obtained from here https://www.kaggle.com/shawon10/ckplus.

## Results
We have obtained 100% accuracy using both hold-out, and cross-validation.
