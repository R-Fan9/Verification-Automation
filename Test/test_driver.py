from cmath import nan
import Checker
import pytest as pt
import pandas as pd

KEY = 'PF'
COL_1 = 'A'
COL_2 = 'B'



class TestChecker:

    def __form_df(self, data):
        return pd.DataFrame(data, columns=[KEY, COL_1, COL_2])

    def __eq_data(self, d_tru, d_rel):
        return d_tru == d_rel

    def setup_method(self, method):
        self.checker = Checker

        self.data1 = [[]]

        self.data2 = [
            ['a', 401, nan],
            ['c', 238, 238],
            ['d', nan, 1],
            ['e', nan, nan],
            ['f', 523, 645]
        ]
        self.data2_fst = [
            ['a', 401],
            ['c', 238],
            ['d', nan],
            ['e', nan],
            ['f', 523]
        ]
        self.data2_snd = [
            ['e', nan],
            ['d', 1],
            ['c', 238],
            ['f', 645],
            ['a', nan],
        ]

        self.data3 = [
            ['a', 32, 452],
            ['b', 263, 253],
            ['c', 101, 101],
            ['d', abs(-3), 3]    
        ]
        self.data3_fst = [
            ['a', 32],
            ['b', 263],
            ['c', 101],
            ['d', -3]    
        ]
        self.data3_snd = [
            ['c', 101],
            ['a', 452],
            ['d', 3],   
            ['b', 253], 
        ]

        self.data4 = [
            ['a', 31, 31],
            ['b', 36, 36],
            ['c', 8754, 8754]   
        ]
        self.data4_fst = [
            ['a', 31],
            ['b', 36],
            ['c', 8754]   
        ]
        self.data4_snd = [
            ['b', 36, 36],
            ['c', 8754, 8754],
            ['a', 31, 31],
        ]

    def teardown_method(self, method):
        self.checker = None
        self.data1 = None
        self.data2 = None
        self.data2_fst = None
        self.data2_snd = None
        self.data3 = None
        self.data3_fst = None
        self.data3_snd = None
        self.data4 = None
        self.data2_fst = None
        self.data2_snd = None

    def test_get_unmatches(self):
        # case1: empty data
        d1_tru = [[]]
        # case2: rows with value and N/A pair
        d2_tru = [['c', 238, 238]]
        # case3: rows with different values
        d3_tru = [['c', 101, 101],['d', 3, 3]]
        # case4: rows with matching values
        d4_tru = [['a', 31, 31],['b', 36, 36],['c', 8754, 8754]]

        d1_rel = self.checker.get_unmatches(self.__form_df(self.data1), COL_1, COL_2).values.tolist()
        d2_rel = self.checker.get_unmatches(self.__form_df(self.data2), COL_1, COL_2).values.tolist()
        d3_rel = self.checker.get_unmatches(self.__form_df(self.data3), COL_1, COL_2).values.tolist()
        d4_rel = self.checker.get_unmatches(self.__form_df(self.data4), COL_1, COL_2).values.tolist()

        assert self.__eq_data(d1_tru, d1_rel)
        assert self.__eq_data(d2_tru, d2_rel)
        assert self.__eq_data(d3_tru, d3_rel)
        assert self.__eq_data(d4_tru, d4_rel)

    def test_join_df(self):
        # case1: two empty data
        # case2: one empty data
        # case3: data with unequal number of rows
        # case4: data with duplicate prefixes
        # case5: data with unmatching prefixes
        # case6: data with all matching prfixed (in order)
        # case7: data with all matching prfixed (out of order)
        pass

    def test_sum_df_cols(self):
        # case1: empty data
        # case2: rows with missing values
        # case3: rows with no missing values
        # case4: rows with values that are not number
        pass

    def test_avg_df_cols(self):
        # case1: empty data
        # case2: rows with missing values
        # case3: rows with no missing values
        # case4: rows with values that are not number
        pass