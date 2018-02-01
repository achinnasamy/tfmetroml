
import numpy as np
import tensorflow as tf


corpus_raw = 'The investment made on the contract is void and null. The money and euros is good.'

corpus_raw = corpus_raw.lower()

print(corpus_raw)

words = []

for word in corpus_raw.split():
    if word != '.':  # because we don't want to treat . as a word
        words.append(word)


words = set(words)

word2int = {}
int2word = {}

vocab_size = len(words)


print (words)