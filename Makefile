#
all: urdf_to_collada

GIT_DIR = build/robot_model/src
GIT_URL = https://github.com/ros/robot_model.git
GIT_REVISION = hydro-devel
PATCH_DIR = $(CURDIR)
GIT_PATCH = ${PATCH_DIR}/use_assimp_devel.patch
BUILD_BIN_DIR  = build/robot_model/devel/lib/collada_urdf
include $(shell rospack find mk)/git_checkout.mk

urdf_to_collada:$(GIT_DIR) patched
	(cd build/robot_model; PKG_CONFIG_PATH=`rospack find assimp_devel`/lib/pkgconfig:${PKG_CONFIG_PATH} catkin_make --pkg collada_urdf --force-cmake)
	cp $(BUILD_BIN_DIR)/urdf_to_collada .

clean:
	if [ -f build/robot_model/build ] ; then catkin_make clean; fi
	rm -fr build/robot_model/build
	rm -rf installed patched
	rm -f urdf_to_collada

wipe: clean
	rm -rf $(SRC_DIR)
