#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio


# async/await


# 从Python 3.5开始引入了针对coroutine的新语法async和await，
# 只需要做两步简单的替换：
#   @asyncio.coroutine替换为async
#   yield from替换为await


# asyncio提供了完善的异步IO支持；
# 异步操作需要在coroutine中通过yield from完成；
# 多个coroutine可以封装成一组Task然后并发执行。

# 用asyncio的异步网络连接来获取sina、sohu和163的网站首页


async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()       # similar to flush
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# 3个连接由一个线程通过coroutine并发完成
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

''''
wget www.163.com...
wget www.sohu.com...
wget www.sina.com.cn...
www.163.com header > HTTP/1.0 302 Moved Temporarily
www.163.com header > Server: Cdn Cache Server V2.0
www.163.com header > Date: Wed, 31 Aug 2016 17:10:39 GMT
www.163.com header > Content-Length: 0
www.163.com header > Location: http://www.163.com/special/0077jt/error_isp.html
www.163.com header > Connection: close
www.sohu.com header > HTTP/1.1 200 OK
www.sohu.com header > Content-Type: text/html
www.sohu.com header > Content-Length: 91791
www.sohu.com header > Connection: close
www.sohu.com header > Date: Wed, 31 Aug 2016 17:10:37 GMT
www.sohu.com header > Server: SWS
www.sohu.com header > Vary: Accept-Encoding
www.sohu.com header > Cache-Control: no-transform, max-age=120
www.sohu.com header > Expires: Wed, 31 Aug 2016 17:12:37 GMT
www.sohu.com header > Last-Modified: Wed, 31 Aug 2016 16:51:30 GMT
www.sohu.com header > Content-Encoding: gzip
www.sohu.com header > X-RS: 10511343.19686393.11189627
www.sohu.com header > FSS-Cache: HIT from 10255086.18512632.11592044
www.sohu.com header > FSS-Proxy: Powered by 3308164.4618894.4645016
www.sina.com.cn header > HTTP/1.1 200 OK
www.sina.com.cn header > Server: nginx
www.sina.com.cn header > Date: Wed, 31 Aug 2016 17:10:29 GMT
www.sina.com.cn header > Content-Type: text/html
www.sina.com.cn header > Last-Modified: Wed, 31 Aug 2016 17:09:51 GMT
www.sina.com.cn header > Vary: Accept-Encoding
www.sina.com.cn header > Expires: Wed, 31 Aug 2016 17:11:29 GMT
www.sina.com.cn header > Cache-Control: max-age=60
www.sina.com.cn header > X-Powered-By: shci_v1.03
www.sina.com.cn header > Age: 10
www.sina.com.cn header > Content-Length: 590251
www.sina.com.cn header > X-Cache: HIT from ctc.gz.1cf2.38.spool.sina.com.cn
www.sina.com.cn header > Connection: close
'''











