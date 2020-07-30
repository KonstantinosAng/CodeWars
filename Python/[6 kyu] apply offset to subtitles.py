# see https://www.codewars.com/kata/5e454bf176551c002ee36486/train/python

from TestFunction import Test


def subs_offset_apply(string, offset):
  elements = string.split(" ")
  # start_time
  start = elements[0].split(":")
  temp_secs = start[2].split(",")
  start_time = [int(start[0]), int(start[1]), int(temp_secs[0]), int(temp_secs[1])]
  # end time
  end = elements[2].split(":")
  temp_secs = end[2].split(",")
  end_time = [int(end[0]), int(end[1]), int(temp_secs[0]), int(temp_secs[1])]
  positive = True if offset >= 0 else False
  offset = abs(offset)
  # offset
  offset_secs = offset // 1000
  offset_ms = offset - offset_secs*1000 
  offset_minutes = offset_secs // 60
  offset_secs = offset_secs - offset_minutes*60
  offset_hours = offset_minutes // 60
  offset_minutes = offset_minutes - offset_hours*60
  if positive:
    # fix start time
    start_time[3] += offset_ms
    if start_time[3] >= 1000: 
      start_time[2] += 1
      start_time[3] -= 1000
    start_time[2] += offset_secs
    if start_time[2] >= 60: 
      start_time[1] += 1
      start_time[2] -= 60
    start_time[1] += offset_minutes
    if start_time[1] >= 60: 
      start_time[0] += 1
      start_time[1] -= 60
    start_time[0] += offset_hours
    # fix end time
    end_time[3] += offset_ms
    if end_time[3] >= 1000: 
      end_time[2] += 1
      end_time[3] -= 1000
    end_time[2] += offset_secs
    if end_time[2] >= 60: 
      end_time[1] += 1
      end_time[2] -= 60
    end_time[1] += offset_minutes
    if end_time[1] >= 60: 
      end_time[0] += 1
      end_time[1] -= 60
    end_time[0] += offset_hours
  else:
    # fix start time
    start_time[3] -= offset_ms
    if start_time[3] < 0: 
      start_time[2] -= 1
      start_time[3] += 1000
    start_time[2] -= offset_secs
    if start_time[2] < 0: 
      start_time[1] -= 1
      start_time[2] += 60
    start_time[1] -= offset_minutes
    if start_time[1] < 0: 
      start_time[0] -= 1
      start_time[1] += 60
    start_time[0] -= offset_hours
    # fix end time
    end_time[3] -= offset_ms
    if end_time[3] < 0: 
      end_time[2] -= 1
      end_time[3] += 1000
    end_time[2] -= offset_secs
    if end_time[2] < 0: 
      end_time[1] -= 1
      end_time[2] += 60
    end_time[1] -= offset_minutes
    if end_time[1] < 0: 
      end_time[0] -= 1
      end_time[1] += 60
    end_time[0] -= offset_hours
  sh = '0'*(2 - len(str(start_time[0]))) + str(start_time[0])
  sm = '0'*(2 - len(str(start_time[1]))) + str(start_time[1])
  ss = '0'*(2 - len(str(start_time[2]))) + str(start_time[2])
  sms = '0'*(3 - len(str(start_time[3]))) + str(start_time[3])
  eh = '0'*(2 - len(str(end_time[0]))) + str(end_time[0])
  em = '0'*(2 - len(str(end_time[1]))) + str(end_time[1])
  es = '0'*(2 - len(str(end_time[2]))) + str(end_time[2])
  ems = '0'*(3 - len(str(end_time[3]))) + str(end_time[3])
  rv = f"{sh}:{sm}:{ss},{sms} --> {eh}:{em}:{es},{ems}"
  for elem in elements[3:]:
    rv += f' {elem}'
  if start_time[0] < 0 or end_time[0] < 0 or len(str(start_time[0])) >= 3 or len(str(end_time[0])) >= 3: return "Invalid offset"
  return rv

test = Test(None)
result1 = subs_offset_apply("01:09:02,684 --> 01:09:03,601 Run Forrest, run!", 3663655) 
test.assert_equals(result1, "02:10:06,339 --> 02:10:07,256 Run Forrest, run!")
result2 = subs_offset_apply("00:43:22,074 --> 00:43:24,159 No, I am your father.", 1789) 
test.assert_equals(result2, "00:43:23,863 --> 00:43:25,948 No, I am your father.")
result3 = subs_offset_apply("00:03:06,241 --> 00:03:07,618 I'll be back.", -21789) 
test.assert_equals(result3, "00:02:44,452 --> 00:02:45,829 I'll be back.")
result4 = subs_offset_apply("00:03:14,917 --> 00:03:16,001 My name is Bond. James Bond.", -195000) 
test.assert_equals(result4, "Invalid offset")
result5 = subs_offset_apply("01:00:00,000 --> 01:00:02,000 Let`s start with this.", -3600000) 
test.assert_equals(result5, "00:00:00,000 --> 00:00:02,000 Let`s start with this.")
result6 = subs_offset_apply("01:00:00,000 --> 01:00:02,000 Let`s finish this.", 356397999) 
test.assert_equals(result6, "99:59:57,999 --> 99:59:59,999 Let`s finish this.")
