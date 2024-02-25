class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def parenth_insert(list_parenth: List[str] = []) -> list[str]:

            if list_parenth == []:
                return ["()"]
            
            new_list = set()
            
            for valid_parenth in list_parenth:
                for index in range(len(valid_parenth)):
                    new_parenth = valid_parenth[0:index] + "()" + valid_parenth[index:len(valid_parenth)]
                    
                    new_list.add(new_parenth)
                      

            return list(new_list)

        first_list = parenth_insert([])
        second_list = parenth_insert(first_list)

        p_list = []
        for i in range(0, n):
            p_list = parenth_insert(p_list)

        return p_list