#include <bits/stdc++.h>

using namespace std;

typedef long long			ll;
typedef vector<int>			vi;
typedef pair<int, int>		ii;
typedef vector<vi>			vvi;
typedef vector<ii>			vii;
 
#define fast_io				ios_base::sync_with_stdio(false);cin.tie(NULL)
#define SET(a,b)			memset(a,b,sizeof(a))	
#define forall(i,a,b)		for(int i=a; i<b; i++)
#define forrev(i,a,b)		for(int i=a; i>=b; i--)
#define forr(it,container)  for(auto it=container.begin(); it!=container.end(); it++)
#define w(t)				int t;si(t);while(t--)

int main(){
    //fast_io;
    freopen("input_large.in","r",stdin);
	freopen("output_large.out","w",stdout);

    int num_horses, test_case;
    double max_vel, destination_pos, pos, vel, timee;

    cin >> test_case;

    forall(i,1,test_case+1){
        timee = 0;
        cin >> destination_pos >> num_horses;

        forall(j, 0, num_horses){
            cin >> pos >> vel;
            timee = max((destination_pos - pos)/vel, timee);
        }

        max_vel = destination_pos/timee;
        printf("Case #%d: %f\n", i, max_vel);
    }

    
    return 0;
}