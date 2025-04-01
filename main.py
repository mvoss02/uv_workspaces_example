from data_ingest.main import data_ingest_main
from data_pre.main import data_pre_main


def main():
    print('Running all...')
    
    print('Data ingestion:')
    data_ingest_main()
    
    print('Data pre processing:')
    data_pre_main()
    
if __name__ == "__main__":
    main()