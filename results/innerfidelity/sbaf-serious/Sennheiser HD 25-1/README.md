# Sennheiser HD 25-1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.4; 28 2.0; 31 1.7; 34 1.6; 37 1.5; 41 1.5; 45 1.4; 49 1.4; 54 1.5; 60 1.2; 66 0.9; 72 0.9; 79 0.2; 87 -1.3; 96 -3.0; 106 -3.6; 116 -3.4; 128 -2.8; 141 -2.3; 155 -1.6; 170 -1.6; 187 -1.0; 206 -0.6; 227 0.2; 249 1.0; 274 1.3; 302 1.7; 332 2.3; 365 2.8; 402 2.7; 442 2.6; 486 2.2; 535 2.0; 588 2.0; 647 1.8; 712 1.4; 783 1.2; 861 0.7; 947 0.3; 1042 -0.1; 1146 -0.5; 1261 -1.0; 1387 -1.8; 1526 -2.6; 1678 -3.4; 1846 -3.5; 2031 -3.2; 2234 -2.1; 2457 -0.2; 2703 1.3; 2973 2.7; 3270 2.7; 3597 3.3; 3957 4.8; 4353 5.7; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.3; 8482 -4.3; 9330 -4.0; 10263 -0.1; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 122 Hz  | 0.81 | -7.8 dB |
| Peaking | 125 Hz  | 0.18 | 4.6 dB  |
| Peaking | 1807 Hz | 1.44 | -5.5 dB |
| Peaking | 5307 Hz | 0.83 | 7.3 dB  |
| Peaking | 8682 Hz | 2.94 | -8.6 dB |
| Peaking | 38 Hz   | 2.68 | -0.7 dB |
| Peaking | 74 Hz   | 5.96 | 1.0 dB  |
| Peaking | 214 Hz  | 4.91 | -0.7 dB |
| Peaking | 376 Hz  | 4.43 | 0.7 dB  |
| Peaking | 944 Hz  | 3.8  | -0.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025-1/Sennheiser%20HD%2025-1.png)