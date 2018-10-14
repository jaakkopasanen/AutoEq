# Sennheiser PXC300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.2; 72 4.6; 79 5.0; 87 4.4; 96 3.3; 106 2.6; 116 2.4; 128 2.1; 141 1.7; 155 1.5; 170 1.6; 187 1.7; 206 2.2; 227 2.2; 249 2.2; 274 2.0; 302 2.2; 332 2.4; 365 2.8; 402 2.9; 442 2.7; 486 2.8; 535 3.0; 588 2.9; 647 2.8; 712 2.4; 783 1.9; 861 1.2; 947 0.4; 1042 -0.4; 1146 -1.2; 1261 -1.8; 1387 -2.3; 1526 -2.6; 1678 -2.5; 1846 -1.9; 2031 -1.9; 2234 -2.6; 2457 -2.5; 2703 -1.4; 2973 -0.2; 3270 0.7; 3597 1.2; 3957 1.5; 4353 0.3; 4788 -2.4; 5267 -0.6; 5793 1.1; 6373 -0.8; 7010 -3.7; 7711 -2.5; 8482 -2.6; 9330 -6.2; 10263 -8.0; 11289 -1.5; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.45 | 6.5 dB  |
| Peaking | 547 Hz   | 0.69 | 3.1 dB  |
| Peaking | 1410 Hz  | 1.6  | -3.5 dB |
| Peaking | 2330 Hz  | 4.73 | -2.3 dB |
| Peaking | 9858 Hz  | 3.74 | -8.5 dB |
| Peaking | 81 Hz    | 7.93 | 0.9 dB  |
| Peaking | 4820 Hz  | 5.04 | -7.1 dB |
| Peaking | 4889 Hz  | 1.94 | 4.8 dB  |
| Peaking | 7019 Hz  | 5.78 | -4.0 dB |
| Peaking | 11903 Hz | 7.15 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC300/Sennheiser%20PXC300.png)