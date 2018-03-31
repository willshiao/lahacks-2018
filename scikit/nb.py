from __future__ import division

import numpy as np
import nltk
import re 
import pickle
import os.path
import tensorflow as tf
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB

#turn phrases into stemmed word representations
def cleanUp(message):
	corpus = []
	for i in range(len(message)):
		phrase = re.sub('[^a-zA-Z]',' ',message[i])
		phrase = phrase.lower()
		phrase = phrase.split()
		st = PorterStemmer()
		phrase = [st.stem(word) for word in phrase if not word in set(stopwords.words('english'))]
		phrase = ' '.join(phrase)
		corpus.append(phrase.lower())	
	return	corpus

def save_NB_Model(model,filename):
	with open(filename,'wb') as f:
		pickle.dump(model,f)
	return

def load_NB_Model(filename):
	if os.path.isfile(filename):
		with open(filename,'rb') as f:
			loaded = pickle.load(f)
		return loaded
	return GaussianNB()
		

def train_NB_Model(x_test, y_test, filename):
	model = load_model(filename)
	model.partial_fit(x_test,y_test,classes=np.unique([0,1]))
	save_model(model,filename)
	return

def createWordSets(words):
	word2int = {}
	int2word = {}
	l = []
	for word in words:	
		for w in word.split():
			l.append(w)
	l = set(l)
	for i,word in enumerate(l):
		word2int[word] = i
		int2word[i] = word	
	return word2int, int2word

 	
def main():
	filename = 'model.pkl'
	messages1 = ['I wanted to die','Please kill me', 'I hate my life','got to risk it for the biscuit']
	y1 = [0,1,1,1]
	messages2 = ['I love  myself']
	y2 = [1]
	#get words
	corpus = cleanUp(messages1)	
	word2int, int2word = createWordSets(corpus)
if __name__ == "__main__":
	main()
