# Etymotic hf5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.5; 37 5.3; 41 5.0; 45 4.7; 49 4.4; 54 4.1; 60 3.7; 66 3.3; 72 3.1; 79 2.6; 87 2.2; 96 1.9; 106 1.6; 116 1.4; 128 1.1; 141 0.8; 155 0.6; 170 0.4; 187 0.3; 206 0.2; 227 0.2; 249 0.1; 274 0.1; 302 0.2; 332 0.4; 365 0.6; 402 0.9; 442 1.0; 486 1.1; 535 1.0; 588 1.0; 647 1.2; 712 1.2; 783 1.1; 861 0.8; 947 0.4; 1042 -0.3; 1146 -0.9; 1261 -1.6; 1387 -2.3; 1526 -3.1; 1678 -3.6; 1846 -3.6; 2031 -3.5; 2234 -3.1; 2457 -2.2; 2703 -0.7; 2973 1.3; 3270 3.6; 3597 5.4; 3957 5.3; 4353 4.2; 4788 4.6; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.6  | 4.4 dB  |
| Peaking | 43 Hz   | 0.55 | 3.0 dB  |
| Peaking | 1956 Hz | 1.67 | -4.6 dB |
| Peaking | 3685 Hz | 2.67 | 5.7 dB  |
| Peaking | 5711 Hz | 2.88 | 6.1 dB  |
| Peaking | 639 Hz  | 3.33 | -1.2 dB |
| Peaking | 654 Hz  | 1.59 | 2.4 dB  |
| Peaking | 1392 Hz | 3.48 | -1.0 dB |
| Peaking | 6578 Hz | 7.92 | 2.1 dB  |
| Peaking | 7723 Hz | 2.37 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20hf5/Etymotic%20hf5.png)