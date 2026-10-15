# Ideas de El León de Wall Street

Dashboard público con las ideas de inversión de la comunidad: compras, ventas y rendimiento vs S&P 500 y QQQ.

## Cómo agregar o quitar operaciones

Edita `data/trades.csv` (en GitHub: abre el archivo, lápiz ✏️, "Commit changes"). Al guardar, GitHub Actions baja los precios y republica la página en 1 a 2 minutos.

Columnas:

| columna | qué va | ejemplo |
|---|---|---|
| id | identificador único | t17 |
| date | fecha AAAA-MM-DD | 2026-10-20 |
| ticker | ticker de Yahoo Finance | TSLA |
| side | `buy` o `sell` | buy |
| price | precio de la operación | 250 |
| usd | monto de la compra (vacío en ventas por %) | 100 |
| fraction | en ventas: parte de la posición que vendes (1 = todo, 0.5 = mitad) | 1 |
| date_basis | `dada` o `estimada` | dada |
| note | nota opcional (sin comas) | Recompra post earnings |

Ejemplos:

```
t17,2026-10-20,TSLA,buy,250,100,,dada,Nueva idea
t18,2026-10-22,NU,sell,16,,0.5,dada,Vendí la mitad
```

Para quitar una operación, borra su fila.

## Cómo se actualiza

- `scripts/update_prices.py` baja cierres diarios de Yahoo Finance para cada ticker de `trades.csv` más SPY y QQQ.
- `.github/workflows/update.yml` corre con cada cambio y cada día hábil a las 5:30 pm de Bogotá.
- `index.html` lee los dos CSV y calcula todo en el navegador.
