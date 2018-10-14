# Sennheiser PXC 450

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 -0.4; 25 -1.1; 28 -1.6; 31 -1.5; 34 -1.3; 37 -1.1; 41 -0.8; 45 -0.5; 49 -0.2; 54 -0.2; 60 -0.4; 66 -0.5; 72 -0.7; 79 -0.8; 87 -0.9; 96 -1.1; 106 -1.3; 116 -1.5; 128 -1.8; 141 -2.2; 155 -2.3; 170 -2.3; 187 -2.7; 206 -2.8; 227 -2.9; 249 -3.2; 274 -3.7; 302 -3.7; 332 -3.7; 365 -3.9; 402 -4.1; 442 -4.4; 486 -4.4; 535 -4.3; 588 -3.9; 647 -3.2; 712 -2.3; 783 -1.4; 861 -0.6; 947 -0.3; 1042 0.3; 1146 1.0; 1261 1.3; 1387 1.7; 1526 0.7; 1678 0.2; 1846 1.9; 2031 5.9; 2234 6.0; 2457 1.8; 2703 -1.9; 2973 2.4; 3270 5.2; 3597 3.7; 3957 5.5; 4353 6.0; 4788 5.8; 5267 4.8; 5793 5.0; 6373 4.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 232 Hz  |  0.67 | -2.8 dB |
| Peaking | 486 Hz  |  4.13 | 1.9 dB  |
| Peaking | 493 Hz  |  2.02 | -5.1 dB |
| Peaking | 2110 Hz |  5.97 | 6.2 dB  |
| Peaking | 4612 Hz |  1.48 | 6.2 dB  |
| Peaking | 31 Hz   |  2.49 | -1.5 dB |
| Peaking | 1244 Hz |  3.63 | 1.6 dB  |
| Peaking | 2673 Hz | 10.65 | -5.1 dB |
| Peaking | 3211 Hz |  8.7  | 2.6 dB  |
| Peaking | 8603 Hz |  4.26 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC%20450/Sennheiser%20PXC%20450.png)