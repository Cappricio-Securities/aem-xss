#!/usr/bin/env python

"""
 * aem-xss
 * aem-xss Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */

"""
import getpass
username = getpass.getuser()


def display_help():
    help_banner = f"""

👋 Hey \033[96m{username}
   \033[92m                                           v1.0
    ___                       _  ____________
   /   | ___  ____ ___       | |/ / ___/ ___/
  / /| |/ _ \/ __ `__ \______|   /\__ \\__ \\
 / ___ /  __/ / / / / /_____/   |___/ /__/ /
/_/  |_\___/_/ /_/ /_/     /_/|_/____/____/

                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1maem-xss : Bug scanner for WebPentesters and Bugbounty Hunters

\x1b[31;1m$ \033[92maem-xss\033[0m [option]

Usage: \033[92maem-xss\033[0m [options]

Options:
  -u, --url     URL to scan                                aem-xss -u https://target.com
  -i, --input   <filename> Read input from txt             aem-xss -i target.txt
  -o, --output  <filename> Write output in txt file        aem-xss -i target.txt -o output.txt
  -c, --chatid  Creating Telegram Notification             aem-xss --chatid yourid
  -b, --blog    To Read about aem-xss Bug                  aem-xss -b
  -h, --help    Help Menu
    """
    print(help_banner)


def banner():
    help_banner = f"""
    \033[94m
👋 Hey \033[96m{username}
      \033[92m                                      v1.0
    ___                       _  ____________    
   /   | ___  ____ ___       | |/ / ___/ ___/
  / /| |/ _ \/ __ `__ \______|   /\__ \\__  \\
 / ___ /  __/ / / / / /_____/   |___/ /__/ /
/_/  |_\___/_/ /_/ /_/     /_/|_/____/____/

                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1maem-xss : Bug scanner for WebPentesters and Bugbounty Hunters

\033[0m"""
    print(help_banner)
