# FEALPy: Finite Element Analysis Library in Python

我在学习陈龙老师 IFEM 软件包基础上， 开发了一个 Python 有限元软件包
FEALPy。 FEALPy 借助 Python 中的多维数组模块 Numpy， 完全继承了 IFEM 面向数组的编程模式， 
也可以用简短的代码写出比较高效的数值计算程序。 与 IFEM 不同的是， FEALPy
采用了面向对象的编程模式来组织程序，与面向过程的编程模式相比，大大提高了程序的重用性和可扩展性。

FEALPy 开源托管在 Github 上，主页为： github.com/weihuayi/fealpy, 欢迎大家试用。目前 FEALPy 核心
框架已经搭建完成， 实现了

* 丰富的网格数据结构类型, 包括二维三维的常见网格类型。
* 简单区域上的网格生成。
* 任意维的高次拉格朗日有限元空间。
* 高次曲面有限元空间。
* 多边形上的高次虚单元空间。
* 自适应算法,包括三角形网格的二分法, 四叉树和八叉树。


今天，我将介绍如何在 Ubuntu 下安装 FEALPy， 后续的文章中我也会介绍在 Windows 和
Mac 系统下的安装配置。 

你可以到 FEALPy 的主页上， 点击 `clone or download` 按钮， 在弹出的小页面中点击
`Download Zip` 直接下载得到压缩文件 `fealpy-master.zip`, 然后

```
$ unzip fealpy-master.zip # 解压得到 fealpy-master 文件夹
$ cd fealpy-master/
```

或者在 Ubuntu 命令行终端中直接用 git 克隆一份：

```
$ git clone https://github.com/weihuayi/fealpy.git
$ cd fealpy/
```


```
sudo apt install python3 python3-pip ipython3 
```

```
git clone 
