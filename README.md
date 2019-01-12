
**Install build dependencies:**
```shell
sudo apt install python3 python3-pip clang-tidy g++
pip install --user conan ninja cmake
```

**Install library dependencies:**
```shell
conan install . -if build -o build_tests=True
```

**Build project:**
```shell
conan build . -bf build
```
