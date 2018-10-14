# Sennheiser HD 540 reference-II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.3; 31 4.6; 34 4.0; 37 3.5; 41 3.0; 45 2.5; 49 2.1; 54 1.6; 60 1.2; 66 1.0; 72 0.7; 79 -0.4; 87 -1.6; 96 -2.5; 106 -3.1; 116 -3.8; 128 -4.3; 141 -4.7; 155 -5.0; 170 -5.2; 187 -5.3; 206 -5.4; 227 -5.4; 249 -5.3; 274 -5.1; 302 -4.8; 332 -4.5; 365 -4.2; 402 -3.9; 442 -3.7; 486 -3.5; 535 -3.2; 588 -2.8; 647 -2.5; 712 -2.2; 783 -2.0; 861 -1.4; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 0.1; 1387 0.7; 1526 1.4; 1678 2.0; 1846 2.3; 2031 1.9; 2234 1.0; 2457 0.1; 2703 -0.8; 2973 -1.1; 3270 -0.4; 3597 1.0; 3957 -0.9; 4353 -1.2; 4788 -3.9; 5267 -3.0; 5793 -3.1; 6373 -5.7; 7010 -1.4; 7711 -2.3; 8482 -2.0; 9330 0.0; 10263 0.0; 11289 -2.9; 12418 -9.2; 13660 -8.3; 15026 -3.0; 16529 -2.4; 18182 -5.7; 20000 -6.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 540 reference-II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.9dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.17 | 6.5 dB   |
| Peaking | 172 Hz   | 0.38 | -6.8 dB  |
| Peaking | 1736 Hz  | 2.21 | 2.9 dB   |
| Peaking | 6012 Hz  | 2.62 | -4.4 dB  |
| Peaking | 13134 Hz | 2.94 | -10.2 dB |
| Peaking | 970 Hz   | 8.61 | 1.2 dB   |
| Peaking | 2094 Hz  | 4.61 | 0.5 dB   |
| Peaking | 2816 Hz  | 5    | -1.1 dB  |
| Peaking | 10287 Hz | 4.93 | 2.8 dB   |
| Peaking | 19318 Hz | 1.75 | -7.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20540%20reference-II/Sennheiser%20HD%20540%20reference-II.png)