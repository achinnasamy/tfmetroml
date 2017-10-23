import tensorflow as tf
statement = tf.constant('\n\n\n Tensor flow is installed correctly...')
sess = tf.Session()
print(sess.run(statement))