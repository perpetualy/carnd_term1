# Solution is available in the other "solution.py" tab
import tensorflow as tf

# TODO: Convert the following to TensorFlow:
x = tf.constant(10)
y = tf.constant(2)
z = tf.subtract(tf.cast(tf.divide(x,y),tf.int32), 1)

# TODO: Print z from a session
with tf.Session() as sess:
    output = sess.run(z)
    print(output)