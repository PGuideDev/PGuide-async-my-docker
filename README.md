# Async-my-docker

解决自动化收集可用docker镜像源地址，并且确保容器镜像安全

## 使用方法

环境参考

> python: 3.13
> 

1. 可选：配置pip镜像源

参考[项导文档](https://docs.pguide.studio/public-service/cqmu-mirror/wiki/#pypi)配置校园网联合镜像pip源

2. 安装依赖

```shell
pip install -r req
```

## 开发进度
1. [x] 将可用镜像源保存进`mirrors.md`
2. [x] 添加阿里云私有docker镜像源
3. [ ] webhook双向同步重医镜像源
4. [ ] 前端使用查询工具检索镜像源内容
5. [ ] Kaniko镜像构建优化