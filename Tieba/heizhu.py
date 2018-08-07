# coding:utf-8
import requests
from requests.exceptions import MissingSchema
import pathlib


PICTURE_DIR = r'D:\test\pictures'

# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
# }
# response = requests.get(r'https://tieba.baidu.com/p/3019590556#!/l/p1', headers=header)
url_list = [
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=15&pic_id=5d0f918fa0ec08fad23124225bee3d6d55fbda0a&_=1533531847282',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=7a1a0924ab18972be74a374fe4cd7b899f510aca&_=1533531847400',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=93d7b6fd5266d0163921a9ad952bd40735fa3502&_=1533531861456',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=27bdcb1349540923295254fb9058d109b3de490c&_=1533531864600',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=671d728b4710b912d3f5c17bc1fdfc039245220e&_=1533531885334',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=82341f30e924b899c6434ebd6c061d950b7bf6c0&_=1533531888393',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=d8020cf3d7ca7bcb9f0ef0aabc096b63f724a8ce&_=1533531893614',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=0747d11373f08202197fa5ba49fbfbedaa641b55&_=1533531896991',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=282acffc1e178a82efd34b25f403738da877e850&_=1533531899943',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=271c01e93901213f69dd7a5956e736d12e2e9551&_=1533531907592',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=265894eef01f3a29c70fe14b9b25bc315d607c78&_=1533531910678',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=8b33b80e7bec54e7e22d2e9bbb389b504ec26a7a&_=1533531913934',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=e0e12e738bd4b31ce184a03e85d6277f9f2ff883&_=1533531917646',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=3d27d40735fae6cd4c0e9fe40db30f2443a70f8c&_=1533531920630',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=435c352ac65c1038e681fa47b0119313b17e8940&_=1533531923607',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=733fc895d143ad4b916b724580025aafa50f06fd&_=1533531926376',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=a059b319ebc4b74512d38393cdfc1e178b8215ff&_=1533531928646',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=fd2011dfa9ec8a131d5a6365f503918fa1ecc0fb&_=1533531934478',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=3423070828381f308795b92cab014c086f06f0b7&_=1533531941871',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=18f743166d224f4aad1747960bf790529922d1b1&_=1533532174086',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=ec2f09f790529822e1ec0c46d5ca7bcb0b46d460&_=1533535862378',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=a63f8744ebf81a4cf135d84cd52a6059252da638&_=1533535865288',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=1a72ca8065380cd72c1f9668a344ad345982813a&_=1533535868777',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=8f21d42a2834349bab045a00cbea15ce37d3bec5&_=1533535872795',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=06a32edda3cc7cd9407d005c3b01213fb90e91eb&_=1533535873945',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=19d29c82d158ccbf91ee81bf1bd8bc3eb03541f5&_=1533535874827',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=d33d0a55b319ebc4e690431c8026cffc1f171652&_=1533535876025',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=631b7f3e6709c93d63183b729d3df8dcd000545c&_=1533535877196',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=9ea45edf8db1cb13ba7e0896df54564e92584b28&_=1533535886376',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=e6046e061d950a7b77247a4108d162d9f2d3c92a&_=1533535887393',
    r'http://tieba.baidu.com/photo/bw/picture/guide?kw=%25E6%25BC%25AB%25E7%2594%25BB&tid=3019590556&see_lz=0&from_page=0&alt=jview&next=15&prev=0&pic_id=a07702087bf40ad11af7f366552c11dfa9ecce34&_=1533535888644'
]

for url in url_list:
    try:
        response = requests.get(url)
        data = response.json().get('data')
        pic_list = data.get('pic_list')
        for k, v in pic_list.items():
            img_data = v.get('img')
            origin_img_data = img_data.get('original')
            waterurl = origin_img_data.get('waterurl')
            img_content = requests.get(waterurl).content
            img_file = pathlib.Path(PICTURE_DIR, "{}.jpg".format(k))
            print('{} --> {}'.format(k, img_file))
            with open(img_file, 'wb') as fp:
                fp.write(img_content)
    except MissingSchema:
        # waterurl中没有值
        print("invalid url -- > {}".format(url))
