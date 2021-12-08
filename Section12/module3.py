#모듈에서 원하는 함수만 읽어올 때
from converter import kilometer_to_miles
#모듈에서 모든 함수를 읽어올 때
#from converter import *  === import converter

miles = kilometer_to_miles(200)
print('200kilometer to {}miles'.format(miles))
