## 电视剧本生成

一个非常好的   文本  生成器  RNN   例子

#### 文本：
1. 包括文本的预处理，将文本转化为数值
2. 使用embedding技术将文本映射到高维空间进行
3. 使用tf.nn.embedding_lookup()训练查询表，将相似语义词组进行聚类
4. 可对符号一起进行预测

#### 生成器 RNN
使用RNN作为生成器，一方面学习语境特征，一方面将特征用于预测


#### 小坑

lr_ = tf.placeholder(<code><font color="#A52A2A" size="3">tf.float32</font></code>, name='lr')

啊啊啊啊啊啊啊啊啊啊啊啊啊，这里一定要小心，不能写成<code><font color="#A52A2A" size="3">int32</font></code>啊啊啊啊啊啊啊啊啊啊

否则<code><font color="#A52A2A" size="3">loss</font></code>值就不下降了。。。。囧

optimizer = tf.train.AdamOptimizer(lr)

应该是这里使用了Adam优化器，这东西会自适应调整lr

int3貌似会丢失精度。。。囧




