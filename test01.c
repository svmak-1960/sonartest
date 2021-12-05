void f1 ( )
{
  int a1[ 10 ];
  int a2[ 10 ];
  int * p1 = a1;
  if ( p1 < a2 ) // Non-compliant, p1 and a2 point to different arrays.
  {
  }
  if ( p1 - a2 > 0 ) // Non-compliant, p1 and a2 point to different arrays.
  {
  }
  if ( a1 == a2) // Non-compliant (in C++). Comparing different array for equality is deprecated
  {
  }
}
