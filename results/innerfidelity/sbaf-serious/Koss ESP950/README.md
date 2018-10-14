# Koss ESP950

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 5.3; 96 4.3; 106 3.4; 116 2.8; 128 2.8; 141 2.7; 155 2.7; 170 2.4; 187 2.3; 206 2.2; 227 2.2; 249 2.1; 274 2.2; 302 2.1; 332 2.1; 365 2.1; 402 2.0; 442 2.0; 486 1.7; 535 1.6; 588 1.6; 647 1.4; 712 1.2; 783 1.1; 861 0.6; 947 0.3; 1042 0.0; 1146 -0.4; 1261 -1.0; 1387 -1.5; 1526 -1.6; 1678 -0.9; 1846 1.1; 2031 3.1; 2234 4.6; 2457 5.1; 2703 3.1; 2973 2.1; 3270 2.5; 3597 4.3; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.8; 5793 5.5; 6373 4.4; 7010 2.5; 7711 0.3; 8482 -0.4; 9330 -1.3; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP950 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.09 | 6.1 dB  |
| Peaking | 1489 Hz | 3.36 | -2.8 dB |
| Peaking | 2299 Hz | 4.13 | 4.3 dB  |
| Peaking | 5026 Hz | 1.15 | 6.7 dB  |
| Peaking | 8662 Hz | 2.27 | -3.1 dB |
| Peaking | 83 Hz   | 1.47 | 2.6 dB  |
| Peaking | 106 Hz  | 1.22 | -2.6 dB |
| Peaking | 452 Hz  | 1.09 | 1.3 dB  |
| Peaking | 3111 Hz | 6.74 | -1.4 dB |
| Peaking | 3903 Hz | 7.96 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20ESP950/Koss%20ESP950.png)