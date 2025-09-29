public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        var dictWord = new Dictionary<string, List<string>>();

        foreach (string w in strs)
        {
            var chars = w.ToCharArray();
            Array.Sort(chars);
            var sortedWord = new string(chars);

            if (dictWord.ContainsKey(sortedWord))
            {
                dictWord[sortedWord].Add(w);
            }
            else
            {
                dictWord[sortedWord] = new List<string> { w };
            }
        }    

        var result = new IList<IList<string>>();
        foreach (var value in dictWord.Values)
        {
            result.Add(value);
        }

        return result;
    }
}