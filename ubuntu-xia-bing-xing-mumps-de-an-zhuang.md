# MUMPS

因为 Ubuntu 系统中自带的 MUMPS 的版本比较旧， 所以想用比较新的版本， 就需要学会自己编译安装 MUMPS。 本文将介绍 Ubuntu 下的 MUMPS 及其依赖软件包的安装过程编译安装过程， 其它的 Linux 发行版本类似可以安装。 

## 多核版本的安装过程 
https://mailman-mail5.webfaction.com/pipermail/kwant-discuss/2016-October/000976.html
### scotch
```
cd scotch_6.0.4/src/
cp Make.inc/Makefile.inc.x86-64_pc_linux2 Makefile.inc
``
Add "-fPIC” to the line that starts with "CFLAGS"

```
$ make -j8
$ make esmumps
$ make install prefix=/home/why/local/multicore
$ cp ../lib/libesmumps.a /home/why/local/multicore/lib/
$ cp ../include/esmumps.h /home/why/local/multicore/include/
```

### 

## 安装依赖软件包 

### mpich 

```
$ ./configure --prefix=/home/why/local # 指定安装目录
$ make -j8 # 并行编译， 这里用了 8 个线程
$ make install # 安装到 /home/why/local  下面
```

### metis 

```
```
1. metis
1. parmetis
1. 










