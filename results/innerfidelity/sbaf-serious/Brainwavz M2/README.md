# Brainwavz M2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.9; 37 5.5; 41 4.9; 45 4.4; 49 3.9; 54 3.3; 60 2.7; 66 2.2; 72 1.7; 79 1.0; 87 0.5; 96 -0.0; 106 -0.5; 116 -0.7; 128 -1.0; 141 -1.4; 155 -1.6; 170 -1.7; 187 -1.7; 206 -1.8; 227 -1.6; 249 -1.5; 274 -1.3; 302 -1.1; 332 -0.8; 365 -0.5; 402 -0.2; 442 0.3; 486 0.4; 535 0.7; 588 1.2; 647 1.4; 712 1.3; 783 1.4; 861 1.0; 947 0.4; 1042 -0.3; 1146 -0.9; 1261 -1.5; 1387 -2.6; 1526 -3.3; 1678 -3.5; 1846 -2.4; 2031 0.5; 2234 2.6; 2457 2.5; 2703 4.4; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.9; 4788 4.5; 5267 4.2; 5793 4.5; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz M2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.63 | 6.4 dB  |
| Peaking | 164 Hz  | 1.01 | -2.4 dB |
| Peaking | 1630 Hz | 2.72 | -5.6 dB |
| Peaking | 3442 Hz | 1.11 | 6.7 dB  |
| Peaking | 6237 Hz | 5.85 | 3.7 dB  |
| Peaking | 297 Hz  | 2.15 | -0.7 dB |
| Peaking | 708 Hz  | 1.34 | 1.7 dB  |
| Peaking | 1185 Hz | 2.52 | -1.0 dB |
| Peaking | 6733 Hz | 1.8  | 1.8 dB  |
| Peaking | 7784 Hz | 1.75 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20M2/Brainwavz%20M2.png)