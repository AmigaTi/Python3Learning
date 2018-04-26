#!/usr/bin/python
# -*- coding: utf-8 -*-

from prettytable import PrettyTable


def make_table(header, align_map=None, rows=None):
    """ Wrapper for pretty table """
    table = PrettyTable()
    table.horizontal_char = table.vertical_char = table.junction_char = ' '
    try:
        table.field_names = header
    except Exception as err:
        print(header)
        raise err
    if align_map:
        for field, align in zip(header, align_map):
            table.align[field] = align
    if rows:
        for row in rows:
            if len(row) < len(table.field_names):
                continue
            try:
                table.add_row(row)
            except Exception as err:
                print('fields:', table.field_names)
                print('row:', row)
                print('rows:', rows)
                raise err
    return table
