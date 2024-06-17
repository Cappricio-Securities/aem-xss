<div align="center">
  <img src="https://blogs.cappriciosec.com/uploaders/aem-xss-tool.png" alt="logo">
</div>


## Badges



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![PyPI - Version](https://img.shields.io/pypi/v/aem-xss)
![PyPI - Downloads](https://img.shields.io/pypi/dm/aem-xss)
![GitHub all releases](https://img.shields.io/github/downloads/Cappricio-Securities/aem-xss)
<a href="https://github.com/Cappricio-Securities/CVE-2023-27524/releases/"><img src="https://img.shields.io/github/release/Cappricio-Securities/aem-xss"></a>![Profile_view](https://komarev.com/ghpvc/?username=Cappricio-Securities&label=Profile%20views&color=0e75b6&style=flat)
[![Follow Twitter](https://img.shields.io/twitter/follow/cappricio_sec?style=social)](https://twitter.com/cappricio_sec)
<p align="center">

<p align="center">







## License

[MIT](https://choosealicense.com/licenses/mit/)



## Installation 

1. Install Python3 and pip [Instructions Here](https://www.python.org/downloads/) (If you can't figure this out, you shouldn't really be using this)

   - Install via pip
     - ```bash
          pip install aem-xss 
        ```
   - Run bellow command to check
     - `aem-xss -h`

## Configurations 
2. We integrated with the Telegram API to receive instant notifications for vulnerability detection.
   
   - Telegram Notification
     - ```bash
          aem-xss --chatid <YourTelegramChatID>
        ```
   - Open your telegram and search for [`@CappricioSecuritiesTools_bot`](https://web.telegram.org/k/#@CappricioSecuritiesTools_bot) and click start

## Usages 
3. This tool has multiple use cases.
   
   - To Check Single URL
     - ```bash
          aem-xss -u http://example.com 
        ```
   - To Check List of URL 
      - ```bash
          aem-xss -i urls.txt 
        ```
   - Save output into TXT file
      - ```bash
          aem-xss -i urls.txt -o out.txt
        ```
   - Want to Learn about [`aem-xss`](https://blogs.cappriciosec.com/blog/190/aem-xss)? Then Type Below command
      - ```bash
         aem-xss -b
        ```
     
<p align="center">
  <b>🚨 Disclaimer</b>
  
</p>
<p align="center">
<b>This tool is created for security bug identification and assistance; Cappricio Securities is not liable for any illegal use. 
  Use responsibly within legal and ethical boundaries. 🔐🛡️</b></p>


## Working PoC Video

[![asciicast](https://blogs.cappriciosec.com/uploaders/Screenshot%202024-06-17%20at%202.38.35%20PM.png)](https://asciinema.org/a/2pdaUbFFEARv6ywnte3UVkELE)




## Help menu

#### Get all items

```bash
👋 Hey Hacker
                                              v1.0
    ___                       _  ____________
   /   | ___  ____ ___       | |/ / ___/ ___/
  / /| |/ _ \/ __ `__ \______|   /\__ \__ \
 / ___ /  __/ / / / / /_____/   |___/ /__/ /
/_/  |_\___/_/ /_/ /_/     /_/|_/____/____/

                              Developed By https://cappriciosec.com


aem-xss : Bug scanner for WebPentesters and Bugbounty Hunters

$ aem-xss [option]

Usage: aem-xss [options]
```


| Argument | Type     | Description                | Examples |
| :-------- | :------- | :------------------------- | :------------------------- |
| `-u` | `--url` | URL to scan | aem-xss -u https://target.com |
| `-i` | `--input` | filename Read input from txt  | aem-xss -i target.txt | 
| `-o` | `--output` | filename Write output in txt file | aem-xss -i target.txt -o output.txt |
| `-c` | `--chatid` | Creating Telegram Notification | aem-xss --chatid yourid |
| `-b` | `--blog` | To Read about aem-xss Bug | aem-xss -b |
| `-h` | `--help` | Help Menu | aem-xss -h |



## 🔗 Links
[![Website](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://cappriciosec.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/karthikeyan--v/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/karthithehacker)



## Author

- [@karthithehacker](https://github.com/karthi-the-hacker/)



## Feedback

If you have any feedback, please reach out to us at contact@karthithehacker.com


