corpus = [
    # ruleYear
    ('Time[]{2019-X-X X:X (X/X)}',
     '2018-03-07T12:43',
     ('2019',)),
    # ruleToday
    ('Time[]{2018-03-07 X:X (X/X)}',
     '2018-03-07T12:43',
     ('heute',
      'zu dieser zeit',
      'today')),
    # ruleNow
    ('Time[]{2018-03-07 12:43 (X/X)}',
     '2018-03-07T12:43',
     ('jetzt',
      'genau jetzt'
      'gerade eben',
      'rightnow',
      'just now')),
    # ruleTomorrow
    ('Time[]{2019-01-01 X:X (X/X)}',
     '2018-12-31T12:43',
     ('morgen',
      'tomorrow')),
    # ruleYesterday
    # test on a leap-year
    ('Time[]{2020-02-29 X:X (X/X)}',
     '2020-03-01T12:43',
     ('gestern',
      'yesterday')),
    # ruleEOM
    ('Time[]{2018-03-31 X:X (X/X)}',
     '2018-03-07T12:43',
     ('ende des Monats',
      'eom',
      'end of the month')),
    # ruleEOY
    ('Time[]{2018-12-31 X:X (X/X)}',
     '2018-03-07T12:43',
     ('ende des Jahres',
      'eoy',
      'end of the year')),
    # ruleDOWMonday
    ('Time[]{2018-03-12 X:X (X/X)}',
     '2018-03-07T12:43',
     ('Montag',
      'Mo.',
      'mondays')),
    # ruleDOWTuesday
    ('Time[]{2018-03-13 X:X (X/X)}',
     '2018-03-07T12:43',
     ('Dienstags',
      'Die.',
      'tuesday',
      'tue')),
    # ruleDOWWednesday
    ('Time[]{2018-03-14 X:X (X/X)}',
     '2018-03-07T12:43',
     ('Mittwoch',
      'Mi.',
      'wednesday',
      'Wed.')),
    # ruleDOWThursday
    ('Time[]{2018-03-08 X:X (X/X)}',
     '2018-03-07T12:43',
     ('Donnerstags',
      'Do',
      'thursdays',
      'Thu')),
    # ruleDOWFriday
    ('Time[]{2018-03-09 X:X (X/X)}',
     '2018-03-07T12:43',
     ('Freitag',
      'Fr.',
      'friday',
      'Fri.')),
    # ruleDOWSaturday
    ('Time[]{2018-03-10 X:X (X/X)}',
     '2018-03-07T12:43',
     ('Sonnabend',
      'Samstag',
      'Sa.',
      'saturday',
      'sat')),
    # ruleDOWSunday
    ('Time[]{2018-03-11 X:X (X/X)}',
     '2018-03-07T12:43',
     ('Sonntags',
      'So.',
      'sunday',
      'Sun.')),
    # ruleDOWMonday + POD
    ('Time[]{2018-03-12 X:X (X/morning)}',
     '2018-03-07T12:43',
     ('Montagmorgen',)),
    # ruleDOWTuesday + POD
    ('Time[]{2018-03-13 X:X (X/evening)}',
     '2018-03-07T12:43',
     ('Dienstagabend',)),
    # ruleDOWWednesday + POD
    ('Time[]{2018-03-14 X:X (X/beforenoon)}',
     '2018-03-07T12:43',
     ('Mittwochvormittag',)),
    # ruleDOWThursday + POD
    ('Time[]{2018-03-08 X:X (X/noon)}',
     '2018-03-07T12:43',
     ('Donnerstagmittag',)),
    # ruleDOWFriday + POD
    ('Time[]{2018-03-09 X:X (X/afternoon)}',
     '2018-03-07T12:43',
     ('Freitagnachmittag',)),
    # ruleDOWSaturday + POD
    ('Time[]{2018-03-10 X:X (X/morning)}',
     '2018-03-07T12:43',
     ('Samstagfrüh',)),
    # ruleDOWSunday + POD
    ('Time[]{2018-03-11 X:X (X/evening)}',
     '2018-03-07T12:43',
     ('Sonntagabends',)),
    # ruleMonthJanuary
    ('Time[]{X-01-X X:X (X/X)}',
     '2018-03-07T12:43',
     ('Januar',
      'Jan.')),
    # ruleMonthFebruary
    ('Time[]{X-02-X X:X (X/X)}',
     '2018-03-07T12:43',
     ('February',
      'Feb')),
    # ruleMonthMarch
    ('Time[]{X-03-X X:X (X/X)}',
     '2018-03-07T12:43',
     ('März',
      'March',
      'mar.')),
    # ruleMonthApril
    ('Time[]{X-04-X X:X (X/X)}',
     '2018-03-07T12:43',
     ('April',
      'apr.')),
    # ruleMonthMay
    ('Time[]{X-05-X X:X (X/X)}',
     '2018-03-07T12:43',
     ('May',
      'mai')),
    # ruleMonthJune
    ('Time[]{X-06-X X:X (X/X)}',
     '2018-03-07T12:43',
     ('June',
      'Juni',
      'Jun.')),
    # ruleMonthJuli
    ('Time[]{X-07-X X:X (X/X)}',
     '2018-03-07T12:43',
     ('Juli',
      'July',
      'Jul.')),
    # ruleMonthAugust
    ('Time[]{X-08-X X:X (X/X)}',
     '2018-03-07T12:43',
     ('August',
      'Aug.')),
    # ruleMonthSeptember
    ('Time[]{X-09-X X:X (X/X)}',
     '2018-03-07T12:43',
     ('September',
      'Sep.',
      'Sept.')),
    # ruleMonthOctober
    ('Time[]{X-10-X X:X (X/X)}',
     '2018-03-07T12:43',
     ('Oktober',
      'Oct',
      'Okt.')),
    # ruleMonthNovember
    ('Time[]{X-11-X X:X (X/X)}',
     '2018-03-07T12:43',
     ('November',
      'Nov.')),
    # ruleMonthDecember
    ('Time[]{X-12-X X:X (X/X)}',
     '2018-03-07T12:43',
     ('Dezember',
      'December',
      'Dec.',
      'Dez.')),
    # ruleAtDOW
    ('Time[]{2018-03-13 X:X (X/X)}',
     '2018-03-07T12:43',
     ('am Dienstag',
      'on Tue')),
    ('Time[]{2018-03-14 X:X (X/X)}',
     '2018-03-07T12:43',
     ('this Wednesday',
      'diesen Mittwoch')),
    # ruleNextDOW
    ('Time[]{2018-03-16 X:X (X/X)}',
     '2018-03-07T12:43',
     ('am nächsten Freitag',
      'on the following Friday')),
    # ruleDOYYear, ruleDDMM
    ('Time[]{2018-05-08 X:X (X/X)}',
     '2018-03-07T12:43',
     ('8.5.2018',
      '8. Mai 2018',
      '8. Mai 18',
      '8.5.',
      '8th May',
      '8th of May',
      'May 8th')),
    # ruleDOWDOM
    ('Time[]{2018-05-08 X:X (X/X)}',
     '2018-03-07T12:43',
     ('Tuesday 8th',
      'Tuesday the 8th',
      'Dienstag der 8.')),
    # rulePOD, ruleLatentPOD
    ('Time[]{2018-03-08 X:X (X/morning)}',
     '2018-03-07T12:43',
     ('morgens',
      'morning')),
    ('Time[]{2018-03-08 X:X (X/earlymorning)}',
     '2018-03-07T12:43',
     ('früh morgens',
      'early morning')),
    ('Time[]{2018-03-07 X:X (X/afternoon)}',
     '2018-03-07T12:43',
     ('nach mittags',
      'nachmittag',
      'after noon',
      'afternoon')),
    ('Time[]{2018-03-08 X:X (X/noon)}',
     '2018-03-07T12:43',
     ('mittags',
      'noon')),
    # ruleTODPOD
    ('Time[]{2018-03-08 08:00 (X/X)}',  # next day since moning is already over
     '2018-03-07T12:43',
     ('um 8 morgens',
      'at 8 late morning')),
    ('Time[]{2018-03-07 16:30 (X/X)}',
     '2018-03-07T12:43',
     ('um 4:30 nachmittags',
      'at 4:30 in the afternoon')),
    # rulePODTOD
    ('Time[]{2018-03-08 08:00 (X/X)}',  # next day since moning is already over
     '2018-03-07T12:43',
     ('morgens um 8',
      'late morning at 8')),
    ('Time[]{2018-03-07 16:30 (X/X)}',
     '2018-03-07T12:43',
     ('nachmittags um 16:30',
      'afternoon at 16:30')),
    # ruleDateTOD
    ('Time[]{2018-08-05 08:00 (X/X)}',
     '2018-03-07T12:43',
     ('5. August um 8',
      'August 5th at 8')),
    # ruleTODDate
    ('Time[]{2018-08-05 08:00 (X/X)}',
     '2018-03-07T12:43',
     ('um 8 am 5. August',
      'at 8 on August 5th')),
    # ruleDateDate
    ('Interval[]{2018-08-05 X:X (X/X) - 2018-08-16 X:X (X/X) (X)}',
     '2018-03-07T12:43',
     ('5.8. - 16.8.',
      'August 5th - August 16th')),
    # ruleDateTimeDateTime
    ('Interval[]{2018-08-05 08:00 (X/X) - 2018-08-16 13:00 (X/X) (X)}',
     '2018-03-07T12:43',
     ('5.8. 8Uhr - 16.8. 13Uhr',
      'August 5th 8h - August 16th 13h')),
    # ruleTODTOD, ruleLatentTimeInterval
    ('Interval[]{2018-03-08 08:00 (X/X) - 2018-03-08 13:00 (X/X) (X)}',
     '2018-03-07T12:43',
     ('08:00 - 13:00',
      '8Uhr - 13Uhr',
      '8h to 13h')),
    # ruleAfterTime
    ('Interval[]{2017-11-26 08:00 (X/X) - None (X)}',
     '2018-03-07T12:43',
     ('26.11.2017 ab 08:00 Uhr',)),
    ('Interval[]{2018-11-26 08:00 (X/X) - None (X)}',
     '2018-03-07T12:43',
     ('26.11.2018 ab 08:00 Uhr',
      '26.11. ab 08:00 Uhr')),
    #
    # -----------------------------------------------------------------------------
    # OLD CORPUS
    # -----------------------------------------------------------------------------
    #
    ('Interval[]{2017-12-19 09:30 (X/X) - 2017-12-19 10:45 (X/X) (X)}',
     '2017-12-18T12:34',
     [
         'tomorrow 09:30 - 10:45',
         'tomorrow 0930 - 1045',
         '19. Dezember von 09:30 bis 10:45',
         '19th of December from 09:30 til 10:45',
         '19.12. 09:30 - 10:45',
         '19.12.17 09:30 - 10:45',
         '19.12.2017 09:30 - 19.12.2017 10:45',
         '19.12.2017 09:30 - 10:45'
     ]),
    ('Interval[]{2018-02-16 X:X (X/X) - 2018-02-21 X:X (X/X) (X)}',
     '2017-12-18T12:34',
     [
         '16.02.2018 - 21.02.2018',
         '16. bis 21.02.2018'
     ]),
    ('Interval[]{2018-08-07 X:X (X/X) - 2018-08-10 X:X (X/X) (X)}',
     '2017-12-18T12:34',
     [
         '07.-10.08.2018'
     ]),
    # ('Range[]{2018-12-09 - 2018-12-13}',
    #  '2017-12-18T12:34',
    #  [
    #      '09.-13.12.2018 von Samstag bis Donnerstag'
    #  ]),
    # ('Range[]{2018-04-27 - 2018-04-30}',
    #  '2017-12-18T12:34',
    #  [
    #      # 'from the 27th to the 30th of April 2018',
    #      '27.-30.04.2018 von Freitag bis Montag'
    #  ]),
    ('Time[]{2018-01-13 X:X (X/X)}',
     '2017-12-18T12:34',
     [
         'am 13.1.',
         'am 13.01.',
         'am 13. Januar',
         '13.01',
         '13.1',
         '13th Jan'
     ]),
    ('Time[]{2017-12-19 X:X (X/X)}',
     '2017-12-18T12:34',
     [
         'am Dienstag',
         'am 19.12',
         'Dienstag 19.12',
         'Tuesday 19th of December',
         'Tuesday December 19th',
         'Dienstag 19. Dezember',
         'Dienstag Dezember 19.',
         'Dienstag'
     ]),
    ('Time[]{2018-03-01 14:30 (X/X)}',
     '2017-12-18T12:34',
     [
         # mm/dd does not work yet
         # '03/01/2018 at 2:30 pm',
         'am 01.03.2018 um 14:30',
         'Mar. 1st 2:30 pm',
         '1. März um 1430 Uhr',
         '01.03.2018 14:30']),
    ('Time[]{2018-01-03 14:30 (X/X)}',
     '2017-12-18T12:34',
     [
         # mm/dd does not work yet
         # '01/03/2018 at 2:30 pm',
         'am 03.01.2018 um 14:30',
         'Jan. 3rd 2:30 pm',
         '3. Januar 1430 Uhr',
         '03.01.2018 14:30',
         '3. Jan. 2018 14:30'
     ]),
    ('Time[]{2018-04-23 11:00 (X/X)}',
     '2017-12-18T12:34',
     ['23.04.2018 11:00']),
    ('Time[]{2018-11-19 18:00 (X/X)}',
     '2017-12-18T12:34',
     [
         '19.11.2018 18:00'
     ]),
    ('Time[]{2017-12-20 X:X (X/morning)}',
     '2017-12-18T12:34',
     ['Wednesday, 20th December morning']),
    # ('DateTime[]{2017-12-20Tmorning}',
    #  '2017-12-18T12:34',
    #  ['Wednesday, morning, 20.12.17']),
    # ('DateTime[]{2017-12-20Tafternoon}',
    #  '2017-12-18T12:34',
    #  ['Wednesday, afternoon, 20.12.17']),
    # ('DateTime[]{2017-12-20 XX:XX (X/evening)}',
    #  '2017-12-18T12:34',
    #  ['Wednesday, evening, 20.12.17']),
    ('Time[]{2017-12-20 06:45 (X/X)}',
     '2017-12-18T12:34',
     ['6.45 Uhr 20.12.2017']),
    ('Time[]{2018-08-04 15:00 (X/X)}',
     '2017-12-18T12:34',
     ['04.08.2018 15:00']),
    ('Time[]{2018-09-01 01:00 (X/X)}',
     '2017-12-18T12:34',
     ['01.09.2018 01:00']),
    ('Time[]{2018-11-29 22:00 (X/X)}',
     '2017-12-18T12:34',
     ['29.11.2018 22:00']),
    ('Time[]{2018-02-27 07:00 (X/X)}',
     '2017-12-18T12:34',
     ['27.02.2018 07:00']),
    ('Time[]{2018-05-09 09:30 (X/X)}',
     '2017-12-18T12:34',
     ['09.05.2018 09:30']),
    ('Time[]{2018-01-17 14:30 (X/X)}',
     '2017-12-18T12:34',
     ['17.01.2018 14:30']),
    ('Interval[]{2018-06-21 11:00 (X/X) - 2018-06-21 13:00 (X/X) (X)}',
     '2017-12-18T12:34',
     [
         '21.06.2018 11:00 - 21.06.2018 13:00'
     ]),
    ('Interval[]{2018-07-09 08:00 (X/X) - 2018-07-13 10:00 (X/X) (X)}',
     '2017-12-18T12:34',
     [
         '09.07.2018 08:00 - 13.07.2018 10:00'
     ])
]
