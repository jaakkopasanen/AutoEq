# Ostry KC06

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.1; 25 3.6; 28 3.0; 31 2.6; 34 2.1; 37 1.8; 41 1.3; 45 1.0; 49 0.6; 54 0.2; 60 -0.3; 66 -0.7; 72 -1.2; 79 -1.6; 87 -2.1; 96 -2.6; 106 -2.9; 116 -3.0; 128 -3.4; 141 -3.6; 155 -3.7; 170 -3.8; 187 -3.7; 206 -3.6; 227 -3.4; 249 -3.2; 274 -2.9; 302 -2.5; 332 -2.2; 365 -1.7; 402 -1.3; 442 -0.8; 486 -0.4; 535 0.0; 588 0.7; 647 0.9; 712 1.0; 783 1.2; 861 0.8; 947 0.4; 1042 -0.3; 1146 -1.0; 1261 -1.9; 1387 -3.1; 1526 -4.1; 1678 -4.8; 1846 -5.0; 2031 -4.8; 2234 -4.3; 2457 -2.4; 2703 0.1; 2973 3.1; 3270 5.8; 3597 6.0; 3957 6.0; 4353 5.1; 4788 4.2; 5267 4.2; 5793 2.4; 6373 -2.1; 7010 -6.1; 7711 -4.2; 8482 -1.0; 9330 -1.3; 10263 -4.1; 11289 -2.0; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ostry KC06 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.84 | 4.6 dB  |
| Peaking | 158 Hz   | 0.75 | -4.1 dB |
| Peaking | 2034 Hz  | 1.56 | -8.9 dB |
| Peaking | 3870 Hz  | 0.88 | 8.8 dB  |
| Peaking | 7200 Hz  | 2.19 | -8.5 dB |
| Peaking | 751 Hz   | 2.01 | 1.9 dB  |
| Peaking | 1452 Hz  | 4.23 | -1.4 dB |
| Peaking | 5607 Hz  | 9.86 | 1.9 dB  |
| Peaking | 8626 Hz  | 6.91 | 2.4 dB  |
| Peaking | 10477 Hz | 5.64 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ostry%20KC06/Ostry%20KC06.png)