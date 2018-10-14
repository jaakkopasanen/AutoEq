# Grado iGi

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.7; 25 2.4; 28 2.0; 31 1.6; 34 1.4; 37 1.1; 41 0.8; 45 0.5; 49 0.3; 54 -0.0; 60 -0.5; 66 -0.8; 72 -0.9; 79 -1.1; 87 -1.4; 96 -1.5; 106 -1.6; 116 -1.6; 128 -1.7; 141 -1.7; 155 -1.7; 170 -1.6; 187 -1.4; 206 -1.2; 227 -0.9; 249 -0.6; 274 -0.2; 302 0.2; 332 0.5; 365 0.8; 402 1.1; 442 1.3; 486 1.5; 535 1.7; 588 1.9; 647 2.0; 712 1.9; 783 1.7; 861 1.3; 947 0.5; 1042 -0.2; 1146 -0.8; 1261 -1.4; 1387 -1.4; 1526 -1.3; 1678 -2.0; 1846 -0.9; 2031 1.1; 2234 3.8; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.6; 6373 0.8; 7010 1.9; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado iGi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.63 | 3.6 dB  |
| Peaking | 125 Hz  | 0.59 | -2.1 dB |
| Peaking | 582 Hz  | 0.9  | 2.2 dB  |
| Peaking | 1605 Hz | 1.42 | -5.7 dB |
| Peaking | 3120 Hz | 0.8  | 7.9 dB  |
| Peaking | 1928 Hz | 5.38 | -1.0 dB |
| Peaking | 2380 Hz | 3.96 | 1.8 dB  |
| Peaking | 3166 Hz | 3.33 | -1.0 dB |
| Peaking | 5433 Hz | 2.87 | 4.5 dB  |
| Peaking | 6579 Hz | 1.13 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20iGi/Grado%20iGi.png)