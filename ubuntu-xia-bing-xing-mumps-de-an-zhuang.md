# Ubuntu 下的 MUMPS 安装过程

因为 Ubuntu 系统中自带的 MUMPS 的版本比较旧， 所以想用比较新的版本， 就需要学会自己编译安装 MUMPS。 本文将介绍 Ubuntu 下的串行 MUMPS 及其依赖软件包的编译安装过程， 其它的 Linux 发行版本类似可以安装。
 
* metis
* scotch
* openblas

目前大部分的个人电脑的 CPU 都是多核的， 为了充分利用多核资源， 获得更快的计算速度，



https://mailman-mail5.webfaction.com/pipermail/kwant-discuss/2016-October/000976.html
### metis

把 `metis.h` 中的

```
#define IDXTYPEWIDTH 32 
#define REALTYPEWIDTH 32
```

修改为 

```
#define IDXTYPEWIDTH 32 // 32 位整型已经够用了 
#define REALTYPEWIDTH 64
```

```
$ make config prefix=/home/why/local/multicore
$ make -j8
$ make install
```

### scotch

```
cd scotch_6.0.4/src/
cp Make.inc/Makefile.inc.x86-64_pc_linux2 ./Makefile.inc
``
在 `CFLAGS =` 后面加 ` -fPIC `

```
$ make -j8
$ make esmumps
$ make install prefix=/home/why/local/multicore
$ cp ../lib/libesmumps.a /home/why/local/multicore/lib/
$ cp ../include/esmumps.h /home/why/local/multicore/include/
```


### OpenBLAS

```
$ make -j8 NO_SHARED=1
$ make PREFIX=/home/why/local/multicore NO_SHARED=1 install
```

### MUMPS

```
$ cp Make.inc/Makefile.inc.generic.SEQ  ./Makefile.inc
```

```
cp include/* /home/why/local/multicore/include/
cp lib/* /home/why/local/multicore/lib/
cp libseq/libmpiseq.a /home/why/local/multicore/lib/
cp libseq/*.h /home/why/local/multicore/include/
```

如果基于 OpenBLAS 来编译串行版本的 MUMPS， 是不需要打开 openmp 选项的。 如果打开，求解的时间反而增加了。 

### MUMPS 的 Matlab 接口


### MUMPS 的 Python 接口













