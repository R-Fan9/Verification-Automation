from cmath import nan
from Checker import Checker
import pandas as pd

KEY = 'PF'
COL_1 = 'A'
COL_2 = 'B'
COL_SUM = 'sum'
COL_AVG = 'avg'

COL_3 = 'C'
COL_4 = 'D'

class TestChecker:

    def __form_df(self, data, cols=[KEY, COL_1, COL_2]):
        return pd.DataFrame(data, columns=cols)

    def __eq_data(self, d_tru, d_rel):
        return d_tru == d_rel

    def setup_method(self, method):
        self.checker = Checker

        self.data1 = []

        self.data2 = [
            ['a', 401, 0],
            ['c', 238, 238],
            ['d', 0, 1],
            ['e', 0, 0],
            ['f', 523, 645]
        ]
        self.data2_fst = [
            ['a', 401],
            ['c', 238],
            ['d', 0],
            ['e', 0],
            ['f', 523]
        ]
        self.data2_snd = [
            ['e', 0],
            ['d', 1],
            ['c', 238],
            ['f', 645],
            ['a', 0],
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
            ['d', abs(-3)]    
        ]
        self.data3_snd = [
            ['c', 101],
            ['a', 452],
            ['d', 3],   
            ['b', 253], 
        ]

        self.data4 = [
            ['e', 31, 31],
            ['f', 36, 36],
            ['g', 8754, 8754]   
        ]
        self.data4_fst = [
            ['e', 31],
            ['f', 36],
            ['g', 8754]   
        ]
        self.data4_snd = [
            ['f', 36],
            ['g', 8754],
            ['e', 31],
        ]

        self.data5 = [
            ['a', nan, 1],
            ['b', nan, nan],
            [nan, 1, nan],
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
        self.data4_fst = None
        self.data4_snd = None
        self.data5 = None

    def test_get_unmatch(self):
        # case1: empty data
        d1_tru = []
        # case2: rows with value and N/A pair
        d2_tru = [['a', 401.0, 0.0],['d', 0.0, 1.0],['f', 523.0, 645.0]]
        # case3: rows with different values
        d3_tru = [['a', 32, 452],['b', 263, 253]]
        # case4: rows with matching values
        d4_tru = []

        d1_rel = self.checker.get_unmatch(self.__form_df(self.data1), COL_1, COL_2).values.tolist()
        d2_rel = self.checker.get_unmatch(self.__form_df(self.data2), COL_1, COL_2).values.tolist()
        d3_rel = self.checker.get_unmatch(self.__form_df(self.data3), COL_1, COL_2).values.tolist()
        d4_rel = self.checker.get_unmatch(self.__form_df(self.data4), COL_1, COL_2).values.tolist()

        assert self.__eq_data(d1_tru, d1_rel)
        assert self.__eq_data(d2_tru, d2_rel)
        assert self.__eq_data(d3_tru, d3_rel)
        assert self.__eq_data(d4_tru, d4_rel)

    def test_join_df(self):
        d1_tru = []

        d2_tru = []
        # self.data1 = []
        # self.data2_snd = [
        #     ['e', 0.0],
        #     ['d', 1],
        #     ['c', 238],
        #     ['f', 645],
        #     ['a', 0.0],
        # ]

        d3_tru = [['a', 401, 32], ['c', 238, 101], ['d', 0.0, 3]]
        # self.data2_fst = [
        #     ['a', 401],
        #     ['c', 238],
        #     ['d', nan],
        #     ['e', nan],
        #     ['f', 523]
        # ]
        # self.data3_fst = [
        #     ['a', 32],
        #     ['b', 263],
        #     ['c', 101],
        #     ['d', abs(-3)]    
        # ]

        d4_tru = [['d', 1, 3], ['c', 238, 101], ['a', 0, 452]]
        # self.data2_snd = [
        #     ['e', nan],
        #     ['d', 1],
        #     ['c', 238],
        #     ['f', 645],
        #     ['a', nan],
        # ]
        # self.data3_snd = [
        #     ['c', 101],
        #     ['a', 452],
        #     ['d', 3],   
        #     ['b', 253], 
        # ]

        # case4: data with unmatching prefixes
        d5_tru = []
        # self.data3_snd = [
        #     ['c', 101],
        #     ['a', 452],
        #     ['d', 3],   
        #     ['b', 253], 
        # ]
        # self.data4_fst = [
        #     ['e', 31],
        #     ['f', 36],
        #     ['g', 8754]   
        # ]

        # case5: data with all matching prefix
        d6_tru = [['e', 31, 31], ['f', 36, 36], ['g', 8754, 8754]]
        # self.data4_fst = [
        #     ['e', 31],
        #     ['f', 36],
        #     ['g', 8754]   
        # ]
        # self.data4_snd = [
        #     ['f', 36],
        #     ['g', 8754],
        #     ['e', 31],
        # ]

        d1_rel = self.checker.join_df(
            self.__form_df(self.data1),
            self.__form_df(self.data1, cols=[KEY, COL_3, COL_4]),
            KEY
            ).values.tolist()
        d2_rel = self.checker.join_df(
            self.__form_df(self.data1, cols=[KEY, COL_1, COL_3]), 
            self.__form_df(self.data2_snd, cols=[KEY, COL_2]), 
            KEY,
            ).values.tolist()
        d3_rel = self.checker.join_df(
            self.__form_df(self.data2_fst, cols=[KEY, COL_1]), 
            self.__form_df(self.data3_fst, cols=[KEY, COL_2]), 
            KEY
            ).values.tolist()
        d4_rel = self.checker.join_df(
            self.__form_df(self.data2_snd, cols=[KEY, COL_1]), 
            self.__form_df(self.data3_snd, cols=[KEY, COL_2]), 
            KEY
            ).values.tolist()
        d5_rel = self.checker.join_df(
            self.__form_df(self.data3_snd, cols=[KEY, COL_1]), 
            self.__form_df(self.data4_fst, cols=[KEY, COL_2]), 
            KEY
            ).values.tolist()
        d6_rel = self.checker.join_df(
            self.__form_df(self.data4_fst, cols=[KEY, COL_1]), 
            self.__form_df(self.data4_snd, cols=[KEY, COL_2]), 
            KEY
            ).values.tolist()

        assert self.__eq_data(d1_tru, d1_rel)
        assert self.__eq_data(d2_tru, d2_rel)
        assert self.__eq_data(d3_tru, d3_rel)
        assert self.__eq_data(d4_tru, d4_rel)
        assert self.__eq_data(d5_tru, d5_rel)
        assert self.__eq_data(d6_tru, d6_rel)

    def test_sum_df_cols(self):
        # case1: empty data
        d1_tru = []
        # case2: rows with missing values
        d2_tru = [
            ['a', 401, 0, 32, 452, 885], 
            ['c', 238, 238, 101, 101, 678], 
            ['d', 0, 1, 3, 3, 7]
        ]
        # self.data2 = [
        #     ['a', 401, 0],
        #     ['c', 238, 238],
        #     ['d', 0, 1],
        #     ['e', 0, 0],
        #     ['f', 523, 645]
        # ]
        # self.data3 = [
        #     ['a', 32, 452],
        #     ['b', 263, 253],
        #     ['c', 101, 101],
        #     ['d', abs(-3), 3]    
        # ]

        # case4: rows with values that are not number
        d3_tru = [
            ['a', 32, 452, 484], 
            ['b', 263, 253, 516], 
            ['c', 101, 101, 202],
            ['d', 3, 3, 6]
        ]
        # self.data3_fst = [
        #     ['a', 32],
        #     ['b', 263],
        #     ['c', 101],
        #     ['d', abs(-3)]    
        # ]
        # self.data3_snd = [
        #     ['c', 101],
        #     ['a', 452],
        #     ['d', 3],   
        #     ['b', 253], 
        # ]
        
        d4_tru = [
            ['e', 0, 31, 31, 62], 
            ['f', 645, 36, 36, 717]
            ]
        # self.data2_snd = [
        #     ['e', 0],
        #     ['d', 1],
        #     ['c', 238],
        #     ['f', 645],
        #     ['a', 0],
        # ]
        # self.data4 = [
        #     ['e', 31, 31],
        #     ['f', 36, 36],
        #     ['g', 8754, 8754]   
        # ]

        d5_tru = []
        # self.data3 = [
        #     ['a', 32, 452],
        #     ['b', 263, 253],
        #     ['c', 101, 101],
        #     ['d', abs(-3), 3]    
        # ]
        # self.data4_fst = [
        #     ['e', 31],
        #     ['f', 36],
        #     ['g', 8754]   
        # ]

        d1 = self.__form_df(self.data1)
        self.checker.sum_df_cols(d1)
        d1_rel = d1.values.tolist()

        d2 = self.checker.join_df(
                    self.__form_df(self.data2),
                    self.__form_df(self.data3, cols=[KEY, COL_3, COL_4]),
                    KEY
                )
        self.checker.sum_df_cols(d2)
        d2_rel = d2.values.tolist()

        d3 = self.checker.join_df(
                        self.__form_df(self.data3_fst, cols=[KEY, COL_1]),
                        self.__form_df(self.data3_snd, cols=[KEY, COL_2]),
                        KEY
                    )
        self.checker.sum_df_cols(d3)
        d3_rel = d3.values.tolist()

        d4 = self.checker.join_df(
                        self.__form_df(self.data2_snd, cols=[KEY, COL_1]),
                        self.__form_df(self.data4, cols=[KEY, COL_2, COL_3]),
                        KEY
                    )
        self.checker.sum_df_cols(d4)
        d4_rel = d4.values.tolist()

        d5 = self.checker.join_df(
                        self.__form_df(self.data3, cols=[KEY, COL_1, COL_2]),
                        self.__form_df(self.data4_fst, cols=[KEY, COL_3]),
                        KEY
                    )
        self.checker.sum_df_cols(d5)
        d5_rel = d5.values.tolist()

        assert self.__eq_data(d1_tru, d1_rel)
        assert self.__eq_data(d2_tru, d2_rel)
        assert self.__eq_data(d3_tru, d3_rel)
        assert self.__eq_data(d4_tru, d4_rel)
        assert self.__eq_data(d5_tru, d5_rel)

    def test_avg_df_cols(self):
        d1_tru = []

        d2_tru = [
            ['a', 401, 0, 32, 452, 885/4], 
            ['c', 238, 238, 101, 101, 678/4], 
            ['d', 0, 1, 3, 3, 7/4]
        ]
        # self.data2 = [
        #     ['a', 401, nan],
        #     ['c', 238, 238],
        #     ['d', nan, 1],
        #     ['e', nan, nan],
        #     ['f', 523, 645]
        # ]
        # self.data3 = [
        #     ['a', 32, 452],
        #     ['b', 263, 253],
        #     ['c', 101, 101],
        #     ['d', abs(-3), 3]    
        # ]

        d3_tru = [
            ['a', 32, 452, 484/2], 
            ['b', 263, 253, 516/2], 
            ['c', 101, 101, 202/2],
            ['d', 3, 3, 6/2]
        ]        
        # self.data3_fst = [
        #     ['a', 32],
        #     ['b', 263],
        #     ['c', 101],
        #     ['d', abs(-3)]    
        # ]
        # self.data3_snd = [
        #     ['c', 101],
        #     ['a', 452],
        #     ['d', 3],   
        #     ['b', 253], 
        # ]

        d4_tru = [
            ['e', 0, 31, 31, 62/3], 
            ['f', 645, 36, 36, 717/3]
            ]
        # self.data2_snd = [
        #     ['e', nan],
        #     ['d', 1],
        #     ['c', 238],
        #     ['f', 645],
        #     ['a', nan],
        # ]

        # self.data4 = [
        #     ['e', 31, 31],
        #     ['f', 36, 36],
        #     ['g', 8754, 8754]   
        # ]

        d5_tru = []
        # self.data3 = [
        #     ['a', 32, 452],
        #     ['b', 263, 253],
        #     ['c', 101, 101],
        #     ['d', abs(-3), 3]    
        # ]
        # self.data4_fst = [
        #     ['e', 31],
        #     ['f', 36],
        #     ['g', 8754]   
        # ]

        d1 = self.__form_df(self.data1)
        self.checker.sum_df_cols(d1)
        d1_rel = d1.values.tolist()

        d2 = self.checker.join_df(
                    self.__form_df(self.data2),
                    self.__form_df(self.data3, cols=[KEY, COL_3, COL_4]),
                    KEY
                )
        self.checker.avg_df_cols(d2)
        d2_rel = d2.values.tolist()

        d3 = self.checker.join_df(
                        self.__form_df(self.data3_fst, cols=[KEY, COL_1]),
                        self.__form_df(self.data3_snd, cols=[KEY, COL_2]),
                        KEY
                    )
        self.checker.avg_df_cols(d3)
        d3_rel = d3.values.tolist()

        d4 = self.checker.join_df(
                        self.__form_df(self.data2_snd, cols=[KEY, COL_1]),
                        self.__form_df(self.data4, cols=[KEY, COL_2, COL_3]),
                        KEY
                    )
        self.checker.avg_df_cols(d4)
        d4_rel = d4.values.tolist()

        d5 = self.checker.join_df(
                        self.__form_df(self.data3, cols=[KEY, COL_1, COL_2]),
                        self.__form_df(self.data4_fst, cols=[KEY, COL_3]),
                        KEY
                    )
        self.checker.avg_df_cols(d5)
        d5_rel = d5.values.tolist()

        assert self.__eq_data(d1_tru, d1_rel)
        assert self.__eq_data(d2_tru, d2_rel)
        assert self.__eq_data(d3_tru, d3_rel)
        assert self.__eq_data(d4_tru, d4_rel)
        assert self.__eq_data(d5_tru, d5_rel)

    def test_nan_to_zero(self):
        d_tru = [
            ['a', 0, 1],
            ['b', 0, 0],
            [0, 1, 0]
        ]
        # self.data5 = [
        #     ['a', nan, 1],
        #     ['b', nan, nan],
        #     [nan, 1, nan],
        #     ]

        d = self.__form_df(self.data5)  
        self.checker.nan_to_zero(d)
        d_rel = d.values.tolist()

        assert self.__eq_data(d_tru, d_rel)

    def test_rename_col(self):
        cols_tru = [KEY, COL_1, COL_3]

        d = self.__form_df(self.data1)  
        self.checker.rename_col(d, COL_2, COL_3)
        cols_rel = list(d.columns)

        assert self.__eq_data(cols_tru, cols_rel)

    def test_keep_cols(self):
        d_tru = [
           ['a', 0],
           ['c', 238],
           ['d', 1],
           ['e', 0],
           ['f', 645]
        ]
        # self.data2 = [
            # ['a', 401, 0],
            # ['c', 238, 238],
            # ['d', 0, 1],
            # ['e', 0, 0],
            # ['f', 523, 645]
        # ]

        d = self.__form_df(self.data2)  
        self.checker.keep_cols(d, [KEY, COL_2])
        d_rel = d.values.tolist()

        assert self.__eq_data(d_tru, d_rel)





 