# Environment

## about independent

### sysmon and winlogbeat

- sysmon: v12.03
- metricbeat oss: v7.9.1
- wazuh:

### gui interface

- Nodejs : v14.15.1
- npm : 6.14.8
- vue/cli : 4.5.4

### api server interface

- conda : 4.9.2
- python : 3.8.5
- python package list

**installed package**

```
flask                     1.1.2                      py_0
flask-cors                3.0.9                      py_0    anaconda
flask-restx               0.2.0                    pypi_0    pypi
elasticsearch             7.10.1                     pypi   for connecting elk stack
-
------------------------below is unnecessary, just for my recording------------
beautifulsoup4            4.9.3              pyhb0f4dca_0   (not used)
urllib3                   1.25.11                    py_0   (not used)
selenium                  3.141.0         py38he774522_1000 (not used)
```

# How to Use....

1. run vue

```nodejs
cd project-gui-interface
npm install #You only need to run it once.
npm run serve
```

2. run flask => from conda

```conda
pip install (packages) # refer for independent
python app.py
```

# Update

2021-02-01 is version 1.0

As follow updated, increated version!

# Front struct

```
App.vue
-> views(MainPage.vue , Homepage.vue)
--->MainPage.vue (depends common)
---->components
---->dashboard(call kibana dashboard by iframe)
---->alert.vue(call api -> /processCreate/addblacklist,/processCreate/BlackList)
(component folder => dashboard folder => for several environment)
```

# How to Use

Alert.vue can add or delete images. close button of chip can do this. if you want to add image, input image text field and press add button!

don't forget submit button at last.
