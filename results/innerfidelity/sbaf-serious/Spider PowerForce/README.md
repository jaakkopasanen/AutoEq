# Spider PowerForce

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.2; 23 -2.0; 25 -2.6; 28 -3.5; 31 -4.2; 34 -4.8; 37 -5.4; 41 -6.0; 45 -6.5; 49 -7.0; 54 -7.4; 60 -7.9; 66 -8.1; 72 -8.3; 79 -8.6; 87 -8.7; 96 -8.9; 106 -8.9; 116 -8.9; 128 -8.9; 141 -8.9; 155 -8.7; 170 -8.0; 187 -7.4; 206 -6.3; 227 -5.3; 249 -3.0; 274 -1.7; 302 -2.3; 332 -2.6; 365 -2.7; 402 -2.9; 442 -3.1; 486 -3.1; 535 -2.7; 588 -2.0; 647 -1.4; 712 -0.0; 783 -0.2; 861 -0.2; 947 -0.0; 1042 0.2; 1146 0.3; 1261 0.4; 1387 -0.0; 1526 -0.2; 1678 -0.7; 1846 -0.8; 2031 -0.9; 2234 -1.1; 2457 -0.5; 2703 0.1; 2973 1.1; 3270 1.9; 3597 4.1; 3957 6.0; 4353 6.0; 4788 -1.3; 5267 2.0; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spider PowerForce ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 70 Hz   | 0.57 | -7.8 dB |
| Peaking | 156 Hz  | 1.35 | -5.0 dB |
| Peaking | 477 Hz  | 2.71 | -2.5 dB |
| Peaking | 3979 Hz | 4.76 | 6.6 dB  |
| Peaking | 6116 Hz | 5.24 | 6.4 dB  |
| Peaking | 264 Hz  | 2.03 | -2.0 dB |
| Peaking | 270 Hz  | 4.45 | 3.6 dB  |
| Peaking | 1731 Hz | 0.78 | 1.4 dB  |
| Peaking | 1991 Hz | 1.67 | -2.5 dB |
| Peaking | 8630 Hz | 2.58 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Spider%20PowerForce/Spider%20PowerForce.png)