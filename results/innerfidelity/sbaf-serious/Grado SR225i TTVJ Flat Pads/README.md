# Grado SR225i TTVJ Flat Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.2; 45 4.0; 49 2.9; 54 1.8; 60 0.7; 66 -0.1; 72 -0.7; 79 -1.0; 87 -1.6; 96 -1.9; 106 -2.2; 116 -2.3; 128 -2.5; 141 -2.5; 155 -2.5; 170 -2.4; 187 -2.3; 206 -2.3; 227 -1.9; 249 -1.6; 274 -1.4; 302 -1.4; 332 -1.5; 365 -1.4; 402 -1.2; 442 -0.9; 486 -0.8; 535 -0.7; 588 -0.2; 647 -0.1; 712 -0.1; 783 0.2; 861 -0.1; 947 0.1; 1042 0.0; 1146 -0.0; 1261 -0.2; 1387 -0.6; 1526 -1.2; 1678 -1.1; 1846 -1.4; 2031 -4.8; 2234 -4.0; 2457 -0.2; 2703 2.0; 2973 3.5; 3270 4.4; 3597 3.5; 3957 5.0; 4353 6.0; 4788 6.0; 5267 5.0; 5793 6.0; 6373 4.9; 7010 0.9; 7711 -1.2; 8482 -1.8; 9330 -1.6; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i TTVJ Flat Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.62 | 9.3 dB  |
| Peaking | 82 Hz    | 0.36 | -4.6 dB |
| Peaking | 2103 Hz  | 4.07 | -7.1 dB |
| Peaking | 5356 Hz  | 0.8  | 7.9 dB  |
| Peaking | 8157 Hz  | 1.73 | -6.7 dB |
| Peaking | 1488 Hz  | 6.37 | -1.3 dB |
| Peaking | 3182 Hz  | 3.19 | 1.2 dB  |
| Peaking | 3626 Hz  | 7.96 | -1.7 dB |
| Peaking | 9982 Hz  | 6.5  | 0.7 dB  |
| Peaking | 13694 Hz | 1.11 | -0.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20TTVJ%20Flat%20Pads/Grado%20SR225i%20TTVJ%20Flat%20Pads.png)