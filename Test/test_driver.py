import Checker
import pytest as pt
import pandas as pd


class TestChecker:
    def setup_method(self, method):
        self.checker = Checker

        self.data1 = [[]]

        self.data2 = [
            [],
            []
        ]
        self.data3 = [
            [],
            []    
        ]

    def teardown_method(self, method):
        self.checker = None
        self.data1 = None
        self.data2 = None
        self.data3 = None

    def test_get_unmatches(self):
        # case1: empty data
        # case2: rows with value and N/A pair
        # case3: rows with different values
        # case4: rows with matching values
        pass

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