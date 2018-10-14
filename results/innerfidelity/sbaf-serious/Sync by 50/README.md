# Sync by 50

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 -1.6; 23 -2.5; 25 -3.2; 28 -4.1; 31 -4.9; 34 -5.6; 37 -6.1; 41 -6.8; 45 -7.2; 49 -7.6; 54 -8.0; 60 -8.3; 66 -8.6; 72 -8.8; 79 -9.1; 87 -9.4; 96 -9.8; 106 -9.9; 116 -10.0; 128 -10.1; 141 -10.1; 155 -10.1; 170 -9.9; 187 -9.7; 206 -9.3; 227 -8.7; 249 -8.5; 274 -8.9; 302 -9.0; 332 -8.6; 365 -8.3; 402 -8.1; 442 -8.0; 486 -7.6; 535 -6.2; 588 -3.2; 647 -0.3; 712 1.6; 783 2.2; 861 1.5; 947 0.5; 1042 -0.4; 1146 -0.8; 1261 -0.4; 1387 0.3; 1526 -0.9; 1678 -2.5; 1846 -3.1; 2031 -3.1; 2234 -2.3; 2457 -1.2; 2703 0.3; 2973 1.3; 3270 1.5; 3597 0.7; 3957 -0.4; 4353 0.2; 4788 3.0; 5267 4.5; 5793 2.6; 6373 4.9; 7010 -0.9; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.4dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sync by 50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 79 Hz   | 0.46 | -8.7 dB |
| Peaking | 218 Hz  | 0.97 | -5.2 dB |
| Peaking | 420 Hz  | 2.47 | -5.6 dB |
| Peaking | 1950 Hz | 4.24 | -3.6 dB |
| Peaking | 5539 Hz | 2.8  | 4.3 dB  |
| Peaking | 537 Hz  | 4.19 | -4.0 dB |
| Peaking | 809 Hz  | 1.07 | 6.5 dB  |
| Peaking | 1019 Hz | 2.73 | -2.9 dB |
| Peaking | 1034 Hz | 0.29 | -1.7 dB |
| Peaking | 3080 Hz | 4.38 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sync%20by%2050/Sync%20by%2050.png)