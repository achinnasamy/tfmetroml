


import tensorflow as tf


svn_fv_contract = tf.constant(998)
svn_fv_timeline = tf.constant(97)

dot_product = svn_fv_contract * svn_fv_timeline


# Approach One with using the Session()
with tf.Session() as session:

    print (session.run(dot_product))
    print (dot_product.eval())


# Approach Two with using the InteractiveSession()
# A convenient method of syntactic sugar to keep the session open
tf.InteractiveSession()
print (dot_product.eval())
