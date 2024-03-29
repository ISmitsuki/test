#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from functools import reduce


class Perceptron(object):
    #初始化输入层和激活函数
    def __init__(self, input_num, activator):

        self.activator = activator
        self.weights = [0.0 for _ in range(input_num)]
        self.bias = 0.0

    #返回权重与偏置
    def __str__(self):
        return 'weights\t:%s\nbias\t:%f\n' % (self.weights, self.bias)

    #输入向量，输出感知器的计算结果
    def predict(self, input_vec):
        return self.activator(
            reduce(lambda a, b: a + b,
                   map(lambda xw: xw[0] * xw[1],
                       zip(input_vec, self.weights))
                   , 0.0) + self.bias)

    #输入向量，与每个向量对应的label，训练轮数，学习率
    def train(self, input_vecs, labels, iteration, rate):
        for i in range(iteration):
            self._one_iteration(input_vecs, labels, rate)

    #所有数据训练一次，计算并更新权重
    def _one_iteration(self, input_vecs, labels, rate):
        samples = zip(input_vecs, labels)
        for (input_vec, label) in samples:
            output = self.predict(input_vec)
            self._update_weights(input_vec, output, label, rate)

    #按感知器规则更新权重
    def _update_weights(self, input_vec, output, label, rate):
        delta = label - output
        self.weights = list(map(
            lambda xw: xw[1] + rate * delta * xw[0],
            zip(input_vec, self.weights)))
        self.bias += rate * delta

#激活函数
def f(x):
    return 1 if x > 0 else 0


def get_training_dataset():
    input_vecs = [[1, 1], [0, 0], [1, 0], [0, 1]]
    labels = [1, 0, 0, 0]
    return input_vecs, labels


def train_and_perceptron():
    p = Perceptron(2, f)
    input_vecs, labels = get_training_dataset()
    p.train(input_vecs, labels, 10, 0.1)
    return p


if __name__ == '__main__':
    # 训练and感知器
    and_perception = train_and_perceptron()
    # 打印训练获得的权重
    print(and_perception)
    # 测试
    print('1 and 1 = %d' % and_perception.predict([1, 1]))
    print('0 and 0 = %d' % and_perception.predict([0, 0]))
    print('1 and 0 = %d' % and_perception.predict([1, 0]))
    print('0 and 1 = %d' % and_perception.predict([0, 1]))