class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        # Empty string
       
        
         # Empty list
        # print()
        if not len(strs):
            return ""
        
        for i, raw_string in enumerate(strs):
            for char in raw_string: 
                encoded_string += str(ord(char)).zfill(3)

            #Add delimiter as ascii ends at 256 we use #### as the delimiter
            encoded_string += '####'
        return '####' + encoded_string


    def decode(self, s: str) -> List[str]:
        # Check for empty string
        # return list(s)
        if s == "":
            return list()

        s = s[4:-4]

        encoded_list = s.split('####')
        decoded_list = list()

        for encoded_string in encoded_list:
            decoded_word = ""
            for i in range(0, len(encoded_string), 3):
                decoded_char = chr(int(encoded_string[i : i+3]))
                decoded_word += decoded_char
            decoded_list.append(decoded_word)


        return decoded_list
