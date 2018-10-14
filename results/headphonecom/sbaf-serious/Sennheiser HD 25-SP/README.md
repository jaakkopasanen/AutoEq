# Sennheiser HD 25-SP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.7; 25 1.1; 28 0.2; 31 -0.4; 34 -0.8; 37 -0.9; 41 -1.5; 45 -2.6; 49 -3.3; 54 -3.7; 60 -4.0; 66 -4.2; 72 -4.6; 79 -4.3; 87 -4.0; 96 -5.6; 106 -7.0; 116 -7.0; 128 -6.8; 141 -6.0; 155 -5.1; 170 -5.5; 187 -6.5; 206 -6.5; 227 -5.9; 249 -4.8; 274 -4.0; 302 -2.8; 332 -1.2; 365 0.0; 402 1.0; 442 1.2; 486 1.3; 535 1.4; 588 1.4; 647 1.3; 712 1.1; 783 0.9; 861 0.6; 947 0.2; 1042 -0.2; 1146 -0.7; 1261 -1.4; 1387 -2.4; 1526 -3.4; 1678 -4.3; 1846 -4.7; 2031 -4.6; 2234 -4.0; 2457 -3.5; 2703 -2.6; 2973 -0.4; 3270 0.8; 3597 1.4; 3957 0.4; 4353 0.9; 4788 0.8; 5267 3.8; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -6.1; 9330 -9.0; 10263 -4.3; 11289 -0.2; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-SP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 108 Hz  | 0.96 | -6.4 dB  |
| Peaking | 213 Hz  | 2.7  | -4.7 dB  |
| Peaking | 1944 Hz | 2.11 | -5.4 dB  |
| Peaking | 6112 Hz | 2.6  | 7.1 dB   |
| Peaking | 9148 Hz | 4.41 | -11.1 dB |
| Peaking | 16 Hz   | 0.89 | 4.0 dB   |
| Peaking | 58 Hz   | 0.64 | -2.0 dB  |
| Peaking | 86 Hz   | 3.69 | 3.0 dB   |
| Peaking | 545 Hz  | 1.5  | 2.3 dB   |
| Peaking | 3432 Hz | 7.42 | 1.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%2025-SP/Sennheiser%20HD%2025-SP.png)