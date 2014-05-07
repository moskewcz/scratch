#include <iostream>
#include <boost/random/mersenne_twister.hpp>
#include <boost/random/discrete_distribution.hpp>

using namespace std;

typedef boost::mt19937::result_type rv_t;

int main( void ) {

  boost::mt19937 gen;
  assert( sizeof( rv_t ) == 4 );
  uint64_t val = (uint64_t(gen()) << 32) + gen();
  cout << val << endl;

#if 0
  string ret;
  uint32_t num_bytes = 3;
  for (int i = 0; i < ( (num_bytes-1) / sizeof( rv_t ) +1 ) ; ++i) {
    const rv_t rv = gen();
    for( uint32_t b = 0; b < sizeof( rv_t ); ++b ) {
      ret.push_back( uint8_t(rv >>(b*8)) );
    }
  }
  assert( ret.size() >= num_bytes );
  ret.resize( num_bytes );
  for( string::const_iterator i = ret.begin(); i != ret.end(); ++i ) {
    cout << uint32_t( uint8_t( *i ) ) << endl;
  }
#endif
}
