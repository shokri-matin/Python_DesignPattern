from abc import ABC, abstractmethod


# Abstract Class + Template Method
class Compiler(ABC):
    @abstractmethod
    def collect_source(self):
        pass

    @abstractmethod
    def compile_to_object(self):
        pass

    @abstractmethod
    def run(self):
        pass

    # Template Method
    def compile_and_run(self):
        self.collect_source()
        self.compile_to_object()
        self.run()


# Client
class iOS_compiler(Compiler):
    def collect_source(self):
        print("Collecting Swift Source Code")

    def compile_to_object(self):
        print("Compiling Swift code to LLVM bitcode")

    def run(self):
        print("Program running on runtime environment")


iOS = iOS_compiler()
iOS.compile_and_run()