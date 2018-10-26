# Ubuntu 下的 MUMPS 安装过程

因为 Ubuntu 系统中自带的 MUMPS 版本比较旧， 所以想用比较新的版本， 就需要学会自己编译安装 MUMPS。 本文将介绍 Ubuntu 下的串行 MUMPS 及其依赖软件包的编译安装过程， 其它的 Linux 发行版本类似可以安装。

MUMPS 能调用 `metis` 和 `scotch` 来做稀疏矩阵元素的重新排序， 可以大大减少矩阵分解产生的非零元，从而节省矩阵分解需要的内存开销。 下面首先介绍 `metis` 的安装过程：

```
$ wget http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-5.1.0.tar.gz
$ tar -xvf metis-5.1.0.tar
$ cd metis-5.1.0/
```

如果需要 `metis` 支持 64 位的整型和浮点型， 可以把 `include/metis.h` 中的 

```
#define IDXTYPEWIDTH 32
#define REALTYPEWIDTH 32
```

修改为

```
#define IDXTYPEWIDTH 64 
#define REALTYPEWIDTH 64
```

然后编译安装：

```
$ make config prefix=/home/why/local/multicore # 替换为你的安装路径
$ make -j8 # 并行编译， 8 个核
$ make install
```

下面安装 scotch,

```
$ wget https://gforge.inria.fr/frs/download.php/file/37622/scotch_6.0.6.tar.gz
$ tar -xvf scotch_6.0.6.tar.gz
$ cd scotch_6.0.6/src
$ cp Make.inc/Makefile.inc.x86-64_pc_linux2 ./Makefile.inc
```

注意要修改 `Makefile.inc` 中的 `CFLAGS` 行， `=` 后面加 `-fPIC`。 然后编译安装

```
$ make -j8
$ make esmumps
$ make install prefix=/home/why/local/multicore
$ cp ../lib/libesmumps.a /home/why/local/multicore/lib/
$ cp ../include/esmumps.h /home/why/local/multicore/include/
```

下面安装 OpenBLAS, 它是一个优化的 BLAS 包， 支持多线程， 运行速度更快。目前大部分的个人电脑的 CPU 都是多核的， 所以为了充分利用多核资源， 获得更快的计算速度， 强烈建议安装

```
$ git clone https://github.com/xianyi/OpenBLAS.git
$ cd OpenBLAS/
$ make -j8 NO_SHARED=1
$ make PREFIX=/home/why/local/multicore NO_SHARED=1 install
```

下面安装 MUMPS， 但它的安装包需要到官网（http://mumps.enseeiht.fr/）填个表， 开发人员会把包发到你的邮箱。

```
$ tar -xvf MUMPS_5.1.2.tar.gz
$ cd MUMPS_5.1.2/
$ cp Make.inc/Makefile.inc.generic.SEQ  ./Makefile.inc
```

下面要对 `Makefile.inc` 做修改， 主要就是告诉 make， MUMPS 依赖的包的头文件和库文件在什么地方， 我这里修改的内容如下：


```
SCOTCHDIR  = ${HOME}/local/multicore
ISCOTCH    = -I$(SCOTCHDIR)/include

LSCOTCH    = -L$(SCOTCHDIR)/lib -lesmumps -lscotch -lscotcherr

LPORDDIR = $(topdir)/PORD/lib/
IPORD    = -I$(topdir)/PORD/include
LPORD    = -L$(LPORDDIR) -lpord

LMETISDIR = ${HOME}/local/multicore/lib
IMETIS   = -I${HOME}/local/multicore/include 

LMETIS    = -L$(LMETISDIR) -lmetis


ORDERINGSF  = -Dpord -Dscotch -Dmetis
ORDERINGSC  = $(ORDERINGSF)

LORDERINGS = $(LMETIS) $(LPORD) $(LSCOTCH)
IORDERINGSF = $(ISCOTCH)
IORDERINGSC = $(IMETIS) $(IPORD) $(ISCOTCH)


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

LIBBLAS = -L${HOME}/local/multicore/lib -lopenblas

LIBOTHERS = -lpthread

CDEFS = -DAdd_

OPTF    = -O -fPIC
OPTC    = -O -fPIC
OPTL    = -O -fPIC

INCS = $(INCSEQ)
LIBS = $(LIBSEQ)
LIBSEQNEEDED = libseqneeded
```

然后编译安装


```
$ make -j8
$ cp include/* /home/why/local/multicore/include/
$ cp lib/* /home/why/local/multicore/lib/
$ cp libseq/libmpiseq.a /home/why/local/multicore/lib/
$ cp libseq/*.h /home/why/local/multicore/include/
```

下面安装 MUMPS 的 Matlab 接口  

```
$ cd MATLAB/ # 在 MUMPS 的主目录下， 进入 MATLAB 文件夹。 
```

修改 `make.inc` 文件如下， 注意其中的目录要替换为你自己的目录哦。

```
MEX         = /opt/matlab/R2018a/bin/mex -g -largeArrayDims # 替换为你的 mex 位置

# Main MUMPS_DIR
MUMPS_DIR = ${HOME}/local/multicore

# Orderings (see main Makefile.inc file from MUMPS)
LSCOTCHDIR  = ${HOME}/local/multicore/lib
LSCOTCH    = -L$(LSCOTCHDIR)/lib -lesmumps -lscotch -lscotcherr
LMETISDIR = ${HOME}/local/multicore/lib
LMETIS     = -L$(LMETISDIR) -lmetis
LPORDDIR   = $(MUMPS_DIR)/PORD/lib
LPORD      = -L$(LPORDDIR) -lpord
LORDERINGS = $(LPORD) $(LMETIS) $(LSCOTCH)

LIBFORT = -lgfortran

LIBBLAS = -L${HOME}/local/multicore/lib -lopenblas

OPTC    = -DINTSIE64 -g 
```

然后编译

```
$ make 
$ ls *.mexa64
dmumpsmex.mexa64  zmumpsmex.mexa64 # 实数和复数版本的
```

在 `MATLAB` 目录下， 有一个 `simple_example.m` 文件， 打开 matlab, 运行就可以测试有没有问题了。 

如果以上编译过程有问题， 可以给我发邮件 weihuayi@xtu.edu.cn。













