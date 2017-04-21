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
    UNIQUE
    
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

void clear_words(map<char, int>* words){
    words['Z']
}

int main(){
    fast_io;
    map<char, int> words;
    vi numbers;
    int number;
    char ch[] = {'Z, W, U, X, G, H, F, O, S, I'};
    map<char, char> w_numb;

    w_numb['Z'] = ['Z','E', 'R', 'O'];
    w_numb['W'] = ['T', 'W','O'];
    w_numb['U'] = ['F','O', 'U', 'R'];
    w_numb['X'] = ['S', 'I', 'X'];
    w_numb['G'] = ['E', 'I', 'G', 'H', 'T'];
    w_numb['H'] = ['T', 'H', 'R', 'E', 'E'];
    w_numb['F'] = ['F', 'I', 'V', 'E'];
    w_numb['O'] = ['O', 'N', 'E'];
    w_numb['S'] = ['S', 'E', 'V', 'E', 'N'];
    w_numb['I'] = ['N', 'I', 'N', 'E'];

    int test_case;
    string word;

    si(test_case);

    forall(i,1,test_case+1){
        cin >> word;
        numbers.clear();
        words.clear();

        forall(j, 0, word.size()){
            words[word[j]] ++;
        }

        forall(j, 0, 10){
            while(word.find(ch[j]) != npos){

            }
        }



        printf("Case #%d: %d", test_case, number);
    }
    //freopen("input.in","r",stdin);
	//freopen("output.out","w",stdout);

    
    return 0;
}