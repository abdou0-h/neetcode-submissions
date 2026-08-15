class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()  # 1. تقطيع النص إلى كلمات
        
        # إذا كان عدد الكلمات لا يساوي عدد حروف الـ pattern
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            # فحص التطابق من الحرف للكلمة
            if char in char_to_word and char_to_word[char] != word:
                return False
            # فحص التطابق العكسي (من الكلمة للحرف)
            if word in word_to_char and word_to_char[word] != char:
                return False

            char_to_word[char] = word
            word_to_char[word] = char

        return True


            

