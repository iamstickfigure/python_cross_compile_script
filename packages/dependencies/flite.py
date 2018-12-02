{
	'repo_type' : 'archive',
	'download_locations' : [
		#UPDATECHECKS: http://www.speech.cs.cmu.edu/flite/packed/
		{ "url" : "http://ftp2.za.freebsd.org/pub/FreeBSD/ports/distfiles/flite-1.4-release.tar.bz2", "hashes" : [ { "type" : "sha256", "sum" : "45c662160aeca6560589f78daf42ab62c6111dd4d244afc28118c4e6f553cd0c" }, ], },
		{ "url" : "http://www.speech.cs.cmu.edu/flite/packed/flite-1.4/flite-1.4-release.tar.bz2", "hashes" : [ { "type" : "sha256", "sum" : "45c662160aeca6560589f78daf42ab62c6111dd4d244afc28118c4e6f553cd0c" }, ], },
	],
	'patches' : (
		('https://raw.githubusercontent.com/DeadSix27/python_cross_compile_script/master/patches/flite_64.diff', '-p0'),
	),
	'cpu_count' : '1',
	'needs_make_install' : False,
	'run_post_patch': (
		'sed -i.bak "s|i386-mingw32-|{cross_prefix_bare}|" configure',
		'sed -i "s|-DWIN32 -shared|-DWIN64 -static|" configure',
	),
	"run_post_build": (
		'mkdir -pv "{target_prefix}/include/flite"',
		'cp -fv include/* "{target_prefix}/include/flite"',
		'cp -fv ./build/{bit_name}-mingw32/lib/*.a "{target_prefix}/lib"',
	),
	'configure_options': '--host={target_host} --prefix={target_prefix} --disable-shared --enable-static',
	'_info' : { 'version' : '1.4', 'fancy_name' : 'flite' },
}