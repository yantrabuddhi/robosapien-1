# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/abeni/rob/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/abeni/rob/build

# Utility rule file for opentld.

# Include the progress variables for this target.
include tld_tracker/CMakeFiles/opentld.dir/progress.make

tld_tracker/CMakeFiles/opentld: tld_tracker/CMakeFiles/opentld-complete

tld_tracker/CMakeFiles/opentld-complete: tld_tracker/libopentld/src/opentld-stamp/opentld-install
tld_tracker/CMakeFiles/opentld-complete: tld_tracker/libopentld/src/opentld-stamp/opentld-mkdir
tld_tracker/CMakeFiles/opentld-complete: tld_tracker/libopentld/src/opentld-stamp/opentld-download
tld_tracker/CMakeFiles/opentld-complete: tld_tracker/libopentld/src/opentld-stamp/opentld-update
tld_tracker/CMakeFiles/opentld-complete: tld_tracker/libopentld/src/opentld-stamp/opentld-patch
tld_tracker/CMakeFiles/opentld-complete: tld_tracker/libopentld/src/opentld-stamp/opentld-configure
tld_tracker/CMakeFiles/opentld-complete: tld_tracker/libopentld/src/opentld-stamp/opentld-build
tld_tracker/CMakeFiles/opentld-complete: tld_tracker/libopentld/src/opentld-stamp/opentld-install
	$(CMAKE_COMMAND) -E cmake_progress_report /home/abeni/rob/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Completed 'opentld'"
	cd /home/abeni/rob/build/tld_tracker && /usr/bin/cmake -E make_directory /home/abeni/rob/build/tld_tracker/CMakeFiles
	cd /home/abeni/rob/build/tld_tracker && /usr/bin/cmake -E touch /home/abeni/rob/build/tld_tracker/CMakeFiles/opentld-complete
	cd /home/abeni/rob/build/tld_tracker && /usr/bin/cmake -E touch /home/abeni/rob/build/tld_tracker/libopentld/src/opentld-stamp/opentld-done

tld_tracker/libopentld/src/opentld-stamp/opentld-install: tld_tracker/libopentld/src/opentld-stamp/opentld-build
	$(CMAKE_COMMAND) -E cmake_progress_report /home/abeni/rob/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Performing install step for 'opentld'"
	cd /home/abeni/rob/build/tld_tracker/libopentld/src/opentld && /home/abeni/rob/src/tld_tracker/opentld/install.sh /home/abeni/rob/devel/lib/../
	cd /home/abeni/rob/build/tld_tracker/libopentld/src/opentld && /usr/bin/cmake -E touch /home/abeni/rob/build/tld_tracker/libopentld/src/opentld-stamp/opentld-install

tld_tracker/libopentld/src/opentld-stamp/opentld-mkdir:
	$(CMAKE_COMMAND) -E cmake_progress_report /home/abeni/rob/build/CMakeFiles $(CMAKE_PROGRESS_3)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Creating directories for 'opentld'"
	cd /home/abeni/rob/build/tld_tracker && /usr/bin/cmake -E make_directory /home/abeni/rob/build/tld_tracker/libopentld/src/opentld
	cd /home/abeni/rob/build/tld_tracker && /usr/bin/cmake -E make_directory /home/abeni/rob/build/tld_tracker/libopentld/src/opentld
	cd /home/abeni/rob/build/tld_tracker && /usr/bin/cmake -E make_directory /home/abeni/rob/build/tld_tracker/libopentld
	cd /home/abeni/rob/build/tld_tracker && /usr/bin/cmake -E make_directory /home/abeni/rob/build/tld_tracker/libopentld/tmp
	cd /home/abeni/rob/build/tld_tracker && /usr/bin/cmake -E make_directory /home/abeni/rob/build/tld_tracker/libopentld/src/opentld-stamp
	cd /home/abeni/rob/build/tld_tracker && /usr/bin/cmake -E make_directory /home/abeni/rob/build/tld_tracker/libopentld/src
	cd /home/abeni/rob/build/tld_tracker && /usr/bin/cmake -E touch /home/abeni/rob/build/tld_tracker/libopentld/src/opentld-stamp/opentld-mkdir

tld_tracker/libopentld/src/opentld-stamp/opentld-download: tld_tracker/libopentld/src/opentld-stamp/opentld-svninfo.txt
tld_tracker/libopentld/src/opentld-stamp/opentld-download: tld_tracker/libopentld/src/opentld-stamp/opentld-mkdir
	$(CMAKE_COMMAND) -E cmake_progress_report /home/abeni/rob/build/CMakeFiles $(CMAKE_PROGRESS_4)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Performing download step (SVN checkout) for 'opentld'"
	cd /home/abeni/rob/build/tld_tracker/libopentld/src && /usr/bin/svn co https://github.com/Ronan0912/OpenTLD/trunk/ -rHEAD --non-interactive opentld
	cd /home/abeni/rob/build/tld_tracker/libopentld/src && /usr/bin/cmake -E touch /home/abeni/rob/build/tld_tracker/libopentld/src/opentld-stamp/opentld-download

