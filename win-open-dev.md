# Windows 下开源开发环境的搭建

因工作需要在 Windows 下测试开发的程序， 所以研究了一下如何在 Windows 下搭建基于 gcc 的开源开发环境。

我们这里使用 MSYS2， 是 Windows 下的一款软件构建和发布平台， 网址为 https://www.msys2.org。 它提供了和 Linux 系统几乎一样开发接口和环境， 而且它自带了一个软件包的管理工具 `pacman`, 可以像 Ubutnu 中 `apt` 一样管理需要的开源软件包。

MSYS2 可以在其官网下载， 有 32 位和 64位版本的。 因为现在大部分机器和系统都是 64 位的， 所以下面只介绍 64 位版本安装情况。

首先下载 [msys2-x86_64-latest.exe](http://repo.msys2.org/distrib/msys2-x86_64-latest.exe) 运行安装， 默认安装在 `C:\msys64`。

在目录 `C:\msys64` 下， 点击运行 `msys2`, 启动 MSYS2 命令行， 多次输入下面命令把 MSYS2 更新到最新。 注意每次更新完， 可能需要关闭命令行， 再打开才能重新执行下面的命令。

```
$ pacman -Syuu
```

下面安装安装编译器和开发工具, 注意这里只安装 64 位的版本：

```
pacman -S --needed base-devel mingw-w64-x86_64-toolchain git mingw-w64-x86_64-cmake
```

安装完成后， `C:\msys64\` 目录下会出现 `mingw64` 的命令行程序， 点击打开， 就可以命令行中调用 `gcc`, `g++`等编译器和工具了。

MSYS2 有很多已经编译好的开源软件包， 可以通过 `pacman` 从网上的仓库中搜索、下载和安装。 比如要安装 `boost`

```
$ pacman -Ss boost # 搜索 boost
mingw32/mingw-w64-i686-boost 1.60.0-2
    Free peer-reviewed portable C++ source libraries (mingw-w64)
mingw64/mingw-w64-x86_64-boost 1.60.0-2
    Free peer-reviewed portable C++ source libraries (mingw-w64)
$ pacman -Sy mingw-w64-x86-64-boost # 安装 64位 boost
```

## Windows 下 Mumps 的安装

有了上面的环境， 下面将介绍如何利用 mingw64 来编译安装 Mumps。

首先， 安装依赖软件包 metis 和 openblas

```
$ pacman -Sy mingw-w64-x86-64-metis
$ pacman -Sy mingw-w64-x86_64-openblas
```

下面安装 MUMPS， 但它的安装包需要到官网（http://mumps.enseeiht.fr/）填个表， 开发人员会把包发到你的邮箱。

```
$ tar -xvf MUMPS_5.1.2.tar.gz
$ cd MUMPS_5.1.2/
$ cp Make.inc/Makefile.inc.generic.SEQ  ./Makefile.inc
```

下面要对 `Makefile.inc` 针对 Windows 系统做一些修改， 主要就是告诉 make， MUMPS 依赖包的头文件和库文件在 Windows 系统的什么地方， 具体内容如下：
```
# Makefile.inc
LPORDDIR = $(topdir)/PORD/lib/
IPORD    = -I$(topdir)/PORD/include/
LPORD    = -L$(LPORDDIR) -lpord
LMETISDIR = /C/msys64/mingw64/lib
IMETIS    = -I/C/msys64/mingw64/include
LMETIS    = -L$(LMETISDIR) -lmetis
ORDERINGSF  = -Dmetis -Dpord
ORDERINGSC  = $(ORDERINGSF)

PLAT    =
LIBEXT  = .a
OUTC    = -o
OUTF    = -o
RM      = /bin/rm -f
CC      = gcc
FC      = gfortran
FL      = gfortran
AR      = ar vr
RANLIB  = ranlib

INCSEQ  = -I$(topdir)/libseq
LIBSEQ  = $(LAPACK) -L$(topdir)/libseq -lmpiseq

LIBBLAS = -lopenblas
LIBOTHERS = -lpthread

CDEFS = -DAdd_
OPTF    = -O -fPIC
OPTC    = -O -fPIC
OPTL    = -O -fPIC

INCS = $(INCSEQ)
LIBS = $(LIBSEQ)
LIBSEQNEEDED = libseqneeded
```

另外， 在 `MUMPS_5.1.2/example` 下的 `Makefile` 中， 也要做些修改：
```
```

打开 `mingw64` 的命令行程序， 并进行 `MUMPS` 的代码目录

```
$ make
```

## Windows 下安装 Mumps Interface for Matlab

首先， 在 Matlab 命令行中设置环境变量，
```
>> setenv('MW_MINGW64_LOC','C:\msys64\mingw64')
```
或者直接在 Windows 系统中添加系统环境变量 `MW_MINGW64_LOC`, 其值设为 `C:\msys64\mingw64`， 如何添加系统环境变量请自行网络搜索网络。

在 Matlab 命令行中运行：
```
>> mex -setup
```
就可以让 Matlab 的 `mex` 命令识别到 `mingw64`， 然后就可以用 `mingw64` 提供的编译器来编译 mex 程序， 并被 Matlab 的程序调用。

但实际上要编译出在 Matlab 中可以直接调用的 `mex` 程序， 不用 `mex` 命令， 甚至不用打开 Matlab， 也是可以的做到的。 因为 `mex` 生成的可执行文件本质是上**动态联接库文件**， 而且 Matlab 为 Matlab 与 C\C++ 的混合编程提供了相应的函数库， 如：

* libmx.lib
* libmex.lib
* libmat.lib
* libeng.lib

直接把 `MUMPS_5.1.2/MATLAB/` 中 `Makefile` 文件直接替换为下面在内容
```
# MUMPS_5.1.2/MATLAB 下的 Makefile 文件
MATLABROOT  = /C/MATLAB/R2016b
MUMPSROOT   = /C/msys64/home/why/software/MUMPS_5.1.2
MINGWROOT   = /C/msys64/mingw64

MUMPSLIBS   = -L${MUMPSROOT}/lib -ldmumps -lmumps_common -lpord -L${MUMPSROOT}/libseq -lmpiseq
LIBS        = -L${MINGWROOT}/usr/lib -lmetis -lopenblas -lgfortran                                  # 注意  
MEXLIBS     = -L${MATLABROOT}/extern/lib/win64/microsoft -llibmex -llibeng -llibmat -llibmx -llibut # 这两行中引用软件包名字的区别
CC          = gcc
CCFLAGS     = -I${MATLABROOT}/extern/include -I${MUMPSROOT}/include -I${MUMPSROOT}/libseq

.PHONY: all

all: dmumpsmex.mexw64

dmumpsmex.mexw64: mumpsmex.c
	@${CC} ${CCFLAGS} -shared -fPIC -DMUMPS_ARITH=MUMPS_ARITH_d -O2 -o $@ $< ${MUMPSLIBS} ${LIBS} ${MEXLIBS}
	@strip $@

clean:
	@-rm -f *.o *.mexw64
```

**注意**， 上面 `MEXLIBS` 变量中索引 Matlab 的库文件时， 用的是 `-llibmex -llibeng -llibmat -llibmx -llibut`， 而 `MUMPSLIBS` 和 `LIBS` 变量中用的是 Linux 下常用的方式, 如 `-lmetis`， 没有 `lib` 字符串。 我猜 `mingw64`  用了两种完全方式来
