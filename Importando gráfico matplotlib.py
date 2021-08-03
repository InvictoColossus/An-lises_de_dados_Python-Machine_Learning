import matplotlib.pyplot as plt
nomes = ['rafael','maria','ana']
idades = [10,20,15]

plt.figure(figsize=(5,2))
plt.bar(nomes,idades)
plt.xlabel('nomes')
plt.ylabel('idades')

plt.plot(nomes,idades)
