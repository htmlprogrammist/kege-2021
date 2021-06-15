#include <iostream>
#include <cmath>
int main()
{
  const int divCount = 2;    
  int divs[divCount] = {};
  for( int n = 174457; n <= 174505; n++ ) {
    int count = 0;
    int d = 2; 
	while( d*d <= n ) {
      if( n % d == 0 ) {
        count += 2;
        if( count <= divCount ) {
          divs[count-2] = d;
          if( d != n / d ) 
            divs[count-1] = n / d;
          }
        else break; 
        }  
      d += 1;  
  	  }
    if( count == divCount ) {
      for( int i = 0; i < divCount; i++ )
        std::cout << divs[i] << ' ';
      std::cout << std::endl;
      }    
    }
}

