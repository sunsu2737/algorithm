#include<iostream>
using namespace std;

typedef struct lol {          // 챔피언정보를 저장할 구조체
	string name;
	int hp;
	int mp;
	int range;
	int speed;
	string position;
	struct lol* next;
}LOL;


LOL head;               //연결리스트의 헤드
LOL tail;               //연결리스트의 테일
bool isEmpty() {                // 연결리스트가 비었는지검사
	if (head.next == NULL) {
		return true;
	}
	return false;
}


LOL* makeNew() {                //새로운 챔피언 정보를 입력 받아 구조체를 생성하여 반환
	string name;
	int hp;
	int mp;
	int range;
	int speed;
	string position;
	cout << "name: "; cin >> name;
	cout << "HP: "; cin >> hp;
	cout << "MP: "; cin >> mp;
	cout << "Range: "; cin >> range;
	cout << "Speed: "; cin >> speed;
	cout << "Position: "; cin >> position;
	LOL* l = new LOL;
	l->hp = hp;
	l->mp = mp;
	l->name = name;
	l->position = position;
	l->range = range;
	l->speed = speed;
	l->next = NULL;
	return l;
}

void Insert_SL(LOL* new_node) {         //정렬된 상태로 새로운 구조체 삽입
	if (isEmpty()) {                    // 연결리스트가 비었으면 첫번째에 삽입
		head.next = new_node;
		tail.next = new_node;
		new_node->next = new_node;
		return;
	}
	else {                          //연결리스트가 비어있지 않으면
		LOL* p = head.next;         //p에 첫번째 구조체 
		LOL* q = p->next;           //q에 다음 구조체

		if (p->hp < new_node->hp) {             //새로운 노드의 체력이 가장크면 맨앞에 삽입
			head.next = new_node;
			new_node->next = tail.next->next;
			tail.next->next = new_node;
			return;
		}

		while (q != head.next) {
			if (q->hp < new_node->hp) {             //q와 새로운 노드를 비교하여 체력이 더크면 q앞에 새로운 노드를 삽입
				p->next = new_node;
				new_node->next = q;
				return;
			}
			else {
				p = q;
				q = q->next;
			}
		}
		p->next = new_node;             //새로운 노드의 체력이 가장낮으면 맨뒤에 삽입
		new_node->next = head.next;
		tail.next = new_node;
		return;
	}
}

void PrintNode(LOL* p) {             //노드를 인수로 받아 정보를 출력
	cout << "name: " << p->name << "\n";
	cout << "HP: " << p->hp << "\n";
	cout << "MP: " << p->mp << "\n";
	cout << "Range: " << p->range << "\n";
	cout << "Speed: " << p->speed << "\n";
	cout << "Position: " << p->position << "\n";
	cout << '\n';
}

void PrintALL_SL() {
	if (isEmpty()) {            //연결리스트에 노드가 없으면 비었다고 출력
		cout << "Empty!!\n";
	}
	else {
		LOL* p = head.next;
		do {                                    //연결리스트를 순회하며 정보들을 출력
			PrintNode(p);
			p = p->next;
		} while (p != head.next);
	}
}
void Array2LinkedList(LOL nodes[], int size) {         // 챔피언이 저장된 배열을 돌면서 연결리스트에 저장
	for (int i = 0; i < size; i++) {
		LOL* node = new LOL;					//메모리할당을해서 배열의 챔피언정보를 저장
		node->name = nodes[i].name;
		node->hp = nodes[i].hp;
		node->mp = nodes[i].mp;
		node->range = nodes[i].range;
		node->speed = nodes[i].speed;
		node->position = nodes[i].position;

		Insert_SL(node);
	}
}

LOL* Search_SL(string name) {
	if (isEmpty()) {
		cout << "Empty!!\n";              // 연결리스트가 비었으면 비었다고 출력
	}
	LOL* p = head.next;       //p에 첫번째노드 저장
	do {                     //연결리스트를 순회하며 이름이 같은 노드를 찾아서 반환
		if (p->name == name) {
			return p;
		}
		else {
			p = p->next;
		}
	} while (p != head.next);
	return NULL;    //찾는 챔피언이없으면 NULL 리턴
}

