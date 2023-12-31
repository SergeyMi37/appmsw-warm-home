![](https://raw.githubusercontent.com/SergeyMi37/appmsw-warm-home/master/doc/warmhome.png)
## apptools-warm-home

[![OEX](https://img.shields.io/badge/Available%20on-Intersystems%20Open%20Exchange-00b2a9.svg)](https://openexchange.intersystems.com/package/appmsw-warm-home) 
[![Demo](https://img.shields.io/badge/Demo%20on-Cloud%20Run%20Deploy-F4A460)](https://warmhome.demo.community.intersystems.com/apptoolsrest/a/warmhome&namespace=USER)
[![license](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Quality Gate Status](https://community.objectscriptquality.com/api/project_badges/measure?project=intersystems_iris_community%2Fzapm&metric=alert_status)](https://community.objectscriptquality.com/dashboard?id=intersystems_iris_community%2Fappmsw-warm-home)

Template and examples for creating a user interface for a smart home

The project includes a python [program](https://raw.githubusercontent.com/SergeyMi37/appmsw-warm-home/master/python/check-send.py) for `Raspberry Pi` to read the temperature sensor and send a message to the telebot

## Installation with ZPM

If ZPM the current instance is not installed, then in one line you can install the latest version of ZPM.
```
set $namespace="%SYS", name="DefaultSSL" do:'##class(Security.SSLConfigs).Exists(name) ##class(Security.SSLConfigs).Create(name) set url="https://pm.community.intersystems.com/packages/zpm/latest/installer" Do ##class(%Net.URLParser).Parse(url,.comp) set ht = ##class(%Net.HttpRequest).%New(), ht.Server = comp("host"), ht.Port = 443, ht.Https=1, ht.SSLConfiguration=name, st=ht.Get(comp("path")) quit:'st $System.Status.GetErrorText(st) set xml=##class(%File).TempFilename("xml"), tFile = ##class(%Stream.FileBinary).%New(), tFile.Filename = xml do tFile.CopyFromAndSave(ht.HttpResponse.Data) do ht.%Close(), $system.OBJ.Load(xml,"ck") do ##class(%File).Delete(xml)
```
If ZPM is installed, then ZAPM can be set with the command
```
zpm:USER>install apptools-warmhome
```
## Installation with Docker

## Prerequisites
Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker desktop](https://www.docker.com/products/docker-desktop) installed.

## Installation 
Clone/git pull the repo into any local directory

```
$ git clone https://github.com/SergeyMi37/appmsw-warm-home.git
```

Open the terminal in this directory and run:

```
$ docker-compose build
```

3. Run the IRIS container with your project:

```
$ docker-compose up -d
```

## How to Test it
Open IRIS terminal:

```
$ docker-compose exec iris iris session iris
USER>
USER>zpm
zpm:USER>install appmsw-warm-home
```
