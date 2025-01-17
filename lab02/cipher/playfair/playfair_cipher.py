class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key_set = set(key)
        key = key.replace("J", "I")  # Chuyển "J" thành "I" trong khóa
        key = key.upper()
        key_set = key_set - set(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = [
            letter for letter in alphabet if letter not in list(key_set)
        ]
        matrix = []
        for letter in remaining_letters:
            matrix.append(letter)
        if len(matrix) == 25:
            playfair_matrix = [matrix[i : i + 5] for i in range(0, len(matrix), 5)]
            return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace(
            "J", "I"
        )  # Chuyển "J" thành "I" trong văn bản đầu vào
        plain_text = plain_text.upper()
        encrypted_text = ""
        for i in range(0, len(plain_text), 2):
            pair = plain_text[i : i + 2]
            if len(pair) == 1:  # Xử lý nếu số lượng ký tự lẻ
                pair += "X"
            rowl, coll = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if rowl == row2:
                encrypted_text += (
                    matrix[rowl][(coll + 1) % 5] + matrix[row2][(col2 + 1) % 5]
                )
            elif coll == col2:
                encrypted_text += (
                    matrix[(rowl + 1) % 5][coll] + matrix[(row2 + 1) % 5][col2]
                )
            else:
                encrypted_text += matrix[rowl][col2] + matrix[row2][col2]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i : i + 2]
            rowl, coll = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if rowl == row2:
                decrypted_text += (
                    matrix[rowl][(coll - 1) % 5] + matrix[row2][(col2 - 1) % 5]
                )
            elif coll == col2:
                decrypted_text += (
                    matrix[(rowl - 1) % 5][coll] + matrix[(row2 - 1) % 5][col2]
                )
            else:
                decrypted_text += matrix[rowl][col2] + matrix[row2][col2]
        return decrypted_text
