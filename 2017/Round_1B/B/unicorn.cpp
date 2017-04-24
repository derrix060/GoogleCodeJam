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


string imp = "IMPOSSIBLE";

void print_map(map<char, int> *un){ 
    for(map<char,int>::iterator it = (*un).begin(); it != (*un).end(); it++){ 
        cout << it->first << ", " << it->second << "\n"; 
    } 
} 

void clear_map(map<char, int> *un){
    for(map<char,int>::iterator it = (*un).begin(); it != (*un).end(); it++){
        if (it->second == 0)
            un->erase(it);
    }
}

pair<char, int> next_small(map<char, int> *un, pair<char, int> actual, char fst){
    clear_map(un);
    pair<char,int> rtn = make_pair('Z', -1);

    for (map<char,int>::iterator it = (*un).begin(); it != (*un).end(); it++){
        if (it->first == actual.first){
            it->second = actual.second;
        }
        else if (it->second == rtn.second && it->first == fst){
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


string small_answ(map<char, int> *un, int answ_size,  pair<char,int> fst, char fst_c){
    string rtn = "";
    pair<char,int> actual;

    if (fst_c == 'z'){
        actual = next_small(un, fst, fst_c);
        fst_c = actual.first;
    }else{
        actual = fst;
    }
    
    //cout << "actual: " << actual.first << ", " << actual.second << " | fst_c: " << fst_c << "\n";

    while (rtn.size() != answ_size && actual.first != 'Z'){
        actual = next_small(un, actual, fst_c);
        rtn += actual.first;
        actual.second --;
        //cout << rtn << "\n";
    }
    if (actual.first == 'Z')
        return imp;
    else
        return rtn;
}

bool exist_answ(map<char, int> *un){
    int qtde, qt;

    qtde = (*un)['O'];
    qt = (*un)['B'];
    if (qtde > qt) return false;

    qtde = (*un)['G'];
    qt = (*un)['R'];
    if (qtde > qt) return false;

    qtde = (*un)['V'];
    qt = (*un)['Y'];
    if (qtde > qt) return false;

    return true;

}

bool big_continue(map<char, int> *un){
    //print_map(un);
    if ((*un)['V'] > 0 || (*un)['G'] > 0 || (*un)['O'] > 0)
        return true;
    else
        return false;
}

char next_big(char actual, map<char,int> *un){
    char bigs[3] = {'V', 'G', 'O'};
    char c;
    int maior = 0;

    if ((*un)[actual] > 0)
        return actual;

    forall(i, 0, 3){
        if (bigs[i] != actual && (*un)[bigs[i]] > maior){
            c = bigs[i];
            maior = (*un)[c];
        }
    }

    if (maior == 0){
        return 'n';
    }

    return c;
}

string big_answ(map<char,int> *un, int answ_size){
    string rtn = "";
    string smll = "";
    string tmp;
    char c = 'z';
    char c_ant;
    char c_al;
    int cur = 0;
    pair<char, int> fst;
    char fst_c = 'z';
    int new_size;

    fst = make_pair('z', -1);
    

    map<char,char> allowed;
    allowed['O'] = 'B';
    allowed['G'] = 'R';
    allowed['V'] = 'Y';

    if (!exist_answ(un)){
        return imp;
    }

    while(big_continue(un)){
        c_ant = c;
        c = next_big(c_ant, un);

        if (c == 'n') break;

        c_al = allowed[c];


        if(fst_c == 'z'){
            fst_c = c_al;
        }
        

        if (c != c_ant){
            tmp = c_al;
            rtn.append(tmp);
            cur ++;
            (*un)[c_al] --;
        }
        
        tmp = c;
        rtn.append(tmp);
        cur ++;
        if (cur == answ_size) {
            if (rtn[0] != c_al){
                return imp;
            }
            break;
        }
        tmp = c_al;
        rtn.append(tmp);
        cur ++;
        (*un)[c] --;
        (*un)[c_al] --;

        //cout << "c: " << c << ", c_al: " << c_al << "\n";
        cout << rtn << "\n\n";
    }

    new_size = answ_size - cur;

    fst = make_pair(c_al, (*un)[c_al]);
    //cout << "fst: " << fst.first << ", " << fst.second << "\n";
    
    smll = small_answ(un, new_size, fst, fst_c);

    if (smll == imp) return imp;

    return rtn + smll;

    //return "big";
}

int main(){
    fast_io;
    //freopen("input_big.in","r",stdin);
	//freopen("output_big.out","w",stdout);

    map<char, int> un;
    pair<char,int> tmp;
    int un_count;
    string answ;


    int test_case;

    cin >> test_case;

    forall(i,1,test_case+1){
        un.clear();
        answ = "";

        //N, R, O, Y, G, B, and V.
        cin >> un_count >> un['R'] >> un['O'] >> un['Y'] >> un['G'] >> un['B'] >> un['V'];

        if (un['O'] == 0 && un['G'] == 0 && un['V'] == 0){
            tmp = make_pair('z', -1);
            answ = small_answ(&un, un_count, tmp, 'z');
        }
        else{
            answ = big_answ(&un, un_count);
        }

        if (answ[0] == answ[un_count - 1])
            answ = imp;


        cout << "Case #" << i << ": " << answ << "\n";
    }

    
    return 0;
}