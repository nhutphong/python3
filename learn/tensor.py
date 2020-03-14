import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 0: ALL, 1: WARNING + ERR, 2: ERR, 3: NOTHING


def demo():
    # tf.placeholder => nhu 1 pattern de xuong feed_dict{ :truyen data vao}
    tf_placeholder = tf.placeholder(tf.float32,(3,4))
    can_tim =  tf_placeholder + 2

    sess = tf.Session()
    # print(sess.run(y)) # will cause an error

    df = np.random.randint(1,50, (3,4))
    print(sess.run(can_tim, feed_dict={tf_placeholder:df}))