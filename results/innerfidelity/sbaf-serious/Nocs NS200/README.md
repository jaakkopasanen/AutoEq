# Nocs NS200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 21 -8.5; 23 -8.3; 25 -8.1; 28 -7.7; 31 -7.4; 34 -7.2; 37 -7.0; 41 -6.7; 45 -6.5; 49 -6.3; 54 -6.2; 60 -6.0; 66 -6.0; 72 -5.9; 79 -6.0; 87 -6.1; 96 -6.2; 106 -6.1; 116 -6.1; 128 -6.1; 141 -6.0; 155 -6.0; 170 -5.8; 187 -5.6; 206 -5.4; 227 -5.1; 249 -4.8; 274 -4.4; 302 -4.0; 332 -3.6; 365 -3.1; 402 -2.6; 442 -2.0; 486 -1.7; 535 -1.2; 588 -0.4; 647 -0.1; 712 0.2; 783 0.5; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -0.9; 1387 -1.6; 1526 -2.2; 1678 -2.8; 1846 -3.1; 2031 -3.3; 2234 -3.7; 2457 -3.4; 2703 -2.8; 2973 -0.5; 3270 2.2; 3597 3.8; 3957 3.3; 4353 1.0; 4788 -0.8; 5267 -2.1; 5793 -5.3; 6373 -4.4; 7010 -1.2; 7711 0.3; 8482 0.0; 9330 -0.8; 10263 -0.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.9dB` and instead set Global volume in the UI for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.14 | -8.0 dB |
| Peaking | 183 Hz  | 0.71 | -4.5 dB |
| Peaking | 2287 Hz | 1.61 | -4.4 dB |
| Peaking | 3626 Hz | 3.16 | 5.7 dB  |
| Peaking | 5950 Hz | 4.78 | -6.2 dB |
| Peaking | 14 Hz   | 1.92 | -1.0 dB |
| Peaking | 370 Hz  | 2.3  | -0.7 dB |
| Peaking | 788 Hz  | 1.64 | 1.4 dB  |
| Peaking | 1548 Hz | 3.76 | -0.9 dB |
| Peaking | 7554 Hz | 9.64 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS200/Nocs%20NS200.png)