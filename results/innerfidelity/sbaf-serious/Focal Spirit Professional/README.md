# Focal Spirit Professional

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.9; 23 -3.0; 25 -3.0; 28 -3.1; 31 -3.1; 34 -3.1; 37 -3.1; 41 -3.1; 45 -3.2; 49 -3.1; 54 -3.1; 60 -3.2; 66 -3.2; 72 -3.2; 79 -3.1; 87 -3.1; 96 -3.6; 106 -3.9; 116 -3.7; 128 -3.4; 141 -3.5; 155 -3.4; 170 -2.9; 187 -2.9; 206 -2.6; 227 -2.1; 249 -1.8; 274 -1.4; 302 -1.1; 332 -0.9; 365 -0.4; 402 -0.3; 442 -0.7; 486 -1.4; 535 -1.4; 588 -0.9; 647 -0.8; 712 -0.7; 783 -0.3; 861 -0.2; 947 0.1; 1042 -0.0; 1146 0.1; 1261 0.2; 1387 -0.1; 1526 -0.4; 1678 -0.4; 1846 0.1; 2031 0.5; 2234 1.0; 2457 1.7; 2703 1.9; 2973 1.7; 3270 0.4; 3597 -0.5; 3957 0.1; 4353 1.5; 4788 3.0; 5267 5.1; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.3; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit Professional ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.44 | -2.8 dB |
| Peaking | 130 Hz  | 0.67 | -3.0 dB |
| Peaking | 2651 Hz | 2.51 | 3.1 dB  |
| Peaking | 4961 Hz | 0.62 | -2.8 dB |
| Peaking | 5747 Hz | 2.16 | 9.0 dB  |
| Peaking | 408 Hz  | 2.57 | 1.5 dB  |
| Peaking | 484 Hz  | 2.06 | -1.6 dB |
| Peaking | 933 Hz  | 4.58 | 0.4 dB  |
| Peaking | 1227 Hz | 6.83 | 0.4 dB  |
| Peaking | 3602 Hz | 9.61 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Spirit%20Professional/Focal%20Spirit%20Professional.png)