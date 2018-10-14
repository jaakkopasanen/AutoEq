# Sennheiser HD 800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.5; 31 5.1; 34 4.8; 37 4.5; 41 4.1; 45 3.8; 49 3.7; 54 3.8; 60 3.9; 66 3.5; 72 2.7; 79 2.0; 87 1.4; 96 0.8; 106 0.3; 116 -0.2; 128 -0.6; 141 -0.9; 155 -1.2; 170 -1.4; 187 -1.5; 206 -1.7; 227 -1.8; 249 -1.7; 274 -1.6; 302 -1.4; 332 -1.2; 365 -1.0; 402 -0.9; 442 -0.9; 486 -0.8; 535 -0.7; 588 -0.6; 647 -0.5; 712 -0.4; 783 -0.3; 861 -0.3; 947 -0.1; 1042 0.1; 1146 0.3; 1261 0.9; 1387 1.7; 1526 2.2; 1678 2.5; 1846 2.5; 2031 2.7; 2234 2.4; 2457 1.1; 2703 0.3; 2973 0.1; 3270 0.9; 3597 1.2; 3957 0.5; 4353 -0.7; 4788 -2.5; 5267 -5.6; 5793 -8.2; 6373 -4.4; 7010 -2.2; 7711 -3.5; 8482 -0.4; 9330 0.0; 10263 -0.1; 11289 -4.8; 12418 -6.7; 13660 -6.0; 15026 -4.0; 16529 -3.2; 18182 -4.5; 20000 -8.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.12 | 6.2 dB  |
| Peaking | 60 Hz    | 2.61 | 3.1 dB  |
| Peaking | 1912 Hz  | 1.77 | 3.0 dB  |
| Peaking | 5708 Hz  | 5.13 | -8.0 dB |
| Peaking | 21331 Hz | 0.17 | -6.1 dB |
| Peaking | 243 Hz   | 0.88 | -1.9 dB |
| Peaking | 3694 Hz  | 4.95 | 1.8 dB  |
| Peaking | 9942 Hz  | 2.46 | 7.3 dB  |
| Peaking | 11764 Hz | 1.1  | -6.3 dB |
| Peaking | 15943 Hz | 1.73 | 3.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20800/Sennheiser%20HD%20800.png)