//sigmoid

#include <bits/stdc++.h>
using namespace std;
double sigmoid(double a){
	double ans=1/(1+exp(a));
	return ans;
}
int main()
{
	double a;
	cin>>a;
	cout<<sigmoid(a)<<endl;
}