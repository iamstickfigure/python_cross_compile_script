{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/2.10.0/freetype-2.10.0.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'fccc62928c65192fff6c98847233b28eb7ce05f12d2fea3f6cc90e8b4e5fbe06' }, ], },
		{ 'url' : 'https://fossies.org/linux/misc/freetype-2.10.0.tar.bz2', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'fccc62928c65192fff6c98847233b28eb7ce05f12d2fea3f6cc90e8b4e5fbe06' }, ], },
	],
	'folder_name' : 'freetype-with-harfbuzz',
	'rename_folder' : 'freetype-with-harfbuzz',
	'configure_options' : '--host={target_host} --build=x86_64-linux-gnu --prefix={target_prefix} --disable-shared --enable-static --with-zlib={target_prefix} --without-png --with-harfbuzz=yes',
	'run_post_install' : [
		'sed -i.bak \'s/Libs: -L${{libdir}} -lfreetype.*/Libs: -L${{libdir}} -lfreetype -lbz2 -lharfbuzz/\' "{pkg_config_path}/freetype2.pc"',
	],
	'update_check' : { 'url' : 'https://sourceforge.net/projects/freetype/files/freetype2/', 'type' : 'sourceforge', },
	'_info' : { 'version' : '2.10.0', 'fancy_name' : 'freetype2' },
}