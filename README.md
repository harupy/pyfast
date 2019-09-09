# Pyfast

A python script to log the internet speed using [fast.com](https://fast.com)

## Requirements

- python 3.6
- selenium
- chromedriver

## Setup

Download a chromedriver in the link below and put it in the project directory.

https://chromedriver.chromium.org/

And run the following comands:

```console
pip install pipenv
pipenv install
pipenv run python log_internet_speed.py --out_file output.csv
```

The output looks like:

```csv
datetime,speed,unit
2019/09/09 14:30:51,54,Mbps
2019/09/09 14:31:22,31,Mbps
2019/09/09 14:31:52,46,Mbps
2019/09/09 14:32:23,49,Mbps
2019/09/09 14:32:53,39,Mbps
```

## Scheduler

Set schedule in `config.py`

```
SCHEDULE = [
  '17:10',
  '17:12',
  '17:14',
]
```
