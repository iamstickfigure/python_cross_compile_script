{
	'is_dep_inheriter' : True,
	'depends_on' : [
		'sdl2', 
		'iconv', 
		'libass', 
		'libbluray', 
		'freetype', 
		'liblame', 
		'opencore-amr', 
		'libopus', 
		'libsnappy', 
		'libsoxr', 
		'libtheora', 
		'libvpx',
		'wavpack',
		'libwebp', 
		'libx264', 
		'libx265_multibit', 
		'libxml2', 
		'zlib', 
		'xz', 
		'vidstab', 
		'libvorbis', 
		'vo-amrwbenc', 
		'libmysofa', 
		'libspeex', 
		'libxvid', 
		'libaom',  
		'intel_quicksync_mfx', 
		'amf_headers', 
		'nv-codec-headers',

		# TLS options
		'gnutls', 
		'libnettle', # Req for gnutls
		# 'mbedtls',
		# 'libressl',

		# Won't build
		# 'twolame', 

		# Aren't needed for ffmpeg 4.1
		# 'libdav1d', 
		# 'openmpt', 

		# Possibly extra
		'bzip2', 
		'libzimg', 
		'libpng', 
		'gmp', 
		'frei0r', 
		'srt', 
		'libsndfile', 
		'libbs2b', 
		'libgme_game_music_emu', 
		'flite', 
		'libgsm', 
		'libogg', 
		'davs2', 
		'expat', 
		'xavs', 
		'xavs2', 
		'kvazaar',
		'vamp_plugin', 
		'fftw3', 
		'libcaca', 
		'libmodplug',
		'zvbi', 
		'libilbc', 
		'libfribidi', 
		'gettext', 
		'libcdio', 
		'libcdio-paranoia', 
		'vapoursynth_libs', 

		# Aren't needed
		# 'lensfun',
		
		# Won't build, and aren't needed
		# 'tesseract', 'libsamplerate', 'librubberband' 
	],
}
