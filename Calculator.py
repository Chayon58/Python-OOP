class My_Calculator:
    def product(self, *nums):
        pro = 1
        #print(nums)
        for x in nums:
            pro = pro *x
        print(pro)
#=============================================================================
c1 = My_Calculator()
c1.product(4)
c1.product(4,5)
c1.product(4,5,6,7,8)



    