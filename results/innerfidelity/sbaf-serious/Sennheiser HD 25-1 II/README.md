# Sennheiser HD 25-1 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.4; 66 4.7; 72 3.9; 79 3.3; 87 3.2; 96 3.1; 106 1.6; 116 0.7; 128 -0.4; 141 -1.5; 155 -1.7; 170 -1.8; 187 -2.1; 206 -1.9; 227 -1.7; 249 -1.5; 274 -1.1; 302 -1.1; 332 -1.0; 365 -0.7; 402 -0.3; 442 -0.2; 486 -0.2; 535 -0.1; 588 0.2; 647 0.3; 712 0.2; 783 0.4; 861 0.2; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.6; 1387 -1.2; 1526 -1.9; 1678 -2.7; 1846 -2.9; 2031 -2.9; 2234 -2.5; 2457 -1.1; 2703 0.8; 2973 2.5; 3270 2.5; 3597 2.2; 3957 2.7; 4353 2.4; 4788 3.8; 5267 5.2; 5793 5.5; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -2.4; 9330 -2.3; 10263 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.79 | 7.1 dB  |
| Peaking | 2056 Hz | 1.69 | -4.3 dB |
| Peaking | 3040 Hz | 2.08 | 3.3 dB  |
| Peaking | 5836 Hz | 1.99 | 6.0 dB  |
| Peaking | 8759 Hz | 4.41 | -4.6 dB |
| Peaking | 36 Hz   | 1.07 | -5.5 dB |
| Peaking | 36 Hz   | 0.24 | 4.6 dB  |
| Peaking | 165 Hz  | 0.88 | -4.5 dB |
| Peaking | 764 Hz  | 1.59 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025-1%20II/Sennheiser%20HD%2025-1%20II.png)