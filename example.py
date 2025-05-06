"""
⚠️ WARNING: EDUCATIONAL USE ONLY ⚠️

Microsoft Account Login Example using MailHub
-------------------------------------------
This example demonstrates how to use the MailHub library for Microsoft account authentication.
Use only with accounts you own or have permission to test.

DISCLAIMER:
- Never share your real credentials in code
- This is for educational purposes only
- Unauthorized access violates Microsoft's ToS
"""

from mailhub.mailhub import MailHub

def safe_input(prompt, hide=False):
    """Safely handle user input with optional hiding"""
    import getpass
    return getpass.getpass(prompt) if hide else input(prompt)

def main():
    print("""
    ███╗   ███╗ █████╗ ██╗██╗     ██╗  ██╗██╗   ██╗██████╗ 
    ████╗ ████║██╔══██╗██║██║     ██║  ██║██║   ██║██╔══██╗
    ██╔████╔██║███████║██║██║     ███████║██║   ██║██████╔╝
    ██║╚██╔╝██║██╔══██║██║██║     ██╔══██║██║   ██║██╔══██╗
    ██║ ╚═╝ ██║██║  ██║██║███████╗██║  ██║╚██████╔╝██║  ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
    """)
    
    print("⚠️ WARNING: Use only with test accounts you own ⚠️\n")
    
    # Initialize MailHub
    mailhub = MailHub()
    
    # Get credentials (in production, use environment variables)
    email = safe_input("Enter TEST email (e.g., example@outlook.com): ")
    password = safe_input("Enter TEST password: ", hide=True)
    
    # Proxy configuration (optional)
    use_proxy = safe_input("Use proxy? (y/n): ").lower() == 'y'
    proxy = None
    
    if use_proxy:
        proxy = {
            "http": safe_input("HTTP proxy (e.g., http://user:pass@ip:port): "),
            "https": safe_input("HTTPS proxy (e.g., http://user:pass@ip:port): ")
        }
    
    print(f"\nAttempting login with: {email[:3]}...{email[-10:]}")
    
    try:
        result = mailhub.loginMICROSOFT(email, password, proxy)
        
        if result[0] == "ok":
            print("\n✅ Login successful (Demo Only!)")
            print(f"Session token: {result[1][:15]}... (truncated)")
        elif result[0] == "nfa":
            print("\n⚠️  Additional verification required (NFA)")
        elif result[0] == "custom":
            print("\n⛔ Account has special restrictions")
        elif result[0] == "fail":
            print("\n❌ Login failed - Invalid credentials")
        elif result[0] == "retry":
            print("\n🔄 Temporary error - Try again later")
        else:
            print("\n❓ Unknown response:", result)
            
    except Exception as e:
        print(f"\n🔥 Error: {str(e)}")
        print("Please check your network connection or library documentation")

if __name__ == "__main__":
    print(__doc__)
    confirm = input("\nDo you understand this is for EDUCATIONAL USE ONLY? (y/n): ")
    if confirm.lower() == 'y':
        main()
    else:
        print("Operation cancelled")
