#!/usr/bin/env python
# -*- coding: utf-8 -*-

import js2py


# Js2Py
# https://pypi.org/project/Js2Py/0.23/
# https://github.com/PiotrDabkowski/Js2Py
# pip install js2py


# js2py 执行单个语句
a = js2py.eval_js('var a = "hello Js2Py"; a')
print(a)

# js2py 执行函数
add = js2py.eval_js('function add(a, b){return a + b;}')
print(add(1, 2))

jsLen = js2py.eval_js("function(str){return str.length;}")
print('length = ', jsLen('js length'))

js = js2py.EvalJs({})
js.execute("""
var sum = 0;
for(var i = 0; i < 10; i++){
    sum += i;
}
console.log("i = " + i);
""")
