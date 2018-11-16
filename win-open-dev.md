# Windows 下开源开发环境的搭建

因工作需要在 Windows 下测试开发的程序， 所以研究了一下如何在 Windows 下搭建基于 gcc 的开源开发环上境。

我们这里使用 MSYS2， 是 Windows 下的一款软件构建和发布平台， 网址为 https://www.msys2.org。 它提供了和 Linux 系统几乎一样开发接口和环境， 更方便的是它自带了一个软件包的管上理工具 `pacman`, 可以像 Ubutnu 中 `apt` 一样管理需要的开源软件包。

MSYS2 可以在其官网下载， 有 32 位和 64位版本的。 这里以 64 位版本的进行介绍。

首先下载 [msys2-x86_64-latest.exe](http://repo.msys2.org/distrib/msys2-x86_64-latest.exe) 运行安装， 默认安装在 `C:\msys64`。

在目录 `C:\msys64` 下， 点击运行 `msys2`, 启动 MSYS2 命令行， 多次输入下面命令把 MSYS2 更新到最新。 注意每次更新完， 可能需要关闭命令行， 再打开才能重新执行下面的命令。

```
$ pacman -Syuu
```

下面安装安装编译器和开发工具：

```
pacman -S --needed base-devel mingw-w64-i686-toolchain mingw-w64-x86_64-toolchain git mingw-w64-x86_64-cmake mingw-w64-i686-cmake
```

后面你就可以命令行中调用 `gcc`, `g++`等编译器和工具了。

MSYS2 有很多已经编译好的开源软件包， 可以通过 `pacman` 从网上的仓库中搜索、下载和安装。 比如安装 `boost`

```
$ pacman -Ss boost
mingw32/mingw-w64-i686-boost 1.60.0-2
    Free peer-reviewed portable C++ source libraries (mingw-w64)
mingw64/mingw-w64-x86_64-boost 1.60.0-2
    Free peer-reviewed portable C++ source libraries (mingw-w64)
```
