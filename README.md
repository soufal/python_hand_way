## NOTE:    
### 继承：    
#### 继承和组合
**继承的大多数用法可以简化或用组合替换，并且应该不惜一切代价避免多重继承。**  
子类和父类交互的三种方式：
* 对子类的行为意味着对父类的行为。
* 子类上的操作覆盖父类上的操作。
* 对子类的操作改变了对父类的操作      

### 多重继承：        

#### C3算法：    
C3算法的本质就是Merge，不断地把mro()函数返回的序列进行Merge，规则如下：

1. 如果第一个序列的第一个元素，是后续序列的第一个元素，或者不再后续序列中再次出现，则将这个元素合并到最终的方法解析顺序序列中，并从当前操作的全部序列中删除。

2. 如果不符合，则跳过此元素，查找下一个列表的第一个元素，重复1的判断规则    

#### super（）：    
* mro())：生成method resolution order列表    
* 当代码执行到super实例化后，先去找同级父类，若没有其余父类，再执行自身父类，再往下走，
* 简洁点的三个原则就是：子类在父类前，所有类不重复调用，从左到右