tld_tracker/libopentld/src/opentld-stamp/opentld-update: tld_tracker/libopentld/src/opentld-stamp/opentld-download
	$(CMAKE_COMMAND) -E cmake_progress_report /home/abeni/rob/build/CMakeFiles $(CMAKE_PROGRESS_5)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Performing update step (SVN update) for 'opentld'"
	cd /home/abeni/rob/build/tld_tracker/libopentld/src/opentld && /usr/bin/svn up -rHEAD --non-interactive

tld_tracker/libopentld/src/opentld-stamp/opentld-patch: tld_tracker/libopentld/src/opentld-stamp/opentld-download
	$(CMAKE_COMMAND) -E cmake_progress_report /home/abeni/rob/build/CMakeFiles $(CMAKE_PROGRESS_6)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Performing patch step for 'opentld'"
	cd /home/abeni/rob/build/tld_tracker/libopentld/src/opentld && patch -p0 -i /home/abeni/rob/src/tld_tracker/opentld/patches/diff1.patch && patch -p0 -i /home/abeni/rob/src/tld_tracker/opentld/patches/diff2.patch
	cd /home/abeni/rob/build/tld_tracker/libopentld/src/opentld && /usr/bin/cmake -E touch /home/abeni/rob/build/tld_tracker/libopentld/src/opentld-stamp/opentld-patch

tld_tracker/libopentld/src/opentld-stamp/opentld-configure: tld_tracker/libopentld/tmp/opentld-cfgcmd.txt
tld_tracker/libopentld/src/opentld-stamp/opentld-configure: tld_tracker/libopentld/src/opentld-stamp/opentld-update
tld_tracker/libopentld/src/opentld-stamp/opentld-configure: tld_tracker/libopentld/src/opentld-stamp/opentld-patch
	$(CMAKE_COMMAND) -E cmake_progress_report /home/abeni/rob/build/CMakeFiles $(CMAKE_PROGRESS_7)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Performing configure step for 'opentld'"
	cd /home/abeni/rob/build/tld_tracker/libopentld/src/opentld && /usr/bin/cmake "-GUnix Makefiles" /home/abeni/rob/build/tld_tracker/libopentld/src/opentld
	cd /home/abeni/rob/build/tld_tracker/libopentld/src/opentld && /usr/bin/cmake -E touch /home/abeni/rob/build/tld_tracker/libopentld/src/opentld-stamp/opentld-configure

tld_tracker/libopentld/src/opentld-stamp/opentld-build: tld_tracker/libopentld/src/opentld-stamp/opentld-configure
	$(CMAKE_COMMAND) -E cmake_progress_report /home/abeni/rob/build/CMakeFiles $(CMAKE_PROGRESS_8)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Performing build step for 'opentld'"
	cd /home/abeni/rob/build/tld_tracker/libopentld/src/opentld && cmake --build .
	cd /home/abeni/rob/build/tld_tracker/libopentld/src/opentld && /usr/bin/cmake -E touch /home/abeni/rob/build/tld_tracker/libopentld/src/opentld-stamp/opentld-build

opentld: tld_tracker/CMakeFiles/opentld
opentld: tld_tracker/CMakeFiles/opentld-complete
opentld: tld_tracker/libopentld/src/opentld-stamp/opentld-install
opentld: tld_tracker/libopentld/src/opentld-stamp/opentld-mkdir
opentld: tld_tracker/libopentld/src/opentld-stamp/opentld-download
opentld: tld_tracker/libopentld/src/opentld-stamp/opentld-update
opentld: tld_tracker/libopentld/src/opentld-stamp/opentld-patch
opentld: tld_tracker/libopentld/src/opentld-stamp/opentld-configure
opentld: tld_tracker/libopentld/src/opentld-stamp/opentld-build
opentld: tld_tracker/CMakeFiles/opentld.dir/build.make
.PHONY : opentld

# Rule to build all files generated by this target.
tld_tracker/CMakeFiles/opentld.dir/build: opentld
.PHONY : tld_tracker/CMakeFiles/opentld.dir/build

tld_tracker/CMakeFiles/opentld.dir/clean:
	cd /home/abeni/rob/build/tld_tracker && $(CMAKE_COMMAND) -P CMakeFiles/opentld.dir/cmake_clean.cmake
.PHONY : tld_tracker/CMakeFiles/opentld.dir/clean

tld_tracker/CMakeFiles/opentld.dir/depend:
	cd /home/abeni/rob/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/abeni/rob/src /home/abeni/rob/src/tld_tracker /home/abeni/rob/build /home/abeni/rob/build/tld_tracker /home/abeni/rob/build/tld_tracker/CMakeFiles/opentld.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tld_tracker/CMakeFiles/opentld.dir/depend

