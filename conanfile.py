from conans import ConanFile, CMake, tools
import re


def get_cmake_version():
    content = tools.load("CMakeLists.txt")
    version = re.search(r"project\(.* VERSION (\d+\.\d+\.\d+)\)", content).group(1)
    return version


class Project(ConanFile):
    name = "mylib"
    version = get_cmake_version()
    license = "MIT"

    url = "https://github.com/mycorp/mylib"
    description = "Example project"

    settings = "os", "compiler", "build_type", "arch"

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "build_tests": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
        "build_tests": False,
    }

    generators = "cmake", "cmake_find_package", "cmake_paths"
    exports_sources = "*"

    requires = (
        "boost/1.66.0@conan/stable",
    )

    def build_requirements(self):
        if self.options.build_tests:
            self.build_requires("Catch2/2.5.0@catchorg/stable")

    def configure(self):
        self.options["boost"].shared = self.options.shared

    def configure_cmake(self):
        cmake = CMake(self, generator='Ninja')
        cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.definitions["BUILD_TESTING"] = self.options.build_tests
        cmake.configure()
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()
        if self.options.build_tests:
            self.run("{}/bin/tests".format(self.build_folder))

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["mylib"]