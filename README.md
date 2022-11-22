# Economic_data_api
You can use this api to get the infomation from https://rili.jin10.com/day/

- To use this api by import `economicdata.py` in this repo

## Function 
- Get Critical Events
  - You can use get_events() to get the critical events that will happen or have already happened today.
  
For example:
```python = 
import economicdata 
todays_important_data = economicdata.get_events()
```
the information you get would be ike:
```
07:30 日本8月失業率
==========
09:30 中國9月官方製造業PMI
==========
09:45 中國9月財新製造業PMI
==========
14:00 英國第二季度GDP年率終值
==========
14:00 英國9月Nationwide房價指數月率
==========
14:00 英國第二季度經常帳(億英鎊)
==========
14:30 瑞士8月實際零售銷售年率
==========
14:45 法國9月CPI月率
==========
...
```

**There are going to be more functions...**
