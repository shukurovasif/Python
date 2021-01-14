import unittest
from src.caesar_cipher.caesar_cipher import Caesar

class CipherTest(unittest.TestCase):

    def setUp(self):
        self.caesar = Caesar(1, 'abc')
    
    def test_encrypt(self):
        encrypted = self.caesar.encrypt()
        self.assertEqual(encrypted, 'bcd')

    def test_decrypt(self):
        self.caesar.encrypt()
        decrypted = self.caesar.decrypt()
        self.assertEqual(decrypted, 'abc')
        
        
