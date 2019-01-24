# Windows 系统下 FEALPy 的安装

首先下载安装 Visual Studio IDE， https://visualstudio.microsoft.com 。 在安装时
，只要选择安装 C++ 模块就可以了。这里主要是为了安装编译器，在安装一些 Python 软
件时用到。很多 Python 软件包核心代码是 C\C++ 写的，安装时需要首先编译出库文件才
能安装。


然后下载最新版的 Anaconda3， 下载地址为： https://repo.continuum.io/archive/Anaconda3-2018.12-Windows-x86_64.exe ， 
默认安装即可。关于 Anaconda3 的介绍，请见

* [Python 环境搭建](./install_python.md) 

因为在 Windows 系统下，  FEALPy 用到的 meshpy 和 pyamg 默认安装有问题，所以只能
采用手工方式安装。美国加州大学欧文分校生物医学工程系的 Christoph Gohlke 提供了
一个非官方的 Python 软件包下载服务， 网址为 https://www.lfd.uci.edu/~gohlke/pythonlibs/ 。
上面一般都有最新版本的软件包下载， meshpy 和 pyamg 的下载链接为： 

* https://www.lfd.uci.edu/~gohlke/pythonlibs/#meshpy
* https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyamg

这里需要下载最新的适合 Python 3.7 的版本。下载之后，在 Windows 桌面搜索框输入
`Anaconda Prompt`, 回车即可以打开一个命令行, 显示如下内容:

```
(base) C:\Users\username>
```

注意上面 `username` 实际上会显示为你自己的用户名。

比如下载的目录为: `D:\dowloads`, 依次输入以下命令, 并回车：

```
(base) C:\Users\username>D: 
(base) D:\>cd dowloads 
(base) D:\downloads> pip install MeshPy‑2018.2.1‑cp37‑cp37m‑win_amd64.whl # For 64 bit win system with python 3.7
(base) D:\downloads> pip install pyamg‑4.0.0‑cp37‑cp37m‑win_amd64.whl # For 64 bit win system with python 3.7
```

注意上面命令中的 `install` 后的文件名，都是适用于 64 位 Windows 系统，对应的 Python 版本是 3.7。
。

最后在 FEALPy 的 `https://github.com/weihuayi/fealpy`  主页上， 点击 `clone or
download` 按钮， 在弹出的小页面中点击 `Download Zip` 直接下载得到压缩文件
`fealpy-master.zip`, 然后解压。 比如解压到目录 `D:\fealpy-master` 下面， 则在命
令行中首先切换到该目录下，然后安装 fealpy

```
(base) D:\downloads> cd ../fealpy-master
(base) D:\fealpy-master> pip install -e ./ 
```

如果没有报什么错误，就说明安装成功了。下面就可以进行测试了， 比如可以进入
`example` 目录，运行命令 `python PoissonFEMRate.py 2 1 3 4` 进行测试， 这里的 `2
1 3 4` 分别代表 2 维问题， 用 1 次元求解， 初始网格首先加密 3 次， 再迭代加密网
格 4 次并求解。 具体测试结果如下


```
(base) D:\fealpy-master> cd example 
(base) D:\fealpy-master\example>python PoissonFEMRate.py 2 1 3 4
Can not import spsolve from mumps!Using spsolve in scipy!
Can not import spsolve from mumps!Using spsolve in scipy!
Construct linear system time: 0.01743110000000314
Solve time: 0.006151400000000251
Construct linear system time: 0.006938899999997972
Solve time: 0.0007587999999998374
Construct linear system time: 0.042748799999998255
Solve time: 0.004435099999998471
Construct linear system time: 0.08573089999999794
Solve time: 0.02161789999999897
\begin{table}[!htdp]
\begin{tabular}[c]{|c|c|c|c|c|}\\\hline
Dof &   81 &  289 & 1089 & 4225
$|| u - u_h||_0$ & 1.9408e-02 & 4.9543e-03 & 1.2452e-03 & 3.1173e-04
Order & -- & 1.97 & 1.99 & 2.
$||\nabla u - \nabla u_h||_0$ & 4.3180e-01 & 2.1754e-01 & 1.0898e-01 & 5.4514e-02
Order & -- & 0.99 & 1.   & 1.
\end{tabular}
\end{table}
```

注意，上面的测试中，报出信息 `Can not import spsolve from mumps!Using spsolve in
scipy!`， 是因为上面的安装默认没有安装并行直接解法器 pymumps （它是 mpi 版本的， 目前
fealpy 还不能充分发挥它的潜力）, 程序就转为调用 scipy 中的的解法器。`scipy` 中的解法器
求解 100 万规模左右的问题还可以，但更大的时间上就有点受不了啦。这里也没有默
认用 `pyamg`, 因为高次元还是解不了， 不过线性元还是比较高效的。

总的来说， fealpy 的解法器还有待加强。我计划自己开发一个 mumps 多线程版本的
python 接口，以便能充分利用我的 48 核工作站。当然也非常欢迎你去尝试把 pymumps 在
Windows下的安装搞定， 如果搞定请把安装笔记发给我。




