"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments. 
#
BREVET_TIMES = {200: [15, 34, 13.50], 300: [15, 32, 20], 400: [15, 32, 27], 600: [15, 30, 40], 1000: [11.428, 28, 75], 1300: [13.333, 26]}
BREVET_ORDERED_KEYS = [200, 300, 400, 600, 1000, 1300]


def open_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    print("control_dist_km= " + str(control_dist_km))
    control_start_time = 0
    for key in BREVET_ORDERED_KEYS:
      if key <= control_dist_km:
        control_dist_km -= key
        control_start_time += key/BREVET_TIMES[key][1]
      elif control_dist_km > 0:
        control_start_time += control_dist_km/BREVET_TIMES[key][1]
        control_dist_km = 0

    print("control_start_time= " + str(control_start_time))
    minute, hour = math.modf(control_start_time)
    print("hour= " + str(hour))
    return brevet_start_time.replace(hours=+int(hour)).replace(minutes=+(int(60*minute)))

def close_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    control_close_time = 0
    print("brevet_dist_km= " + str(brevet_dist_km))
    print("Before control_dist_km= " + str(control_dist_km))

    if brevet_dist_km*0.8 <= control_dist_km and control_dist_km <= brevet_dist_km*1.2:
      print("Passed condition")
      control_close_time = BREVET_TIMES[brevet_dist_km][2]
      minute, hour = math.modf(control_close_time)
      print("hours = " + str(hour) + " minute= " + str(minute))
      return brevet_start_time.replace(hours=+int(hour)).replace(minutes=+(int(60*minute)))

    for key in BREVET_ORDERED_KEYS:
      if key <= control_dist_km:
        control_dist_km -= key
        control_close_time += key/BREVET_TIMES[key][0]
      elif control_dist_km > 0:
        control_close_time += control_dist_km/BREVET_TIMES[key][0]
        control_dist_km = 0

    print("control_close_time= " + str(control_close_time))
    minute, hour = math.modf(control_close_time)
    print("hour= " + str(hour) + " minute= " + str(int(60*minute)))
    return brevet_start_time.replace(hours=+int(hour)).replace(minutes=+(int(60*minute)))



