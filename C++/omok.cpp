#include<iostream>
#include<vector>
#include<istream>
#include<ostream>
#include<fstream>
using namespace std;

char board[19][19];     //문제마다 오목판 크기달라서 정식규격인19*19로했습니다
vector<pair<int, int> > S; // 무르기를위한 스택
vector<pair<int, int> > S2;// 무르기 취소를 위한 스택
int B, W;
int best;					//가장 긴 돌들의 길이
int best_sx, best_sy, best_ex, best_ey; // 가장 긴 돌들의 시작과 끝좌표
char best_color;

void warning(int x, int y, char S) {
	int sum = 1;
	int sx, sy;	//시작 좌표
	int ex, ey;	//끝 좌표
	int flag = 0; // 한칸띈거까지 세기
	//양방향검사로 8번 수행합니다
	for (int i = 1; i <= 4; i++) {			// 아래방향검사
		if (0 > x + i || x + i > 18 || 0 > y || y > 18) {
			if (board[x + i - 1][y] == '+') {
				sx = x + i - 2; sy = y;
			}
			else {
				sx = x + i - 1; sy = y;
			}
			break;
		}
		if (board[x + i][y] == S) {
			sum++;
		}
		else if (board[x + i][y] == '+') {
			if (flag == 0) {
				flag = 1;
			}
			else {
				if (board[x + i - 1][y] == '+') {
					sx = x + i - 2; sy = y;
				}
				else {
					sx = x + i - 1; sy = y;
				}
				break;
			}
		}
		else {
			if (board[x + i - 1][y] == '+') {
				sx = x + i - 2; sy = y;
			}
			else {
				sx = x + i - 1; sy = y;
			}
			break;
		}
	}
	for (int i = 1; i <= 4; i++) {			// 위방향검사
		if (0 > x - i || x - i > 18 || 0 > y || y > 18) {
			if (board[x - i + 1][y] == '+') {
				ex = x - i + 2; ey = y;
			}
			else {
				ex = x - i + 1; ey = y;
			}
			break;
		}
		if (board[x - i][y] == S) {
			sum++;
		}
		else if (board[x - i][y] == '+') {
			if (flag == 0) {
				flag = 1;
			}
			else {
				if (board[x - i + 1][y] == '+') {
					ex = x - i + 2; ey = y;
				}
				else {
					ex = x - i + 1; ey = y;
				}
				break;
			}
		}
		else {
			if (board[x - i + 1][y] == '+') {
				ex = x - i + 2; ey = y;
			}
			else {
				ex = x - i + 1; ey = y;
			}
			break;
		}
	}
	if (sum > best) {
		best = sum;
		best_sx = sx;
		best_sy = sy;
		best_ex = ex;
		best_ey = ey;
		best_color = S;
		
	}
	sum = 1;
	flag = 0;
	for (int i = 1; i <= 4; i++) {			// 위방향검사
		if (0 > x - i || x - i > 18 || 0 > y || y > 18) {
			if (board[x - i + 1][y] == '+') {
				sx = x - i + 2; sy = y;
			}
			else {
				sx = x - i + 1; sy = y;
			}
			break;
		}
		if (board[x - i][y] == S) {
			sum++;
		}
		else if (board[x - i][y] == '+') {
			if (flag == 0) {
				flag = 1;
			}
			else {
				if (board[x - i + 1][y] == '+') {
					sx = x - i + 2; sy = y;
				}
				else {
					sx = x - i + 1; sy = y;
				}
				break;
			}
		}
		else {
			if (board[x - i + 1][y] == '+') {
				sx = x - i + 2; sy = y;
			}
			else {
				sx = x - i + 1; sy = y;
			}
			break;
		}
	}
	for (int i = 1; i <= 4; i++) {			// 아래방향검사
		if (0 > x + i || x + i > 18 || 0 > y || y > 18) {
			if (board[x + i - 1][y] == '+') {
				ex = x + i - 2; ey = y;
			}
			else {
				ex = x + i - 1; ey = y;
			}
			break;
		}
		if (board[x + i][y] == S) {
			sum++;
		}
		else if (board[x + i][y] == '+') {
			if (flag == 0) {
				flag = 1;
			}
			else {
				if (board[x + i - 1][y] == '+') {
					ex = x + i - 2; ey = y;
				}
				else {
					ex = x + i - 1; ey = y;
				}
				break;
			}
		}
		else {
			if (board[x + i - 1][y] == '+') {
				ex = x + i - 2; ey = y;
			}
			else {
				ex = x + i - 1; ey = y;
			}
			break;
		}
	}
	if (sum > best) {
		best = sum;
		best_sx = sx;
		best_sy = sy;
		best_ex = ex;
		best_ey = ey;
		best_color = S;
	}
	sum = 1;
	flag = 0;
	for (int i = 1; i <= 4; i++) {			// 왼쪽 방향검사
		if (0 > x || x > 18 || 0 > y - i || y - i > 18) {
			if (board[x][y - i + 1] == '+') {
				sx = x; sy = y - i + 2;
			}
			else {
				sx = x; sy = y - i + 1;
			}
			break;
		}
		if (board[x][y - i] == S) {
			sum++;
		}
		else if (board[x][y - i] == '+') {
			if (flag == 0) {
				flag = 1;
			}
			else {
				if (board[x][y - i + 1] == '+') {
					sx = x; sy = y - i + 2;
				}
				else {
					sx = x; sy = y - i + 1;
				}
				break;
			}
		}
		else {
			if (board[x][y - i + 1] == '+') {
				sx = x; sy = y - i + 2;
			}
			else {
				sx = x; sy = y - i + 1;
			}
			break;
		}
	}
	for (int i = 1; i <= 4; i++) {			// 오른쪽 방향검사
		if (0 > x || x > 18 || 0 > y + i || y + i > 18) {
			if (board[x][y + i - 1] == '+') {
				ex = x; ey = y + i - 2;
			}
			else {
				ex = x; ey = y + i - 1;
			}
			break;
		}
		if (board[x][y + i] == S) {
			sum++;
		}
		else if (board[x][y + i] == '+') {
			if (flag == 0) {
				flag = 1;
			}
			else {
				if (board[x][y + i - 1] == '+') {
					ex = x; ey = y + i - 2;
				}
				else {
					ex = x; ey = y + i - 1;
				}
				break;
			}
		}
		else {
			if (board[x][y + i - 1] == '+') {
				ex = x; ey = y + i - 2;
			}
			else {
				ex = x; ey = y + i - 1;
			}
			break;
		}
	}
	if (sum > best) {
		best = sum;
		best_sx = sx;
		best_sy = sy;
		best_ex = ex;
		best_ey = ey;
		best_color = S;
		best_color = S;
	}
	sum = 1;
	flag = 0;
	for (int i = 1; i <= 4; i++) {			// 오른쪽 방향검사
		if (0 > x || x > 18 || 0 > y + i || y + i > 18) {
			if (board[x][y + i - 1] == '+') {
				sx = x; sy = y + i - 2;
			}
			else {
				sx = x; sy = y + i - 1;
			}
			break;
		}
		if (board[x][y + i] == S) {
			sum++;
		}
		else if (board[x][y + i] == '+') {
			if (flag == 0) {
				flag = 1;
			}
			else {
				if (board[x][y + i - 1] == '+') {
					sx = x; sy = y + i - 2;
				}
				else {
					sx = x; sy = y + i - 1;
				}
				break;
			}
		}
		else {
			if (board[x][y + i - 1] == '+') {
				sx = x; sy = y + i - 2;
			}
			else {
				sx = x; sy = y + i - 1;
			}
			break;
		}
	}

	for (int i = 1; i <= 4; i++) {			// 왼쪽 방향검사
		if (0 > x || x > 18 || 0 > y - i || y - i > 18) {
			if (board[x][y - i + 1] == '+') {
				ex = x; ey = y - i + 2;
			}
			else {
				ex = x; ey = y - i + 1;
			}
			break;
		}
		if (board[x][y - i] == S) {
			sum++;
		}
		else if (board[x][y - i] == '+') {
			if (flag == 0) {
				flag = 1;
			}
			else {
				if (board[x][y - i + 1] == '+') {
					ex = x; ey = y - i + 2;
				}
				else {
					ex = x; ey = y - i + 1;
				}
				break;
			}
		}
		else {
			if (board[x][y - i + 1] == '+') {
				ex = x; ey = y - i + 2;
			}
			else {
				ex = x; ey = y - i + 1;
			}
			break;
		}
	}
	if (sum > best) {
		best = sum;
		best_sx = sx;
		best_sy = sy;
		best_ex = ex;
		best_ey = ey;
		best_color = S;
	}
	sum = 1;
	flag = 0;
	for (int i = 1; i <= 4; i++) {			// 오른쪽 아래 방향검사
		if (0 > x + i || x + i > 18 || 0 > y + i || y + i > 18) {
			if (board[x + i - 1][y + i - 1] == '+') {
				sx = x + i - 2; sy = y + i - 2;
			}
			else {
				sx = x + i - 1; sy = y + i - 1;
			}
			break;
		}
		if (board[x + i][y + i] == S) {
			sum++;
		}
		else if (board[x + i][y + i] == '+') {
			if (flag == 0) {
				flag = 1;
			}
			else {
				if (board[x + i - 1][y + i - 1] == '+') {
					sx = x + i - 2; sy = y + i - 2;
				}
				else {
					sx = x + i - 1; sy = y + i - 1;
				}
				break;
			}
		}
		else {
			if (board[x + i - 1][y + i - 1] == '+') {
				sx = x + i - 2; sy = y + i - 2;
			}
			else {
				sx = x + i - 1; sy = y + i - 1;
			}
			break;
		}
	}

	for (int i = 1; i <= 4; i++) {			// 왼쪽 위 방향검사
		if (0 > x - i || x - i > 18 || 0 > y - i || y - i > 18) {
			if (board[x - i + 1][y - i + 1] == '+') {
				ex = x - i + 2; ey = y - i + 2;
			}
			else {
				ex = x - i + 1; ey = y - i + 1;
			}
			break;
		}
		if (board[x - i][y - i] == S) {
			sum++;
		}
		else if (board[x - i][y - i] == '+') {
			if (flag == 0) {
				flag = 1;
			}
			else {
				if (board[x - i + 1][y - i + 1] == '+') {
					ex = x - i + 2; ey = y - i + 2;
				}
				else {
					ex = x - i + 1; ey = y - i + 1;
				}
				break;
			}
		}
		else {
			if (board[x - i + 1][y - i + 1] == '+') {
				ex = x - i + 2; ey = y - i + 2;
			}
			else {
				ex = x - i + 1; ey = y - i + 1;
			}
			break;
		}
	}
	if (sum > best) {
		best = sum;
		best_sx = sx;
		best_sy = sy;
		best_ex = ex;
		best_ey = ey;
		best_color = S;
	}
	sum = 1;
	flag = 0;
	for (int i = 1; i <= 4; i++) {			// 왼쪽 위 방향검사
		if (0 > x - i || x - i > 18 || 0 > y - i || y - i > 18) {
			if (board[x - i + 1][y - i + 1] == '+') {
				ex = x - i + 2; ey = y - i + 2;
			}
			else {
				ex = x - i + 1; ey = y - i + 1;
			}
			break;
		}
		if (board[x - i][y - i] == S) {
			sum++;
		}
		else if (board[x - i][y - i] == '+') {
			if (flag == 0) {
				flag = 1;
			}
			else {
				if (board[x - i + 1][y - i + 1] == '+') {
					ex = x - i + 2; ey = y - i + 2;
				}
				else {
					ex = x - i + 1; ey = y - i + 1;
				}
				break;
			}
		}
		else {
			if (board[x - i + 1][y - i + 1] == '+') {
				ex = x - i + 2; ey = y - i + 2;
			}
			else {
				ex = x - i + 1; ey = y - i + 1;
			}
			break;
		}
	}
	for (int i = 1; i <= 4; i++) {			// 오른쪽 아래 방향검사
		if (0 > x + i || x + i > 18 || 0 > y + i || y + i > 18) {
			if (board[x + i - 1][y + i - 1] == '+') {
				sx = x + i - 2; sy = y + i - 2;
			}
			else {
				sx = x + i - 1; sy = y + i - 1;
			}
			break;
		}
		if (board[x + i][y + i] == S) {
			sum++;
		}
		else if (board[x + i][y + i] == '+') {
			if (flag == 0) {
				flag = 1;
			}
			else {
				if (board[x + i - 1][y + i - 1] == '+') {
					sx = x + i - 2; sy = y + i - 2;
				}
				else {
					sx = x + i - 1; sy = y + i - 1;
				}
				break;
			}
		}
		else {
			if (board[x + i - 1][y + i - 1] == '+') {
				sx = x + i - 2; sy = y + i - 2;
			}
			else {
				sx = x + i - 1; sy = y + i - 1;
			}
			break;
		}
	}


	if (sum > best) {
		best = sum;
		best_sx = sx;
		best_sy = sy;
		best_ex = ex;
		best_ey = ey;
		best_color = S;
	}
	sum = 1;
	flag = 0;
	for (int i = 1; i <= 4; i++) {			// 왼쪽 아래 방향검사
		if (0 > x + i || x + i > 18 || 0 > y - i || y - i > 18) {
			if (board[x + i - 1][y - i + 1] == '+') {
				ex = x + i - 2; ey = y - i + 2;
			}
			else {
				ex = x + i - 1; ey = y - i + 1;
			}
			break;
		}
		if (board[x + i][y - i] == S) {
			sum++;
		}
		else if (board[x + i][y - i] == '+') {
			if (flag == 0) {
				flag = 1;
			}
			else {
				if (board[x + i - 1][y - i + 1] == '+') {
					ex = x + i - 2; ey = y - i + 2;
				}
				else {
					ex = x + i - 1; ey = y - i + 1;
				}
				break;
			}
		}
		else {
			if (board[x + i - 1][y - i + 1] == '+') {
				ex = x + i - 2; ey = y - i + 2;
			}
			else {
				ex = x + i - 1; ey = y - i + 1;
			}
			break;
		}
	}
	for (int i = 1; i <= 4; i++) {			// 오른쪽 위 방향검사
		if (0 > x - i || x - i > 18 || 0 > y + i || y + i > 18) {
			if (board[x - i + 1][y + i - 1] == '+') {
				sx = x - i + 2; sy = y + i - 2;
			}
			else {
				sx = x - i + 1; sy = y + i - 1;
			}
			break;
		}
		if (board[x - i][y + i] == S) {
			sum++;
		}
		else if (board[x - i][y + i] == '+') {
			if (flag == 0) {
				flag = 1;
			}
			else {
				if (board[x - i + 1][y + i - 1] == '+') {
					sx = x - i + 2; sy = y + i - 2;
				}
				else {
					sx = x - i + 1; sy = y + i - 1;
				}
				break;
			}
		}
		else {
			if (board[x - i + 1][y + i - 1] == '+') {
				sx = x - i + 2; sy = y + i - 2;
			}
			else {
				sx = x - i + 1; sy = y + i - 1;
			}
			break;
		}
	}


	if (sum > best) {
		best = sum;
		best_sx = sx;
		best_sy = sy;
		best_ex = ex;
		best_ey = ey;
		best_color = S;
	}
	sum = 1;
	flag = 0;
	for (int i = 1; i <= 4; i++) {			// 오른쪽 위 방향검사
		if (0 > x - i || x - i > 18 || 0 > y + i || y + i > 18) {
			if (board[x - i + 1][y + i - 1] == '+') {
				sx = x - i + 2; sy = y + i - 2;
			}
			else {
				sx = x - i + 1; sy = y + i - 1;
			}
			break;
		}
		if (board[x - i][y + i] == S) {
			sum++;
		}
		else if (board[x - i][y + i] == '+') {
			if (flag == 0) {
				flag = 1;
			}
			else {
				if (board[x - i + 1][y + i - 1] == '+') {
					sx = x - i + 2; sy = y + i - 2;
				}
				else {
					sx = x - i + 1; sy = y + i - 1;
				}
				break;
			}
		}
		else {
			if (board[x - i + 1][y + i - 1] == '+') {
				sx = x - i + 2; sy = y + i - 2;
			}
			else {
				sx = x - i + 1; sy = y + i - 1;
			}
			break;
		}
	}
	for (int i = 1; i <= 4; i++) {			// 왼쪽 아래 방향검사
		if (0 > x + i || x + i > 18 || 0 > y - i || y - i > 18) {
			if (board[x + i - 1][y - i + 1] == '+') {
				ex = x + i - 2; ey = y - i + 2;
			}
			else {
				ex = x + i - 1; ey = y - i + 1;
			}
			break;
		}
		if (board[x + i][y - i] == S) {
			sum++;
		}
		else if (board[x + i][y - i] == '+') {
			if (flag == 0) {
				flag = 1;
			}
			else {
				if (board[x + i - 1][y - i + 1] == '+') {
					ex = x + i - 2; ey = y - i + 2;
				}
				else {
					ex = x + i - 1; ey = y - i + 1;
				}
				break;
			}
		}
		else {
			if (board[x + i - 1][y - i + 1] == '+') {
				ex = x + i - 2; ey = y - i + 2;
			}
			else {
				ex = x + i - 1; ey = y - i + 1;
			}
			break;
		}
	}


	if (sum > best) {
		best = sum;
		best_sx = sx;
		best_sy = sy;
		best_ex = ex;
		best_ey = ey;
		best_color = S;
	}
	sum = 1;
	flag = 0;
}

