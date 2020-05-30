class Sol:
    def is_one_bit_char(self,nums):
        if nums[-2]==1:
            return False
        return True
if __name__ == '__main__':
    p=Sol()
    print(p.is_one_bit_char([1, 1, 1, 0]))

