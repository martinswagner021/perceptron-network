import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def ReLU(x):
  return np.maximum(0,x)

def softmax(X):
  return np.exp(X) / sum(np.exp(X))

def forward_prop(W1, b1, W2, b2, pixels):
  Z1 = W1.dot(pixels)+b1
  A1 = ReLU(Z1)
  Z2 = W2.dot(A1)+b2
  A2 = softmax(Z2)
  return Z1, A1, Z2, A2

def prediction(A2):
  return np.argmax(A2,0)[0]

def make_prediction(custom_img):
  W1 = np.load('/home/wagner/Documents/perceptron-network/Drawing/utils/W1.npy', allow_pickle=True)
  W2 = np.load('/home/wagner/Documents/perceptron-network/Drawing/utils/W2.npy', allow_pickle=True)
  b1 = np.load('/home/wagner/Documents/perceptron-network/Drawing/utils/b1.npy', allow_pickle=True)
  b2 = np.load('/home/wagner/Documents/perceptron-network/Drawing/utils/b2.npy', allow_pickle=True)
  # make_prediction() automatically transposes and divides it by 255, so that
  # any raw image in 784 array format is allowed
  custom_img = custom_img/255
  _, _, _, A2 = forward_prop(W1, b1, W2, b2, custom_img.T)
  return prediction(A2)