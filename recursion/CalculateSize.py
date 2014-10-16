#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this script is to calculate the size of the folder using recursive function.
import os
def disk_usage(path):
    total = os.path.getsize(path)
    if not os.path.isdir(path):
        return os.path.getsize(path)
    else:
        for i in os.listdir(path):
            total = total+disk_usage(os.path.join(path, i))
    return total/(1024*1024)