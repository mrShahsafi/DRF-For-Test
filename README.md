# DRF-For-Test
a very simple API for Insert, Delete and Select in SQLs dataBases
---
>pip install -r requirements.txt

***API Usage:***

> /RestApi/hero/?name=''
 #returns a hero by its name or alias

> /RestApi/hero/all
#returns all heroes

> /RestApi/hero/search/?q=''
#returns a lis of heroes by your q value

> /RestApi/hero/submit
#submit a new hero By 3 parameters:(name,alias,world_id) - world_id is the pk of the world

> /RestApi/hero/delete
#delete an existing hero by pass 2 parameters:(name,flag) - flag = 1  is delete confirmation

> /RestApi/world//?world_name=''
#returns a world by its name or content

> /RestApi/world/all
#returns all worlds
