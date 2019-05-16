{
	'repo_type' : 'git',
	'url' : 'https://github.com/ARMmbed/mbedtls.git',
	'folder_name' : 'mbedtls_git',
	# 'configure_options' : '--host={target_host} --prefix={target_prefix} --disable-shared WINDOWS_BUILD=1',
	# 'patches' : [
	# ],
	'needs_configure': False,
	'needs_make': True,
	#'needs_make_install': False,
	'build_options': '{make_prefix_options} no_test WINDOWS_BUILD=1',
	'_info' : { 'version' : None, 'fancy_name' : 'mbedtls' },
}
