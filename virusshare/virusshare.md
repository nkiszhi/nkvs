# 介绍

我们的项目是爬取*[https://virusshare.com/]()*网页种子的链接，并利用transmission种子下载器下载种子。

------
![Image](img/flow-process.png)

------
# 文件函数说明

**1.virusshare/vs.config**

说明：配置文件，保存登录网页的用户名，密码；文件保存的相对路径等

**2.virusshare/core/setting.py**

说明：读取配置文件信息，返回一个字典config

**3.virusshare/check_update.py**

说明：判断是否更新

**3.virusshare/get_vslist.py**

3.1 get_html()

说明：模拟登录，获得网页信息

3.2 get_url_list()

说明：从网页信息中爬取网页链接

**4.virusshare/update.py**

说明：判断网页链接是否更新

**5.virusshare/get_torrents.py**

说明：根据网页链接下载种子文件

**6.virusshare/get_zip.py**

说明：获取种子文件里面的压缩包文件

**7.virusshare/unzip_samples.py**

说明：解压压缩包文件

**8.virusshare/get_sha256.py**

说明：得到sha256

**8.VirusShare/mov_sha256.py**

说明：基于sha256移动

------

# 安装依赖

sudo apt-get install transmission

pip install transmissionrpc

------

# 运行方式

python start.py
