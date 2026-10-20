Write-Host "=== Checking Compilers & Running Tests ===" -ForegroundColor Cyan

# 1. Check C
Write-Host "`n--- Testing C ---" -ForegroundColor Yellow
if (Get-Command gcc -ErrorAction SilentlyContinue) {
    Write-Host "gcc detected:" (gcc --version | Select-Object -First 1) -ForegroundColor Green
    gcc test.c -o test_c.exe
    if (Test-Path .\test_c.exe) {
        .\test_c.exe
        Remove-Item .\test_c.exe
    }
} elseif (Get-Command clang -ErrorAction SilentlyContinue) {
    Write-Host "clang detected:" (clang --version | Select-Object -First 1) -ForegroundColor Green
    clang test.c -o test_c.exe
    if (Test-Path .\test_c.exe) {
        .\test_c.exe
        Remove-Item .\test_c.exe
    }
} else {
    Write-Host "No C compiler (gcc / clang) found in PATH." -ForegroundColor Red
}

# 2. Check C++
Write-Host "`n--- Testing C++ ---" -ForegroundColor Yellow
if (Get-Command g++ -ErrorAction SilentlyContinue) {
    Write-Host "g++ detected:" (g++ --version | Select-Object -First 1) -ForegroundColor Green
    g++ test.cpp -o test_cpp.exe
    if (Test-Path .\test_cpp.exe) {
        .\test_cpp.exe
        Remove-Item .\test_cpp.exe
    }
} elseif (Get-Command clang++ -ErrorAction SilentlyContinue) {
    Write-Host "clang++ detected:" (clang++ --version | Select-Object -First 1) -ForegroundColor Green
    clang++ test.cpp -o test_cpp.exe
    if (Test-Path .\test_cpp.exe) {
        .\test_cpp.exe
        Remove-Item .\test_cpp.exe
    }
} else {
    Write-Host "No C++ compiler (g++ / clang++) found in PATH." -ForegroundColor Red
}

# 3. Check Rust
Write-Host "`n--- Testing Rust ---" -ForegroundColor Yellow
if (Get-Command rustc -ErrorAction SilentlyContinue) {
    Write-Host "rustc detected:" (rustc --version) -ForegroundColor Green
    rustc test.rs -o test_rust.exe
    if (Test-Path .\test_rust.exe) {
        .\test_rust.exe
        Remove-Item .\test_rust.exe
    }
} else {
    Write-Host "No Rust compiler (rustc) found in PATH." -ForegroundColor Red
}

Write-Host "`n=== Test Completed ===" -ForegroundColor Cyan
