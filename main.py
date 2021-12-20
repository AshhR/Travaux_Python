# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def fibo(a):
    # Commentaire
    if a == 0 or a == 1:
        return a
    else:
        return fibo(a - 1) + fibo(a - 2)


