
public class StackUtility {
	static String alphabets = "abcdefghijklmnopqrstuvwxyz";
	
	public static String operate(MyStack s1, MyStack s2) throws Exception {
		
		// 1 alphabet = 2 number --> total alphabet = s1/2
		int pairOfWord = s1.size()/2;
		
		String word = "";
		
		// loop for finding alphabet
		for (int pair = 0; pair < pairOfWord; pair++) {
			// pull first number on top + pop it out
			int pair1 = s1.top();
			s1.pop();
			
			// pull second number on top + pop it out
			int pair2 = s1.top();
			s1.pop();
			
			//pull the one that determines operations
			int symbol = s2.top();
			s2.pop();
			
			// operations
			if (symbol < 0) {
				word = alphabets.charAt(pair1 - pair2) + word;
			} else if (symbol >= 0) {
				word= alphabets.charAt(pair1 + pair2) + word;
			}
			
		} return word;
		
	}
}

