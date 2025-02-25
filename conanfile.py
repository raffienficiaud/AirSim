from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake
from conan.errors import ConanInvalidConfiguration


class Airsim(ConanFile):
    name = "airsim"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"

    default_options = {
    }

    options = {
    }

    def requirements(self):
        self.requires("rpclib/2.3.0")
        self.requires("eigen/3.3.7")

    def configure(self):
        pass

    def generate(self):
        cmake = CMakeToolchain(self)
        cmake_args = {
        }

        for k, v in cmake_args.items():
            cmake.cache_variables[k] = v

        cmake.generate()

        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        """Generates artifacts for downstream"""
        pass