void init() {        //오목판 초기화
	for (int i = 0; i < 19; i++) {
		for (int j = 0; j < 19; j++) {
			board[i][j] = '+';
		}
	}
}

void print_board() { //오목판 출력함수
	cout << "  ";
	for (int i = 0; i < 19; i++) {
		if (i < 10)
			cout << i << ' ';
		else

			cout << char('A' - 10 + i) << ' ';
	}
	cout << '\n';
	for (int i = 0; i < 19; i++) {
		if (i < 10)
			cout << i << ' ';
		else

			cout << char('A' - 10 + i) << ' ';
		for (int j = 0; j < 19; j++) {
			cout << board[i][j] << ' ';
		}
		cout << '\n';
	}
	cout << "검은돌: " << B << "    하얀돌: " << W << '\n';
	cout << "가장 긴 돌: " << best_color << ", 길이: " << best << ", 시작: " << best_sx << "," << best_sy << " 끝: " << best_ex << "," << best_ey << "\n";
	
}

void stone(int* flag) {
	if (*flag == 0) {
		int x, y;       //좌표입력받기
		cout << "흑돌 차례\n(ex: 0 18)>> ";
		cin >> x >> y;
		if (0 > x || x > 18 || 0 > y || y > 18) {
			cout << "좌표오류\n";
			return;
		}
		//비어있으면 돌을 놓고 돌이놓여있으면 문구출력
		if (board[x][y] == '+') {
			board[x][y] = 'B';
			*flag = 1;
			B++; // 놓여있는 검은돌 갯수
			S.push_back(make_pair(x, y));
			S2.clear();
			warning(x, y, 'B');
		}
		else {
			cout << "이미 돌이 놓여있습니다.\n";
		}
	}
	else {//흰돌차례일때
		int x, y;       //좌표입력받기
		cout << "백돌 차례\n(ex: 0 18)>> ";
		cin >> x >> y;
		if (0 > x || x > 18 || 0 > y || y > 18) {
			cout << "좌표오류\n";
			return;
		}
		//비어있으면 돌을 놓고 돌이놓여있으면 문구출력
		if (board[x][y] == '+') {
			board[x][y] = 'W';
			*flag = 0;
			W++; // 놓여있는 흰돌 갯수
			S.push_back(make_pair(x, y));
			S2.clear();
			warning(x, y, 'W');
		}
		else {
			cout << "이미 돌이 놓여있습니다.\n";
		}
	}
}

