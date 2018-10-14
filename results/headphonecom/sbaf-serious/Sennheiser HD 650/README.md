# Sennheiser HD 650

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 21 0.0; 23 4.5; 25 3.9; 28 3.1; 31 2.4; 34 1.8; 37 1.4; 41 1.4; 45 1.8; 49 1.3; 54 0.2; 60 -0.4; 66 -0.5; 72 -0.7; 79 -1.4; 87 -1.9; 96 -2.3; 106 -2.5; 116 -2.7; 128 -2.9; 141 -3.1; 155 -3.1; 170 -3.2; 187 -3.0; 206 -2.9; 227 -2.7; 249 -2.4; 274 -2.3; 302 -2.0; 332 -1.8; 365 -1.5; 402 -1.2; 442 -1.0; 486 -0.8; 535 -0.6; 588 -0.2; 647 0.1; 712 0.0; 783 0.4; 861 0.0; 947 0.1; 1042 -0.1; 1146 -0.4; 1261 -0.5; 1387 -0.6; 1526 -0.8; 1678 -1.0; 1846 -1.2; 2031 -1.4; 2234 -1.3; 2457 -1.0; 2703 -1.0; 2973 -0.6; 3270 -0.2; 3597 1.1; 3957 1.9; 4353 0.5; 4788 0.3; 5267 2.9; 5793 2.8; 6373 1.6; 7010 2.0; 7711 0.3; 8482 -0.1; 9330 -1.5; 10263 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.7dB` and instead set Global volume in the UI for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.3dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 12 Hz   |  0.58 | 7.4 dB  |
| Peaking | 152 Hz  |  0.65 | -3.4 dB |
| Peaking | 2220 Hz |  1.53 | -1.5 dB |
| Peaking | 3837 Hz |  6.25 | 2.0 dB  |
| Peaking | 5668 Hz |  3.89 | 3.3 dB  |
| Peaking | 17 Hz   |  0.35 | 0.2 dB  |
| Peaking | 754 Hz  |  2.95 | 0.7 dB  |
| Peaking | 4613 Hz | 13.15 | -1.1 dB |
| Peaking | 6946 Hz | 10.66 | 1.5 dB  |
| Peaking | 9244 Hz |  7.92 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)