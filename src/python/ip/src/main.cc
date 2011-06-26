/**
 * @file src/python/ip/src/main.cc 
 * @author <a href="mailto:andre.dos.anjos@cern.ch">Andre Anjos</a> 
 *
 * @brief Combines all modules to make up the complete bindings
 */

#include <boost/python.hpp>

using namespace boost::python;

void bind_ip_exception();
void bind_ip_ipcore();
void bind_ip_color();
void bind_ip_lbp();
void bind_ip_filters();
void bind_ip_block();
void bind_ip_crop_shift();
void bind_ip_extrapolate_mask();
void bind_ip_flipflop();
void bind_ip_gamma_correction();
void bind_ip_generate_with_center();
void bind_ip_integral();
void bind_ip_scale();
void bind_ip_shear();
void bind_ip_zigzag();
void bind_ip_rotate();
void bind_ip_flow();
void bind_ip_dctfeatures();
void bind_ip_gabor();
void bind_ip_geomnorm();
void bind_ip_faceeyesnorm();
void bind_ip_tantriggs();
void bind_ip_histogram();
void bind_ip_lbp_new();
void bind_ip_gaussian();

BOOST_PYTHON_MODULE(libpytorch_ip) {
  docstring_options docopt; 
# if !defined(TORCH_DEBUG)
  docopt.disable_cpp_signatures();
# endif
  scope().attr("__doc__") = "Torch image processing classes and sub-classes";
  bind_ip_exception();
  bind_ip_ipcore();
  bind_ip_color();
  bind_ip_lbp();
  bind_ip_filters();
  bind_ip_block();
  bind_ip_crop_shift();
  bind_ip_extrapolate_mask();
  bind_ip_flipflop();
  bind_ip_gamma_correction();
  bind_ip_generate_with_center();
  bind_ip_integral();
  bind_ip_scale();
  bind_ip_shear();
  bind_ip_zigzag();
  bind_ip_rotate();
  bind_ip_flow();
  bind_ip_dctfeatures();
  bind_ip_gabor();
  bind_ip_geomnorm();
  bind_ip_faceeyesnorm();
  bind_ip_tantriggs();
  bind_ip_histogram();
  bind_ip_lbp_new();
  bind_ip_gaussian();
}
