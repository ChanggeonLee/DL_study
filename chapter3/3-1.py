import tensorflow as tf

# 그래프를 만드는 부분
hello = tf.constant('Hello, TensorFlow');
print(hello);

a = tf.constant(10)
b = tf.constant(32)
c = tf.add(a,b)
print(c)

# 만든 그래프를 실행하는 부분
sess = tf.Session()

print(sess.run(hello))
print(sess.run([a,b,c]))

sess.close()
