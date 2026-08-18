class Solution:

    def encode(self, strs: List[str]) -> str:
        encoder = []
        for word in strs:
            encoder.append(str(len(word)))
            encoder.append("#")
            encoder.append(word)
        return "".join(encoder)

    def decode(self, s: str) -> List[str]:
        decoder = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoder.append(s[i:j])
            i = j
        return decoder

                
            
            
