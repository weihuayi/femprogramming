# MUMPS

最近在算一个三维线弹性问题， 自由度规模有 50 多万， 结果发现没有什么好用的解法器。 Matlab 的直接解法器根本算不出结果。 用了几个代数多重网格解法器， 发现都不怎么稳健， 要么收敛速度慢，要么算的快但结果对不上。 理论总是很美好， 但遇到实际问题还是需要一翻尝试和探索。 

最终还是找到 [MUMPS（MUltifrontal Massively Parallel sparse direct Solver）](http://mumps.enseeiht.fr/) 是一款高效的并行稀疏矩阵直接解法器， 用的算法是[多波前方法](https://en.wikipedia.org/wiki/Frontal_solver)。 当然， 它还是一款自由软件, 从 1999 年开始获得 CERFACS、 IRIT-ENSEEIHT 和 INRIA

测试了一下， 50 多万的自由度， 用 4 个线程， 40 秒左右就可以解出结果。 如果手头没有现成的快速解法器， 可以考虑用下这个解法器。 


```
$ sudo apt install libmumps-dev
$ sudo -H pip3 install PyMUMPS
```


