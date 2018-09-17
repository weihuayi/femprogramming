# Hypre 安装笔记

求解线性代数系统 $Ax =b$ 是科学计算中很重要的组成部分。 对于困难一点的问题， 可能大部分时间都花在线性代数系统求解上面了。 以前都是算一些很简单的小问题， 没什么太多体会。 最近算三维高次元和线弹性问题， 才知道经典的代数多重网格方法求解这些问题根本不管用， 但手头熟悉的 Matlab 和 Python 软件包基本都是经典的方法， 根本满足不了实际的需要。 本来想自己重新学习实现， 但苦于能力和精力有限， 最后只能求助于更加专业强大的软件包， 比如 Hypre。 这里记录下自己学习使用的过程， 分享给你， 希望对你有点用处。 

## Hypre 简介

[Hypre](https://computation.llnl.gov/projects/hypre-scalable-linear-solvers-multigrid-methods/software) 为美国劳伦斯利佛摩国家实验室（英语：Lawrence Livermore National Laboratory，缩写： LLNL）开发的并行稀疏代数系统解法器， 主要特色是并行多重网格， 实现语言为 C 语言， 并行用 MPI 实现。 另外， 它也是跨平台的， 在主流系统下都可以安装。

Hypre 遵循的开源协议为 [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)， 该协议比原来的 [GPL](https://en.wikipedia.org/wiki/GNU_General_Public_License) 协议要宽松。 如果以库的形式调用 Hypre， 你的程序也可以是不开源的。 

## 在 Windows 下安装 Hypre

在 Linux 下安装 Hypre 很容易， 下面主要介绍在 Widnows 如何安装 Hypre

* 下载安装 [MicroSoft .Net Framework 4.7](https://www.microsoft.com/zh-CN/download/details.aspx?id=55170)
* 下载安装 [Visual Studio IDE Community 2017](https://visualstudio.microsoft.com/zh-hans/) 
* 安装 [mpi](https://www.microsoft.com/en-us/download/details.aspx?id=56727)




