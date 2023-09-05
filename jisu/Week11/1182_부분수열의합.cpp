#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int N, sum;
vector<int> arr;

int cnt = 0;
void solve(int idx, int tmp) {

	if (idx == N) return;
	if (tmp + arr[idx] == sum) cnt++;

	solve(idx + 1, tmp);
	solve(idx + 1, tmp + arr[idx]);
}

int main() {
	
	cin >> N >> sum;

	for (int i = 0; i < N; i++) {
		int tmp;
		cin >> tmp;
		arr.push_back(tmp);
	}

	solve(0, 0);
	cout << cnt;

	return 0;
}

/*
<< 오 답 >>

#include <iostream>
using namespace std;

int N, S;
int arr[20];
bool selected[20];
int ans = 0;
int tmp = 0;

void DFS(int Cnt, int goalCnt, int sumOfNum){
    if (Cnt = goalCnt){
        if (sumOfNum == S) ans ++;
        return;
    }
    for (int i = 0; i < N; i++){ // N번째 인덱스까지 탐색
        if(!selected[i]){
            selected[i] = true;
            DFS(Cnt + 1, goalCnt, sumOfNum + arr[i]);
            selected[i] = false;
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> S; // N개의 정수, 합이 S가 됨

    for (int i = 0; i < N; i++)
        cin >> arr[i];

    for (int j = 1; j <= N; j++){ // 수를 j개 선택할 때
        tmp = 0;
        DFS(0, j, 0);
    }

    cout << ans;


}
*/
