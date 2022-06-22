def add_time(start, duration, *args):
    def calc_end_time(start_time, duration, start_weekday):
      weekdays = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
      ]
      
      _total_minute = (start_time['minute'] + duration['minute'])
      end_time_minute = str(_total_minute % 60)
      if len(end_time_minute) == 1:
        end_time_minute = '0' + end_time_minute
      _total_hour = (start_time['hour'] + duration['hour']) + _total_minute // 60
      end_time_hour = _total_hour % 24
      hour_unit = 'PM' if end_time_hour > 11 else 'AM'
      if end_time_hour > 12 and hour_unit == 'PM':
        end_time_hour = end_time_hour - 12
      elif end_time_hour == 0 and hour_unit == 'AM':
        end_time_hour = end_time_hour + 12
      days = _total_hour // 24
      end_weekday = weekdays[(weekdays.index(start_weekday) + days) % 7] if start_weekday else ''

      return end_time_hour, end_time_minute, hour_unit, end_weekday, days
      
  
    _start_time, _unit = start.split(' ')
    _hour, _minute = _start_time.split(':')
    start_time = {
      'hour': int(_hour) + 12 if _unit == 'PM' else int(_hour),
      'minute': int(_minute)
    }
    _duration_hour, _duration_minute = duration.split(':')
    duration_time = {
      'hour': int(_duration_hour),
      'minute': int(_duration_minute)
    }
    start_weekday = args[0].capitalize() if len(args) else ''

    end_time_hour, end_time_minute, hour_unit, end_weekday, days = calc_end_time(start_time, duration_time, start_weekday)
    new_time = f'{end_time_hour}:{end_time_minute} {hour_unit}'
    if start_weekday:
      new_time += f', {end_weekday}'
    if days > 0:
      if days == 1:
        new_time += ' (next day)'
      else:
        new_time += f' ({days} days later)'

    return new_time