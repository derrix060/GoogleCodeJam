#include <bits/stdc++.h>

using namespace std;

#define si(a)				scanf("%d",&a)
#define sl(a)				scanf("%lld",&a)
#define pi(a)				printf("%d\n",a)
#define pl(a)				printf("%lld\n",a)
 
typedef long long			ll;
typedef vector<int>			vi;
typedef pair<int, int>		ii;
typedef vector<vi>			vvi;
typedef vector<ii>			vii;
 
#define fast_io				ios_base::sync_with_stdio(false);cin.tie(NULL)
#define SET(a,b)			memset(a,b,sizeof(a))	
#define forall(i,a,b)		for(int i=a; i<b; i++)
#define forrev(i,a,b)		for(int i=a; i>=b; i--)
#define forr(type,it,container)  for(type it=container.begin(); it!=container.end(); it++)
#define w(t)				int t;si(t);while(t--)


/*
    
    Z - ZERO
    W - TWO
    U - FOUR
    X - SIX
    G - EIGHT
    H - THREE
    F - FIVE
    O - ONE
    S - SEVEN
    I - NINE

    z, w, u, x, g, h, f, o, s, i
*/


int main(){
    fast_io;


    freopen("A-large-practice.in","r",stdin);
	freopen("A-large-practice.out","w",stdout);

    map<char, int> words;
    vi numbers;
    int number;
    char ch[] = {'Z', 'W', 'U', 'X', 'G', 'H', 'F', 'O', 'S', 'I'};
    map<char, string> w_numb;
    map<int, int> numb_corresp;
    char c, cc;
    int test_case;
    string word;
    string s;

    w_numb['Z'] = "ZERO";
    numb_corresp[0] = 0;
    w_numb['W'] = "TWO";
    numb_corresp[1] = 2;
    w_numb['U'] = "FOUR";
    numb_corresp[2] = 4;
    w_numb['X'] = "SIX";
    numb_corresp[3] = 6;
    w_numb['G'] = "EIGHT";
    numb_corresp[4] = 8;
    w_numb['H'] = "THREE";
    numb_corresp[5] = 3;
    w_numb['F'] = "FIVE";
    numb_corresp[6] = 5;
    w_numb['O'] = "ONE";
    numb_corresp[7] = 1;
    w_numb['S'] = "SEVEN";
    numb_corresp[8] = 7;
    w_numb['I'] = "NINE";
    numb_corresp[9] = 9;
    

    cin >> test_case;

    forall(i,1,test_case+1){
        cin >> word;
        numbers.clear();
        words.clear();

        forall(j, 0, word.size()){
            words[word[j]] ++;
        }

        forall(j, 0, 10){
            c = ch[j];
            s = w_numb[c];
            while(words[c] > 0){
                numbers.push_back(numb_corresp[j]);
                forall(k, 0, w_numb[c].size()){
                    cc = w_numb[c][k];
                    words[cc]--;
                }
            }
        }

        sort(numbers.begin(), numbers.end());


        cout << "Case #" << i << ": ";

        forall(j, 0, numbers.size()){
            cout << "" << numbers[j];
        }
        cout << "\n";
    }

    
    return 0;
}