# Sennheiser MM 50 iP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 21 -0.3; 23 -0.9; 25 -1.5; 28 -2.2; 31 -2.8; 34 -3.3; 37 -3.8; 41 -4.3; 45 -4.8; 49 -5.3; 54 -5.8; 60 -6.3; 66 -6.8; 72 -7.2; 79 -7.7; 87 -8.1; 96 -8.4; 106 -8.6; 116 -8.8; 128 -8.9; 141 -9.0; 155 -9.1; 170 -9.0; 187 -8.8; 206 -8.5; 227 -8.1; 249 -7.6; 274 -7.5; 302 -7.3; 332 -6.8; 365 -6.0; 402 -5.3; 442 -4.7; 486 -4.0; 535 -3.2; 588 -2.5; 647 -1.8; 712 -1.1; 783 -0.6; 861 -0.2; 947 -0.1; 1042 0.0; 1146 0.4; 1261 0.2; 1387 0.1; 1526 -0.5; 1678 -1.1; 1846 -0.9; 2031 -0.5; 2234 0.1; 2457 0.7; 2703 1.2; 2973 1.8; 3270 2.7; 3597 3.1; 3957 1.7; 4353 -0.9; 4788 -2.7; 5267 -4.4; 5793 -8.2; 6373 -7.4; 7010 -3.4; 7711 -1.9; 8482 -4.0; 9330 -6.7; 10263 -2.7; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.2dB` and instead set Global volume in the UI for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 50 iP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 112 Hz   | 0.46 | -8.5 dB |
| Peaking | 296 Hz   | 1.05 | -3.3 dB |
| Peaking | 3451 Hz  | 2.97 | 3.9 dB  |
| Peaking | 5934 Hz  | 3.49 | -9.1 dB |
| Peaking | 9374 Hz  | 5.79 | -6.8 dB |
| Peaking | 20 Hz    | 2.52 | 0.9 dB  |
| Peaking | 492 Hz   | 2.08 | -0.9 dB |
| Peaking | 1033 Hz  | 0.85 | 1.1 dB  |
| Peaking | 1767 Hz  | 3.27 | -1.6 dB |
| Peaking | 11110 Hz | 7.44 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20MM%2050%20iP/Sennheiser%20MM%2050%20iP.png)