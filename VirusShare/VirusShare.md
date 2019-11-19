# 介绍

我们的项目是爬取*[https://virusshare.com/]()*网页种子的链接，并利用transmission种子下载器下载种子。

------

# 文件函数说明

**1.VirusShare/virusshare.config**

说明：配置文件，保存登录网页的用户名，密码；文件保存的相对路径等

**2.VirusShare/core/setting.py**

说明：读取配置文件信息，返回一个字典config

**3.VirusShare/update.py**

说明：判断是否更新

**3.VirusShare/load_url.py**

3.1 get_html()

说明：模拟登录，获得网页信息

3.2 get_url_list()

说明：从网页信息中爬取网页链接

**4.VirusShare/update.py**

说明：判断网页链接是否更新

**5.VirusShare/load_torrent.py**

说明：根据网页链接下载种子文件

**6.VirusShare/load_zip.py**

说明：获取种子文件里面的压缩包文件

**7.VirusShare/unzip.py**

说明：解压压缩包文件

------

# 安装依赖

sudo apt-get install transmission-cli transmission-daemon

------

# 运行方式

python start.py

#### 
