#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <istream>
#include <ostream>
using namespace std;

class Node
{

public:
	string name;
	string company;
	string address;
	string zip;
	string phone;
	string email;
	string color;
	Node* left;
	Node* right;
	Node* parrent;
	Node(string name, string company, string address, string zip, string phone, string email)
	{
		this->name = name;
		this->company = company;
		this->address = address;
		this->zip = zip;
		this->phone = phone;
		this->email = email;
		left = nullptr;
		right = nullptr;
		parrent = nullptr;
	}

	void print_address()
	{
		cout << name << '\n';
		cout << "\tCompany: " << company << '\n';
		cout << "\tAddress: " << address << '\n';
		cout << "\tZipcode: " << zip << '\n';
		cout << "\tPhones: " << phone << '\n';
		cout << "\tEmail: " << email << '\n';

	}
};

class Address
{
public:
	Address() : root(nullptr) {};
	~Address() {};
	void AddNode(vector<string> value);
	bool SearchValue(string name);
	void RemoveNode(string name);
	void Display();
	bool trace(string name);
	void save(string f);
private:
	Node* root;

	void Inorder(Node* current)
	{
		if (current != nullptr)
		{
			Inorder(current->left);
			current->print_address();
			Inorder(current->right);
		}
	}
	Node* SearchMaxNode(Node* node)
	{
		if (node == NULL)
			return NULL;
		while (node->right != NULL)
		{
			node = node->right;
		}
		return node;
	}
	void save_all(ofstream& f, Node* node);
	Node* RemoveSeqence(Node* node, string _vaule);
};

Node* Address::RemoveSeqence(Node* node, string name)
{
	if (node == nullptr)
		return node;

	else if (node->name > name)
		node->left = RemoveSeqence(node->left, name);
	else if (node->name < name)
		node->right = RemoveSeqence(node->right, name);
	else
	{
		Node* ptr = node; //자식이없을떄
		if (node->right == nullptr && node->left == nullptr)
		{
			delete node;
			node = nullptr;
		} //자식이 하나일떄
		else if (node->right == nullptr)
		{
			node = node->left;
			node->parrent = ptr->parrent;
			delete ptr;
		}
		else if (node->left == nullptr)
		{
			node = node->right;
			node->parrent = ptr->parrent;
			delete ptr;
		} //자식이 두개일떄 :: 왼쪽 노드중 가장큰값 찾아 부모노드로 바꾸기
		else
		{
			ptr = SearchMaxNode(node->left);
			node->name = ptr->name;
			node->company = ptr->company;
			node->address = ptr->address;
			node->zip = ptr->zip;
			node->phone = ptr->phone;
			node->email = ptr->email;
			node->left = RemoveSeqence(node->left, ptr->name);
		}
	}
	return node;
}
void Address::RemoveNode(string name)
{
	Node* ptr = root;
	RemoveSeqence(ptr, name);
	
}

void Address::Display() { Inorder(root); }
void Address::save_all(ofstream& f, Node* node) {
	if (node != nullptr) {

		save_all(f, node->left);
		f << "\"" << node->name << "\",";
		f << "\"" << node->company << "\",";
		f << "\"" << node->address << "\",";
		f << "\"" << node->zip << "\",";
		f << "\"" << node->phone << "\",";
		f << "\"" << node->email << "\"" << endl;

		save_all(f, node->right);
	}
}
void Address::save(string f) {
	ofstream fout(f);

	fout << "name,";
	fout << "company,";
	fout << "address,";
	fout << "zip,";
	fout << "phone,";
	fout << "email" << endl;
	save_all(fout, root);
	fout.close();
}
bool Address::trace(string name) {
	Node* ptr = root;
	Node* tmpRoot = nullptr;
	while (ptr != nullptr)
	{
		cout << ptr->name << '\n';
		if (ptr->name == name)
		{
			ptr->print_address();
			return true;
		}
		else if (ptr->name > name)
			ptr = ptr->left;
		else
			ptr = ptr->right;

	}
	cout << name << " not found\n";
	return false;
}

