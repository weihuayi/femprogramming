# MUMPS

最近在算一个三维线弹性问题， 自由度规模有 50 多万， 结果发现没有什么好用的解法器。 Matlab 的直接解法器根本算不出结果。 用了几个代数多重网格解法器， 发现都不怎么稳健， 要么收敛速度慢，要么算的快但结果对不上。 理论总是很美好， 但遇到实际问题还是需要一翻尝试和探索。

最终还是找到 [MUMPS（MUltifrontal Massively Parallel sparse direct Solver）](http://mumps.enseeiht.fr/) 是一款高效的并行稀疏矩阵直接解法器， 用的算法是[多波前方法](https://en.wikipedia.org/wiki/Frontal_solver)。 当然， 它还是一款由欧洲科学计算研究中心（CERFACS）、 法国图卢兹计算机研究所（IRIT-ENSEEIHT) 和法国国立计算机及自动化研究院(INRIA)联合支持的自由软件， 它的软件许可协议为 [CeCILL-C](https://en.wikipedia.org/wiki/CeCILL)， 该协议是和 GPL 协议兼容。

测试了一下， 50 多万的自由度， 用 4 个线程， 40 秒左右就可以解出结果。 如果手头没有现成的快速解法器， 可以考虑用下这个解法器。


## Ubuntu 下的安装

Ubuntu 下, 用如下两条命令即可安装好 mumps：

```
$ sudo apt install libmumps-dev # 安装 mumps 的库文件和头文件
$ sudo -H pip3 install PyMUMPS # 安装 mumps 的 Python 3 接口
```

调用也很简单

```
from mumps import spsolve # 导入求解接口
#....... 生成你的矩阵和右端
x = spsolve(A, b) # 求解
```

在后续的文章中， 我会找机会介绍一些更复杂的安装与使用方式， 如：
* 并行版本的编译与安装
* Matlab 接口的安装

## 
