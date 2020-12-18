import unittest
import CipherTool as tool

class test_Cipher(unittest.TestCase):
    def test_ceasrerEncy(self):
        
        result = tool.Encryp_ceaser_t("thequickbrownfoxjumpsoverthelazydog", -3)
        self.assertEqual(result, "qebnrfzhyoltkclugrjmplsboqebixwvald")

    def test_ceasrerDecry(self):
        
        result = tool.Decryp_ceaser_t("qebnrfzhyoltkclugrjmplsboqebixwvald", -3)
        self.assertEqual(result, "thequickbrownfoxjumpsoverthelazydog")
    
    def test_affEncy(self):
        
        result = tool.Encryp_Affine_t("affinecipher", 5,8)
        self.assertEqual(result, "ihhwvcswfrcp")

    def test_affDecry(self):
        
        result = tool.Decryp_Affine_t("ihhwvcswfrcp", 5,8)
        self.assertEqual(result, "affinecipher")

    def test_keyEncy(self):
        
        result = tool.Encryp_Keyword_t("knowledgeispower","kryptos")
        self.assertEqual(result, "dghvetpstbmihvtl")

    def test_keyDecry(self):
        
        result = tool.Decryp_Keyword_t("dghvetpstbmihvtl", "kryptos")
        self.assertEqual(result, "knowledgeispower")

    def test_rot13Ency(self):
        
        result = tool.Encryp_Rot_13_t("whydidthechickencrosstheroad")
        self.assertEqual(result, "julqvqgurpuvpxrapebffgurebnq")

    def test_rot13Decry(self):
        
        result = tool.Decryp_Rot_13_t("julqvqgurpuvpxrapebffgurebnq")
        self.assertEqual(result, "whydidthechickencrosstheroad")
    
    def test_VigEncy(self):
        
        result = tool.Encryp_Vigenere_t("attackatdawn","lemon")
        self.assertEqual(result, "lxfopvefrnhr")

    def test_vigDecry(self):
        
        result = tool.Decryp_Vigenere_t("lxfopvefrnhr","lemon")
        self.assertEqual(result, "attackatdawn")
    
    # def test_bifEncy(self):
        
    #     result = tool.Encryp_Bifid("defendtheeastwallofthecastle",5)
    #     self.assertEqual(result, "ffyhmkhycpliashadtrlhcchlblr")

    # def test_bifDecry(self):
        
    #     result = tool.Decryp_Bifid("ffyhmkhycpliashadtrlhcchlblr",5)
    #     self.assertEqual(result, "defendtheeastwallofthecastle")    
    

if __name__ == '__main__':
    unittest.main()
