import os
from datetime import datetime
import csv
import argparse

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def now_as_str():
  return datetime.now().strftime('%Y/%m/%d %H:%M:%S')


def init_out_file(fp):
  with open(fp, 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['datetime', 'speed', 'unit'])


def log_data(fp, data):
  with open(fp, 'a', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(data)


def main():
  # parse arguments
  parser = argparse.ArgumentParser(description='Log internet speed using fast.com')
  parser.add_argument('--out_file', default='output.csv', help='output csv file')
  args = parser.parse_args()

  out_file = args.out_file
  assert out_file.endswith('.csv'), 'output file should be a csv file'

  # create out_file if it doesn't exist
  if not os.path.exists(out_file):
    init_out_file(out_file)

  try:
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome('./chromedriver', options=options)
    print('Chrome is running in the headless mode (Press Ctrl-C if you want to quit).')

    driver.get('https://fast.com')

    while True:
      # wait until the 'Show more info' button shows up
      WebDriverWait(driver, 600).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.more-info-container'), 'Show more info')
      )

      # extract speed value and units
      speed_value = driver.find_element_by_id('speed-value').text
      speed_unit = driver.find_element_by_id('speed-units').text
      now = now_as_str()

      # save the data
      data = [now, speed_value, speed_unit]
      log_data(out_file, data)
      print(data)

      driver.refresh()

  except Exception as e:
    print(e)
  finally:
    driver.quit()


if __name__ == '__main__':
  main()
