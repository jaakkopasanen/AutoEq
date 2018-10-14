# Grado GR8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.3; 25 2.3; 28 2.2; 31 2.1; 34 2.0; 37 1.8; 41 1.7; 45 1.6; 49 1.4; 54 1.0; 60 0.7; 66 0.4; 72 0.1; 79 -0.2; 87 -0.5; 96 -0.8; 106 -1.1; 116 -1.6; 128 -1.8; 141 -2.1; 155 -2.4; 170 -2.6; 187 -2.7; 206 -2.8; 227 -2.8; 249 -2.7; 274 -2.6; 302 -2.5; 332 -2.3; 365 -2.1; 402 -1.5; 442 -1.3; 486 -1.1; 535 -0.8; 588 -0.6; 647 -0.2; 712 0.0; 783 0.2; 861 0.2; 947 0.1; 1042 -0.0; 1146 -0.0; 1261 -0.2; 1387 -0.6; 1526 -1.4; 1678 -1.8; 1846 -1.7; 2031 -1.6; 2234 -1.2; 2457 0.3; 2703 3.9; 2973 6.0; 3270 6.0; 3597 6.0; 3957 1.7; 4353 1.6; 4788 3.5; 5267 5.8; 5793 6.0; 6373 4.0; 7010 -1.7; 7711 -1.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GR8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 26 Hz   |  0.6  | 2.5 dB  |
| Peaking | 203 Hz  |  0.78 | -3.1 dB |
| Peaking | 3213 Hz |  2.27 | 11.3 dB |
| Peaking | 3517 Hz |  0.64 | -4.8 dB |
| Peaking | 5532 Hz |  3.23 | 8.7 dB  |
| Peaking | 1053 Hz |  1.31 | 1.4 dB  |
| Peaking | 2041 Hz |  1.11 | -1.3 dB |
| Peaking | 2772 Hz | 10.11 | 2.7 dB  |
| Peaking | 7074 Hz |  2.37 | 2.9 dB  |
| Peaking | 7189 Hz |  5.86 | -5.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20GR8/Grado%20GR8.png)