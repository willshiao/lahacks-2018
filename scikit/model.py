import numpy as np
import tensorflow as tf

def createNBWords(input):
	data = []
	WINDOW_SIZE = 2
	for sentence in input:
		for word_index, word in enumerate(sentence):
			for nb_word in sentence[max(word_index - WINDOW_SIZE,0) : min(word_index + WINDOW_SIZE, len(sentence)) + 1] :
				if nb_word != word:
					data.append([word,nb_word])
	return data

def createWordSets(words):
	word2int = {}
	int2word = {}
	for i,word in enumerate(words):
		word2int[word] = i
		int2word[i] = word
	return word2int,int2word

def to_one_hot(index,size):
	temp = np.zeros(size)
	temp[index] = 1
	return temp
			
def main():
	words = ['I wanted to die','Please kill me', 'I hate my life','got to risk it for the biscuit']
	for i in range(len(words)):
		words[i] = words[i].lower()	
	#remove duplicates
	vocab_size = len(words) 
	
	#create maching sets of words with respective number representation
	word2int,int2word = createWordSets(words)
	
	#create sentences
	raw_sentences = words.split('.')
	sentences = []
	for sen in raw_sentences:
		sentences.append(sen.split())
	
	#split into neighboring words matrix
	data = createNBWords(sentences)
	print(data)
	x_train = []
	y_train = []
	for data_word in data:
		x_train.append(to_one_hot(word2int[ data_word[0] ], vocab_size))
		y_train.append(to_one_hot(word2int[ data_word[0] ], vocab_size))
	x_train = np.asarray(x_train)
	y_train = np.asarray(y_train)

	x = tf.placeholder(tf.float32, shape=(None, vocab_size))
	y_label = tf.placeholder(tf.float32, shape=(None, vocab_size))
	
	EMBEDDING_DIM = 5
	
	w1 = tf.Variable(tf.random_normal([vocab_size,EMBEDDING_DIM]))
	b1 = tf.Variable(tf.random_normal([EMBEDDING_DIM]))
	hidden_layer = tf.add(tf.matmul(x,w1),b1)
	
	w2 = tf.Variable(tf.random_normal([EMBEDDING_DIM,vocab_size]))
	b2 = tf.Variable(tf.random_normal([vocab_size]))
	prediction = tf.nn.softmax(tf.add(tf.matmul(hidden_layer,w2),b2))

	sess = tf.Session()
	init = tf.global_variables_initializer()
	sess.run(init)
	cross_entropy_loss = tf.reduce_mean(-tf.reduce_sum(y_label * tf.log(prediction), reduction_indices=[1]))
	train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy_loss)

	n_iters = 10000

	# train for n_iter iterations

	for _ in range(n_iters):
		sess.run(train_step, feed_dict={x: x_train, y_label: y_train})

	print('loss is : ', sess.run(cross_entropy_loss, feed_dict={x: x_train, y_label: y_train}))

if __name__ == "__main__":
	main()
