#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 存储分页信息，用于分页显示Blog的功能
# Page.limit/Page.offset 用于SQL语句的条件设定limit=(p.offset, p.limit)
class Page(object):
    def __init__(self, item_count, page_index=1, page_size=10):
        self.item_count = item_count                            # blog总篇数
        self.page_size = page_size                              # 每页显示数，即页大小
        self.page_count = item_count // page_size + (1 if item_count % page_size > 0 else 0)    # 总页数
        if (item_count == 0) or (page_index > self.page_count):  # 若blog总篇数为0或者页索引大于总页数则重置为第一页
            self.offset = 0
            self.limit = 0
            self.page_index = 1
        else:
            self.page_index = page_index                        # 页索引从1开始
            self.offset = self.page_size * (page_index - 1)     # 页偏移量 = 每页大小 * (页索引 - 1)
            self.limit = self.page_size                         # 保存页大小
        self.has_next = self.page_index < self.page_count       # 是否有下一页，当页索引小于页总数时为True
        self.has_previous = self.page_index > 1                 # 是否有上一页，当页索引大于1时为True

