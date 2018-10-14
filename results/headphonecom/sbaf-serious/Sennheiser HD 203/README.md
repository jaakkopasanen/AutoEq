# Sennheiser HD 203

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.0dB
GraphicEQ: 21 0.0; 23 5.4; 25 4.6; 28 3.7; 31 3.1; 34 2.5; 37 1.6; 41 0.2; 45 -0.7; 49 -1.1; 54 -1.7; 60 -2.6; 66 -3.1; 72 -3.1; 79 -2.5; 87 -2.8; 96 -3.7; 106 -3.7; 116 -3.3; 128 -2.9; 141 -2.2; 155 -1.2; 170 0.1; 187 2.4; 206 5.9; 227 6.0; 249 5.8; 274 5.0; 302 4.0; 332 2.3; 365 0.8; 402 0.4; 442 0.1; 486 -0.3; 535 -0.2; 588 0.1; 647 0.3; 712 0.5; 783 0.3; 861 0.1; 947 0.2; 1042 -0.3; 1146 -0.4; 1261 -0.7; 1387 -1.0; 1526 -1.1; 1678 -0.7; 1846 0.8; 2031 1.9; 2234 3.4; 2457 4.9; 2703 5.9; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 2.1; 4788 1.7; 5267 5.1; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.0dB` and instead set Global volume in the UI for both channels to **-69**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 203 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  0.9  | 7.0 dB  |
| Peaking | 157 Hz  |  0.43 | -7.6 dB |
| Peaking | 231 Hz  |  1.24 | 13.1 dB |
| Peaking | 3125 Hz |  1.8  | 6.8 dB  |
| Peaking | 5948 Hz |  4.14 | 5.8 dB  |
| Peaking | 1533 Hz |  3.42 | -2.0 dB |
| Peaking | 2377 Hz |  5.94 | 1.5 dB  |
| Peaking | 4084 Hz |  7.3  | 3.0 dB  |
| Peaking | 4496 Hz | 10.64 | -4.0 dB |
| Peaking | 8314 Hz |  4.68 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20203/Sennheiser%20HD%20203.png)