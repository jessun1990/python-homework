# 第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 **Redis** 非关系型数据库中。
import redis
from generater import generater


def generater2Redis(listname="default_list", a_list=[1, 2, 3, 4, 5]):
    r = redis.StrictRedis(host='localhost', port=6379, db=0, password="root")
    # 清空
    r.delete(listname)
    a = r.rpush(listname, *a_list)
    print("插入的数据长度为{0}".format(a))
    b = r.lrange(listname, 0, -1)
    print(b)

if __name__ == '__main__':
    test_list = [generater(random_length=20) for i in range(200)]
    generater2Redis(listname="acodes", a_list=test_list)
