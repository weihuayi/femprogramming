# Python 容器： tuple

元组（tuple）容器是 Python 中另一个常用的数据结构， 在使用 Numpy 的过程中你会经常用到它。 它有以下两个特点

* 有序
* 不可修改

## 基本语法

Python 中用 `()` 来创建元组， 如：
```python
thistuble = (`cat`, `dog`, 1)
print(thistuble)
```
注意元组中的元素可以是任何 Python 对象， 包括元组本身。 

创建只含一个元素的元组语法如下:
```python
one_tuble = ('cat',)
print(one_tuple)
```
**注意**其中的 **`,`** 不能省略。 

创建一个空元组的语法如下：
```python
empty_tuple = tuple()
print(empty_tuple)
```

也可以从列表创建元组:
```python
test_tuple = tuple([2, 3, 4])
print(test_tuple)
```

访问元组第 i 个元素的语法为：
```python
thistuple[i] # i 可以是负值， 表示倒数第 |i| 个元素
```
另外， 可以用**切片**语法得到元组的一个**子元组**：
```python
thistuple[start:stop:step]
```
**注意**， 无论切片中包含多少个元素， 返回的都是**元组**对象， 如：
```python
thistuple[:0] # 返回一个空元组 ()
thistuple[:1] # 返回只包含一个元素的元组, 包含元素为 thistuple 的第 0 个元素
```
**注意**， 对**列表**的切片操作， 也是得到列表的一个**子列表**。 

虽然元组不能修改， 即你不能修改某个元素的值或者插入一个新的元素， 但与**列表**一样， 你可以把两个元组用 `+` 拼接起来：
```python
tuple_0 = (1, 2)
tuple_1 = (3, 4)
print(tuple_0 + tuple_1) # 返回 (1, 2, 3, 4)
```

最后， 获得元组长度的语法为
```python
len(thistuple)
```

## 总结

元组在 Python 函数的定义中经常用到， 主要是用于多个参数的输入和返回; 在 Numpy 中 ， 多维数组的形状 `shape` 就是一个元组。 上面强调**注意**的地方， 是我自己在编程过程中经常会出错的地方，你也要多加**注意**哦。