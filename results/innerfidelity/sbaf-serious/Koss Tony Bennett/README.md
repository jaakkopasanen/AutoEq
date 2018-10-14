# Koss Tony Bennett

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.7; 28 5.1; 31 4.4; 34 3.8; 37 3.3; 41 2.7; 45 2.1; 49 1.7; 54 1.2; 60 0.6; 66 0.2; 72 -0.0; 79 0.7; 87 1.8; 96 0.6; 106 -1.3; 116 -2.1; 128 -2.7; 141 -3.5; 155 -3.9; 170 -3.5; 187 -4.3; 206 -4.5; 227 -4.2; 249 -4.1; 274 -3.5; 302 -2.8; 332 -2.2; 365 -1.8; 402 -2.1; 442 -2.9; 486 -3.8; 535 -3.7; 588 -3.1; 647 -2.4; 712 -1.9; 783 -0.7; 861 0.3; 947 1.0; 1042 0.2; 1146 1.1; 1261 2.2; 1387 2.5; 1526 2.5; 1678 2.5; 1846 2.6; 2031 2.7; 2234 2.1; 2457 2.2; 2703 2.0; 2973 2.0; 3270 1.3; 3597 4.2; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.0; 9330 -1.9; 10263 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Tony Bennett ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.56 | 6.5 dB  |
| Peaking | 194 Hz  | 1.08 | -4.7 dB |
| Peaking | 544 Hz  | 2    | -3.5 dB |
| Peaking | 1574 Hz | 1.18 | 2.6 dB  |
| Peaking | 4883 Hz | 1.69 | 6.8 dB  |
| Peaking | 88 Hz   | 8.86 | 2.1 dB  |
| Peaking | 3865 Hz | 5.54 | 3.7 dB  |
| Peaking | 4062 Hz | 1.86 | -1.9 dB |
| Peaking | 6325 Hz | 5.61 | 2.9 dB  |
| Peaking | 8992 Hz | 2.8  | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Tony%20Bennett/Koss%20Tony%20Bennett.png)