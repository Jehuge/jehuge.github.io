import os
import logging  # 改用内置logging模块

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 修改替换文件内容，进行字符串替换
def changfile(blog_md_file,old_str,new_str):
    try:
        with open(blog_md_file, "r+",encoding='utf-8') as file:  # 打开文件
            contents = file.read()  # 读取文件内容
            contents = contents.replace(old_str, new_str)  # 替换字符串
            file.seek(0)  # 定位到文件开头
            file.write(contents)  # 将修改后的内容写入文件
            file.truncate()  # 删除文件剩余部分
            logger.info(blog_md_file+'文件中的'+old_str+'已替换成'+new_str)
    except PermissionError:
        logger.error("Permission denied when trying to open the file.")
    except FileNotFoundError:
        logger.error("File not found.")
    except UnicodeDecodeError:
        logger.error("The file was not decoded correctly.")
    return None


# 读取目录解析md文件并进行字符串替换
def changfilebypath(filepath='',old_str='',new_str=''):
    try:
        files = os.listdir(filepath)
        for file in files:
            if file.find('.md') > 0:
                blog_file = os.path.join(filepath, file)
                changfile(blog_file,old_str,new_str)
    except FileNotFoundError as e:
        logger.error('请确认输入是否正确!',e)

if __name__ == '__main__':
    old_img_url = 'https://xiejava1018.github.io/xiejavaimagesrc'  # Github图床
    new_img_url = 'https://cdn.jsdelivr.net/gh/xiejava1018/xiejavaimagesrc'  # jsdelivr加速
    changfilebypath(filepath=r'D:\CloudStation\personal\xiejavablog\myhexo\myblog\source\_posts',old_str=old_img_url,new_str=new_img_url)
