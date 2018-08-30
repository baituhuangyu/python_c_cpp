#include <boost/python.hpp>
#include "greet.cpp"

BOOST_PYTHON_MODULE(hello_ext)
{
    using namespace boost::python;
    def("greet", greet);
}