# -*- coding: utf8 -*-




class Solution(object):

    def mergeSort(self,arr):
        """
        归并排序
        :param arr:
        :return:
        """
        if len(arr) < 2:return arr
        mid = len(arr) // 2
        left_arr = self.mergeSort(arr[:mid])
        right_arr = self.mergeSort(arr[mid:])
        return self.merge(left_arr,right_arr)
    def merge(self,left_arr,right_arr):
        """
        合并分治结果
        :param left_arr:
        :param right_arr:
        :return:
        """
        result = []
        while 1:
            if left_arr and right_arr:
                if left_arr[0] <= right_arr[0]:
                    min,left_arr = left_arr[0],left_arr[1:]
                else:
                    min,right_arr = right_arr[0],right_arr[1:]
            elif left_arr and not right_arr:
                min,left_arr = left_arr[0],left_arr[1:]
            elif right_arr and not left_arr:
                min, right_arr = right_arr[0], right_arr[1:]
            else:break
            result.append(min)
        return result

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        x = float(x)
        res = 1
        for i in range(n):
            res *= x
        if n >= 0:
            return res
        else:
            return 1/res

    def myPow2(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
        return self.divide(x,n)   

    def divide(self,x,n):
        """
        分治
        :param x:
        :param n:
        :return:
        """
        if n == 1:return x
        if n == 0:return 1
        sub_res = self.divide(x,n//2)
        if n % 2 == 1:
            return sub_res * sub_res * x
        else:
            return sub_res * sub_res










if __name__ == '__main__':
    slt = Solution()
    arr = [6,3,4,1,5,2,2]
    print(slt.mergeSort(arr))
