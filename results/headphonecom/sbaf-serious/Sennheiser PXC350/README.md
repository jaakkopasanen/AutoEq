# Sennheiser PXC350

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.7; 25 2.1; 28 1.5; 31 1.1; 34 1.0; 37 0.9; 41 1.0; 45 1.1; 49 1.1; 54 1.3; 60 1.5; 66 1.5; 72 1.6; 79 1.8; 87 1.8; 96 1.4; 106 1.3; 116 1.2; 128 1.2; 141 1.2; 155 1.3; 170 1.8; 187 1.9; 206 2.3; 227 2.4; 249 2.2; 274 2.0; 302 1.8; 332 1.6; 365 1.3; 402 0.8; 442 0.3; 486 -0.3; 535 -0.5; 588 -0.4; 647 -0.6; 712 -0.4; 783 -0.2; 861 0.3; 947 -0.0; 1042 0.2; 1146 0.3; 1261 0.2; 1387 -0.3; 1526 -1.2; 1678 -2.7; 1846 -4.1; 2031 2.4; 2234 6.0; 2457 -2.6; 2703 -4.6; 2973 -0.1; 3270 2.8; 3597 2.5; 3957 4.3; 4353 6.0; 4788 3.2; 5267 5.2; 5793 3.5; 6373 0.4; 7010 -0.6; 7711 0.3; 8482 -0.5; 9330 -2.6; 10263 -2.5; 11289 -0.6; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -3.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.06 | 1.7 dB  |
| Peaking | 1874 Hz | 4.09 | -7.3 dB |
| Peaking | 2156 Hz | 5.11 | 10.5 dB |
| Peaking | 2580 Hz | 6.21 | -8.3 dB |
| Peaking | 4340 Hz | 2.26 | 5.8 dB  |
| Peaking | 254 Hz  | 2.05 | 1.2 dB  |
| Peaking | 569 Hz  | 2.21 | -1.3 dB |
| Peaking | 5535 Hz | 8.92 | 6.5 dB  |
| Peaking | 5647 Hz | 2.86 | -2.5 dB |
| Peaking | 9780 Hz | 4.37 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC350/Sennheiser%20PXC350.png)