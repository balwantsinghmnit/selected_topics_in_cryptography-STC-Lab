#include<iostream>
using namespace std;

int main()
{
	int a,b,r=1,c,count,n1,n2;
	cout<<"Enter first number\n";
	cin>>a;
	cout<<"Enter second number\n";
	cin>>b;
	n1=a;
	n2=b;

	if(a>b)
	{
		int temp = a;
		a=b;
		b=temp;
	}

	while(r!=0)
	{
		count = 0;
		while((a*count)<=b)
			count++;
		r = b-(a*(count-1));
		cout<<b<<" = "<<a<<" x "<<count-1<<" + "<<r<<endl;
		b = a;
		a = r;
	}
	cout<<"gcd("<<n1<<","<<n2<<") = "<<b<<endl;
	return(0);
}