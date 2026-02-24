# ==========================================
# CTF-COACH
# Graduation Project - Single File Version
# Interactive Step-by-Step CTF Methodology
# ==========================================

def banner():
    print("\n" + "="*75)
    print("🧠 CTF-COACH | Interactive CTF Training Assistant")
    print("🎓 Graduation Project Edition")
    print("="*75)

def ask(question):
    return input(f"\n❓ {question}\n> ").lower()

def step(title, content):
    print("\n" + "-"*75)
    print(f"🔹 {title}")
    print("-"*75)
    print(content)

def main():
    banner()

    target = input("\n📍 Enter Target IP / URL: ")

    # STEP 1: NMAP
    step(
        "STEP 1: Reconnaissance (Nmap)",
        f"""
✍️ Run this command:
nmap -sC -sV {target}

🎯 Goal:
Discover open ports and running services.
"""
    )

    services = ask("What services or ports did you find? (example: http ssh ftp)")

    # WEB PATH
    if "http" in services:
        step(
            "STEP 2: Web Service Detected",
            f"""
✍️ Open in browser:
http://{target}

👀 Look for:
- Login pages
- URL parameters
- Error messages
"""
        )

        web_obs = ask("What did you notice on the website? (login / parameters / empty page)")

        step(
            "STEP 3: Directory Enumeration",
            f"""
✍️ Run:
gobuster dir -u http://{target} -w /usr/share/wordlists/dirb/common.txt

🎯 Goal:
Find hidden directories.
"""
        )

        dirs = ask("Which directories were found? (admin / upload / backup / none)")

        # Upload
        if "upload" in dirs:
            step(
                "STEP 4: File Upload Analysis",
                """
👀 Focus on:
- Allowed file types
- Extension filtering
- Upload location

✍️ Try uploading a test file.
"""
            )

            shell = ask("Were you able to upload a shell? (yes/no)")

            if "yes" in shell:
                step(
                    "STEP 5: Web Shell Obtained",
                    """
✍️ Run inside the shell:
whoami
id
uname -a

🎯 Goal:
Identify current user and system.
"""
                )
            else:
                step(
                    "STEP 5: Upload Failed",
                    """
🔍 Try:
- shell.php.jpg
- Changing Content-Type
- Bypassing extension filters
"""
                )

        # Login
        elif "admin" in dirs or "login" in web_obs:
            step(
                "STEP 4: Login Page Analysis",
                """
👀 Test for:
- SQL Injection
- Authentication bypass
- Default credentials

✍️ Example test:
admin' OR '1'='1
"""
            )

            login = ask("Did you manage to login? (yes/no)")

            if "yes" in login:
                step(
                    "STEP 5: Authenticated Access",
                    """
🔍 Look for:
- File upload
- Settings panels
- Command execution features
"""
                )
            else:
                step(
                    "STEP 5: Login Failed",
                    """
🔍 Focus on:
- Parameters
- Cookies
- Source code
"""
                )

        else:
            step(
                "STEP 4: No Interesting Directories",
                """
🔍 Focus on:
- URL parameters (id=, page=)
- JavaScript files
- LFI / XSS testing
"""
            )

    else:
        step(
            "STEP 2: No Web Service Found",
            """
🔍 Focus on:
- FTP anonymous access
- Service version exploits
- Credential reuse
"""
        )

    # PRIVILEGE ESCALATION
    got_shell = ask("Did you obtain a shell on the system? (yes/no)")

    if "yes" in got_shell:
        step(
            "STEP 6: Privilege Escalation Enumeration",
            """
✍️ Run:
sudo -l
id
find / -perm -4000 2>/dev/null

🎯 Goal:
Find privilege escalation vectors.
"""
        )

        privesc = ask("What caught your attention? (sudo / suid / cron / nothing)")

        if "sudo" in privesc:
            step(
                "STEP 7: Sudo Privilege Abuse",
                """
👀 If NOPASSWD is present:
- Search GTFOBins
- Check allowed commands
"""
            )

        elif "suid" in privesc:
            step(
                "STEP 7: SUID Exploitation",
                """
👀 Look for exploitable SUID binaries:
- find
- vim
- python
- bash
"""
            )

        elif "cron" in privesc:
            step(
                "STEP 7: Cron Jobs",
                """
👀 Check:
- Writable scripts
- PATH hijacking
"""
            )

        else:
            step(
                "STEP 7: Manual Privilege Escalation",
                """
🔍 Check:
- Kernel exploits
- Configuration files
- Stored credentials
"""
            )

    print("\n" + "="*75)
    print("🏁 Training Session Completed")
    print("💡 You followed a real CTF methodology — no spoilers, pure learning.")
    print("="*75)

if __name__ == "__main__":
    main()
