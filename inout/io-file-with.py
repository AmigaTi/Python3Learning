#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

# ===============================================
# 读文件
# ===============================================

f = None
try:
    f = open('./with_file.txt', 'r')  # 以只读模式打开文件
    s = f.read()  # 读取文件的全部内容
    print(s)  # 打印文件内容
finally:
    if f:  # 如果f不为None
        f.close()  # 关闭文件
print('----------------------------')
'''
Hello world
Hello me
'''

# ===============================================
# with...as         自动调用close()方法
# ===============================================
# read()            小文件，一次性读取
# read(size)        不能确定文件大小，每次最多读取size个字节的内容
# readline()        每次读取一行内容，可用于配置文件读取
# readlines()       一次读取所有内容并按行返回list

with open('./with_file.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())  # 去掉末尾的\n
print('----------------------------')
'''
Hello world
Hello me
'''

# 读取文件同时输出行号和内容
with open('./with_file.txt', 'r') as f:
    for n, line in enumerate(f):
        print("%d,%s" % (n, line.strip()))
print('----------------------------')
'''
0,Hello world
1,Hello me
'''

# 二进制文件，打开模式为rb
with open('./with_monkey.jpg', 'rb') as f:
    print(f.read())
print('----------------------------')

# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
# 遇到编码错误，则通过errors参数设置为ignore直接忽略掉

with open('./with_gbk.txt', 'r', encoding='gbk', errors='ignore') as f:
    print(f.read())
print('----------------------------')
'''
你好，世界
你好，我
'''


# ===============================================
# 写文件
# ===============================================

with open('./with_file2.txt', 'w') as f:
    f.write('You look so beautiful.')

# 测试是否内容写入成功
with open('./with_file2.txt', 'r') as f:
    print(f.read())
print('----------------------------')
'''
You look so beautiful.
'''


# ===============================================
# 读写文件
# ===============================================
result_format = []
with open('./info_web_service.soap', 'r', encoding='utf-8') as f:
    soap = f.read()
    print(soap)
    pattern = r'(.*?{)([^}].*)'
    re_soap = re.compile(pattern)
    pattern2 = r'(.*?;\s)(.*)'
    re_soap2 = re.compile(pattern2)

    # 使用正则表达式pattern将soap内容分成两部分，第一次匹配部分和其他部分
    # while re_soap.search(soap):
    #     print(re_soap.search(soap).group(1))      # 第一次匹配部分 (对此部分进行正则表达式pattern2的匹配)
    #     print(re_soap.search(soap).group(2))      # 其他部分
    #     soap = re_soap.search(soap).group(2)      # 对其他部分进行递归式的进行正则表达式pattern的匹配，结果也分成两部分

    result = []
    while re_soap.search(soap):
        soap2 = re_soap.search(soap).group(1)
        if re_soap2.search(soap2):
            while re_soap2.search(soap2):
                result.append(re_soap2.search(soap2).group(1))
                print(re_soap2.search(soap2).group(1))
                # print(re_soap2.search(soap2).group(2))
                soap2 = re_soap2.search(soap2).group(2)
            result.append(soap2)
            print(soap2)
        else:
            result.append(re_soap.search(soap).group(1))
            print(re_soap.search(soap).group(1))
        # print(re_soap.search(soap).group(2))
        soap = re_soap.search(soap).group(2)
    if re_soap2.search(soap):           # process the tail
        while re_soap2.search(soap):
            result.append(re_soap2.search(soap).group(1))
            print(re_soap2.search(soap).group(1))
            # print(re_soap2.search(soap).group(2))
            soap = re_soap2.search(soap).group(2)
        result.append(soap)
        print(soap)
    else:
        result.append(soap)
        print(soap)

    print('----------------------------------')
    pattern3 = r'.*{$'          # schema=anyType{0
    re_type3 = re.compile(pattern3)
    pattern4 = r'.*{};\s$'      # element=anyType{};1
    re_type4 = re.compile(pattern4)
    pattern5 = r'};\s$'         # };2
    re_type5 = re.compile(pattern5)
    pattern6 = r'.*;\s$'          # WordKey=shell;3
    re_type6 = re.compile(pattern6)
    pattern7 = r'}'             # }4
    re_type7 = re.compile(pattern7)
    prev, cur = -1, -1
    indent = 0
    for s in result:
        # print(s)
        type_code = -1
        if re_type3.match(s):
            type_code = 0
        elif re_type4.match(s):
            type_code = 1
        elif re_type5.match(s):
            type_code = 2
        elif re_type6.match(s):
            type_code = 3
        elif re_type7.match(s):
            type_code = 4
        # print('%s%d' % (s, type_code))

        prev = cur
        cur = type_code
        if cur == 0 and prev == -1:
            pass
        elif cur == 0 and prev == 0:
            indent += 1
        elif cur == 1 and prev == 0:
            indent += 1
        elif cur == 1 and prev == 1:
            pass
        elif cur == 2 and prev == 1:
            indent -= 1
        elif cur == 2 and prev == 2:
            indent -= 1
        elif cur == 0 and prev == 2:
            pass
        elif cur == 3 and prev == 0:
            indent += 1
        elif cur == 1 and prev == 3:
            pass
        elif cur == 3 and prev == 1:
            pass
        elif cur == 3 and prev == 3:
            pass
        elif cur == 2 and prev == 3:
            indent -= 1
        elif cur == 4 and prev == 2:
            indent -= 1
        print('%s%s%d' % (' ' * 4 * indent, s, indent))
        result_format.append('%s%s' % (' ' * 4 * indent, s))

with open('./info_web_service_formatted.soap', 'w', encoding='utf-8') as f:
    for s in result_format:
        f.write(s)
        f.write('\n')

'''
anyType{0
    schema=anyType{1
        element=anyType{2
            complexType=anyType{3
                choice=anyType{4
                    element=anyType{5
                        complexType=anyType{6
                            sequence=anyType{7
                                element=anyType{}; 8
                                element=anyType{}; 8
                                element=anyType{}; 8
                                element=anyType{}; 8
                                element=anyType{}; 8
                            }; 7
                        }; 6
                    }; 5
                    element=anyType{5
                        complexType=anyType{6
                            sequence=anyType{7
                                element=anyType{}; 8
                            }; 7
                        }; 6
                    }; 5
                    element=anyType{5
                        complexType=anyType{6
                            sequence=anyType{7
                                element=anyType{}; 8
                                element=anyType{}; 8
                            }; 7
                        }; 6
                    }; 5
                }; 4
            }; 3
        }; 2
    }; 1
    diffgram=anyType{1
        Dictionary=anyType{2
            Trans=anyType{3
                WordKey=shell; 4
                Pron=ʃel; 4
                Info=anyType{}; 4
                Translation=n. 贝壳,壳,外形；v. 去壳,脱落；n.[计算机] DOS命令 : 安装备用的COMMAND.COM文件, 并改变环境尺寸; 4
                Mp3=12448.mp3; 4
            }; 3
            Sentence=anyType{3
                Orig=Shells were bursting all around.; 4
                Trans=炮弹在四处爆炸。; 4
            }; 3
            Sentence=anyType{3
                Orig=There is an ornament made of shells on the wall.; 4
                Trans=墙上有一个贝壳做成的装饰品。; 4
            }; 3
            Sentence=anyType{3
                Orig=All that remained of the building after the fire was an empty shell.; 4
                Trans=一场大火过后，这座建筑剩下的只是一个空壳。; 4
            }; 3
        }; 2
    }; 1
}0
'''