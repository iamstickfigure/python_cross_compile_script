{
	'repo_type' : 'archive',
	'download_locations' : [
		#UPDATECHECKS https://www.freedesktop.org/software/harfbuzz/release/?C=M;O=D
		{ "url" : "https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-2.2.0.tar.bz2", "hashes" : [ { "type" : "sha256", "sum" : "b7ccfcbd56b970a709e8b9ea9fb46c922c606c2feef8f086fb6a8492e530f810" }, ], },
		{ "url" : "https://fossies.org/linux/misc/harfbuzz-2.2.0.tar.bz2", "hashes" : [ { "type" : "sha256", "sum" : "b7ccfcbd56b970a709e8b9ea9fb46c922c606c2feef8f086fb6a8492e530f810" }, ], },
	],
	'run_post_install': [
		'sed -i.bak \'s/Libs: -L${{libdir}} -lharfbuzz.*/Libs: -L${{libdir}} -lharfbuzz -lfreetype/\' "{pkg_config_path}/harfbuzz.pc"',
	],
	'folder_name' : 'harfbuzz-with-freetype',
	'rename_folder' : 'harfbuzz-with-freetype',
	'configure_options': '--host={target_host} --prefix={target_prefix} --with-freetype --with-fontconfig=no --disable-shared --with-icu=no --with-glib=no --with-gobject=no --disable-gtk-doc-html',
	'_info' : { 'version' : '2.2.0', 'fancy_name' : 'harfbuzz (with freetype2)' },
}