void Delete_SL(string name) {
	if (isEmpty()) {                    // 연결리스트가 비었으면 비었다고 출력
		cout << "Empty!!\n";
		return;
	}
	else {                          //연결리스트가 비어있지 않으면
		LOL* p = head.next;         //p에 첫번째 구조체 
		LOL* q = p->next;           //q에 다음 구조체

		if (p->name == name) {             //첫 번째노드가 찾는 노드이면 삭제
			head.next = p->next;

			tail.next->next = p->next;
			delete p;
			cout << "Delete Complete!!\n";
			return;
		}

		while (q != tail.next) {
			if (q->name == name) {             //찾는 노드가 첫번째 노드가아닐때
				p->next = q->next;
				delete q;
				cout << "Delete Complete!!\n";
				return;
			}
			else {
				p = q;
				q = q->next;
			}
		}
		if (q->name == name) {                  //찾는 노드가 마지막 노드일때
			p->next = q->next;
			tail.next = p;

			delete q;
			cout << "Delete Complete!!\n";
			return;
		}
	}
}

void DeleteAll_SL() {      // 연결리스트를 순회하며 모든 노드를 삭제
	LOL* p = head.next;
	LOL* q = p->next;

	while (p != head.next) {            
		delete p;
		p = q;
		q = q->next;
	}
	head.next = NULL;               // 완료후에 헤드와 테일을 NULL을 가르키도록 변경
	tail.next = NULL;
}

int main() {
	// 챔피언 데이터 20개 넣어 드렸습니다. 일일이 타이핑하느라 힘들었어요 ㅜㅜ
	LOL data[20];
	data[0] = { "Teemo",528,267,500,330,"top" };
	data[1] = { "Vayne",515,231,550,330,"ad" };
	data[2] = { "Blitzcrank",582,267,125,325,"spt" };
	data[3] = { "Lee Sin",575,200,125,345,"jg" };
	data[4] = { "LeBlanc",528,334,525,335,"mid" };
	data[5] = { "Yummi",480,400,500,330,"spt" };
	data[6] = { "Twisted Fate",534,333,525,335,"mid" };
	data[7] = { "Gragas",600,400,125,330,"jg" };
	data[8] = { "Darius",582,263,175,340,"top" };
	data[9] = { "Dr. Mundo",582,0,125,345,"top" };

	data[10] = { "Gnar",510,100,575,335,"top" };
	data[11] = { "Bard",575,350,500,330,"spt" };
	data[12] = { "Vladimir",537,0,450,330,"mid" };
	data[13] = { "Ivern",585,450,475,330,"jg" };
	data[14] = { "Zac",614,0,175,340,"jg" };
	data[15] = { "Jhin",556,300,550,330,"ad" };
	data[16] = { "Zoe",560,425,525,340,"mid" };
	data[17] = { "Kha Zix",572,327,125,350,"jg" };
	data[18] = { "Karthus",528,467,450,335,"jg" };
	data[19] = { "Heimerdinger",488,385,550,340,"ad" };
	Array2LinkedList(data, 20);

	while (true) {
		int N;
		cout << "0.exit 1.Seach_SL 2.Insert_SL 3.Delete_SL 4.DeleteAll_SL 5.PrintAll_SL 6.FindMaxHp_SL \n";
		cout << ">> ";
		cin >> N;

		if (N == 1) {
			cout << "Name: ";
			string name;
			cin >> name;
			LOL* p = Search_SL(name);     // 챔피언을 찾아서 p에 저장
			if (p == NULL) {
				cout << "Not Found\n";  //찾는 챔피언이 없으면 없다고 출력
			}
			else {
				PrintNode(p);
			}
		}
		else if (N == 2) {

			Insert_SL(makeNew());
		}
		else if (N == 3) {
			cout << "Name: ";
			string name;
			cin >> name;
			Delete_SL(name);
		}
		else if (N == 4) {
			DeleteAll_SL();
			cout << "DeleteAll complete!!\n";
		}
		else if (N == 5) {
			PrintALL_SL();
		}
		else if (N == 6) {
			PrintNode(head.next);                   //가장 첫번째노드가 가장 hp가 높은 챔피언 이므로 첫번째 노드 출력
		}
		else if (N == 0) {
			return 0;
		}
	}
}