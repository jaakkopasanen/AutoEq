# Sennheiser HD 280 Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 21 0.0; 23 5.7; 25 5.3; 28 4.7; 31 4.2; 34 3.9; 37 3.6; 41 3.3; 45 3.1; 49 2.9; 54 3.1; 60 3.5; 66 4.4; 72 5.5; 79 5.8; 87 5.9; 96 5.6; 106 5.2; 116 4.8; 128 4.5; 141 4.2; 155 4.0; 170 3.8; 187 2.2; 206 1.4; 227 1.1; 249 0.9; 274 0.6; 302 0.4; 332 0.3; 365 0.3; 402 0.3; 442 0.4; 486 0.3; 535 0.2; 588 0.5; 647 0.4; 712 0.3; 783 0.3; 861 0.1; 947 0.0; 1042 -0.2; 1146 -0.5; 1261 -0.5; 1387 -0.8; 1526 -1.4; 1678 -2.3; 1846 -2.5; 2031 -1.9; 2234 -1.1; 2457 1.5; 2703 4.4; 2973 5.7; 3270 5.0; 3597 4.3; 3957 4.7; 4353 4.0; 4788 3.4; 5267 5.5; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.7; 9330 -3.4; 10263 -0.3; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 280 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  1.02 | 5.2 dB  |
| Peaking | 96 Hz   |  0.9  | 5.6 dB  |
| Peaking | 3223 Hz |  3.05 | 5.6 dB  |
| Peaking | 5685 Hz |  3.13 | 6.3 dB  |
| Peaking | 162 Hz  | 10.15 | 1.8 dB  |
| Peaking | 1913 Hz |  1.97 | -3.4 dB |
| Peaking | 2713 Hz |  7.05 | 2.8 dB  |
| Peaking | 5279 Hz |  0.61 | 0.7 dB  |
| Peaking | 9084 Hz |  4.78 | -4.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20280%20Pro/Sennheiser%20HD%20280%20Pro.png)