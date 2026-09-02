class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lista_final = []
        def popitem(lista):
            if not lista: 
                return
            lista_final.append(lista.pop(0)) 
        
        N = max(len(word1), len(word2)) - 1
        word1 = list(word1)
        word2 = list(word2)
        while word1 or word2:
            popitem(word1)
            popitem(word2)
        s = "".join(lista_final)
        return s

                




