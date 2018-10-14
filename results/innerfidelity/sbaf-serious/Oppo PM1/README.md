# Oppo PM1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.6; 25 4.1; 28 3.7; 31 3.3; 34 3.0; 37 2.9; 41 2.7; 45 2.6; 49 2.7; 54 3.1; 60 2.3; 66 1.6; 72 1.2; 79 0.7; 87 0.4; 96 -0.1; 106 -0.4; 116 -0.6; 128 -0.9; 141 -1.3; 155 -1.5; 170 -1.6; 187 -1.7; 206 -1.9; 227 -1.7; 249 -2.0; 274 -2.3; 302 -2.5; 332 -2.3; 365 -0.7; 402 0.5; 442 -0.1; 486 -1.0; 535 -1.5; 588 -1.5; 647 -1.9; 712 -2.4; 783 -2.5; 861 -2.8; 947 -0.4; 1042 -0.3; 1146 -0.4; 1261 -0.5; 1387 -1.0; 1526 -1.1; 1678 -1.0; 1846 -0.3; 2031 0.4; 2234 1.1; 2457 2.0; 2703 2.4; 2973 3.2; 3270 3.5; 3597 3.8; 3957 4.6; 4353 4.4; 4788 5.2; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.0; 9330 -0.6; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.72 | 5.2 dB  |
| Peaking | 54 Hz   | 2.21 | 2.0 dB  |
| Peaking | 216 Hz  | 0.89 | -2.2 dB |
| Peaking | 769 Hz  | 2.31 | -2.6 dB |
| Peaking | 4845 Hz | 1.32 | 6.1 dB  |
| Peaking | 1004 Hz | 6.65 | 1.1 dB  |
| Peaking | 1604 Hz | 2.72 | -1.6 dB |
| Peaking | 2945 Hz | 1.89 | 1.8 dB  |
| Peaking | 6213 Hz | 2.87 | 6.2 dB  |
| Peaking | 6554 Hz | 1.18 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM1/Oppo%20PM1.png)