def faktorial(n):
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)

# ini bagian input dari pengguna
n = int(input("Masukkan angka untuk dihitung faktorialnya: "))
print("Faktorial dari", n, "adalah", faktorial(n))
