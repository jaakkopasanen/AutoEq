# AKG K1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.6; 66 3.8; 72 2.1; 79 0.6; 87 -0.6; 96 -1.4; 106 -1.7; 116 -1.8; 128 -1.9; 141 -1.2; 155 -1.1; 170 -0.7; 187 -0.6; 206 -0.5; 227 -0.2; 249 -0.1; 274 0.2; 302 0.3; 332 0.4; 365 0.5; 402 0.5; 442 0.8; 486 0.7; 535 0.7; 588 0.9; 647 0.9; 712 0.7; 783 0.9; 861 0.6; 947 0.3; 1042 -0.0; 1146 -0.7; 1261 -2.1; 1387 -3.8; 1526 -4.6; 1678 -4.8; 1846 -6.8; 2031 -6.6; 2234 -5.7; 2457 -2.9; 2703 0.1; 2973 2.4; 3270 2.7; 3597 1.2; 3957 -1.8; 4353 -2.7; 4788 -2.7; 5267 -2.8; 5793 -4.4; 6373 -5.2; 7010 -3.9; 7711 -4.1; 8482 -4.7; 9330 -3.9; 10263 -1.3; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.3; 20000 -1.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 72 Hz    | 0.28 | 16.6 dB  |
| Peaking | 104 Hz   | 0.51 | -17.3 dB |
| Peaking | 1948 Hz  | 1.83 | -7.4 dB  |
| Peaking | 3111 Hz  | 3.3  | 5.9 dB   |
| Peaking | 6681 Hz  | 1.13 | -4.9 dB  |
| Peaking | 81 Hz    | 6.12 | -0.5 dB  |
| Peaking | 907 Hz   | 1.82 | 0.9 dB   |
| Peaking | 1395 Hz  | 7.02 | -1.6 dB  |
| Peaking | 9136 Hz  | 4.09 | -3.1 dB  |
| Peaking | 10583 Hz | 1.68 | 2.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K1000/AKG%20K1000.png)