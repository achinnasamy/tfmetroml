
import tensorflow as tf

matrix = [[1.0, 2.0], [3.0, 4.0]]

print type(matrix)



tf_matrix = tf.convert_to_tensor(matrix, dtype=tf.float32)

print type(tf_matrix)