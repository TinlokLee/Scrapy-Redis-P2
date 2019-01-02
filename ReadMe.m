运行：

Slave 端：
scrapy runspider juzi.py

Master 端：
redis-cli > lpush itjuzispider:start_urls http://www.itjuzi.com/company