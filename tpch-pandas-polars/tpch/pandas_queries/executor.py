from common_utils import execute_all
from pandas_queries import q1
from pandas_queries import q2
from pandas_queries import q3
from pandas_queries import q4
from pandas_queries import q5
from pandas_queries import q6
from pandas_queries import q7
from pandas_queries import q8
# running all the queries 10 times
if __name__ == "__main__":
    i=0
    while(i<10):
        q1.q()
        q2.q()
        q3.q()
        q4.q()
        q5.q()
        q6.q()
        q7.q()
        q8.q()
        i=i+1
