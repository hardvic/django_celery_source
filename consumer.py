# !/usr/bin/env python
# -*- coding: utf-8 -*-

from demoapp.tasks import add

if __name__ == '__main__':
    re = add.apply_async((1, 2))
    print(re)