bool Address::SearchValue(string name)
{
	Node* ptr = root;
	Node* tmpRoot = nullptr;
	while (ptr != nullptr)
	{
		if (ptr->name == name)
		{
			ptr->print_address();
			return true;
		}
		else if (ptr->name > name)
			ptr = ptr->left;
		else
			ptr = ptr->right;
	}
	cout << name << " not found\n";
	return false;
}
void left_Rotate(Node* node) {
	Node* y = node->right;
	node->right = y->left;
	y->left->parrent = node;
	y->parrent = node->parrent;
	y->left = node;
	node->parrent = y;
	if (y->parrent->left == node) {
		y->parrent->left = y;
	}
	else {
		y->parrent->right = y;
	}

}
void right_Rotate(Node* node) {
	Node* y = node->left;
	node->left = y->right;
	y->right->parrent = node;
	y->parrent = node->parrent;
	y->right = node;
	node->parrent = y;
	if (y->parrent->left == node) {
		y->parrent->left = y;
	}
	else {
		y->parrent->right = y;
	}

}
void insert_fix_up(Node* node) {

	while (node->parrent != nullptr && node->parrent->color == "red") {
		if (node->parrent->parrent->left == node->parrent) {
			Node* ynode = node->parrent->parrent->right;
			if (ynode != nullptr && ynode->color == "red") {
				node->parrent->color = "black";
				ynode->color == "black";
				node->parrent->parrent->color = "red";
				node = node->parrent->parrent;
			}
			else if (ynode == nullptr || ynode->color == "black") {
				if (node == node->parrent->right) {
					node = node->parrent;
					left_Rotate(node);
				}
				node->parrent->color = "black";
				node->parrent->parrent->color = "red";
				right_Rotate(node->parrent->parrent);
			}

		}
		else if (node->parrent->parrent->right == node->parrent) {
			Node* ynode = node->parrent->parrent->left;
			if (ynode != nullptr && ynode->color == "red") {
				node->parrent->color = "black";
				ynode->color == "black";
				node->parrent->parrent->color = "red";
				node = node->parrent->parrent;
			}
			else if (ynode == nullptr || ynode->color == "black") {
				if (node == node->parrent->left) {
					node = node->parrent;
					right_Rotate(node);
				}
				node->parrent->color = "black";
				node->parrent->parrent->color = "red";
				left_Rotate(node->parrent->parrent);
			}

		}
	}
	if (node->parrent == nullptr)
		node->color = "black";
}
void Address::AddNode(vector<string> value)
{
	string email = value.back();
	value.pop_back();
	string phone = value.back();
	value.pop_back();
	string zip = value.back();
	value.pop_back();
	string address = value.back();
	value.pop_back();
	string company = value.back();
	value.pop_back();
	string name = value.back();
	value.pop_back();
	string color = "red";
	Node* node = new Node(name, company, address, zip, phone, email);
	Node* tmpRoot = nullptr;

	if (root == nullptr)
		root = node;
	else
	{
		Node* ptr = root;
		while (ptr != nullptr)
		{
			tmpRoot = ptr;
			if (node->name < ptr->name)
			{
				ptr = ptr->left;
			}
			else
			{
				ptr = ptr->right;
			}
		} //넣을 위치에 대입
		if (node->name < tmpRoot->name)
		{
			tmpRoot->left = node;
			node->parrent = tmpRoot;
		}
		else
		{
			tmpRoot->right = node;
			node->parrent = tmpRoot;
		}
	}
	insert_fix_up(node);
}

vector<string> csv_read_row(istream& in, char delimiter);
vector<string> tokenize_operator(const string& data);

int main(int argc, char* argv[])

{

	//ifstream은 파일을 읽게 해주는 함수로써 ifstream (파일명 or 경로)
	Address root = Address();

	while (true) {
		cout << "$ ";
		string temp;
		getline(cin, temp);
		if (temp == "") {
			continue;
		}
		stringstream commands;
		commands.str(temp);
		string token;
		vector<string> command;
		while (commands >> token) {
			command.push_back(token);
		}
		if (command[0] == "list") {


			if (command.size() != 1) {
				cout << "command error\n";

			}
			else {
				root.Display();
			}
		}
		else if (command[0] == "read") {
			if (command.size() != 2) {
				cout << "command error\n";

			}
			else {
				ifstream in(command[1]);
				vector<string> row = csv_read_row(in, ',');
				if (in.fail()) return (cout << "File not found" << endl) && 0;
				while (in.good())
				{
					vector<string> row = csv_read_row(in, ',');
					if (row.size() != 6) {
						cout << "file error\n";
						return 0;
					}
					root.AddNode(row);
				}
				in.close();
			}

		}
		else if (command[0] == "exit") {
			if (command.size() != 1) {
				cout << "command error\n";

			}
			else {
				break;
			}

		}
		else if (command[0] == "delete") {
			if (command.size() != 2) {
				cout << "command error\n";
			}
			else {
				root.RemoveNode(command[1]);
			}
		}
		else if (command[0] == "find") {


			if (command.size() != 2) {
				cout << "command error\n";

			}
			else {
				root.SearchValue(command[1]);
			}

		}
		else if (command[0] == "trace") {
			if (command.size() != 2) {
				cout << "command error\n";

			}
			else {
				root.trace(command[1]);
			}
		}
		else if (command[0] == "save") {
			if (command.size() != 2) {
				cout << "command error\n";

			}
			else {
				root.save(command[1]);
			}
		}

		commands.clear();

	}


	return 0;
}



vector<string> csv_read_row(istream& in, char delimiter)
{
	stringstream ss;
	bool inquotes = false;
	vector<string> row;//relying on RVO
	while (in.good())
	{
		char c = in.get();
		if (!inquotes && c == '"') //beginquotechar
		{
			inquotes = true;
		}
		else if (inquotes && c == '"') //quotechar
		{
			if (in.peek() == '"')//2 consecutive quotes resolve to 1
			{
				ss << (char)in.get();
			}
			else //endquotechar
			{
				inquotes = false;
			}
		}
		else if (!inquotes && c == delimiter) //end of field
		{
			row.push_back(ss.str());
			ss.str("");
		}
		else if (!inquotes && (c == '\r' || c == '\n'))
		{
			if (in.peek() == '\n') { in.get(); }
			row.push_back(ss.str());
			return row;
		}
		else
		{
			ss << c;
		}
	}
	row.push_back(ss.str());

	return row;
}