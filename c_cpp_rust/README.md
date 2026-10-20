# C, C++, and Rust Environment Verification

This folder contains test files to verify compiler installations, execution, and IDE extensions.

## Files
- [`test.c`](file:///c:/Users/trahu/OneDrive/Desktop/CodeWorld/Machine_Learning/c_cpp_rust/test.c) - Minimal C verification program
- [`test.cpp`](file:///c:/Users/trahu/OneDrive/Desktop/CodeWorld/Machine_Learning/c_cpp_rust/test.cpp) - Minimal C++ verification program
- [`test.rs`](file:///c:/Users/trahu/OneDrive/Desktop/CodeWorld/Machine_Learning/c_cpp_rust/test.rs) - Minimal Rust verification program
- [`run_tests.ps1`](file:///c:/Users/trahu/OneDrive/Desktop/CodeWorld/Machine_Learning/c_cpp_rust/run_tests.ps1) - Automated PowerShell script to check compilers and run all tests

---

## 1. Quick Automated Test

Open PowerShell in this folder and run:
```powershell
.\run_tests.ps1
```

---

## 2. Manual Commands

### C
```powershell
gcc test.c -o test_c.exe
.\test_c.exe
```

### C++
```powershell
g++ test.cpp -o test_cpp.exe
.\test_cpp.exe
```

### Rust
```powershell
rustc test.rs -o test_rust.exe
.\test_rust.exe
```

---

## 3. Recommended Extensions

1. **C / C++**: Search and install `C/C++` (Microsoft) or `clangd`.
2. **Rust**: Search and install `rust-analyzer`.
