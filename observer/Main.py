from observer.Chart import Chart
from observer.DataSource import DataSource
from observer.SpreadSheet import SpreadSheet

if __name__ == '__main__':
    data_source = DataSource()
    data_source.addObserver(SpreadSheet(data_source))
    data_source.addObserver(SpreadSheet(data_source))
    data_source.addObserver(Chart(data_source))
    data_source.value = 1
