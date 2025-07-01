// https://quera.org/college/3016/chapter/8240/lesson/30088/?comments_page=1&comments_filter=ALL&submissions_page=1
#include <bits/stdc++.h>
#include <iomanip>
using namespace std;
int main(){
  double base;
  int exp;
  cin>>base>>exp;
  double res = pow(base,exp);
  cout<<fixed<<setprecision(3)<<res;
}