{
	'ffmpeg_base_config' : # the base for all ffmpeg configurations.
		'--arch={bit_name2} '
		'--target-os=mingw32 '
		'--cross-prefix={cross_prefix_bare} '
		'--pkg-config=pkg-config '
		'--disable-w32threads '
		'--enable-cross-compile '

		'--enable-libsoxr '
		'--enable-libass '
		'--enable-iconv '
		'--enable-cuvid '
		'--enable-libmp3lame '
		'--enable-version3 '
		'--enable-zlib '
		'--enable-libvorbis '
		'--enable-libtheora '
		'--enable-libspeex '
		'--enable-libopus '
		'--enable-libopencore-amrnb '
		'--enable-libopencore-amrwb '
		'--enable-libvo-amrwbenc '
		'--enable-libvpx '
		'--enable-libwavpack '
		'--enable-libwebp '
		'--enable-dxva2 '
		'--enable-avisynth '
		'--enable-libmysofa '
		'--enable-libsnappy '
		'--enable-libzimg '
		'--enable-libx264 '
		'--enable-libx265 '
		'--enable-libaom '
		'--enable-libvidstab '
		'--enable-libxvid '
		'--enable-gmp '
		'--enable-fontconfig '
		'--enable-libfreetype '
		'--enable-libbluray '
		'--enable-libxml2 '

		# Unavailable in 4.1
		#'--enable-libopenmpt '
		#'--enable-libdav1d '

		# TLS options
		#'--enable-nonfree '
		#'--enable-openssl '
		#'--enable-libtls '
		'--enable-gnutls ' # nongpl: openssl,libtls(libressl)
		#'--enable-mbedtls '
		
		# HW Dec/Enc
		'--enable-libmfx '
		'--enable-amf '
		'--enable-ffnvcodec '
		'--enable-cuvid '
		#'--enable-cuda-sdk ' --enable-nonfree
		'--enable-d3d11va '
		'--enable-nvenc '
		'--enable-nvdec '
		'--enable-dxva2 '
		#'--enable-opengl '
		
		'--enable-gpl '
		
		'--extra-version=DeadSix27/python_cross_compile_script '
		#'--enable-avresample ' # deprecated.
		'--pkg-config-flags="--static" '
		'--extra-libs="-lpsapi" '
		#'--extra-libs="-liconv" ' # -lschannel #-lsecurity -lz -lcrypt32 -lintl -liconv -lpng -loleaut32 -lstdc++ -lspeexdsp -lpsapi
		'--extra-cflags="-DLIBTWOLAME_STATIC" '
		'--extra-cflags="-DMODPLUG_STATIC" '

		# Aren't Needed
		#'--enable-pic '
		#'--enable-libtwolame ' # cannot find -lFLAC
		#'--enable-libzvbi '
		#'--enable-libcaca '
		#'--enable-libmodplug '
		#'--enable-librtmp '
		#'--enable-libgsm '
		#'--enable-bzlib '
		#'--enable-libilbc '
		#'--enable-vapoursynth ' #maybe works?
		#'--enable-gray '
		#'--enable-libflite '
		#'--enable-lzma '
		#'--enable-frei0r '
		#'--enable-filter=frei0r '
		#'--enable-librubberband ' # Error for flac: Missing program 'libtool'
		#'--enable-libxavs '
		#'--enable-libgme '
		#'--enable-runtime-cpudetect '
		#'--enable-libfribidi '
		#'--enable-libfontconfig '
		#'--enable-libcdio '
		#'--disable-schannel '
		#'--disable-gcrypt '
		#'--enable-libcodec2 ' # Requires https://github.com/traviscross/freeswitch/tree/master/libs/libcodec2, too lazy to split that off.
		#'--enable-ladspa '
		#'--enable-libdavs2 '
		#'--enable-libkvazaar '
		#'--enable-libxavs '
		#'--enable-libxavs2 '
		#'--enable-libsrt '
		#'--enable-liblensfun '
		#'--enable-libtesseract ' # stdlib.h: No such file or directory
		#'--enable-libvmaf '
	,
}
