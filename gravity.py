import csv
import time
import logging
import subprocess

logging.basicConfig(filename='gravity.log', level=logging.INFO, format='%(asctime)s %(message)s', )
logger = logging.getLogger('gravity')

csv_file = file('s2.csv', 'rb')
reader = csv.reader(csv_file)
for line in reader:
    cmd = '/py/cleos_2 -u https://api-mainnet.eosgravity.com --wallet-url http://127.0.0.1:8900 push action eosadddddddd transfer \'["eosadddddddd","{}","0.0001 ADD","EOS TPS 1ST TEST FROM EOS ADD/BPC:eosadddddddd"]\' -p eosadddddddd -f'.format(line[0], line[1])
    logger.info('cmd: {}'.format(cmd))
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, errout = p.communicate()
    if errout:
        logger.error('error: {}'.format(errout))
    else:
        logger.info('success: {}'.format(stdout))

csv_file.close()
