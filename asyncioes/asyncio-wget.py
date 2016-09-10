#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio


# asyncio提供了完善的异步IO支持；
# 异步操作需要在coroutine中通过yield from完成；
# 多个coroutine可以封装成一组Task然后并发执行。

# 用asyncio的异步网络连接来获取sina、sohu和163的网站首页

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()       # similar to flush
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()                 # 获取EventLoop
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))    # 3个连接由一个线程通过coroutine并发完成
loop.close()                                    # 关闭EventLoop


''''
wget www.163.com...
wget www.sohu.com...
wget www.sina.com.cn...
www.sina.com.cn header > HTTP/1.1 200 OK
www.sina.com.cn header > Server: nginx
www.sina.com.cn header > Date: Wed, 31 Aug 2016 16:48:39 GMT
www.sina.com.cn header > Content-Type: text/html
www.sina.com.cn header > Last-Modified: Wed, 31 Aug 2016 16:48:22 GMT
www.sina.com.cn header > Vary: Accept-Encoding
www.sina.com.cn header > Expires: Wed, 31 Aug 2016 16:49:39 GMT
www.sina.com.cn header > Cache-Control: max-age=60
www.sina.com.cn header > X-Powered-By: shci_v1.03
www.sina.com.cn header > Age: 22
www.sina.com.cn header > Content-Length: 590265
www.sina.com.cn header > X-Cache: HIT from ctc.gz.1cf2.38.spool.sina.com.cn
www.sina.com.cn header > Connection: close
www.163.com header > HTTP/1.0 302 Moved Temporarily
www.163.com header > Server: Cdn Cache Server V2.0
www.163.com header > Date: Wed, 31 Aug 2016 16:49:59 GMT
www.163.com header > Content-Length: 0
www.163.com header > Location: http://www.163.com/special/0077jt/error_isp.html
www.163.com header > Connection: close
www.sohu.com header > HTTP/1.1 200 OK
www.sohu.com header > Content-Type: text/html
www.sohu.com header > Content-Length: 91778
www.sohu.com header > Connection: close
www.sohu.com header > Date: Wed, 31 Aug 2016 16:46:41 GMT
www.sohu.com header > Server: SWS
www.sohu.com header > Vary: Accept-Encoding
www.sohu.com header > Cache-Control: no-transform, max-age=120
www.sohu.com header > Expires: Wed, 31 Aug 2016 16:48:41 GMT
www.sohu.com header > Last-Modified: Wed, 31 Aug 2016 16:37:24 GMT
www.sohu.com header > Content-Encoding: gzip
www.sohu.com header > X-RS: 11172604.20347654.12509576
www.sohu.com header > FSS-Cache: HIT from 9337568.16677610.10674512
www.sohu.com header > FSS-Proxy: Powered by 3439238.4881040.4776092
'''











