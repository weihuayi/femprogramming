# Python 容器: list
---

前一篇介绍了 Python 中的变量和基本数据类型:

* 整型
* 浮点型
* 字符串型

但这并不能很好满足实际编程应用的需要, 我们还需要复杂一点的数据结构, 如容器(container), 就是用来**存放**其它对象的一种数据结构, 一般称它里面放的对象为**元素**. Python 中有如下内置的容器:

* **list**: 列表, 是一个有序, 可修改, 可**用整数索引**的容器, 允许包含重复的元素.
* **tuple**: 元组, 是一个有序, 不可修改, 可**用整数索引**的容器, 允许包含重复的元素.
* **set**: 集合, 是一个无序, **不能**索引的容器, 没有重复的元素.
* **dict**: 字典, 是一个无序, 可修改, 且可以**索引**的容器, 注意它的索引值不限整数

这次仅介绍 `list`. 首先, 介绍列表的**创建**. Python 是用 `[]` 语法来创建列表的, 如:
``` 
empty = [] #创建一个空列表
pets = ['dog', 'cat', 'fish'] #创建一个长度为 3 的列表
mixed_list = [3, 'flower', [2, 3, 4]] # 创建一个长度为 3 的列表, 注意最后一个元素是一个列表
```
注意一个列表中的元素可以是不同类型的对象, 甚至是另外一个列表对象.

下面介绍列表元素的**索引**, 最基本的用法是索引某个元素, 基本语法: 
```
list_val[i] # 获取第 i 个元素, i 可以是负整数值, 表示索引倒数第 i 个元素
```
如
```
number = [1, 3, 4, 5, 0]
number[0] # 取出第 0 个元素, 其值为 1 
```

另外一种索引用法, 是获取一个列表的**子列表**, 叫做**切片(slice)**索引, 语法如下:
```
list_val[start:stop:step]
```
其中 `start` 表示切片的索引起始位置, 如果是 0, 就可以省略; `stop` 是表示切片的索引结束位置, 如果是一直结尾, 也可以省略不写; `step` 表示切片的步长, 如果是 1, 也可以省略; 而且它们都可以是负值, 表示**倒着数**,

注意在 Python 中整数索引是从 0 开始计数的, 索引放在方括号 `[]` 中, 而 Matlab 的索引是从 1 开始的, 且索引值放在圆括号 `()` 中.  

```
number[1:3] # 取出第 1 个到第 3 个元素之前的元素, 不包括第 3 个元素
number[1:-1] # 取出第 1 个元素到倒数第 1 个之前的元素, 不包括倒数第 1 个元素
number[0::2] # 从第 0 个元素开始到最后一个元素, 每隔 2 个元素取一个
number[-1::-1] # 从倒数第 1 个元素一直取到第 0 个元素, 相当于把列表反过来
```

下面给出一些常用的其它操作:

```
len(number) # 返回列表的长度
number.append(10) #  在列表末尾加上一个元素 10
number.insert(2, 11) # 在第 2 个位置之前插入整数 11, 之后 11 就变成了第 2 个数
number + [7, 8, 9] # 把两个列表拼成一个列表
```

## 总结

这里最关键的是灵活理解和运用**切片**索引, 因为后面我们用 Numpy 中多维数组编程时, 会大量用到**切片**操作, 这是向量化编程的一项基本功.

