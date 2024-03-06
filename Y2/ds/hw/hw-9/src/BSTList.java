import java.util.ArrayList;

public class BSTList {
	BSTNodeList root;
	int size;
	
	public BSTList() {
		root = null;
		size = 0;
	}
	
	public BSTList(BSTNodeList root, int size) {
		this.root = root;
		this.size = size;
	}
	
	public boolean isEmpty() {
		return size == 0;
	}

	public void makeEmpty() {
		root = null;
		size = 0;
	}
	
	public BSTNodeList find(Comparable v) { 
		
		// this function can be implemented from the one Ajarn gave in class 
		// just need some modification !
		
		BSTNodeList temp = root;
		
		// have temp, temp[0][0] != v[0][0]
		while (temp != null && temp.dataList.get(0).first != ((Pairdata) v).first) {
			
			if (((Pairdata) v).first - temp.dataList.get(0).first < 0) {
				temp = temp.left;
			} else {
				temp = temp.right;
			}
		}
		
		if (temp == null) // not found
			return null;
		
		// have temp, temp[0][0] == v[0]v[0]
		else if (temp != null && temp.dataList.get(0).first == ((Pairdata) v).first) {
			if (!temp.dataList.contains(v)) {
				return null;
			}
		}
		return temp;
		
	}
	
	public BSTNodeList insert(Comparable v) {
		
		// this one too ! but has extra pointer for parent
		BSTNodeList parent = null;
		BSTNodeList temp = root;
		
		// parent uses here 
		while (temp != null && temp.dataList.get(0).first != ((Pairdata) v).first) {
			if (((Pairdata) v).first - temp.dataList.get(0).first < 0) {
				parent = temp;
				temp = temp.left;
			} else {
				parent = temp;
				temp = temp.right;
			}
		}

		// when the value v has no match with other leaves on tree
		if (temp == null) {
			BSTNodeList n = new BSTNodeList(new ArrayList<Pairdata>(), temp, temp, parent);
			n.dataList.add((Pairdata) v);
			if (parent == null) {
				root = n;
			} else if (((Pairdata) v).first - parent.dataList.get(0).first < 0) {
				parent.left = n;
			} else {
				parent.right = n;
			}
			size++;
			return n;
			
			
		} else {
			if (!temp.dataList.contains(v)) {
				temp.dataList.add((Pairdata) v);
				
				// This bad boy (this.size) is the number of Pairdata in every node not number of Node 
				size++;
			}
			return temp;

		}


	}
	
	public BSTNodeList findMin(BSTNodeList n) {
		BSTNodeList temp = n;
		if (temp == null)
			return null;
		while (temp.left != null) {
			temp = temp.left;
		}
		return temp;
	}

	

	
}



// here is another solution (which looks a bit more friendly)
// try to minimize writing a lot of condition in while 
// because it will make you confuse :<
// try to write in if so that it will break after condition is met 

// public BSTNodeList find(Comparable v) {
//	BSTNodeList temp = root;
//	
//	// loop until the pointer is at the end of the leave
//	while (temp != null) {
//		if (temp.dataList.get(0).first == ((Pairdata) v).first) {
//			break;
//		}
//		
//		if (((Pairdata) v).first - temp.dataList.get(0).first < 0) {
//			temp = temp.left;
//		} else {
//			temp = temp.right;
//		}
//	}
//	
//	// loop until the pointer is at the end of the leave
//	if (temp == null) {
//		return null;
//	}
//	
//	// check in case the other data is not corresponds
//	// to what it suppose to be 
//	// ex: in brach 7, some data has 10 in the first index
//	if (!temp.dataList.contains(v)) {
//		return null;
//	}
//	return temp;
//}
//

