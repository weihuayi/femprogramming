





For what it’s worth, I’ve put my entire build process below. It’s probably too much information, but the short version is that I’m using Intel’s complier on Linux. The Kwant-specific stuff is near the end. The earlier stuff is compiling Python, SCOTCH, METIS, and MUMPS.

Any advice?

Thanks.  
-Leon

# folders to hold everything

cd  
mkdir local  
mkdir build

cd build

# install python and packages

wget [https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tar.xz](https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tar.xz)  
tar xf Python-3.5.2.tar.xz

cd Python-3.5.2  
./configure --prefix=~/local  
make  
make install  
export PATH=~/local/bin:$PATH  
cd ..

# install important python packages

pip3 install scipy tinyarray matplotlib cython

# get SCOTCH, METIS, MUMPS

wget [http://gforge.inria.fr/frs/download.php/file/34618/scotch\_6.0.4.tar.gz](http://gforge.inria.fr/frs/download.php/file/34618/scotch_6.0.4.tar.gz)  
wget [http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-5.1.0.tar.gz](http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-5.1.0.tar.gz)  
wget [http://graal.ens-lyon.fr/MUMPS/MUMPS\_5.0.2.tar.gz](http://graal.ens-lyon.fr/MUMPS/MUMPS_5.0.2.tar.gz)

tar xf scotch\_6.0.4.tar.gz  
tar xf metis-5.1.0.tar.gz  
tar xf MUMPS\_5.0.2.tar.gz

# install METIS

cd metis-5.1.0  
make config shared=1 prefix=~/local/  
make  
make install  
cd ..

# install SCOTCH

cd scotch\_6.0.4/src/  
cp Make.inc/Makefile.inc.x86-64\_pc\_linux2.icc Makefile.inc

# need to tweak the makefile

nano Makefile.inc

Add "-fPIC” to the line that starts with "CFLAGS"

make  
make esmumps  
make install prefix=~/local

# make install won't install esmumps... copy files manually

cd ../..  
cp scotch\_6.0.4/lib/libesmumps.a ~/local/lib/  
cp scotch\_6.0.4/include/esmumps.h ~/local/include/

# install MUMPS

cd MUMPS\_5.0.2  
cp Make.inc/Makefile.INTEL.SEQ Makefile.inc

# need to make a bunch of changes to Makefile.inc

nano Makefile.inc

1\) change "\#SCOTCHDIR  = ${HOME}/scotch\_6.0"  
to "SCOTCHDIR  = ${HOME}/local/lib"

2\) uncomment the line "LSCOTCH    = -L$\(SCOTCHDIR\)/lib -lesmumps -lscotch -lscotcherr"

3\) change the line "\#LMETISDIR = /local/metis/"  
to "LMETISDIR = ${HOME}/local/lib"

4\) uncomment the line "LMETIS    = -L$\(LMETISDIR\) -lmetis"

5\) change the line "ORDERINGSF  = -Dpord"  
to "ORDERINGSF  = -Dpord -Dscotch -Dmetis"

6\) change "MKLROOT=/opt/intel/mkl/lib/intel64"  
to "MKLROOT=/opt/intel-12.1/mkl/lib/intel64"

7\) add the "-fPIC" compiler flag to the lines that begin "OPTF", "OPTL", and "OPTC"

# about damn time!

make z

# there's no automatic installation...

cp include/_ ~/local/include/  
cp lib/_ ~/local/lib/  
cp libseq/libmpiseq.a ~/local/lib/  
cp libseq/\*.h ~/local/include/

cd ..

# now for kwant

git clone --branch v1.2.2  [http://gitlab.kwant-project.org/kwant/kwant.git](http://gitlab.kwant-project.org/kwant/kwant.git)  
cd kwant

# need to make a new configuration file

nano build.conf

#### START OF FILE

\[lapack\]  
libraries = mkl\_intel\_lp64 mkl\_sequential mkl\_core mkl\_def  
library\_dirs = /opt/intel-12.1/mkl/lib/intel64  
extra\_link\_args = -Wl,-rpath=/opt/intel-12.1/mkl/lib/intel64

\[mumps\]  
libraries = zmumps mumps\_common pord metis esmumps scotch scotcherr mpiseq gfortran  
library\_dirs = /home/lmaurer/local/lib/  
include\_dirs = /home/lmaurer/local/include

#### END OF FILE

# finally make and install kwant

python3 setup.py build  
python3 setup.py install

# need to do the following or kwant won't be able to find libmetis.so

export LD\_LIBRARY\_PATH=~/local/lib/:$LD\_LIBRARY\_PATH

For reference, here are my libs and headers  
$ ls local/lib/  
libesmumps.a  libmpiseq.a        libpord.a        libscotch.a  
libscotcherrexit.a  libzmumps.a  python3.5 libmetis.so   libmumps\_common.a  
libpython3.5m.a  libscotcherr.a  libscotchmetis.a    pkgconfig  
$ ls local/include/  
cmumps\_c.h     cmumps\_struc.h  dmumps\_root.h   elapse.h   metis.h  mpi.h  
mumps\_c\_types.h  scotchf.h  smumps\_c.h     smumps\_struc.h  zmumps\_root.h  
cmumps\_root.h  dmumps\_c.h      dmumps\_struc.h  esmumps.h  mpif.h  
mumps\_compat.h  python3.5m       scotch.h   smumps\_root.h  zmumps\_c.h  
zmumps\_struc.h

