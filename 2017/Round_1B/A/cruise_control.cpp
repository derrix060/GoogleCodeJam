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
    vector<double> times;

    cin >> test_case;

    forall(i,1,test_case+1){
        times.clear();

        //scanf("%f %d", &destination_pos, &num_horses);

        cin >> destination_pos >> num_horses;

        forall(j, 0, num_horses){
            //scanf("%f %f", &pos, &vel);
            cin >> pos >> vel;
            timee = (destination_pos - pos)/vel;
            //printf("timee: %f, destination_pos: %f, pos: %f, vel: %f\n", timee, destination_pos, pos, vel);
            times.push_back(timee);
        }

        sort(times.begin(), times.end(), greater<double>());
        timee = times[0];

        max_vel = destination_pos/timee;
        //printf("max_vel: %f, destination_pos: %f, timee: %f\n", max_vel, destination_pos, timee);

        printf("Case #%d: %f\n", i, max_vel);

        //cout << "Case #" << i << ": ";
        //cout << max_vel << "\n";
        //cout << setprecision(6) << max_vel << "\n";
    }

    
    return 0;
}