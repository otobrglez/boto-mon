# Notes

Some personal notes for `boto-mon`.

## Install notes

On Raspberry Pi,...

```bash
pip install --user virtualenvwrapper
sudo apt-get install build-essential libc6-dev \
  libncurses5-dev libncursesw5-dev libreadline6-dev \
  libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev \
  libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev -q -y
mkdir Python && cd Python
./configure
make -j4
sudo make install
mkvirtualenv --python=`which python3.5` boto-mon
workone boto-mon
```

### Remote SSH volume to Pi

Mount remote project files,...
```bash
sshfs -oauto_cache,reconnect,allow_other,defer_permissions,negative_vncache,noappledouble,volname=BotoProjects boto:/home/pi/Projects /tmp/ssh
umount /tmp/ssh
```

Map connection to localhost so that direct connection to interpreter is possible.
```bash
ssh -L 9999:localhost:9999 a1
```

## OpenCV

```bash
# compile python with shared....
./configure --enable-shared

sudo apt-get update -qy && \
  sudo apt-get install -qy \
  libssl-dev libffi-dev \
  zlib1g-dev libjpeg-dev libtiff-dev libpng-dev libtiff-dev libicu-dev libjasper-dev \
  python3 python3-pip python3-setuptools python3-cffi python3-numpy

pip install -v numpy

sudo apt-get remote -f \
python3 \
python3.5-minimal \
python3.5 \
python3-numpy \
python3.5-venv \
python3.5-dev

# -DPYTHON_EXECUTABLE=/home/pi/.virtualenvs/boto-mon/bin/python3.5
# /home/pi/Python/Python-3.5.2/libpython3.5m.a
cmake \
    -D CMAKE_BUILD_TYPE=Release \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=OFF \
    -D PYTHON3_EXECUTABLE=$(which python3) \
    -D PYTHON3_PACKAGES_PATH=/home/pi/.virtualenvs/boto-mon/lib/python3.5/site-packages \
    -D PYTHON3_NUMPY_INCLUDE_DIRS=/home/pi/.virtualenvs/boto-mon/lib/python3.5/site-packages/numpy/core/include \
    -D PYTHON3_LIBRARY=/home/pi/Python/Python-3.5.2/libpython3.5m.so \
    -D OPENCV_EXTRA_MODULES_PATH=/opt/opencv_contrib/modules \
  	-D BUILD_opencv_python3=ON \
    -D BUILD_NEW_PYTHON_SUPPORT=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D ENABLE_PRECOMPILED_HEADERS=ON \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_TESTS=OFF \
    -D BUILD_PERF_TESTS=OFF \
    -D BUILD_DOCS=OFF \
    -D WITH_FFMPEG=ON \
    -D WITH_V4L=ON \
    -D WITH_FFMPEG=ON \
    -D WITH_GSTREAMER=ON \
    -D WITH_GTK=OFF \
    ..


-D CMAKE_INSTALL_PREFIX=/usr/local \
-D PYTHON3_EXECUTABLE=/path/to/venv3/bin/python \
-D PYTHON3_PACKAGES_PATH=/path/to/venv3/lib/python3.4/site-packages \
-D PYTHON3_LIBRARY=/Library/Frameworks/Python.framework/Versions/3.4/lib/libpython3.4m.dylib \
-D PYTHON3_INCLUDE_DIR=/Library/Frameworks/Python.framework/Versions/3.4/include/python3.4m \
-D PYTHON3_NUMPY_INCLUDE_DIRS=/Users/rainy/Projects/Vision/venv3/lib/python3.4/site-packages/numpy/core/include \

```