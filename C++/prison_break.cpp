#include<iostream>
#include<vector>
#include<queue>
using namespace std;
int r, c;
char prison[2][100][100];
vector<pair<int, int> > open_door;
int human[2][2];
void copy() {
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			prison[1][i][j] = prison[0][i][j];
		}
	}
	for (auto i : open_door) {
		prison[1][i.first][i.second] = '.';
	}
	open_door.clear();
}

typedef struct data {
	int x, y;
	vector<pair<int, int> > door;
}_data;

int escape(int H) {
	queue<_data> Q;
	int cnt = 9999999;
	Q.push({ human[H][0],human[H][1],{} });
	prison[1][human[H][0]][human[H][1]] = '*';
	while (!Q.empty()) {
		_data D = Q.front();
		int x = D.x, y = D.y;
		vector<pair<int, int> > door;
		door.resize(D.door.size());
		door.assign(D.door.begin(), D.door.end());
		Q.pop();
		if (0 > x + 1 || x + 1 >= r || 0 > y || y >= c) {
			if (cnt > door.size()) {
				cnt = door.size();
				open_door.resize(door.size());
				open_door.assign(door.begin(), door.end());
			}
			continue;
		}
		if (0 > x || x >= r || 0 > y + 1 || y + 1 >= c) {
			if (cnt > door.size()) {
				cnt = door.size();
				open_door.resize(door.size());
				open_door.assign(door.begin(), door.end());
			}
			continue;
		}
		if (0 > x - 1 || x - 1 >= r || 0 > y || y >= c) {
			if (cnt > door.size()) {
				cnt = door.size();
				open_door.resize(door.size());
				open_door.assign(door.begin(), door.end());
			}
			continue;
		}
		if (0 > x || x >= r || 0 > y - 1 || y - 1 >= c) {
			if (cnt > door.size()) {
				cnt = door.size();
				open_door.resize(door.size());
				open_door.assign(door.begin(), door.end());
			}
			continue;
		}

		if (0 <= x + 1 && x + 1 < r && 0 <= y && y < c && prison[1][x + 1][y] != '*') {
			if (prison[1][x + 1][y] == '#') {
				door.push_back(make_pair(x + 1, y));

				prison[1][x + 1][y] = '*';
				Q.push({ x + 1,y,door });
				door.pop_back();
			}
			else {
				prison[1][x + 1][y] = '*';
				Q.push({ x + 1,y,door });
			}
		}

		if (0 <= x && x < r && 0 <= y + 1 && y + 1 < c && prison[1][x][y + 1] != '*') {
			if (prison[1][x][y + 1] == '#') {
				door.push_back(make_pair(x, y + 1));

				prison[1][x][y + 1] = '*';
				Q.push({ x,y + 1,door });
				door.pop_back();
			}
			else {
				prison[1][x][y + 1] = '*';
				Q.push({ x,y + 1,door });
			}
		}

		if (0 <= x - 1 && x - 1 < r && 0 <= y && y < c && prison[1][x - 1][y] != '*') {
			if (prison[1][x - 1][y] == '#') {
				door.push_back(make_pair(x - 1, y));

				prison[1][x - 1][y] = '*';
				Q.push({ x - 1,y,door });
				door.pop_back();
			}
			else {
				prison[1][x - 1][y] = '*';
				Q.push({ x - 1,y,door });
			}
		}

		if (0 <= x && x < r && 0 <= y - 1 && y - 1 < c && prison[1][x][y - 1] != '*') {
			if (prison[1][x][y - 1] == '#') {
				door.push_back(make_pair(x, y - 1));

				prison[1][x][y - 1] = '*';
				Q.push({ x,y - 1,door });
				door.pop_back();
			}
			else {
				prison[1][x][y - 1] = '*';
				Q.push({ x,y - 1,door });
			}
		}

	}
	return cnt;
}

int main() {
	int N;
	cin >> N;
	for (int l = 0; l < N; l++) {
		int answer = 0;
		cin >> r >> c;
		int cnt = 0;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				cin >> prison[0][i][j];
				if (prison[0][i][j] == '$') {
					human[cnt][0] = i;
					human[cnt][1] = j;
					cnt++;
				}
			}
		}
		copy();
		int C;
		for (int i = 0; i < 2; i++) {
			C = escape(i);
			copy();
			
			
			


			answer += C;
		}
		cout << answer << '\n';
	}

}