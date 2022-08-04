import redis
# https://www.redis.com.cn/redis-interview-questions.html
if __name__ == '__main__':
    r = redis.Redis(decode_responses=True)
    r.set('mykey', 'thevalueofmykey')
    print(r.get('mykey'))
    print(r.strlen('mykey'))