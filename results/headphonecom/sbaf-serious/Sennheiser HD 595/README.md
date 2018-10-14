# Sennheiser HD 595

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.9; 41 5.3; 45 4.7; 49 4.1; 54 4.0; 60 3.7; 66 3.4; 72 4.2; 79 2.6; 87 1.5; 96 0.8; 106 0.4; 116 0.1; 128 -0.4; 141 -0.8; 155 -1.0; 170 -1.0; 187 -1.2; 206 -1.2; 227 -1.2; 249 -1.4; 274 -1.4; 302 -1.2; 332 -1.1; 365 -0.6; 402 -0.4; 442 0.0; 486 -0.2; 535 -0.3; 588 -0.4; 647 -0.1; 712 0.6; 783 0.3; 861 0.3; 947 0.1; 1042 0.0; 1146 0.4; 1261 0.8; 1387 1.2; 1526 1.4; 1678 1.6; 1846 1.5; 2031 0.9; 2234 0.5; 2457 1.0; 2703 1.9; 2973 1.4; 3270 1.0; 3597 1.7; 3957 2.5; 4353 3.8; 4788 2.6; 5267 3.5; 5793 5.9; 6373 4.7; 7010 0.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.1; 20000 -5.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 595 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.23 | 6.4 dB  |
| Peaking | 145 Hz  | 0.56 | -3.4 dB |
| Peaking | 717 Hz  | 2.97 | 0.4 dB  |
| Peaking | 3121 Hz | 0.66 | 1.6 dB  |
| Peaking | 5817 Hz | 4.64 | 5.5 dB  |
| Peaking | 1637 Hz | 3.17 | 0.9 dB  |
| Peaking | 2238 Hz | 6.14 | -1.2 dB |
| Peaking | 3253 Hz | 7.86 | -0.9 dB |
| Peaking | 4316 Hz | 7.28 | 2.1 dB  |
| Peaking | 8129 Hz | 1.94 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20595/Sennheiser%20HD%20595.png)