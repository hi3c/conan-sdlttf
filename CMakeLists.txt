cmake_minimum_required(VERSION 2.6 FATAL_ERROR)
project(SDL2_ttf)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(OpenGL)

option(BUILD_SHARED_LIBS "" ON)

add_library(SDL2_ttf SDL_ttf.c glfont.c)

target_link_libraries(SDL2_ttf CONAN_PKG::freetype CONAN_PKG::SDL2 OpenGL::GL)
target_compile_definitions(SDL2_ttf PUBLIC $<$<BOOL:${OPENGL_FOUND}>:HAVE_OPENGL>)

add_executable(showfont showfont.c)
target_link_libraries(showfont SDL2_ttf)
