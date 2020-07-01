a, b, c, d = map(float, input().split())
media = ((a * 2) + (b * 3) + (c * 4) + (d * 1)) / 10

print("Media: %.1f" % media)

if media >= 7.0:

    print("Aluno aprovado.")
elif media < 5.0:

    print("Aluno reprovado.")

elif media >= 5.0 and media <= 6.9:
    print("Aluno em exame.")
    extra = float(input())
    print("Nota do exame: %.1f" % extra)
    sum = (media + extra) / 2
    if sum >= 5.0:
        print("Aluno aprovado.")
        print("Media final: %.1f" % sum)
    elif sum <= 4.9:
        print("Aluno reprovado.")
        print("Media final: %.1f" % sum)
