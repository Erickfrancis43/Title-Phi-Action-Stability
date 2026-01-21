
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def auditoria_residuos_campo():
hbar = 6.582119569e-16

# Base de Dados (Mesma do script anterior)  
data = [  
    ("Próton", 938.27e6, 1e35), ("Elétron", 0.511e6, 1e30), ("Neutrino", 0.1, 1e20),  
    ("Nêutron", 939.56e6, 880.0), ("Múon", 105.65e6, 2.19e-6), ("Káon L", 497.61e6, 5.11e-8),  
    ("Píon+", 139.57e6, 2.60e-8), ("Káon S", 497.61e6, 8.95e-11), ("Tau", 1776.8e6, 2.90e-13),  
    ("Lambda", 1115e6, 2.6e-10), ("Higgs", 125.1e9, 1.56e-22), ("Top Quark", 172.7e9, 5.0e-25),  
    ("Bóson Z", 91.18e9, 2.6e-25), ("Bóson W", 80.37e9, 3.0e-25), ("Píon 0", 134.97e6, 8.4e-17)  
]  
  
df = pd.DataFrame(data, columns=["Nome", "Massa", "Vida"])  
df["Phi"] = np.log10((df["Massa"] * df["Vida"]) / hbar)  
df["LogVida"] = np.log10(df["Vida"])  
  
# 1. Regressão Linear Global  
slope, intercept, r_val, p_val, std_err = linregress(df["Phi"], df["LogVida"])  
  
# 2. Cálculo dos Resíduos (Vida Real - Vida Prevista pela Reta)  
df["Predicao"] = slope * df["Phi"] + intercept  
df["Residuo"] = df["LogVida"] - df["Predicao"]  
  
# 3. Visualização do "Kink" de Transição  
plt.figure(figsize=(12, 6))  
  
# Plot dos Resíduos  
plt.scatter(df["Phi"], df["Residuo"], color='purple', s=100, edgecolors='black', label="Desvio do Campo")  
  
# Linha Zero (Onde a física seria linear e trivial)  
plt.axhline(y=0, color='black', linestyle='--', alpha=0.5)  
  
# Limiar Crítico  
plt.axvline(x=25, color='red', linestyle=':', label="Limiar de Transição (Phi ≈ 25)")  
  
for i, txt in enumerate(df["Nome"]):  
    plt.annotate(txt, (df["Phi"].iloc[i], df["Residuo"].iloc[i]), xytext=(5,5), textcoords='offset points')  

plt.xlabel("Φ (Ação Relativa)", fontsize=12)  
plt.ylabel("Resíduo (Diferença Logarítmica)", fontsize=12)  
plt.title("AUDITORIA DE RESÍDUOS: A QUEBRA DA LINEARIDADE", fontsize=14, fontweight='bold')  
plt.grid(True, alpha=0.2)  
plt.legend()  
plt.show()  

return df[["Nome", "Phi", "Residuo"]].sort_values(by="Phi", ascending=False)

df_res = auditoria_residuos_campo()
print(df_res.to_string(index=False))

results

Nome       Phi   Residuo
Próton 59.153962 -4.143525
Elétron 50.890055 -0.141037
Neutrino 34.181634  8.060689
Nêutron 27.099041 -1.279234
Múon 17.545948  0.523623
Káon L 16.586944 -0.063686
Píon+ 15.741400  0.563981
Lambda 14.643882 -0.240412
Káon S 13.830346  0.182683
Tau 11.893671 -0.196977
Píon 0  7.236151  1.338687
Higgs  4.472016 -1.381291
Top Quark  2.117897 -1.310928
Bóson W  1.563849 -0.929212
Bóson Z  1.556507 -0.983361
