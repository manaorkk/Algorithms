class SegTree:
    '''
    自底向上策略
    利用了二进制的特性和树结构的特性
    包含方法：
    1.单点设置 （优点：避免递归 缺点：优化方面不够灵活）
    2.区间查询

    区间更新应该使用自顶向下的策略，并可以使用懒惰传播优化方法
    '''
    def __init__(self, n,l,e,op):
        self.e=e
        self.op=op
        self.length=1<<(n-1).bit_length()
        self.tree=[self.e]*self.length+l+[self.e]*self.length
        for i in range(self.length-1,0,-1):
            self.tree[i]=op(self.tree[2*i],self.tree[2*i+1])
    
    def set(self, value, index):
        index+=self.length
        self.tree[index]=value
        index>>=1
        while index:
            self.tree[index]=self.op(self.tree[index*2],self.tree[index*2+1])
            index>>=1
    
    def get(self, left, right):
        left+=self.length
        right+=self.length
        ans=0
        while left<right:
            if left&1:
                ans=self.op(ans,self.tree[left])
                left+=1
            if right&1:
                ans=self.op(ans,self.tree[right-1])
                right-=1
            left>>=1
            right>>=1
        return ans
        

def m(a,b):
    return max(a,b)


N, D = map(int, input().split())
A = list(map(int, input().split()))
mx=max(A)+1
st=SegTree(mx,[],0,m)

for i, num in enumerate(A):
    l = max(0, num-D)
    r = min(mx, num+D+1)
    nmax = st.get(l,r)
    st.set(nmax+1,num)

print(st.tree[1])
