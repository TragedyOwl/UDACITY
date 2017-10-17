import tensorflow as tf

# 记得给tensor对象定义名字啊~

tf.reset_default_graph()

save_file = './model.ckpt'

# Two Tensor Variables: weights and bias
# 两个 Tensor 变量：权重和偏置项
weights = tf.Variable(tf.truncated_normal([2, 3]), name='weights_0')
bias = tf.Variable(tf.truncated_normal([3]), name='bias_0')

saver = tf.train.Saver()

# Print the name of Weights and Bias
# 打印权重和偏置项的名称
print('Save Weights: {}'.format(weights.name))
print('Save Bias: {}'.format(bias.name))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver.save(sess, save_file)

# Remove the previous weights and bias
# 移除之前的权重和偏置项
tf.reset_default_graph()

# Two Variables: weights and bias
# 两个变量：权重和偏置项
bias = tf.Variable(tf.truncated_normal([3]), name='bias_0')
weights = tf.Variable(tf.truncated_normal([2, 3]) ,name='weights_0')

saver = tf.train.Saver()

# Print the name of Weights and Bias
# 打印权重和偏置项的名称
print('Load Weights: {}'.format(weights.name))
print('Load Bias: {}'.format(bias.name))

with tf.Session() as sess:
    # Load the weights and bias - No Error
    # 加载权重和偏置项 - 没有报错
    saver.restore(sess, save_file)

print('Loaded Weights and Bias successfully.')