# 📌 Suggested Issues for `ferri-syscheck`

This document lists some starter issues and enhancements that contributors can work on.  
Feel free to pick one, or suggest new improvements!

---

## 🔹 1. Add More System Checks
- Extend functionality by checking:
  - Disk usage
  - Memory consumption
  - CPU temperature
- **Labels**: `enhancement`, `help wanted`

---

## 🔹 2. Improve Error Handling
- Show clear error messages when a check fails (e.g., "Python not installed" instead of just failing).
- **Labels**: `bug`, `good first issue`

---

## 🔹 3. Add Unit Tests
- Write tests for each system check to improve reliability.
- Make sure tests run in Linux/Termux environments.
- **Labels**: `testing`, `good first issue`

---

## 🔹 4. Make Output More User-Friendly
- Add ✅ / ❌ icons or colored text for results.
- Optional: Print results in a clean table format.
- **Labels**: `enhancement`, `UX`

---

## 🔹 5. Cross-Platform Support
- Adapt the script to work on **Windows** and **macOS**.
- Detect OS automatically and run the right checks.
- **Labels**: `enhancement`, `help wanted`

---

## 🔹 6. Create GitHub Actions Workflow
- Add CI to automatically:
  - Run system checks
  - Test pull requests
- **Labels**: `automation`, `good first issue`

---

## 🔹 7. Add Documentation Examples
- Improve the `README.md` with usage examples:
  ```bash
  python syscheck.py
