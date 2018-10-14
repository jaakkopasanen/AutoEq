# Grado RS2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.5; 45 4.5; 49 3.6; 54 2.5; 60 1.5; 66 0.9; 72 -0.1; 79 -0.9; 87 -1.5; 96 -2.0; 106 -2.2; 116 -2.3; 128 -2.4; 141 -2.2; 155 -2.1; 170 -1.9; 187 -1.5; 206 -1.7; 227 -1.6; 249 -1.3; 274 -0.9; 302 -0.5; 332 -0.8; 365 -0.6; 402 -0.3; 442 -0.2; 486 -0.1; 535 0.1; 588 0.3; 647 0.5; 712 0.5; 783 0.4; 861 0.3; 947 0.2; 1042 -0.0; 1146 -0.2; 1261 -0.6; 1387 -1.4; 1526 -2.4; 1678 -3.4; 1846 -4.9; 2031 -8.1; 2234 -7.9; 2457 -6.0; 2703 -4.2; 2973 -2.4; 3270 -1.0; 3597 -3.0; 3957 -8.3; 4353 -6.0; 4788 -3.5; 5267 -3.6; 5793 -3.8; 6373 -5.3; 7010 -6.9; 7711 -5.3; 8482 -6.5; 9330 -10.6; 10263 -9.2; 11289 -2.1; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 31 Hz    |  0.52 | 7.2 dB  |
| Peaking | 99 Hz    |  0.69 | -4.4 dB |
| Peaking | 2137 Hz  |  2.96 | -8.5 dB |
| Peaking | 4109 Hz  |  4.26 | -6.8 dB |
| Peaking | 9136 Hz  |  2    | -9.9 dB |
| Peaking | 755 Hz   |  1.92 | 0.9 dB  |
| Peaking | 3377 Hz  | 10.5  | 2.4 dB  |
| Peaking | 6675 Hz  |  6.19 | -3.4 dB |
| Peaking | 11956 Hz |  7.93 | 3.0 dB  |
| Peaking | 13541 Hz |  3.15 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20RS2/Grado%20RS2.png)