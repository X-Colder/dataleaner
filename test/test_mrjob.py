#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:pitmaner
# Datetime:2018/7/16 下午10:53
# Software: PyCharm
# Project: dataleaner
# Filename: test_mrjob


from mrjob.job import MRJob
from ng_line_parser import NgLineParser


class MRPVDay(MRJob):
    ng_line_parser = NgLineParser()

    def mapper(self, _, line):
        self.ng_line_parser.parse(line)
        dy, tm = str(self.ng_line_parser.access_time).split()
        yield dy, 1  # 每一天的
        yield 'total', 1  # 所有的

    def reducer(self, key, values):
        yield key, sum(values)


def main():
    MRPVDay.run()


if __name__ == '__main__':
    main()