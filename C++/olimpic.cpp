#include <iostream>

using namespace std;

typedef struct con {
	int g;
	int s;
	int b;
	int name;
	
}Con;

int myrank(Con con1, Con con2) {
	if (con1.g > con2.g) {
		return 1;
	}
	else if (con1.g == con2.g) {
		if (con1.s > con2.s) return 1;
		else if (con1.s == con2.s) {
			if (con1.b > con2.b) return 1;
			else if (con1.b == con2.b) return 0;
			else return -1;
		}
		else return -1;
	}
	else return -1;
	
}

int main() {
	int N, M;
	cin >> N >> M;
	int cnt = 1;
	Con* con = new Con[N];
	Con temp;
	for (int i = 0; i < N; i++) {
		cin >> con[i].name >> con[i].g >> con[i].s >> con[i].b;
		if (con[i].name == M) {
			temp = con[i];
		}
	}

	for (int i = 0; i < N; i++) {
		if (myrank(con[i], temp) > 0) {
			cnt++;
		}
	}
	printf("%d", cnt);
}