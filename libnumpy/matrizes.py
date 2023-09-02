import numpy as np
import numpy as np

def main():
    # Criando um array
    arr = np.array([1, 2, 3, 4, 5])

    # Imprimindo o array
    print("Array:", arr)

    # Imprimindo o número de dimensões do array
    print("Número de dimensões:", arr.ndim)

    # Imprimindo o formato (shape) do array
    print("Formato (shape):", arr.shape)

    # Imprimindo o tamanho do array
    print("Tamanho do array:", arr.size)

    # Imprimindo o tipo de dados do array
    print("Tipo de dados:", arr.dtype)

    # Realizando operações matemáticas com arrays
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])

    # Soma de arrays
    print("Soma de arrays:", np.add(arr1, arr2))

    # Subtração de arrays
    print("Subtração de arrays:", np.subtract(arr1, arr2))

    # Produto de arrays
    print("Produto de arrays:", np.multiply(arr1, arr2))

    # Divisão de arrays
    print("Divisão de arrays:", np.divide(arr1, arr2))

    # Criando um array com valores aleatórios
    random_arr = np.random.rand(5)
    print("Array aleatório:", random_arr)

    # Encontrando o valor máximo e mínimo em um array
    print("Máximo:", np.max(random_arr))
    print("Mínimo:", np.min(random_arr))

    # Ordenando um array
    sorted_arr = np.sort(arr)
    print("Array ordenado:", sorted_arr)

if __name__ == '__main__':
    main()



