# Environment

## about independent

### sysmon and wazuh (AGENT & WAZUH)

- sysmon: v12.03
- wazuh: v4.1

### gui interface

- Nodejs : v14.15.1
- npm : v6.14.8
- vue/cli : v4.5.4

### api server interface

- conda : 4.9.2
- python : 3.8.5
- python package list

**installed package**

|package name|version|description|
|----|---|---|
|flask|1.1.2|..|
|flask-cors|3.0.9|CORS|
|flask-restx|0.2.0|API|
|elasticsearch|7.10.1|pypi-for connecting elk stack|

## How to Use....

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

## Update

2021-02-01 is version 1.0

As follow updated, increated version!

## Front struct

struct about component

```
App.vue
->views
-->MainPage.vue (depends common)
-->Homepage.vue (depends common)
-->Login.vue (save state in vuex)
-->Notfoundpage.vue

->components
--*dashboard.vue(router-view - depends on dashboard folder)
--*noauth.vue(when user abnomaly approach, view this component)
--*discover.vue(show log => used iframe)
--*check.vue(show basic log => depend on checklist folder)
--*alert.vue(setting for alert)

-->checkList
---*DriverLoad.vue (for checking usb connect)

-->dashboard(call kibana dashboard by iframe)
---*main.vue(list of dashboard)
---*dashMain.vue(show kibana dashboard)

-->common(this component can be called whenever want to use)
---*adModuleList.vue(first page in login state this menu is for admin!)
---*ModuleList.vue(first page in login state this menu is for user!)
---*AppHeader.vue(show menu on left side)
---*Loading.vue(loading page)
---*Toolbar.vue(side menu about user menu)
---*dateSlider.vue(emit => on,offload (link: load value), submitEvent (link:datarow in Datatable) &&&&& props => url(api path))

-->javascript (for chart. data rebuilding)
===================CountEvent.js=================
events => agent,time
(component folder => dashboard folder => for several environment)
```

router link

```
root path: '/' => "/login"
/home
/dashboard
/dashboard/dashmain
/discover
/check
/function
/alert
/management
/no-auth
/login
```

Vuex

```
state - UserInfo, isLogin, isLoginError, userInfo, isAdmin

4 login state
    - userloginSuccess => Only isLogin
    - adminloginSuccess => isLogin and isAdmin
    - loginError => isLoginError
    - Logout => All state false, userInfo is NULL

2 Actions
    - Login() => if admin user then commit adminloginSuccess, not admin then commit userloginSuccess else... commit loginError
    - Logout() => commit logout.
```

## backend struct

used flask API server => you can refer code comment

```
app.py => main
driverload.py => call driverload page -> query elasticsearch
```

## How to Use

Alert.vue can add or delete images. close button of chip can do this. if you want to add image, input image text field and press add button!

don't forget submit button at last.
