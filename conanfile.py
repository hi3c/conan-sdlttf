from conans import ConanFile, CMake, tools
import os
import shutil

class SdlttfConan(ConanFile):
    name = "SDL2_ttf"
    version = "2.0.14_1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "SDL2/2.0.5@hi3c/experimental", "freetype/2.8@hi3c/experimental"
    exports = "CMakeLists.txt"

    def source(self):
        url = "https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-devel-{version}-VC.zip"
        if self.settings.os != "Windows":
            url = "http://libsdl.org/projects/SDL_ttf/release/SDL2_ttf-{version}.zip"

        url = url.format(version=self.version)

        tools.download(url, "SDLttf.zip")
        tools.unzip("SDLttf.zip")
        os.remove("SDLttf.zip")

        shutil.copy("CMakeLists.txt", "SDL2_ttf-2.0.14")


    def build(self):
        if self.settings.os == "Windows":
            return

        cmake = CMake(self)
        cmake.configure(source_dir="SDL2_ttf-2.0.14")
        cmake.build()

    def package(self):
        self.copy("SDL_ttf.h", dst="include", src="SDL2_ttf-2.0.14", keep_path=False)
        self.copy("SDL_config.h", dst="include", src="include")

        if self.settings.os == "Windows":
            archdir = "SDL2_ttf-2.0.14/lib/{}".format("x64" if self.settings.arch == "x86_64" else "x86")
            self.copy("*.lib", src=archdir, dst="lib")
            self.copy("*.dll", src=archdir, dst="bin")

        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["SDL2_ttf"]
