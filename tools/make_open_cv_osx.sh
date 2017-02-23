#!/usr/bin/env bash
set -ex
cd opencv/opencv

mkdir -p build && cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
  -D CMAKE_INSTALL_PREFIX=/usr/local \
  -D PYTHON3_EXECUTABLE=$(which python3) \
  -D PYTHON3_PACKAGES_PATH=~/.virtualenvs/boto-mon/lib/python3.5/site-packages \
  -D PYTHON3_LIBRARY=/usr/local/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/libpython3.5m.dylib \
  -D PYTHON3_INCLUDE_DIR=/usr/local/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/include/python3.5m \
  -D PYTHON3_NUMPY_INCLUDE_DIRS=~/.virtualenvs/boto-mon/lib/python3.5/site-packages/numpy/core/include \
  -D BUILD_opencv_python3=ON \
  -D BUILD_FAT_JAVA_LIB=ON \
  -D BUILD_SHARED_LIBS=ON \
  -D INSTALL_C_EXAMPLES=OFF \
  -D INSTALL_PYTHON_EXAMPLES=OFF \
  -D BUILD_EXAMPLES=OFF \
  -D BUILD_TESTS=OFF \
  -D BUILD_PERF_TESTS=OFF \
  -D OPENCV_EXTRA_MODULES_PATH=/Users/otobrglez/Projects/boto-mon/opencv/opencv_contrib/modules \
  ..

make -j7

# cd -
