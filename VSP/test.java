import java.util.HashMap;
int[] visit = new int[n+1];
HashMap<int,int[]> map1 = new HashMap<int,int[]>();//HashMap생성



check[1]=1;
dfs(1,map1);

1,[0,0,1,0,0,0,0]






public boolean dfs(int node, HashMap<int,int[]> graph){
    

    if (node==5){
        return true
    }
    for (int i=1; i<=n; i++){
        if (check[i]==0){
            if (graph[node][i]==1){
                check[i]=1;
                return dfs(i,graph);
            }
            
        }
    }
    return False
    
}