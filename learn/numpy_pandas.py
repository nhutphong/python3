
import numpy as np
import pandas as pd
from numpy.random import randint, randn

===============================================================================
                                    NUMPY


np_obj = np.arange(50) => array 50 item 1->49

np_obj.reshape(5,10) => array 5 row, 10 col
np_obj.reshape(5,10).T => array, chuyen col dau tien thanh row dau tien cho den
khi het array => tuc la lay cac item1 dau tien cua tung rows cho vao thanh row1
, lay item2 cua tung rows cho vao thanh row2, cu the cho het array

np.random.randint(low=start, high=stop, size=(row, col)) => array()
np.random.randn() => float
np.random.randn(row, col) => array([float])

===============================================================================
                                PANDAS
pandas co cac method() doc cai loai file: csv, excel, html, ...,

lkey = ['a', 'b', 'c']
lvalue = [5,10,15]

dprice = pd.Series(data=lvalue, index=lkey) => dict()
dprice_1 = pd.Series(data=lvalue, index=lkey) => dict()
dprice + dprice_1 => se cong cac value lai voi nhau neu la int float

-------------------------------------------------------------------------------

                            DataFrame = dict()
tao du lieu nhu excel=dict(), co row va col, dict['col'] = [4,5,6]
row tu tao ra nhu index=0 to ..., co the gan khi tao object

ddata = {'col1': [4,5,6], 'col2': [7,8,9]}
lcol = ['col1', 'col2', 'col3', 'col4', 'col5']

df = pd.DataFrame(data=ddata)

ddf = pd.DataFrame(data=randn(3,5), index=None, columns=lcol)
index= chay tu 0-2 => 3 row

                                COLUMN
dff['attribute'] => mac dinh dung cho columns(cot)

ddf['col1'] = ddf.col1 => neu dung ddf['col1'] lay theo COLUMN co the +=*/
ddf[['col1', 'col3']] => print col1 and col3
ddf > 0 => array([True, False])
ddf[ddf>0] => array([]) => values=True thi giu lai, False thi= NaN
ddf[ddf['col3']>0] => row(1 dong) nao = False se bi del khoi ddf

                                ROW
ddf.loc['index=key=row'] = phai dung .loc

muon dung index=key=row phai co .loc
ddf.loc['row1'] => lay theo ROW
ddf.loc['row1', 'col2'] => value giao nhau cua row1 & col2
ddf.loc[['row1', 'row4'], ['col2', 'col5']] => array() = row1-row4 to col2-col5

ddf.iloc[2] => lay theo index=2

