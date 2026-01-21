Import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def auditoria_lei_de_escala():
# Constante de Planck reduzida (eV.s)
hbar = 6.582119569e-16

# 1. BASE DE DADOS EXPANDIDA (32 Partículas)  
# Nome, Massa (eV), Vida Média (s), Categoria  
data = [  
    # Estáveis (Valores de vida mínima observada)  
    ("Próton", 938.27e6, 1e35, "Estável"),  
    ("Elétron", 0.511e6, 1e30, "Estável"),  
    ("Neutrino e", 0.1, 1e20, "Estável"),  
    ("Neutrino m", 0.1, 1e20, "Estável"),  
    ("Neutrino t", 0.1, 1e20, "Estável"),  
      
    # Quase-Estáveis e Penumbra  
    ("Nêutron", 939.56e6, 880.0, "Penumbra"),  
    ("Múon", 105.65e6, 2.19e-6, "Penumbra"),  
    ("Káon Longo", 497.61e6, 5.11e-8, "Penumbra"),  
    ("Píon Carregado", 139.57e6, 2.60e-8, "Penumbra"),  
      
    # Instáveis (Decaimento Fraco/Forte)  
    ("Káon Curto", 497.61e6, 8.95e-11, "Instável"),  
    ("Tau", 1776.8e6, 2.90e-13, "Instável"),  
    ("B Quon", 5279e6, 1.5e-12, "Instável"),  
    ("D Quon", 1864e6, 1.0e-12, "Instável"),  
    ("Lambda", 1115e6, 2.6e-10, "Instável"),  
    ("Sigma 0", 1192e6, 7.4e-20, "Instável"),  
    ("Píon Neutro", 134.97e6, 8.4e-17, "Instável"),  
    ("Eta", 547.8e6, 5.0e-19, "Instável"),  
      
    # Colapso (Bósons e Ressonâncias)  
    ("Higgs", 125.1e9, 1.56e-22, "Colapso"),  
    ("Top Quark", 172.7e9, 5.0e-25, "Colapso"),  
    ("Bóson Z", 91.18e9, 2.6e-25, "Colapso"),  
    ("Bóson W", 80.37e9, 3.0e-25, "Colapso"),  
    ("Ressonância Rho", 775e6, 4.4e-24, "Colapso"),  
    ("Ressonância Delta", 1232e6, 5.6e-24, "Colapso"),  
    ("Omega-", 1672e6, 8.2e-11, "Instável"),  
    ("Xi-", 1321e6, 1.6e-10, "Instável"),  
    ("Sigma+", 1189e6, 8.0e-11, "Instável"),  
    ("Phi", 1019e6, 1.5e-22, "Colapso"),  
    ("J/Psi", 3096e6, 7.1e-21, "Colapso"),  
    ("Upsilon", 9460e6, 1.2e-20, "Colapso"),  
    ("Psi(2S)", 3686e6, 2.1e-21, "Colapso"),  
    ("Kaon*", 892e6, 1.3e-23, "Colapso"),  
    ("Sigma*", 1385e6, 1.8e-23, "Colapso")  
]  
  
# 2. PROCESSAMENTO  
df = pd.DataFrame(data, columns=["Nome", "Massa", "Vida", "Cat"])  
df["Phi"] = np.log10((df["Massa"] * df["Vida"]) / hbar)  
df["LogVida"] = np.log10(df["Vida"])  
  
# 3. REGRESSÃO LINEAR (Apenas instáveis para evitar o 'infinito' das estáveis)  
df_reg = df[df["Cat"] != "Estável"]  
slope, intercept, r_val, p_val, std_err = linregress(df_reg["Phi"], df_reg["LogVida"])  
  
# 4. PLOTAGEM  
plt.figure(figsize=(12, 8))  
colors = {"Estável": "blue", "Penumbra": "green", "Instável": "orange", "Colapso": "red"}  
  
for cat, group in df.groupby("Cat"):  
    plt.scatter(group["Phi"], group["LogVida"], label=cat, color=colors[cat], s=100, edgecolors='black')  
    for i, txt in enumerate(group["Nome"]):  
        plt.annotate(txt, (group["Phi"].iloc[i], group["LogVida"].iloc[i]), xytext=(5,5), textcoords='offset points', fontsize=9)  

# Linha de Regressão  
x_line = np.linspace(df["Phi"].min(), df["Phi"].max(), 100)  
plt.plot(x_line, slope * x_line + intercept, color="black", linestyle="--", alpha=0.5, label=f"R² = {r_val**2:.4f}")  

# Limiar Crítico  
plt.axvline(x=25, color='purple', linestyle='-', linewidth=2, label="Limiar de Estabilidade (Phi ≈ 25)")  
  
plt.xlabel("Φ (Ação Relativa: log10(S/hbar))", fontsize=12)  
plt.ylabel("log10(Vida Média [s])", fontsize=12)  
plt.title("Auditoria de Unificação: Lei de Escala da Ação", fontsize=15, fontweight='bold')  
plt.legend()  
plt.grid(True, alpha=0.3)  
plt.show()  

return df.sort_values(by="Phi", ascending=False), r_val**2, slope

Execução

df_audit, r2, inclina = auditoria_lei_de_escala()
print(f"R² da Correlação: {r2:.4f}")
print(f"Inclinação da Reta: {inclina:.4f}")
print("\nTABELA DE AUDITORIA (TOP 10):")
print(df_audit[["Nome", "Phi", "Cat"]].head(10).to_string(index=False))

Results

R² da Correlação: 0.9890
Inclinação da Reta: 1.0560

TABELA DE AUDITORIA (TOP 10):
Nome       Phi      Cat
Próton 59.153962  Estável
Elétron 50.890055  Estável
Neutrino e 34.181634  Estável
Neutrino m 34.181634  Estável
Neutrino t 34.181634  Estável
Nêutron 27.099041 Penumbra
Múon 17.545948 Penumbra
Káon Longo 16.586944 Penumbra
Píon Carregado 15.741400 Penumbra
Lambda 14.643882 Instável
