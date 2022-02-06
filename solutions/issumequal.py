class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        firstNum, secondNum, targetNum = "", "", ""

	     for char in firstWord:
		    firstNum += str(ord(char) - ord('a'))

	    for char in secondWord:
		    secondNum += str(ord(char) - ord('a'))

	    for char in targetWord:
		    targetNum += str(ord(char) - ord('a'))

	    return int(firstNum) + int(secondNum) == int(targetNum)

        
