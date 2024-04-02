import random

def add_random_elements(my_list):
    """Extend 4 elemen acak."""
    random_elements = [random.randint(1, 50) for _ in range(4)]
    my_list.extend(random_elements)
    print("\n=====================================================================================")
    print("Setelah menambahkan 4 elemen numerik acak:", my_list)

def remove_odd_index_elements(my_list):
    """Delete indeks ganjil."""
    my_list = [elem for idx, elem in enumerate(my_list) if idx % 2 == 0]
    print("Setelah menghapus elemen di indeks ganjil:", my_list)
    return my_list

def reverse_list(my_list):
    """Reverse elemen dalam list."""
    my_list.reverse()
    print("Setelah membalik urutan elemen dalam list:", my_list)

def duplicate_first_element(my_list):
    """Menggandakan elemen pertama dan menambahkannya ke akhir list."""
    first_element = my_list[0]
    my_list.append(first_element * 2)
    print("Setelah menggandakan elemen pertama dan menambahkannya ke akhir list:", my_list)

def remove_min_value(my_list):
    """Mencari dan menghapus elemen dengan nilai terkecil dalam list."""
    min_value = min(my_list)
    my_list.remove(min_value)
    print("Setelah menghapus elemen dengan nilai terkecil:", my_list)

def sort_list_ascending(my_list):
    """Mengurutkan list secara ascending."""
    my_list.sort()
    print("Setelah mengurutkan list secara ascending:", my_list)
    print("=====================================================================================")

def manipulate_list(my_list):
    """Fungsi utama untuk memanipulasi list sesuai dengan langkah-langkah yang diminta."""
    add_random_elements(my_list)
    my_list = remove_odd_index_elements(my_list)
    reverse_list(my_list)
    duplicate_first_element(my_list)
    remove_min_value(my_list)
    sort_list_ascending(my_list)
    return my_list

# Contoh penggunaan program
input_list = []
manipulated_list = manipulate_list(input_list)  # Input awal menggunakan list kosong
print()
print("====================================")
print("List setelah dimanipulasi:", manipulated_list)
print("====================================")