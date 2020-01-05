#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2020/01/05
# @Author   : Air.Lee
# @Brief    : adb自动push脚本

import re
import time
import os
import sys


def doAdbPush(fileName):
    with open(fileName, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("Install:"):
                path = line[8:].strip()
                # print(path)
                pos = 0
                for sub in re.finditer('/', path):
                    pos = sub.start()
                    # print(pos)
                    if pos > 20:  # > lens("out/target/product/")
                        break
                # print("pos: " + str(pos))
                target_path = path[pos:]
                cmd = "adb push " + path + " " + target_path
                print(cmd)
                # time.sleep(0.5)
                os.system(cmd)
                pass


if __name__ == '__main__':
    start = time.time()
    os.system("adb wait-for-device root;adb wait-for-device aremount;")
    doAdbPush(sys.argv[1])
    print('\033[32m Done! Cost Time: %d seconds \033[0m' % (time.time() - start))
