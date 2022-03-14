//perceptron

#include <bits/stdc++.h>
using namespace std;
double activation(vector<double> x, vector<double> w);

int main(){
	vector<double> x;
	vector<double> w;
	x.push_back(1);
	w.push_back(3);
	x.push_back(0);
	w.push_back(4);
	x.push_back(1);
	w.push_back(5);
	double ans=activation(x,w);
	cout<<ans<<endl;

}

double activation(vector<double> x, vector<double> w){
	double ans=0;
	for(int i=0;i<x.size();i++){
		ans=ans+x[i]*w[i];
	}
	return ans;
}