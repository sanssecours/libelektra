file (GLOB SOURCES *.c)

add_lib (highlevel
	 SOURCES
	 ${SOURCES}
	 LINK_ELEKTRA
	 elektra-kdb
	 elektra-ease)

if (BUILD_SHARED)
	set (LIBRARIES "-lelektra-highlevel -lelektra-kdb -lelektra-ease -lelektra-core")
	set (CODEGEN_LIBRARIES "-lelektra-opts -lelektra-invoke -lelektra-highlevel -lelektra-kdb -lelektra-ease -lelektra-core")
elseif (BUILD_FULL)
	set (LIBRARIES "-lelektra-full")
	set (CODEGEN_LIBRARIES "-lelektra-full")
else (BUILD_STATIC)
	set (LIBRARIES "-lelektra-static")
	set (CODEGEN_LIBRARIES "-lelektra-static")
endif ()

configure_file ("${CMAKE_CURRENT_SOURCE_DIR}/elektra-highlevel.pc.in" "${CMAKE_CURRENT_BINARY_DIR}/elektra-highlevel.pc" @ONLY)
install (FILES "${CMAKE_CURRENT_BINARY_DIR}/elektra-highlevel.pc" DESTINATION lib${LIB_SUFFIX}/${TARGET_PKGCONFIG_FOLDER})

configure_file ("${CMAKE_CURRENT_SOURCE_DIR}/elektra-codegen.pc.in" "${CMAKE_CURRENT_BINARY_DIR}/elektra-codegen.pc" @ONLY)
install (FILES "${CMAKE_CURRENT_BINARY_DIR}/elektra-codegen.pc" DESTINATION lib${LIB_SUFFIX}/${TARGET_PKGCONFIG_FOLDER})
