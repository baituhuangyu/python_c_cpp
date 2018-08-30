from distutils.core import setup, Extension


module1 = Extension('hello_ext',
                    sources = ['greet_wrapper.cpp'],
                    libraries=['boost_python'],
                    extra_compile_args=['-std=c++11'],
                    )


setup(name = 'hello_ext',
      version = '1.0',
      description = '',
      ext_modules= [module1])