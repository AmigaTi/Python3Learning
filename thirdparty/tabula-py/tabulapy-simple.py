#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
import unittest
import tabula
import pandas as pd


# Example
# https://github.com/chezou/tabula-py
# https://github.com/tabulapdf/tabula-java
'''
import tabula

# Read pdf into DataFrame
df = tabula.read_pdf("test.pdf", options)

# Read remote pdf into DataFrame
df2 = tabula.read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")

# convert PDF into CSV
tabula.convert_into("test.pdf", "output.csv", output_format="csv")

# convert all PDFs in a directory
tabula.convert_into_by_batch("input_directory", output_format='csv')
'''

# Options
'''
pages (str, int, list of int, optional)
    An optional values specifying pages to extract from. It allows str, int, list of int.
    Example: 1, '1-2,3', 'all' or [1,2]. Default is 1
guess (bool, optional):
    Guess the portion of the page to analyze per page. Default True
area (list of float, optional):
    Portion of the page to analyze(top,left,bottom,right).
    Example: [269.875, 12.75, 790.5, 561]. Default is entire page
lattice (bool, optional):
    [spreadsheet option is deprecated] Force PDF to be extracted using lattice-mode extraction (if there are ruling lines separating each cell, as in a PDF of an Excel spreadsheet).
stream (bool, optional):
    [nospreadsheet option is deprecated] Force PDF to be extracted using stream-mode extraction (if there are no ruling lines separating each cell, as in a PDF of an Excel spreadsheet)
password (bool, optional):
    Password to decrypt document. Default is empty
silent (bool, optional):
    Suppress all stderr output.
columns (list, optional):
    X coordinates of column boundaries.
    Example: [10.1, 20.2, 30.3]
output_format (str, optional):
    Format for output file or extracted object.
    For read_pdf(): json, dataframe
    For convert_into(): csv, tsv, json
output_path (str, optional):
    Output file path. File format of it is depends on format.
    Same as --outfile option of tabula-java.
java_options (list, optional):
    Set java options like -Xmx256m.
pandas_options (dict, optional):
    Set pandas options like {'header': None}.
multiple_tables (bool, optional):
    (Experimental) Extract multiple tables.
    This option uses JSON as an intermediate format, so if tabula-java output format will change, this option doesn't work.
'''


class TestReadPdfTable(unittest.TestCase):
    def test_convert_into_json(self):
        pdf_path = 'res/data.pdf'
        json_path = 'res/data_1.json'
        tabula.convert_into(pdf_path, json_path, output_format='json')
        self.assertTrue(os.path.exists(json_path))

    def test_convert_into_csv(self):
        pdf_path = 'res/data.pdf'
        csv_path = 'res/data_1.csv'
        tabula.convert_into(pdf_path, csv_path, output_format='csv')
        self.assertTrue(os.path.exists(csv_path))

    def test_convert_into_csv_with_option(self):
        pdf_path = 'res/data.pdf'
        csv_path2 = 'res/data_2.csv'
        csv_path3 = 'res/data_2-3.csv'
        tabula.convert_into(pdf_path, csv_path2, pages='2', guess=False)
        self.assertTrue(os.path.exists(csv_path2))
        tabula.convert_into(pdf_path, csv_path3, pages='2,3', guess=False, stream=True)   # guess=True by default
        self.assertTrue(os.path.exists(csv_path3))

    def test_read_pdf(self):
        pdf_path = 'res/data.pdf'
        expected_csv = 'res/data_1.csv'
        df = tabula.read_pdf(pdf_path)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertTrue(df.equals(pd.read_csv(expected_csv)))

    def test_read_pdf_into_json(self):
        pdf_path = 'res/data.pdf'
        expected_json = 'res/data_1.json'
        json_data = tabula.read_pdf(pdf_path, output_format='json')
        self.assertTrue(isinstance(json_data, list))
        with open(expected_json) as json_file:
            data = json.load(json_file)
            self.assertEqual(json_data, data)

    def test_read_pdf_with_option(self):
        pdf_path = 'res/data.pdf'
        expected_csv1 = 'res/data_1.csv'
        expected_csv2 = 'res/data_2-3.csv'
        self.assertTrue(tabula.read_pdf(pdf_path, pages=1).equals(pd.read_csv(expected_csv1)))
        # issues: pages配置成'2-3'还是读取第一页数据
        # "",Sepal.Length,Sepal.Width,Petal.Length,Petal.Width,Species
        # pandas.errors.ParserError: Error tokenizing data. C error: Expected 5 fields in line 8, saw 6
        # solution: 配置guess=False即可
        # 但是提取的数据貌似有点问题：两个列被合并在一起了
        # 145 6.7,3.3,5.7,2.5,virginica
        # 解决方法：对生成的csv文件进行预处理，去掉有问题的行等等
        data = tabula.read_pdf(pdf_path, pages='2,3', guess=False, stream=True)
        print(data)
        self.assertTrue(data.equals(pd.read_csv(expected_csv2)))


if __name__ == '__main__':
    unittest.main()
