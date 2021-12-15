**Автотесты Appium**

**Для запуска автотестов на appium необходмимо**:

- install python
- install pycharm
- install jdk and set environment variables
- install node js
- install android studio
- install appium desktop application


**Настройка переменных. Редактирование баш файла**

Открыть баш файл:


```
user@ip-192-168-0-27 ~ % vi ~/.bash_profile
``` 

где
```i``` - insert (редактировать),
```esc :qw``` - выход из баш файла

Вставить это в файл:

```
export JAVA_HOME=$(/usr/libexec/java_home)
export PATH=$PATH:/usr/local/git/bin:/usr/local/bin:
export ANDROID_HOME=/users/user/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/emulator
```

Сохранить файл:

```
user@ip-192-168-0-27 ~ % source ~/.bash_profile  
```


**Запуск тестов**
1. Установка Appium-Python-Client

    ```
    pip install Appium-Python-Client
    ```

2. Запуск appium сервера

   ```
   appium --address 127.0.0.1 --port 4723 
   ```
   
3. Запуск тестов

   ```
   pytest
   ```