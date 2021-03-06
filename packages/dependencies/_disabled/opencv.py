{
	'repo_type' : 'archive',
	'url' : 'https://github.com/opencv/opencv/archive/3.4.1.tar.gz',
	'folder_name' : 'opencv-3.4.1',
	'source_subfolder' : 'build',
	'configure_options': '.. -G"Unix Makefiles" -DCMAKE_SKIP_RPATH=ON -DBUILD_TESTS=OFF -DBUILD_opencv_world=ON -DBUILD_PERF_TESTS=OFF -DBUILD_DOCS=OFF -DBUILD_opencv_apps=OFF -DWITH_FFMPEG=OFF -DINSTALL_C_EXAMPLES=OFF -DINSTALL_PYTHON_EXAMPLES=OFF -DBUILD_JASPER=OFF -DBUILD_OPENEXR=OFF -DWITH_VTK=OFF -DWITH_IPP=OFF -DWITH_DSHOW=OFF -DENABLE_PRECOMPILED_HEADERS=OFF -DENABLE_STATIC_RUNTIME=OFF -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX={target_prefix} -DCMAKE_SYSTEM_NAME=Windows -DCMAKE_RANLIB={cross_prefix_full}ranlib -DCMAKE_C_COMPILER={cross_prefix_full}gcc -DCMAKE_CXX_COMPILER={cross_prefix_full}g++ -DCMAKE_RC_COMPILER={cross_prefix_full}windres -DCMAKE_FIND_ROOT_PATH={target_prefix}',
	'conf_system' : 'cmake',
	# 'patches' : [
		# ['https://raw.githubusercontent.com/Alexpux/MINGW-packages/master/mingw-w64-opencv/0001-mingw-w64-cmake.patch', '-p1', '..'],
		# ['https://raw.githubusercontent.com/Alexpux/MINGW-packages/master/mingw-w64-opencv/0002-solve_deg3-underflow.patch', '-p1', '..'],
		# ['https://raw.githubusercontent.com/Alexpux/MINGW-packages/master/mingw-w64-opencv/0003-issue-4107.patch', '-p1', '..'],
		# ['https://raw.githubusercontent.com/Alexpux/MINGW-packages/master/mingw-w64-opencv/0004-generate-proper-pkg-config-file.patch', '-p1', '..'],
		# ['https://raw.githubusercontent.com/Alexpux/MINGW-packages/master/mingw-w64-opencv/0005-opencv-support-python-3.6.patch', '-p1', '..'],
		# ['https://raw.githubusercontent.com/Alexpux/MINGW-packages/master/mingw-w64-opencv/0008-mingw-w64-cmake-lib-path.patch', '-p1', '..'],
		# ['https://raw.githubusercontent.com/Alexpux/MINGW-packages/master/mingw-w64-opencv/0009-openblas-find.patch', '-p1', '..'],
		# ['https://raw.githubusercontent.com/Alexpux/MINGW-packages/master/mingw-w64-opencv/0010-find-libpng-header.patch', '-p1', '..'],
		# ['https://raw.githubusercontent.com/Alexpux/MINGW-packages/master/mingw-w64-opencv/0011-dshow-build-fix.patch', '-p1', '..'],
	# ],
	'build_options' : 'VERBOSE=1',
	'install_options' : '{make_prefix_options} prefix={target_prefix} install',
	'_info' : { 'version' : '3.4.1', 'fancy_name' : 'opencv' },
}