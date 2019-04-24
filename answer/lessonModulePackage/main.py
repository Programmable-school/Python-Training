"""
課題 モジュール分割_パッケージ分割
"""
import hello_world as hw
import util.calc as util

hw.show_hello_world()

x = 10
y = 3
print("%d + %d = %d" % (x, y, util.add(x, y)))
print("%d - %d = %d" % (x, y, util.sub(x, y)))
print("%d * %d = %d" % (x, y, util.multi(x, y)))
print("%d / %d = %f" % (x, y, util.div(x, y)))
