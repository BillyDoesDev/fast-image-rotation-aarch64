# fast-image-rotation-aarch64
haha rotation go brrr

install deps
```sh
sudo pacman -Sy aarch64-linux-gnu-gcc glew fmt vtk hdf5 qemu-user-static # or whichever version of the aarch64 gcc compiler you're using
```

build OpenCV
```sh
git clone https://github.com/opencv/opencv.git
cd opencv
mkdir bleh # why just use the generic `build` lol
cd bleh
cmake -DBUILD_SHARED_LIBS=OFF -DSOFTFP=ON -DCMAKE_TOOLCHAIN_FILE=../platforms/linux/aarch64-gnu.toolchain.cmake .. # we need static libs, and a softp version too (yea, doing it without softp really makes everyone really mad)
make -j5 # allocate as much as you safely can. go grab a drink, this will take a while .-.
make install
```

cmake toolchain file (`../platforms/linux/aarch64-gnu.toolchain.cmake`):
```cmake
set(CMAKE_SYSTEM_PROCESSOR aarch64)
set(GCC_COMPILER_VERSION "" CACHE STRING "GCC Compiler version")
set(GNU_MACHINE "aarch64-linux-gnu" CACHE STRING "GNU compiler triple")

set(CMAKE_C_COMPILER /usr/bin/aarch64-linux-gnu-gcc)
set(CMAKE_CXX_COMPILER /usr/bin/aarch64-linux-gnu-g++)
include("${CMAKE_CURRENT_LIST_DIR}/arm.toolchain.cmake")
```

yea, that's about it, it should work now, have fun

## wait, how do i build this?

idk lmao, suffer. figure it out yourself xD</br>
..is what I'd like to say, but unfortunately we live in a society.


Inside this directory, make a build directory and use `cmake` to build your project like so (make sure you have `cmake` installed and added to your path):
> Note: make sure to adjust your compiler paths accordingly.
```sh
mkdir build && cd build
cmake -DCMAKE_C_COMPILER:FILEPATH=/usr/bin/aarch64-linux-gnu-gcc -DCMAKE_CXX_COMPILER:FILEPATH=/usr/bin/aarch64-linux-gnu-g++ -B . -S ..
cmake --build . --target all
# and then run it with an emulator of your choice (for some reason, it seems to run as is on Ubuntu, but as we all all know, Ubuntu is for femboys, so yea)
qemu-aarch64-static ./nuts
```

yea, that's it, I'm done here, peace!</br>
PS: should you encounter any issues cross compiling or whatever, don't come to me. idk. (not even kidding)