void get_board() {
	cout << "가로\n";
	for (int i = 0; i < 19; i++) {   //가로방향확인
		int w = 0, b = 0; // 줄의 돌갯수
		int sw = 0, sb = 0; // 연속된 돌갯수
		int mw = 0, mb = 0; //최대로 연속된 돌갯수
		int flag = 0;  //연속인지 확인
		int xb = 0, xw = 0;//연속된 돌들의 좌표
		int mxb = 0, mxw = 0;//최대로 연속된 돌들의 좌표
		for (int j = 0; j < 19; j++) {
			if (board[i][j] == 'B') {
				b++;
				if (flag == 1) {
					sb++;
				}
				else {
					xb = j;
					flag = 1;
					sb = 1;
				}
				if (sb > mb) {
					mxb = xb;
					mb = sb;
				}
			}
			else if (board[i][j] == 'W') {
				w++;
				if (flag == 2) {
					sw++;
				}
				else {
					xw = j;
					flag = 2;
					sw = 1;
				}
				if (sw > mw) {
					mxw == xw;
					mw = sw;
				}
			}
			else {
				flag = 0;
			}
		}

		if (0 <= i && i <= 9) {
			cout << i << " B" << b << " W" << w << "  MAX";
		}
		else {
			cout << char('A' + i - 10) << " B" << b << " W" << w << "  MAX";
		}

		if (mw > mb) {
			if (mxw > 9)
				cout << " W" << mw << "  " << char('A' + mxw - 10) << "~" << '\n';
			else
				cout << " W" << mw << "  " << mxw << "~" << '\n';
		}
		else if (mw < mb) {
			if (mxb > 9)
				cout << " B" << mw << "  " << char('A' + mxb - 10) << "~" << '\n';
			else
				cout << " B" << mw << "  " << mxb << "~" << '\n';
		}
		else {
			if (mxb > 9)
				cout << " B" << mw << "  " << char('A' + mxb - 10) << "~";
			else
				cout << " B" << mw << "  " << mxb << "~";
			if (mxw > 9)
				cout << " W" << mw << "  " << char('A' + mxw - 10) << "~\n";
			else
				cout << " W" << mw << "  " << mxw << "~\n";

		}
	}
	cout << "세로\n";
	for (int i = 0; i < 19; i++) {   //세로방향확인
		int w = 0, b = 0; // 줄의 돌갯수
		int sw = 0, sb = 0; // 연속된 돌갯수
		int mw = 0, mb = 0; //최대로 연속된 돌갯수
		int flag = 0;  //연속인지 확인
		for (int j = 0; j < 19; j++) {
			if (board[j][i] == 'B') {
				b++;
				if (flag == 1) {
					sb++;
				}
				else {
					flag = 1;
					sb = 1;
				}
				if (sb > mb) {
					mb = sb;
				}
			}
			else if (board[j][i] == 'W') {
				w++;
				if (flag == 2) {
					sw++;
				}
				else {
					flag = 2;
					sw = 1;
				}
				if (sw > mw) {
					mw = sw;
				}
			}
			else {
				flag = 0;
			}
		}

		if (0 <= i && i <= 9) {
			cout << i << " B" << b << " W" << w << "  MAX";
		}
		else {
			cout << char('A' + i - 10) << " B" << b << " W" << w << "  MAX";
		}

		if (mw > mb) {
			cout << " W" << mw << '\n';
		}
		else if (mw < mb) {
			cout << " B" << mb << '\n';
		}
		else {
			cout << " B" << mb << " W" << mw << '\n';
		}
	}

	cout << "우상향 대각선\n";
	for (int i = 0; i < 19; i++) {   //우상향 방향확인 왼쪽절반
		int w = 0, b = 0; // 줄의 돌갯수
		int sw = 0, sb = 0; // 연속된 돌갯수
		int mw = 0, mb = 0; //최대로 연속된 돌갯수
		int flag = 0;  //연속인지 확인
		for (int j = 0; j <= i; j++) {
			if (board[i - j][j] == 'B') {
				b++;
				if (flag == 1) {
					sb++;
				}
				else {
					flag = 1;
					sb = 1;
				}
				if (sb > mb) {
					mb = sb;
				}
			}
			else if (board[i - j][j] == 'W') {
				w++;
				if (flag == 2) {
					sw++;
				}
				else {
					flag = 2;
					sw = 1;
				}
				if (sw > mw) {
					mw = sw;
				}
			}
			else {
				flag = 0;
			}
		}

		if (0 <= i && i <= 9) {
			cout << "(" << i << ",0)" << " (0," << i << ")  MAX";
		}
		else {
			cout << "(" << char('A' + i - 10) << ",0)" << " (0," << char('A' + i - 10) << ")  MAX";

		}

		if (mw > mb) {
			cout << " W" << mw << '\n';
		}
		else if (mw < mb) {
			cout << " B" << mb << '\n';
		}
		else {
			cout << " B" << mb << " W" << mw << '\n';
		}
	}
	for (int i = 1; i < 19; i++) {   //우상향 방향확인 오른쪽절반
		int w = 0, b = 0; // 줄의 돌갯수
		int sw = 0, sb = 0; // 연속된 돌갯수
		int mw = 0, mb = 0; //최대로 연속된 돌갯수
		int flag = 0;  //연속인지 확인
		for (int j = 0; j <= 19 - i; j++) {
			if (board[19 - j][j + i - 1] == 'B') {
				b++;
				if (flag == 1) {
					sb++;
				}
				else {
					flag = 1;
					sb = 1;
				}
				if (sb > mb) {
					mb = sb;
				}
			}
			else if (board[19 - j][j + i - 1] == 'W') {
				w++;
				if (flag == 2) {
					sw++;
				}
				else {
					flag = 2;
					sw = 1;
				}
				if (sw > mw) {
					mw = sw;
				}
			}
			else {
				flag = 0;
			}
		}

		if (0 <= i && i <= 9) {
			cout << "(I," << i << ")" << " (" << i << ",I)  MAX";
		}
		else {
			cout << "(I," << char('A' + i - 10) << ")" << " (" << char('A' + i - 10) << ",I)  MAX";

		}

		if (mw > mb) {
			cout << " W" << mw << '\n';
		}
		else if (mw < mb) {
			cout << " B" << mb << '\n';
		}
		else {
			cout << " B" << mb << " W" << mw << '\n';
		}
	}
	cout << "좌상향 대각선\n";
	for (int i = 18; i >= 0; i--) {   //좌상향 방향확인 왼쪽절반
		int w = 0, b = 0; // 줄의 돌갯수
		int sw = 0, sb = 0; // 연속된 돌갯수
		int mw = 0, mb = 0; //최대로 연속된 돌갯수
		int flag = 0;  //연속인지 확인
		for (int j = 18; j >= i; j--) {
			if (board[j][j - i] == 'B') {
				b++;
				if (flag == 1) {
					sb++;
				}
				else {
					flag = 1;
					sb = 1;
				}
				if (sb > mb) {
					mb = sb;
				}
			}
			else if (board[j][j - i] == 'W') {
				w++;
				if (flag == 2) {
					sw++;
				}
				else {
					flag = 2;
					sw = 1;
				}
				if (sw > mw) {
					mw = sw;
				}
			}
			else {
				flag = 0;
			}
		}

		if (0 <= i && i < 9) {
			cout << "(I," << char('A' + (18 - i - 10)) << ")" << " (" << i << ",0)  MAX";
		}
		else if (i == 9) {
			cout << "(I," << 18 - i << ")" << " (" << i << ",0)  MAX";
		}
		else {
			cout << "(I," << 18 - i << ")" << " (" << char('A' + i - 10) << ",0)  MAX";

		}

		if (mw > mb) {
			cout << " W" << mw << '\n';
		}
		else if (mw < mb) {
			cout << " B" << mb << '\n';
		}
		else {
			cout << " B" << mb << " W" << mw << '\n';
		}
	}
	for (int i = 17; i >= 0; i--) {   //좌상향 방향확인 오른쪽절반
		int w = 0, b = 0; // 줄의 돌갯수
		int sw = 0, sb = 0; // 연속된 돌갯수
		int mw = 0, mb = 0; //최대로 연속된 돌갯수
		int flag = 0;  //연속인지 확인
		for (int j = 17; j >= i; j--) {
			if (board[j - (17 - i)][j + 1] == 'B') {
				b++;
				if (flag == 1) {
					sb++;
				}
				else {
					flag = 1;
					sb = 1;
				}
				if (sb > mb) {
					mb = sb;
				}
			}
			else if (board[j - (17 - i)][j + 1] == 'W') {
				w++;
				if (flag == 2) {
					sw++;
				}
				else {
					flag = 2;
					sw = 1;
				}
				if (sw > mw) {
					mw = sw;
				}
			}
			else {
				flag = 0;
			}
		}

		if (0 <= i && i < 9) {
			cout << "(" << i << ",I)" << " (0," << char('A' + (18 - i - 10)) << ")  MAX";
		}
		else if (i == 9) {
			cout << "(" << 18 - i << ",I)" << " (0," << i << ")  MAX";
		}
		else {
			cout << "(" << char('A' + i - 10) << ",I)" << " (0," << 18 - i << ")  MAX";

		}

		if (mw > mb) {
			cout << " W" << mw << '\n';
		}
		else if (mw < mb) {
			cout << " B" << mb << '\n';
		}
		else {
			cout << " B" << mb << " W" << mw << '\n';
		}
	}
}

