# 🍔 Big Mac Index – Argentina vs. USA

Análisis del Índice Big Mac para Argentina, comparando el precio local con el de Estados Unidos y calculando la brecha cambiaria respecto al dólar blue.

---

## 📊 ¿Qué hace este proyecto?

Este script carga datos históricos del precio del Big Mac en Argentina y Estados Unidos, calcula el tipo de cambio implícito según la teoría de Paridad del Poder Adquisitivo (PPA), y visualiza la brecha entre ese tipo de cambio teórico y el dólar blue.

El resultado es un gráfico de doble eje que muestra:
- La evolución del precio del Big Mac en USD (Argentina vs. USA)
- La brecha porcentual entre el dólar blue y el tipo de cambio implícito Big Mac

---

## 🧠 Teoría: Paridad del Poder Adquisitivo (PPA)

### ¿Qué es el Índice Big Mac?

El **Índice Big Mac** fue creado por *The Economist* en 1986 como una herramienta informal para evaluar si las monedas están sobre o subvaluadas. Se basa en la **Paridad del Poder Adquisitivo (PPA)**, que postula que, en el largo plazo, los tipos de cambio deberían igualarse de modo que un mismo bien cueste lo mismo en distintos países.

La idea es simple: si una Big Mac cuesta lo mismo (en términos reales) en todo el mundo, los tipos de cambio están en equilibrio.

### Tipo de cambio implícito Big Mac

El tipo de cambio implícito se calcula como:

```
BigMac_Implied_FX = Precio_ARS / Precio_USA
```

Esto responde a: *¿a cuántos pesos debería estar el dólar para que el Big Mac cueste lo mismo en Argentina que en Estados Unidos?*

### Brecha cambiaria (FX Gap)

La brecha porcentual entre el dólar blue y el tipo de cambio implícito se calcula como:

```
FX_Gap_Percent = (Dólar_Blue / BigMac_Implied_FX - 1) × 100
```

- Un valor **positivo** indica que el dólar blue está **por encima** del tipo de cambio que equilibraría los precios → el peso está **subvaluado** según este índice.
- Un valor **negativo** indica que el dólar blue está **por debajo** → el peso estaría **sobrevaluado**.

### Limitaciones del índice

- No considera diferencias en costos de producción, impuestos, alquileres ni poder adquisitivo local.
- Argentina presenta distorsiones estructurales (controles de precios, subsidios, inflación) que afectan la comparabilidad.
- El dólar blue es un mercado informal, lo que añade volatilidad adicional al análisis.

---

## 🗂️ Estructura del proyecto

```
bigmac-argentina/
│
├── data/
│   └── BigMac.xlsx          # Dataset con precios históricos
│
├── data_loader.py            # Carga y preprocesamiento del Excel
├── calculations.py           # Cálculo de métricas (PPA y brecha)
├── visualization.py          # Generación del gráfico
├── main.py                   # Punto de entrada
│
└── README.md
```

---

## ⚙️ Instalación

### Requisitos

- Python 3.11+
- Las siguientes librerías:

```bash
pip install pandas matplotlib openpyxl
```

### Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/bigmac-argentina.git
cd bigmac-argentina
```

---

## ▶️ Uso

Colocá tu archivo de datos en `data/BigMac.xlsx` con las siguientes columnas:

| Columna      | Descripción                                 |
|--------------|---------------------------------------------|
| `Date`       | Fecha de la observación                     |
| `Price_ARS`  | Precio del Big Mac en pesos argentinos      |
| `Price_USD`  | Precio del Big Mac en Argentina en dólares  |
| `Price_USA`  | Precio del Big Mac en Estados Unidos (USD)  |
| `Dolar_Blue` | Tipo de cambio informal (dólar blue)        |

Luego ejecutá:

```bash
python main.py
```

---

## 📈 Ejemplo de output

El gráfico generado muestra dos ejes:

- **Eje izquierdo:** precio del Big Mac en USD para Argentina y USA a lo largo del tiempo.
- **Eje derecho (línea punteada):** brecha porcentual entre el dólar blue y el tipo de cambio implícito Big Mac.

---

## 📚 Referencias

- [The Economist – Big Mac Index](https://www.economist.com/big-mac-index)
- Pakko, M. R. & Pollard, P. S. (1996). *For Here or To Go? Purchasing Power Parity and the Big Mac.* Federal Reserve Bank of St. Louis Review.

---

## 📝 Licencia

MIT License. Libre para usar, modificar y distribuir.
