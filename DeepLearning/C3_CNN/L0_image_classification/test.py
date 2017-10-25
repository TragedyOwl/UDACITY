import tensorflow as tf


test_x = tf.placeholder(tf.float32, [None, 32, 32, 5])

print(test_x.get_shape().as_list()[0])



