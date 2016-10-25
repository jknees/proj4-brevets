"""
Nose tests for acp_times.py
"""
import acp_times
import arrow

LIST = [200, 300, 400, 600, 1000]

def test_zero():
	a = arrow.get('2017-01-01T00:00:00+00:00')
	b = arrow.get('2017-01-01T00:00:00+00:00').replace(hours=+1)
	assert acp_times.open_time(0, 200, a) == a
	assert acp_times.close_time(0, 200, a) == b

def test_edge_values():
	answers = [arrow.get('2017-01-01T13:30:00+00:00'), arrow.get('2017-01-01T20:00:00+00:00'), 
		arrow.get('2017-01-02T03:00:00+00:00'), arrow.get('2017-01-02T16:00:00+00:00'), 
		arrow.get('2017-01-04T03:00:00+00:00')]

	a = arrow.get('2017-01-01T00:00:00+00:00')
	for i in range(len(LIST)):
		temp = acp_times.close_time(LIST[i], LIST[i], a)
		print(temp)
		assert temp == answers[i]

def test_general_times():
	a = arrow.get('2017-01-01T00:00:00+00:00')
	assert acp_times.open_time(50.5, 200, a) == arrow.get('2017-01-01T01:30:00+00:00')
	assert acp_times.close_time(50.5, 200, a) == arrow.get('2017-01-01T03:24:00+00:00')

	assert acp_times.open_time(250.5, 300, a) == arrow.get('2017-01-01T07:29:00+00:00')
	assert acp_times.close_time(250.5, 300, a) == arrow.get('2017-01-01T16:44:00+00:00')

	assert acp_times.open_time(350.5, 400, a) == arrow.get('2017-01-01T10:36:00+00:00')
	assert acp_times.close_time(350.5, 400, a) == arrow.get('2017-01-01T23:24:00+00:00')

	assert acp_times.open_time(450.5, 600, a) == arrow.get('2017-01-01T13:50:00+00:00')
	assert acp_times.close_time(450.5, 600, a) == arrow.get('2017-01-02T06:04:00+00:00')

	assert acp_times.open_time(650.5, 1000, a) == arrow.get('2017-01-02T09:05:00+00:00')
	assert acp_times.close_time(650.5, 1000, a) == arrow.get('2017-01-04T03:00:00+00:00')

def test_above_and_below_edge_values():
	answers = [arrow.get('2017-01-01T05:53:00+00:00'), arrow.get('2017-01-01T20:00:00+00:00'), 
		arrow.get('2017-01-02T03:00:00+00:00'), arrow.get('2017-01-02T16:00:00+00:00'), 
		arrow.get('2017-01-04T03:00:00+00:00')]

	a = arrow.get('2017-01-01T00:00:00+00:00')

	for i in range(len(LIST)):
		temp = acp_times.close_time(LIST[i]+10 , LIST[i], a)
		print(temp)
		assert temp == answers[i]

	for i in range(len(LIST)):
		temp = acp_times.close_time(LIST[i]-10 , LIST[i], a)
		print(temp)
		assert temp == answers[i]