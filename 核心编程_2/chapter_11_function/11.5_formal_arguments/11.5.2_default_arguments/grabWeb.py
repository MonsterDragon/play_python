#! /usr/bin/env python3
# -*- coding=UTF-8 -*-

import urllib.request
import sys

def catch(url="http://www.baidu.com"):
    """爬取网页"""
    try:
        response = urllib.request.urlopen(url)
    except Exception as e:
        print("Error:{}".format(e))
    html = response.read()
    html_str = bytes.decode(html, 'utf-8')
    html_list = html_str.split("\n")
    print("html_list:{}".format(html_list))
    return html_list

def firstNotBlank(lines):
    """返回首个不为空的字符串"""
    for startLine in lines:
        if not startLine.strip():
            continue # 终止当前循环，并忽略剩余的语句
    else:
        return startLine

def endNotBlank(lines):
    """返回首个末尾不为空的字符串"""
    lines.reverse()
    endLine = firstNotBlank(lines)
    return endLine

def main():
    """模块入口函数"""
    url = input("Enter the url: ").strip()
    if url:
        html_file = catch(url)
    else:
        html_file = catch()
    first_line = firstNotBlank(html_file)
    end_line = endNotBlank(html_file)
    print("first_line:{}\nend_line:{}".format(first_line, end_line))

if __name__ == "__main__":
    main()
