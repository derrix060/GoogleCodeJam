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

typedef struct un_color{
    char name;
    char col1;
    char col2;
    vector<char> allowed;
} un_color;

pair<char, int> maxCh(map<char, int> *un, un_color atual){
    pair<char, int> resp = make_pair('Z', -1);
    for (map<char, int>::iterator it = (*un).begin(); it != (*un).end(); it++){
        //if (it->second > resp.second && it->first != restr)
            resp = make_pair(it->first, it->second);
    }

    return resp;
}

void clear_map(map<char, int> *un){
    for(map<char,int>::iterator it = (*un).begin(); it != (*un).end(); it++){
        if (it->second == 0)
            un->erase(it);
    }
}

void print_map(map<char, int> *un){
    for(map<char,int>::iterator it = (*un).begin(); it != (*un).end(); it++){
        cout << it->first << ", " << it->second << "\n";
    }
    cout << "\n";
}


vector<un_color> get_colors(){
    vector<un_color> colors;
    vector<char> allowed;

    // Orange = R + Y
    un_color col;
    col.name = 'O';
    col.col1 = 'R';
    col.col2 = 'Y';
    allowed.push_back('B');
    col.allowed = allowed;

    colors.push_back(col);

    // Green = Y + B
    col.name = 'G';
    col.col1 = 'Y';
    col.col2 = 'B';
    allowed.clear();
    allowed.push_back('R');
    col.allowed = allowed;

    colors.push_back(col);

    // Violet = R + B
    col.name = 'V';
    col.col1 = 'R';
    col.col2 = 'B';
    allowed.clear();
    allowed.push_back('Y');
    col.allowed = allowed;

    colors.push_back(col);

    // Red
    col.name = 'R';
    col.col1 = 'R';
    col.col2 = 'R';
    allowed.clear();
    allowed.push_back('G');
    allowed.push_back('Y');
    allowed.push_back('B');
    col.allowed = allowed;

    colors.push_back(col);


    // Yellow
    col.name = 'Y';
    col.col1 = 'Y';
    col.col2 = 'Y';
    allowed.clear();
    allowed.push_back('V');
    allowed.push_back('R');
    allowed.push_back('B');
    col.allowed = allowed;

    colors.push_back(col);

    // Blue
    col.name = 'B';
    col.col1 = 'B';
    col.col2 = 'B';
    allowed.clear();
    allowed.push_back('O');
    allowed.push_back('R');
    allowed.push_back('Y');
    col.allowed = allowed;

    colors.push_back(col);

    return colors;
}

pair<char, int> next_small(map<char, int> *un, pair<char, int> actual, pair<char, int> first){
    clear_map(un);
    pair<char,int> rtn = make_pair('Z', -1);

    for (map<char,int>::iterator it = (*un).begin(); it != (*un).end(); it++){
        if (it->first == actual.first){
            it->second = actual.second;
        }
        else if (it->second == rtn.second && it->first == first.first){
            rtn.first = it->first;
            rtn.second = it->second;
        }
        else if (it->second > rtn.second){
            rtn.first = it->first;
            rtn.second = it->second;
        }
    }

    return rtn;
}

string small_answ(map<char, int> *un, int answ_size){
    string rtn = "";
    
    pair<char,int> actual = make_pair('z', -1);
    pair<char,int> first = next_small(un, actual, actual);
    //cout << "actual: " << actual.first << "first: " << first.first << "\n";

    while (rtn.size() != answ_size && actual.first != 'Z'){
        actual = next_small(un, actual, first);
        rtn += actual.first;
        actual.second --;
        //cout << rtn << "\n";
    }
    if (actual.first == 'Z')
        return "IMPOSSIBLE";
    if (rtn[0] == rtn[answ_size - 1])
        return "IMPOSSIBLE";
    else
        return rtn;
}

}

int main(){
    fast_io;
    //freopen("input_small.in","r",stdin);
	//freopen("output_small.out","w",stdout);

    map<char, int> un;
    int un_count;
    string answ;
    vector<un_color> colors = get_colors();


    int test_case;

    cin >> test_case;

    forall(i,1,test_case+1){
        un.clear();
        answ = "";

        //N, R, O, Y, G, B, and V.
        cin >> un_count >> un['R'] >> un['O'] >> un['Y'] >> un['G'] >> un['B'] >> un['V'];

        if (un['O'] == un['G'] == un['V'] == 0){
            answ = small_answ(&un, un_count);
        }


        cout << "Case #" << i << ": " << answ << "\n";
    }

    
    return 0;
}