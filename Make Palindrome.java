/*
You are given an array of strings arr of size n. You have to find out if it is possible to make a palindromic string by concatenating the strings in any order. Provided that all the strings given in the array are of equal length.

Example 1:

Input:
n = 4
arr = {"djfh", "gadt", "hfjd", "tdag"}
Output:
YES
Explanation:
You can make the string "djfhgadttdaghfjd", by concatenating the given strings which is a palindrome.
Example 2:

Input:
n = 3
arr = {"jhjdf", "sftas", "fgsdf"}
Output:
NO
Explanation:
You can't make a palindromic string with this strings.
Your Task:
You don't need to read input or print anything. Your task is to complete the function makePalindrome() which takes an integer n and an array of strings arr respectively and returns true or false.

Expected Time Complexity: O(n * len(arr[i]))
Expected Space Complexity: O(n * len(arr[i]))

Constraints:
1 <= n <= 104
0 <= |arr[i]| <= 104
The sum of n*|arr[i]| over all test cases won't exceed 106
*/
class Solution{
public:
    bool makePalindrome(int n,vector<string> &arr){
        // Code here
        map<string, int >m ; 
        
        for(auto it: arr )
        {
            string str = it ;
            reverse(begin(str), end(str) ) ;
            if(m[str]>0)
            {
                m[str]++ ;
            }
            else
            {
                m[it]++; 
            }
        }
        int f= 0 ;
        string s ="" ;
        for(auto it: m )
        {
            if(it.second%2==1)
            {f++;
            s = it.first ; 
            }
           
        }
        if(f==0)
        return 1 ;
        if(f==1)
        {
            string x =s ;
            reverse(begin(x), end(x)) ; 
            return x==s ;
        }
        return 0 ;
        
    }
};
