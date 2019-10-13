#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
调用sys.exit()使Python解释其退出。exit()的任何整型参数作为退出状态会返回给调用者，该值默认为0
"""

def foo():
    return True

def bar():
    "bar() does not do much"
    return True

foo.__doc__ = "foo() does not do much"
foo.tester = """
if foo():
    print("PASSED")
else:
    print("FAILED")
"""

if __name__ == "__main__":

    print(dir())
    for eachAttr in dir():
        obj = eval(eachAttr)
        print("obj is ", obj)
        if isinstance(obj, type(foo)):
            if hasattr(obj, "__doc__"):
                print("\nFunction '%s' has a doc string:\n\t%s" % (eachAttr,
                    obj.__doc__))
            if hasattr(obj, "tester"):
                print("Function '%s' has a tester... executing" % eachAttr)
                exec(obj.tester)
            else:
                print("Function '%s' has no tester...skipping" % eachAttr)
        else:
            print('"%s" is not a function' % eachAttr)
