from .models import DICT_REGION
from math import radians,cos,sin,degrees,atan2,sqrt

dict = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def maxDate(year, month):
    year = int(year)
    month = int(month)
    if (year % 100 == 0 and year % 4 == 0) or (year % 4 != 0):
        dict[2] = 28
    else:
        dict[2] = 29
    return dict[month]


def allDay(year):
    all_day_list = []
    year = int(year)
    for i in range(12):
        max_date = maxDate(year, i + 1)
        for j in range(max_date):
            year_month_day = '{0}-{1}-{2}'.format(year, str(i + 1).zfill(2), str(j + 1).zfill(2))
            all_day_list.append(year_month_day)
    return all_day_list


def allRegion():
    result = DICT_REGION.query.filter(DICT_REGION.TYPE != '0').all()
    all_region_dict = {}
    for i in result:
        all_region_dict[i.REGION_CODE] = {'region_name': i.REGION_NAME, 'statistics': '', 'detail': ''}
    return all_region_dict


#计算中心点
def center_geolocation(geolocations):
	'''
	输入多个经纬度坐标(格式：[[lon1, lat1],[lon2, lat2],....[lonn, latn]])，找出中心点
	:param geolocations:
	:return:中心点坐标  [lon,lat]
	'''
	#求平均数  同时角度弧度转化 得到中心点
	x = 0	# lon
	y = 0	# lat
	z = 0
	lenth = len(geolocations)
	for lon, lat in geolocations:
		lon = radians(float(lon))
		#  radians(float(lon))   Convert angle x from degrees to radians
		# 	                    把角度 x 从度数转化为 弧度
		lat = radians(float(lat))
		x += cos(lat) * cos(lon)
		y += cos(lat) * sin(lon)
		z += sin(lat)
		x = float(x / lenth)
		y = float(y / lenth)
		z = float(z / lenth)
	return (degrees(atan2(y, x)), degrees(atan2(z, sqrt(x * x + y * y))))



