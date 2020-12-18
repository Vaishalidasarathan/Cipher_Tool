import unittest
import CipherTool as tool

class test_Cipher(unittest.TestCase):
    def test_ceasrerEncy(self):
        
        result = tool.Encryp_ceaser("thequickbrownfoxjumpsoverthelazydog", -3)
        self.assertEqual(result, "qebnrfzhyoltkclugrjmplsboqebixwvald")

    def test_ceasrerDecry(self):
        
        result = tool.Decryp_ceaser("qebnrfzhyoltkclugrjmplsboqebixwvald", -3)
        self.assertEqual(result, "thequickbrownfoxjumpsoverthelazydog")
    
    def test_affEncy(self):
        
        result = tool.Encryp_Affine("affinecipher", 5,8)
        self.assertEqual(result, "ihhwvcswfrcp")

    def test_affDecry(self):
        
        result = tool.Decryp_Affine("ihhwvcswfrcp", 5,8)
        self.assertEqual(result, "affinecipher")

    def test_keyEncy(self):
        
        result = tool.Encryp_Keyword("knowledgeispower","kryptos")
        self.assertEqual(result, "dghvetpstbmihvtl")

    def test_keyDecry(self):
        
        result = tool.Decryp_Keyword("dghvetpstbmihvtl", "kryptos")
        self.assertEqual(result, "knowledgeispower")

    def test_rot13Ency(self):
        
        result = tool.Encryp_Rot_13("whydidthechickencrosstheroad")
        self.assertEqual(result, "julqvqgurpuvpxrapebffgurebnq")

    def test_rot13Decry(self):
        
        result = tool.Decryp_Rot_13("julqvqgurpuvpxrapebffgurebnq")
        self.assertEqual(result, "whydidthechickencrosstheroad")
    
    def test_rot13Ency(self):
        
        result = tool.Encryp_Vigenere("attackatdawn","lemon")
        self.assertEqual(result, "lxfopvefrnhr")

    def test_rot13Decry(self):
        
        result = tool.Decryp_Vigenere("lxfopvefrnhr","lemon")
        self.assertEqual(result, "attackatdawn")
    

if __name__ == '__main__':
    unittest.main()
