from keras.layers import Layer
import keras.backend as K
from math import sqrt


class Bias(Layer):
    def __init__(self, n_outputs, **kwargs):
        self.output_dim = n_outputs
        self.bias = None
        super(Bias, self).__init__()

    def build(self, input_shape):
        self.bias = self.add_weight(name='bias',
                                    initializer='normal',
                                    shape=(input_shape[-1],))
        self.bias = self.bias / sqrt(self.output_dim)
        super(Bias, self).build(input_shape)

    def __call__(self, *args, **kwargs):
        return super(Bias, self).__call__(*args, **kwargs)

    def call(self, x):
        return x + self.bias
