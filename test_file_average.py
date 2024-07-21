import averaging

def test_avg_2():
	assert averaging.average_2(1,2) == 1.5
	assert averaging.average_2(-1, 1) == 0

def test_avg_3():
	assert averaging.average_3(0,1,2) == 1
	assert averaging.average_3(-1, 0, 1) == 0
	assert averaging.average_3(10,20,30) == 20