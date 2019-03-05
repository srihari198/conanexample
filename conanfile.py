from conans import ConanFile, CMake
class LibaConan(ConanFile):
    name = "LibB"
    version = "1.0.0"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "src/*"
    requires = "LibA/1.0.1@user/testing"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        self.run('cmake %s/src %s'%(self.source_folder, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["b"]