void take_back(int* flag) {  //무르기
	while (true) {
		string s;
		cout << "U:무르기 R:무르기 취소 E:무르기 종료\n>> ";
		cin >> s;
		if (s == "U") {
			if (S.size() == 0) {
				cout << "무르기를 할 수 없습니다.\n";
				continue;
			}
			int x = S.back().first;
			int y = S.back().second;
			S.pop_back();
			board[x][y] = '+';
			S2.push_back(make_pair(x, y));
			if (*flag == 1) { *flag = 0; B--; }
			else { *flag = 1; W--; }
		}
		else if (s == "R") {
			if (S2.size() == 0) {
				cout << "무르기 취소를 할 수 없습니다.\n";
				continue;
			}
			int x = S2.back().first;
			int y = S2.back().second;
			S2.pop_back();
			S.push_back(make_pair(x, y));
			if (*flag == 1) {
				board[x][y] = 'W';
				*flag = 0;
				W++;
			}
			else {
				board[x][y] = 'B';
				*flag = 1;
				B++;
			}
		}
		else if (s == "E")break;
		print_board();
	}
}



int main() {
	init();
	int flag = 0;// 차례 구분용
	while (true) {
		print_board();
		int N;
		cout << "0:종료 1:돌놓기 2:현재상황 3:무르기 4:불러오기 5:저장 \n>>";  //메뉴
		cin >> N;
		if (N == 0) {
			break;
		}
		else if (N == 1) {
			stone(&flag);
		}
		else if (N == 2) {
			get_board();
		}
		else if (N == 3) {
			take_back(&flag);
		}
		else if (N == 4) {
			ifstream in("save.txt");

			if (in.fail()) { cout << "File not found" << endl;  in.close(); continue; }
			B = 0;
			W = 0;
			for (int i = 0; i < 19; i++) {
				for (int j = 0; j < 19; j++) {
					board[i][j] = in.get();
					if (board[i][j] == 'B') {
						B++;
					}
					else if (board[i][j] == 'W') W++;
				}
			}
			flag = int(in.get()-'0');
			
			in.close();
		}
		else if (N == 5) {
			ofstream out("save.txt");
			for (int i = 0; i < 19; i++) {
				for (int j = 0; j < 19; j++) {
					out << board[i][j];

				}
			}
			out << flag;
			

			out.close();
		}

	}
}