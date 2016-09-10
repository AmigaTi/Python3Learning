#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.etree.ElementTree import ElementTree, Element


# 在实际应用中，需要对xml配置文件进行实时修改：
# 1.增加、删除 某些节点
# 2.增加，删除，修改某个节点下的某些属性
# 3.增加，删除，修改某些节点的文本


def read_xml(in_path):
    etree = ElementTree()
    etree.parse(in_path)
    return etree


def write_xml(etree, out_path):
    etree.write(out_path, encoding='utf-8', xml_declaration=True)


def is_match(node, attribs):
    for key in attribs:
        if node.get(key) != attribs.get(key):
            return False
    return True


def find_nodes(etree, path):
    return etree.findall(path)


def get_nodes_by_attribs(node_list, attribs):
    results = []
    for node in node_list:
        if is_match(node, attribs):
            results.append(node)
    return results


def change_nodes_attribs(node_list, attribs, is_delete=False):
    for node in node_list:
        for key in attribs:
            if is_delete:
                if key in node.attrib:
                    del node.attrib[key]
            else:
                node.set(key, attribs.get(key))


def change_nodes_text(node_list, text, is_append=False, is_delete=False):
    for node in node_list:
        if is_append:
            node.text += text
        elif is_delete:
            node.text = ''
        else:
            node.text = text


def create_node(tag, attribs, text):
    element = Element(tag, attribs)
    element.text = text
    return element


def add_child_node(node_list, element):
    for node in node_list:
        node.append(element)


def del_node_by_tag_attribs(node_list, tag, attribs):
    for parent_node in node_list:
        children = parent_node.getchildren()
        for child in children:
            if child.tag == tag and is_match(child, attribs):
                parent_node.remove(child)


if __name__ == '__main__':
    # 1. 读取xml文件
    tree = read_xml('./xmlfile/conf_raw.xml')

    # 2. 修改属性
    # 2.1 找到父节点
    nodes = find_nodes(tree, 'processors/processor')
    # 2.2 通过属性定位子节点
    result_nodes = get_nodes_by_attribs(nodes, {'name': 'BProcessor'})
    # 2.3 修改节点属性
    change_nodes_attribs(result_nodes, {'age': '1'})
    # 2.4 删除节点属性
    change_nodes_attribs(result_nodes, {'value': ''}, is_delete=True)

    # 3. 修改节点
    # 3.1 新建节点
    child_node = create_node('person', {'age': '15', 'money': '5000'}, 'created node')
    # 3.2 插入到父节点下
    add_child_node(result_nodes, child_node)

    # 4. 删除节点
    # 4.1 定位父节点
    del_parent_nodes = find_nodes(tree, 'processors/services/service')
    # 4.2 定位子节点并删除
    del_node_by_tag_attribs(del_parent_nodes, 'chain', {'sequency': 'chain1'})

    # 5. 修改节点文本
    # 5.1 定位节点
    text_nodes = get_nodes_by_attribs(find_nodes(tree, 'processors/services/service/chain'), {'sequency': 'chain3'})
    change_nodes_text(text_nodes, 'new text')

    # 6. 保存至文件
    write_xml(tree, './xmlfile/conf_out.xml')



