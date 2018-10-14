# Sennheiser HD 25-1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.0dB
GraphicEQ: 21 0.0; 23 5.7; 25 5.1; 28 4.6; 31 4.4; 34 4.3; 37 3.6; 41 2.3; 45 1.8; 49 2.1; 54 2.9; 60 3.4; 66 3.1; 72 1.6; 79 0.1; 87 -0.2; 96 -1.8; 106 -1.6; 116 -0.9; 128 -1.2; 141 -1.5; 155 0.1; 170 0.3; 187 -0.5; 206 -1.7; 227 -1.4; 249 -0.6; 274 -0.3; 302 0.4; 332 0.9; 365 1.2; 402 1.5; 442 1.5; 486 1.3; 535 1.3; 588 1.2; 647 1.0; 712 0.8; 783 0.5; 861 0.4; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.7; 1387 -1.6; 1526 -2.6; 1678 -3.2; 1846 -3.7; 2031 -3.9; 2234 -3.1; 2457 -1.6; 2703 0.4; 2973 2.1; 3270 2.5; 3597 2.8; 3957 1.9; 4353 2.6; 4788 4.5; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -4.2; 9330 -6.6; 10263 -3.2; 11289 -1.7; 12418 -1.5; 13660 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.0dB` and instead set Global volume in the UI for both channels to **-69**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 1.27 | 6.1 dB   |
| Peaking | 61 Hz   | 5.08 | 3.2 dB   |
| Peaking | 1935 Hz | 2.3  | -5.1 dB  |
| Peaking | 6160 Hz | 0.99 | 7.7 dB   |
| Peaking | 9048 Hz | 2.26 | -10.5 dB |
| Peaking | 103 Hz  | 2.71 | -2.1 dB  |
| Peaking | 220 Hz  | 3.78 | -2.0 dB  |
| Peaking | 458 Hz  | 1.16 | 1.6 dB   |
| Peaking | 3146 Hz | 3.14 | 3.8 dB   |
| Peaking | 3233 Hz | 1.63 | -2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%2025-1/Sennheiser%20HD%2025-1.png)