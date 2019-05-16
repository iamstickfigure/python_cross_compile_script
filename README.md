[![Discord](https://img.shields.io/badge/Discord-Join-blue.svg)](https://discord.gg/gAvufS2)

# Zeranoe-Replicating FFMpeg Build

This is a modified version of **DeadSix27's Python Cross Compile Script** to replicate the Zeranoe ffmpeg builds.

## Run the following commands to get the script's dependencies.
It's possible that some of these dependencies are not necessary, but this is what was installed on a fresh Ubuntu VM when I ran this script successfully.

```bash
sudo apt-get install ragel curl libtool autoconf pkg-config zlib1g-dev mercurial unzip autogen bzip2 autoconf-archive p7zip-full python3-distutils -y
```

```bash
sudo apt-get install python3 python3-pip
```

```bash
sudo apt-get install subversion texinfo yasm git make automake gcc g++ pax cvs flex bison patch nasm cmake rake gperf gyp p7zip docbook2x nasm
```

```bash
sudo apt-get install autopoint
```

```bash
pip3 install requests progressbar2
```

```bash
pip3 install meson
```

## Before running the script,

* Make sure the git repo url and branch look correct in `packages/products/ffmpeg_static.py`
* Make sure the dependencies look correct in `packages/dependencies/ffmpeg_depends.py`
* Make sure that the build flags look correct in `packages/variables.py`.

## Run the script with

```bash
./cross_compiler.py -p ffmpeg_static
```
---

## Details

The script is going to first build MinGW-w64. 

* Will take awhile, but once it's built, it won't need to build again as long as it stays in `workdir/toolchain`.
* This is what will be used to cross-compile everything to Windows

The script will then use the compiled toolchain to build all of the ffmpeg dependencies listed in `packages/dependencies/ffmpeg_depends.py` and the sub-dependencies of those dependencies.

* Like the toolchain, once these dependencies are built, they will stick around and the script won't try to rebuild them unless the source repository changes for any of the dependencies.
* Many of these dependencies are patched by the script before building. The patches are located in the `patches` directory
* It isn't known what all of the patches are that Zeranoe has done, but after an investigation with Wireshark, the Zeranoe builds seem to have disabled TLS 1.3 in the GnuTLS package. (An important patch to get Facebook rtmps livestreaming to work)
* More can be read about this in a discussion I had on the [Zeranoe forum](https://ffmpeg.zeranoe.com/forum/viewtopic.php?f=5&t=6957)

Finally, the script will begin to configure and build ffmpeg with all of the build flags defined in `packages/variables.py` and some extras like `--libbluray` in `packages/products/ffmpeg_static.py`

Once everything has been built for the first time, if you need to make changes to the ffmpeg code, you can run `make` manually inside `workdir/x86_64_products/ffmpeg_static_git`.

* This will allow `make` to build only the files that you have changed rather than the entire ffmpeg project
* If you re-run the script instead, the dependencies won't be rebuilt, but the entire ffmpeg project will be rebuilt (Which can take about an hour)
* To get this to work, you have to add this to your `PATH` environment variable `/home/username/python_cross_compile_script/workdir/toolchain/x86_64-w64-mingw32/bin` (Or wherever the toolchain binaries are)


# Linux to Windows x64 cross-compile helper script (Original Readme)

This script automatically builds toolchain and target library/program without much user interaction.

See `./cross_compiler.py list -p` and `./cross_compiler.py list -d` for a full list of packages.

---

## **Install**

Clone the repository:

```bash
git clone "https://github.com/DeadSix27/python_cross_compile_script.git"
chmod u+x python_cross_compile_script/cross_compiler.py
```

## **Usage**

Simple usage: `./cross_compiler.py -p <product>` (e.g mpv)

For more see: `./cross_compiler.py --help`

## **System requirements:**

* Python 3.4+ (Tested only on 3.6.x)
  * Required python packages: requests, progressbar2
* GNU/Linux (Tested on ArchLinux & Ubuntu 17+)
* 20+GB is recommended, but sizes vary depending on the packages
* Resulting binaries support Win7 and newer, 64bit only

## **Package requirements (no auto-check yet)**
```
Packages required, tested on:

(This list is possibly incomplete and differs from OS to OS)

global      - texinfo yasm git make automake gcc gcc-c++ pax cvs svn flex bison patch libtoolize nasm hg cmake gettext-autopoint
mkvtoolnix  - libxslt docbook-util rake docbook-style-xsl
gnutls      - gperf
angle       - gyp
vapoursynth - p7zip
flac,expat  - docbook-to-man / docbook2x
youtube-dl  - pando
x264        - nasm 2.13
```

### Thanks to:

- [mxe](https://github.com/mxe/mxe)
- [rdp](https://github.com/rdp/ffmpeg-windows-build-helpers)
- [ArchLinux](https://aur.archlinux.org/packages/)
- [MSYS](https://github.com/Alexpux/MSYS2-packages/)
- [Martchus](https://github.com/Martchus/PKGBUILDs/commits/master)
- [Alexpux](https://github.com/Alexpux/MINGW-packages)
- [shinchiro](https://github.com/shinchiro/mpv-winbuild-cmake)
- and more