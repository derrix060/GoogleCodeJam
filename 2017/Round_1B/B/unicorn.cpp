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



pair<char, int> maxCh(map<char, int> un, char restr){
    pair<char, int> resp = make_pair('Z', -1);
    for (map<char, int>::iterator it = un.begin(); it != un.end(); it++){
        if (it->second > resp.second && it->first != restr)
            resp = make_pair(it->first, it->second);
    }

    return resp;
}

string small_answ(map<char,int> un, int un_count){
    
    pair<char,int> c = maxCh(un);
    string answ = c.first;
    un[c.first]--;

    while (answ.size != un_count - 1){
        c = maxCh(un);


    }

}

int main(){
    fast_io;
    //freopen("input_.in","r",stdin);
	//freopen("output_.out","w",stdout);

    map<char, int> un;
    int un_count;
    string answ;
    priority_queue<int, char> pq;
    map<char, char[]> allowed;

    allowed['O'][1] = {'B'};
    allowed['G'][1] = {'R'};
    allowed['V'][1] = {'Y'};
    allowed['R'][3] = {'G', 'Y', 'B'};
    allowed['Y'][3] = {'V', 'R', 'B'};
    allowed['B'][3] = {'O', 'R', 'Y'};

    int test_case;

    cin >> test_case;

    forall(i,1,test_case+1){
        pq.clear();
        un.clear();
        answ = "";

        //N, R, O, Y, G, B, and V.
        cin >> un_count >> un['R'] >> un['O'] >> un['Y'] >> un['G'] >> un['B'] >> un['V'];

        cout << "Case #" << i << ": " << small_answ(un, un_count) << "\n";
    }

    
    return 0;
}


/*

Can seat between
R -> Y, B, G

O -> B

Y -> R, G, V

G -> R

B -> R, Y, O

V -> Y

Multicolor

O = R + Y
G = Y + B
V = R + B

uni color
R
Y
B

all
O G V
--
R Y B

*/