# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


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
CMAKE_SOURCE_DIR = /home/varun/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/varun/catkin_ws/build

# Include any dependencies generated for this target.
include eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/depend.make

# Include the progress variables for this target.
include eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/progress.make

# Include the compile flags for this target's objects.
include eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/flags.make

eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/src/drone_server.cpp.o: eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/flags.make
eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/src/drone_server.cpp.o: /home/varun/catkin_ws/src/eyantra_drone/edrone_server/src/drone_server.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/varun/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/src/drone_server.cpp.o"
	cd /home/varun/catkin_ws/build/eyantra_drone/edrone_server && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/edroneserver.dir/src/drone_server.cpp.o -c /home/varun/catkin_ws/src/eyantra_drone/edrone_server/src/drone_server.cpp

eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/src/drone_server.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/edroneserver.dir/src/drone_server.cpp.i"
	cd /home/varun/catkin_ws/build/eyantra_drone/edrone_server && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/varun/catkin_ws/src/eyantra_drone/edrone_server/src/drone_server.cpp > CMakeFiles/edroneserver.dir/src/drone_server.cpp.i

eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/src/drone_server.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/edroneserver.dir/src/drone_server.cpp.s"
	cd /home/varun/catkin_ws/build/eyantra_drone/edrone_server && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/varun/catkin_ws/src/eyantra_drone/edrone_server/src/drone_server.cpp -o CMakeFiles/edroneserver.dir/src/drone_server.cpp.s

eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/src/drone_server.cpp.o.requires:

.PHONY : eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/src/drone_server.cpp.o.requires

eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/src/drone_server.cpp.o.provides: eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/src/drone_server.cpp.o.requires
	$(MAKE) -f eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/build.make eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/src/drone_server.cpp.o.provides.build
.PHONY : eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/src/drone_server.cpp.o.provides

eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/src/drone_server.cpp.o.provides.build: eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/src/drone_server.cpp.o


# Object files for target edroneserver
edroneserver_OBJECTS = \
"CMakeFiles/edroneserver.dir/src/drone_server.cpp.o"

# External object files for target edroneserver
edroneserver_EXTERNAL_OBJECTS =

/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/src/drone_server.cpp.o
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/build.make
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /opt/ros/kinetic/lib/libroscpp.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /opt/ros/kinetic/lib/libxmlrpcpp.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /opt/ros/kinetic/lib/libcv_bridge.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_core3.so.3.3.1
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_imgproc3.so.3.3.1
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_imgcodecs3.so.3.3.1
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /opt/ros/kinetic/lib/librosconsole.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /opt/ros/kinetic/lib/librosconsole_log4cxx.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /opt/ros/kinetic/lib/librosconsole_backend_interface.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /usr/lib/x86_64-linux-gnu/liblog4cxx.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /opt/ros/kinetic/lib/libroscpp_serialization.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /opt/ros/kinetic/lib/librostime.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /opt/ros/kinetic/lib/libcpp_common.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so
/home/varun/catkin_ws/devel/lib/edrone_server/edroneserver: eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/varun/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/varun/catkin_ws/devel/lib/edrone_server/edroneserver"
	cd /home/varun/catkin_ws/build/eyantra_drone/edrone_server && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/edroneserver.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/build: /home/varun/catkin_ws/devel/lib/edrone_server/edroneserver

.PHONY : eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/build

eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/requires: eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/src/drone_server.cpp.o.requires

.PHONY : eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/requires

eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/clean:
	cd /home/varun/catkin_ws/build/eyantra_drone/edrone_server && $(CMAKE_COMMAND) -P CMakeFiles/edroneserver.dir/cmake_clean.cmake
.PHONY : eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/clean

eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/depend:
	cd /home/varun/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/varun/catkin_ws/src /home/varun/catkin_ws/src/eyantra_drone/edrone_server /home/varun/catkin_ws/build /home/varun/catkin_ws/build/eyantra_drone/edrone_server /home/varun/catkin_ws/build/eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : eyantra_drone/edrone_server/CMakeFiles/edroneserver.dir/depend

