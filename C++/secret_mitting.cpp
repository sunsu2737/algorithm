#include <iostream>
#include <map>
#include <cstring>
#include <queue>

using namespace std;

int T, N, M, K;
map<int, vector<pair<int,int> > > graph;
map<int,int[5000]>abc;
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> dist;

bool operator<(pair<int, int> a, pair<int, int> b)
{
	return a.first < b.first;
}

void make_map(int KN[])
{
	for (int j=0;j<K;j++)
	{
		int i=KN[j];
		dist.push(make_pair(0, i));

		while (!dist.empty())
		{
			pair<int, int> current = dist.top();
			dist.pop();
			for(auto j:graph[current.second]){
				int total=current.first+j.second;
				if(total<=abc[i][j.first]){
					abc[i][j.first]=total;
					dist.push(make_pair(total,j.first));
				}
			}
		}
	}
}

int main()
{
	cin >> T;
	
	for (int t = 0; t < T; t++)
	{
		int KN[100]={0,};
		cin >> N>> M;
		
		for (int i = 1; i <= M; i++)
		{
			int t1, t2, t3;
			cin >> t1 >> t2 >> t3;
			graph[t1].push_back(make_pair(t2,t3));
	
			graph[t2].push_back(make_pair(t1,t3));
		}
		cin >> K;
		for (int i = 0; i < K; i++)
		{
			cin >> KN[i];
		}
		for(int i=0;i<K;i++){
			int k=KN[i];
			for(int j=1;j<=N;j++){
				abc[k][j]=999999;
				
			}
			abc[k][k]=0;
			
		}
		
		make_map(KN);
		
		int min = 99999999;
		int answer;
		for (int j = 1; j <= N; j++)
		{
			int sum = 0;
			for (auto i : KN)
			{
				sum += abc[i][j];
			}
			if (min > sum)
			{
				min = sum;
				answer=j;
			}
		}
		cout << answer<<'\n';
		graph.clear();
		abc.clear();
		
		
	}
}