from baseball_function import *
from datetime import datetime, timedelta
import time


digit = int(input('몇 자리의 숫자야구를 진행하시겠습니까? : '))
start_time = time.time()
secret_num = new_number(digit)
wow = answer(list(secret_num))

if wow == 1:    # 리턴값에 맞게 출력
    end_time = time.time()
    print(f'맞추기 까지 걸린 시간 : {end_time - start_time:.2f}초')
    print(f'현재 시간 : {datetime.now()}')
elif wow == 0:
    print('게임을 종료합니다.')
