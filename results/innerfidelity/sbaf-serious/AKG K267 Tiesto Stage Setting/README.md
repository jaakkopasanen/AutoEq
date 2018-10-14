# AKG K267 Tiesto Stage Setting

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.5; 23 -2.7; 25 -2.8; 28 -2.9; 31 -3.0; 34 -3.0; 37 -2.9; 41 -2.8; 45 -2.6; 49 -2.4; 54 -2.2; 60 -2.1; 66 -1.9; 72 -1.7; 79 -1.3; 87 -1.4; 96 -2.1; 106 -2.8; 116 -3.2; 128 -3.5; 141 -3.6; 155 -3.3; 170 -2.7; 187 -3.1; 206 -2.7; 227 -2.6; 249 -2.2; 274 -1.4; 302 0.0; 332 1.8; 365 2.8; 402 2.1; 442 1.4; 486 0.6; 535 0.5; 588 0.5; 647 0.3; 712 0.1; 783 0.4; 861 0.2; 947 -0.0; 1042 -0.2; 1146 -0.3; 1261 -1.1; 1387 -3.0; 1526 -4.1; 1678 -3.5; 1846 -2.3; 2031 -1.4; 2234 -0.5; 2457 1.2; 2703 1.3; 2973 2.1; 3270 2.4; 3597 3.1; 3957 5.1; 4353 6.0; 4788 6.0; 5267 2.5; 5793 5.6; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.2; 9330 -1.4; 10263 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K267 Tiesto Stage Setting ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.7  | -3.0 dB |
| Peaking | 146 Hz  | 1.47 | -3.6 dB |
| Peaking | 1580 Hz | 3.41 | -4.6 dB |
| Peaking | 4279 Hz | 2.28 | 6.0 dB  |
| Peaking | 6198 Hz | 5.66 | 4.9 dB  |
| Peaking | 256 Hz  | 2.43 | -2.4 dB |
| Peaking | 360 Hz  | 2.13 | 3.6 dB  |
| Peaking | 2156 Hz | 3.89 | -1.3 dB |
| Peaking | 2495 Hz | 3.61 | 1.4 dB  |
| Peaking | 9083 Hz | 5.35 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K267%20Tiesto%20Stage%20Setting/AKG%20K267%20Tiesto%20Stage%20Setting.png)