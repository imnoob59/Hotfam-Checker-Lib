# 🛡️ MailHub Example - Security Demonstration

```diff
- IMPORTANT LEGAL NOTICE:
! This demonstration is for EDUCATIONAL PURPOSES ONLY
! Unauthorized access to computer systems violates:
! - Microsoft Terms of Service
! - Computer Fraud and Abuse Act (US)
! - GDPR (EU)
! - Various international cybercrime laws
```

## 🔒 Safe Usage Guidelines

1. **Only test with accounts you OWN**
2. **Never store real credentials in code**
3. **Use environment variables for secrets**
   ```python
   import os
   email = os.getenv('TEST_EMAIL')
   ```

## 🚀 Quick Start

1. Install package:
```bash
pip install mailhub
```

2. Clone this repo:
```bash
https://github.com/imnoob59/Hotfam-Checker-Lib.git
```

3. Run with dummy account:
```bash
python example.py
> Enter TEST email: example@outlook.com
> Enter TEST password: [hidden]
```

## ⚠️ Common Scenarios

| Response  | Meaning                     | Legal Status          |
|-----------|-----------------------------|-----------------------|
| OK        | Demo successful             | ✅ Allowed if authorized |
| NFA       | Needs verification          | ⚠️ Proceed with caution |
| FAIL      | Invalid credentials         | ❌ STOP immediately    |

## 📜 Full Disclaimer

> This software is provided "as is" without warranty. The authors disclaim all liability for unauthorized use. By using this code, you affirm that:
> 
> 1. You have permission to test target accounts
> 2. You understand computer crime laws apply
> 3. You accept all responsibility for your actions
