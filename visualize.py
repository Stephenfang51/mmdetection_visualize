import json
import matplotlib.pyplot as plt
import sys
import os
from collections import OrderedDict

class visualize_mmdetection():
    def __init__(self, path):
        self.log = open(path)
        self.dict_list = list()
        self.loss_rpn_bbox = list()
        self.loss_rpn_cls = list()
        self.loss_bbox = list()
        self.loss_cls = list()
        self.loss = list()
        self.acc = list()

    def load_data(self):
        for line in self.log:
            info = json.loads(line)
            self.dict_list.append(info)

        for i in range(1, len(self.dict_list)):
            for value, key in dict(self.dict_list[i]).items():
                # ------------find key for every iter-------------------#
                loss_rpn_cls_value = dict(self.dict_list[i])['loss_rpn_cls']
                loss_rpn_bbox_value = dict(self.dict_list[i])['loss_rpn_bbox']
                loss_bbox_value = dict(self.dict_list[i])['loss_bbox']
                loss_cls_value = dict(self.dict_list[i])['loss_cls']
                loss_value = dict(self.dict_list[i])['loss']
                acc_value = dict(self.dict_list[i])['acc']
                # -------------list append------------------------------#
                self.loss_rpn_cls.append(loss_rpn_cls_value)
                self.loss_rpn_bbox.append(loss_rpn_bbox_value)
                self.loss_bbox.append(loss_bbox_value)
                self.loss_cls.append(loss_cls_value)
                self.loss.append(loss_value)
                self.acc.append(acc_value)
                # -------------clear repeated value---------------------#
        self.loss_rpn_cls = list(OrderedDict.fromkeys(self.loss_rpn_cls))
        self.loss_rpn_bbox = list(OrderedDict.fromkeys(self.loss_rpn_bbox))
        self.loss_bbox = list(OrderedDict.fromkeys(self.loss_bbox))
        self.loss_cls = list(OrderedDict.fromkeys(self.loss_cls))
        self.loss = list(OrderedDict.fromkeys(self.loss))
        self.acc = list(OrderedDict.fromkeys(self.acc))

    def show_chart(self):
        plt.rcParams.update({'font.size': 15})

        plt.figure(figsize=(20, 20))

        plt.subplot(321, title='loss_rpn_cls', ylabel='loss')
        plt.plot(self.loss_rpn_cls)
        plt.subplot(322, title='loss_rpn_bbox', ylabel='loss')
        plt.plot(self.loss_rpn_bbox)

        plt.subplot(323, title='loss_cls', ylabel='loss')
        plt.plot(self.loss_cls)
        plt.subplot(324, title='loss_bbox', ylabel='loss')
        plt.plot(self.loss_bbox)
        plt.subplot(325, title='total loss', ylabel='loss')
        plt.plot(self.loss)
        plt.subplot(326, title='accuracy', ylabel='accuracy')
        plt.plot(self.acc)
        plt.suptitle((sys.argv[1][5:] + "\n training result"), fontsize=30)
        plt.savefig(('output/' + sys.argv[1][5:] + '_result.png'))


if __name__ == '__main__':
    x = visualize_mmdetection(sys.argv[1])
    x.load_data()
    x.show_chart()