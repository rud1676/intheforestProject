# sysmon&metricbeat wazuh config

- ver 1.0 => 기존 설정 그대로 씀.
- [ver 1.01](#02.03)
- [ver 1.02](#02.18) wazuh + sysmon + metricbeat로 변경(metricbeat는 활용도에 따라 변할 수 있음)

## about sysmon config

### HashAlgorith

---

md5,sha256,IMPHASH

### CheckRevocation

---

로드된 드라이버를 확인하고, 코드 서명 인증서가 취소가 됬는지 기록..(무슨소리일까...)

### 사용되지 않는 이벤트

---

ImageLoad, ProcessAccessConfig,PipeMonitoringConfig

### Process Create

---

**기존-가져온-필터링의-정보**

**제외시키는 목록들**

CommandLine에서 다음과 같은 프로그램이 실행이되면...

```
window error report(wermgr.exe),window(DllHost), WMI provider(wmiprvse), 검색Indexer(SearchIndexer),bootchecker(autochk-시작할때 켜지는),session manager(smss), app 사용권한(Runtimebroker)
```

Image(실행 경로)가 일치하게 되면

```
터치키보드,handwriting pannel핼퍼(TabTip32), SSO로그인(TokenBrokerCookies - 뭔지모르겟네), 성능로그,알람DCOM 서버(plasrv),무선네트워크(wifitask),고객경험향상(CompatTelRunner),프린트(PrintIsolationHost),KMS(SppExtComObj-뭔지 모르겟네),항상 켜지는?(audiodg-뭔지모르겟음),CLIHostProcess(conhost),네트워크파일동기화(mobsync),업데이트확인 팝업(musNotification*),전원관리(powercfg),볼륨조절(sndVol),소프트웨어 보호(sppsvc),WMI성능어뎁터host(WmiApSrv-뭔지모르겟네)
```

IntegrityLevel(권한분리레벨) 이 AppContainer인것도 제외 - 샌드박스 어쩌구 하는데 뭔지 1도모르겟네

ParentCommandLine 부분 일치하면..

```
commandShell에서 command사용하면 동작되는 프로그램이지만 속성정보를 제공하지 않는 것(~csrss.exe ObjectDirectory=\Windows),
윈도우 에러보고(wermgr)
```

ParnetImage 일치하면..

```
SearchIndexer 검색을 열면...인데.. 왜 제외시키는건가... 일단 알고잇기
```

CommandLine 이 일치하면...

```
운영체제에대한 정보 MS에 제출(devicecensus),윈도우의 핵심부분(usocoreworker),
```

CommandLine에서 svchost(윈도우서비스)가 일치할 때

[참고사이트](https://ss64.com/nt/syntax-services.html)

```
C:\Windows\system32\svchost.exe -k appmodel => 어떤의미를 가진 명령라인일까(검색해본 바로는 MS에 정보를 보내기 위한 서비스인듯)
carema 서비스
dcomlaunch -s LSM(COM,DCOM Object활성화에 필요하다는데 - 응용프로그램간 통신을 위한 서비스)(LSM은 UserSection을 관리해주는 서비스)
dcomlaunch -s PlugPlay(PlugPlay는 새로운 하드웨어 인식해주는)
defragsvc(파일 시스템 최적화 해주는)
devicesflow(wifi,bluetooth등 연결해주는)
imgsvc(cd굽기관련 서비스)

localService(이것의 정체는 모르겠다.)
->EventSystem(컴퓨터 이벤트 알림..)
->bthserv(블루투스장치 발견)
->BthAvctpSvc(오디오,비디오전송제어 서비스)
->nsi(네트워크 알림)
->w32Time(시간 동기화)

localServiceAndNoImpersonation(네트워크 서비스)
-> SensrSvc(모니터 센서-밝기등)
-> SSDPSRV(UPnP /SSDP devices를 발견해주는.. 네트워크 관련장치라함)
-> SCardSvr(smartcard 지원이라는데 중요한 부분이라함)
localServiceNetworkRestricted(이것도 네트워크 관련 서비스)
->Dhcp(IP할당해주는)
->EventLog(이벤트로그 관리)
->TimeBrokerSvc(WinRT application을 bg로)
->WFDSConMgrSvc(무선네트워크 연결 서비스)
->BTAGService(블루투스오디오)
->NgcCtnrSvc(유저증명키관리와smartcard관리)

LocalSystemNetworkRestricted(이것의 정체도.. 네트워크 관련 그런것인가)
->NcbService(store app과 internet을 연결)
->WPDBusEnum(그룹 정책과,content의동기화와 전송허용)
->fhsvc(윈도우백업)
->DeviceAssociationService(페어링 디바이스)
->SensorService(센서를 관리함)
->TabletInputService(터치키보드등을 허용)
->UmRdpService(RDP영역에서 프린트 드라이버 포트를 리다이렉션을 허용)
->NgcSvc(프로세스 암호화이유로 격리)
->WdiSystemHost(로컬시스템 진단)

netsvcs (멜웨어인지 아닌지 반드시 확인해야되는 프로세스라고함.)
->wuauserv(윈도우 업데이트)
->SessionEnv(원격제어 관련)
->wlidsvc(MS로그인 될때 실행)
->ncaSvc(알림의 직접적 접근)
->BDESVC(안전 시작과 볼륨(장치)암호화)
->BITS(파일전송)
->CertPropSvc(인증관리-smartcard)
->DsmSvc(드라이버 설치)
->Appinfo(추가권한 에플리케이션 실행용이)
->Gpsvc(그룹정책을통한 관리자apply)
->ProfSvc(userprofile을 로드하고 언로드)
->SENS(시스템 이벤트를 모니터링)
->Themes(사용자배경관리)
->Winmgmt(WMI)

networkService(네트워크 관련 서비스)
->DoSvc(콘텐츠 전달 최적화)
->Dnscache(DNSquery를 캐싱하고 컴퓨터이름을 등록)
->LanmanWorkstation(원격서버 연결)
->NlaSvc(네트워크 설정 변경을 알림)
->TermService(원격 컴퓨터 관리)

rPCSS(COM,DCOM의 활동)
secsvcs(캐시와 같은 기능이라는데...)
swprv(백업)
unistackSvcGroup(뭔지모르겟네...)
utcsvc(뭔지모르겟음)
wbioSvcGroup(???)
werSvcGroup(디지털 라이센스를 다운받아주는..)
wusvcs(크로미움 웹 관련프로그램)
wsappx(윈도우 스토어 관련)

MS edge도 필터링했다...
.Net 3.0.30319도 필터링
MSOFice도 필터링됨
미디어플레이어,
크롬도 필터링
```

---

**추가한-필터링**

### 02.03

```
RuntimeBroker => 권한에 대한 관리하는 프로그램.
dllhost => 동적 링크 라이브러리 호스트.... 어렵네 어쨋든 중요한 프로세스
backgroundTaskHost.exe => 백그라운드 작업 호스트 유틸리티를 실행하는 파일
winlogbeat
GoogleUpdate.exe
sppsvc.exe => 디지털 서명을 설치하고 다운로드함. 이것은 안보이게 할 수 없음..
SearchFilterHost => 사용자의 검색이 빠르게 인덱싱 해주는 프로그램
MicrosoftEdgeUpdate.exe
slui=> ms 업데이트, 정품인증을 도와주는 프로세스
smss => session manager 사용자의 세션 시작을 관리하는 프로세스
SearchProtocolHost.exe => 윈도우의 인덱싱 검색 서비스의 종류로 빠른 검색을 위한 파일들의 색인기능
WmiPrvSE=>프로레스,프로그램을 모니터링하고 권한을 부여해주고 신뢰그룹을 편성해주고 하는 호스트 서비스
wermgr=> 윈도우 오류보고 서비스
GoogleCrashHandler.exe
GoogleCrashHandler64.exe
csrss=> 클라이언트 요청에 따라 작업자 스레드를 관리해주는 서버 런타임..
fontdrvhost => 운영체제와 관련된 파일이라는 정보뿐.. 어쨋든 중요한 프로세스
mmc.exe => 자가 시스템을 구성하고 모니터링을 할 수 있는 인터페이스.
MpCmdRun => 멀웨어 방지 프로세스
smartscreen => 멀웨어 , 피싱 방지 소프트웨어
sc.exe => 프로세스 중지 시작 등 관리하는 프로그램
regsvr32 => 레지스트리 등록 취소하는 명령 줄 유틸리티
TiWorker.exe => 컴퓨터가 쉬고있을때 유지보수를 담당 (윈도우 업데이트와 드라이브 업데이트 관리)
TrustedInstaller=>윈도우 업데이트 담당
MoUsoCoreWorker => 절전모드 해제해주는 프로그램
audiodg => 오디오 장치와 그래프 오디오 엔진을 실행 시작시 자동으로 시작
consent.exe=> 인증 레이어인 UAC에 대한 인터페이스를 시작하는 파일
HxTsr=> MS Outlook Communications로 알려진 프로세스임
SppExtComObj=> 키관리 프로세스(KMS)는  최종 사용자가 사용 가능한 데스크톱에 연결해주는 프로세스
LocalBridge.exe => MS office와 관련된 프로그램
MsMpEng=> 악성코드 바이러스 유입을 막는 백신 프로그램
WerFault=>윈도우 에러 리포팅 서비스
runonce=> 컴퓨터를 재부텅 or 시작할때 드라이버와 서비스를 설치해주는 서비스
sysmon64.exe
ClipRenew => 온라인 파일 분석 서비스
```

---

### 02.18

**DNSQuery**

```
.googleapis.com / google로 실행할때 알게모르게 호출하는 주소임 따라서 제외
aa.google.com
ad.wappalyzer.com
```

## ossec.con (wazuh agent)

1. sysmon 설정 추가

## ruleset(wazuh manager)

/var/ossec/ruleset/rules 폴더안에 0595-win-sysmon_rules.xml 파일 수정 => 아래 구문들 바꾸기 (level =0>3으로 수정한것 뿐)

```
  <rule id="61603" level="3">
    <if_sid>61600</if_sid>
    <field name="win.system.eventID">^1$</field>
    <description>Sysmon - Event 1: Process creation $(win.eventdata.description)</description>
    <options>no_full_log</options>
    <group>sysmon_event1,</group>
  </rule>

  <rule id="61604" level="3">
    <if_sid>61600</if_sid>
    <field name="win.system.eventID">^2$</field>
    <description>Sysmon - Event 2: A process changed a file creation time by $(win.eventdata.sourceImage)</description>
    <options>no_full_log</options>
    <group>sysmon_event2,</group>
  </rule>

  <rule id="61605" level="3">
    <if_sid>61600</if_sid>
    <field name="win.system.eventID">^3$</field>
    <description>Sysmon - Event 3: Network connection by $(win.eventdata.sourceImage)</description>
    <options>no_full_log</options>
    <group>sysmon_event3,</group>
  </rule>

  <rule id="61606" level="3">
    <if_sid>61600</if_sid>
    <field name="win.system.eventID">^4$</field>
    <description>Sysmon - Event 4: Sysmon service state changed by $(win.eventdata.sourceImage)</description>
    <options>no_full_log</options>
    <group>sysmon_event4,</group>
  </rule>

  <rule id="61607" level="3">
    <if_sid>61600</if_sid>
    <field name="win.system.eventID">^5$</field>
    <description>Sysmon - Event 5: Process terminated by $(win.eventdata.sourceImage)</description>
    <options>no_full_log</options>
    <group>sysmon_event5,</group>
  </rule>

  <rule id="61608" level="3">
    <if_sid>61600</if_sid>
    <field name="win.system.eventID">^6$</field>
    <description>Sysmon - Event 6: Driver loaded. Signature is $(win.eventdata.signature)</description>
    <options>no_full_log</options>
    <group>sysmon_event6,</group>
  </rule>

  <rule id="61609" level="3">
    <if_sid>61600</if_sid>
    <field name="win.system.eventID">^7$</field>
    <description>Sysmon - Event 7: Image loaded by $(win.eventdata.sourceImage)</description>
    <options>no_full_log</options>
    <group>sysmon_event7,</group>
  </rule>

  <rule id="61610" level="3">
    <if_sid>61600</if_sid>
    <field name="win.system.eventID">^8$</field>
    <description>Sysmon - Event 8: CreateRemoteThread by $(win.eventdata.sourceImage)</description>
    <options>no_full_log</options>
    <group>sysmon_event8,</group>
  </rule>

  <rule id="61611" level="3">
    <if_sid>61600</if_sid>
    <field name="win.system.eventID">^9$</field>
    <description>Sysmon - Event 9: RawAccessRead by $(win.eventdata.sourceImage)</description>
    <options>no_full_log</options>
    <group>sysmon_event9,</group>
  </rule>

  <rule id="61612" level="3">
    <if_sid>61600</if_sid>
    <field name="win.system.eventID">^10$</field>
    <description>Sysmon - Event 10: ProcessAccess by $(win.eventdata.sourceImage)</description>
    <options>no_full_log</options>
    <group>sysmon_event_10,</group>
  </rule>

  <rule id="61613" level="3">
    <if_sid>61600</if_sid>
    <field name="win.system.eventID">^11$</field>
    <description>Sysmon - Event 11: FileCreate by $(win.eventdata.image)</description>
    <options>no_full_log</options>
    <group>sysmon_event_11,</group>
  </rule>

  <rule id="61614" level="3">
    <if_sid>61600</if_sid>
    <field name="win.system.eventID">^12$</field>
    <description>Sysmon - Event 12: RegistryEvent (Object create and delete) by $(win.eventdata.sourceImage)</description>
    <options>no_full_log</options>
    <group>sysmon_event_12,</group>
  </rule>

  <rule id="61615" level="3">
    <if_sid>61600</if_sid>
    <field name="win.system.eventID">^13$</field>
    <description>Sysmon - Event 13: RegistryEvent (Value Set) by $(win.eventdata.Image)</description>
    <options>no_full_log</options>
    <group>sysmon_event_13,</group>
  </rule>

  <rule id="61616" level="3">
    <if_sid>61600</if_sid>
    <field name="win.system.eventID">^14$</field>
    <description>Sysmon - Event 14: RegistryEvent (Key and Value Rename) by $(win.eventdata.Image)</description>
    <options>no_full_log</options>
    <group>sysmon_event_14,</group>
  </rule>

  <rule id="61617" level="3">
    <if_sid>61600</if_sid>
    <field name="win.system.eventID">^15$</field>
    <description>Sysmon - Event 15: FileCreateStreamHash by $(win.eventdata.Image)</description>
    <options>no_full_log</options>
    <group>sysmon_event_15,</group>
  </rule>

  <rule id="61644" level="3">
    <if_sid>61600</if_sid>
    <field name="win.system.eventID">^22$</field>
    <description>Sysmon - Event 22: DNS Query to $(win.eventdata.QueryName) by $(win.eventdata.Image)</description>
    <options>no_full_log</options>
    <group>sysmon_event_15,</group>
  </rule>


```
