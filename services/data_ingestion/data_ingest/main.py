from my_package_1.lib import get_package_1
from my_package_2.lib import get_package_2
import numpy as np


def data_ingest_main():
    print('Hello from data-ingestion!')
    
    print('My Package 1:')
    print(get_package_1())
    
    print('My Package 2:')
    print(get_package_2())

    print('Generating a random matrix:')
    print(np.random.rand(3,2))
    

if __name__ == "__main__":
    data_ingest_main()
