# Sennheiser HD 700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 21 0.0; 23 4.7; 25 4.1; 28 3.4; 31 2.7; 34 2.2; 37 1.7; 41 1.3; 45 0.8; 49 0.4; 54 -0.0; 60 -0.4; 66 -0.8; 72 -1.1; 79 -1.4; 87 -1.8; 96 -2.4; 106 -3.0; 116 -3.2; 128 -3.5; 141 -4.0; 155 -4.2; 170 -4.2; 187 -4.4; 206 -4.3; 227 -4.3; 249 -4.3; 274 -4.1; 302 -3.9; 332 -3.7; 365 -3.5; 402 -3.2; 442 -2.8; 486 -2.7; 535 -2.4; 588 -1.9; 647 -1.7; 712 -1.5; 783 -0.9; 861 -0.8; 947 -0.3; 1042 0.3; 1146 0.6; 1261 1.5; 1387 2.0; 1526 2.9; 1678 3.2; 1846 4.0; 2031 4.5; 2234 4.0; 2457 3.4; 2703 2.8; 2973 2.5; 3270 2.7; 3597 3.6; 3957 2.2; 4353 -1.3; 4788 -3.8; 5267 -5.1; 5793 -6.4; 6373 -9.6; 7010 -4.8; 7711 -1.3; 8482 -1.6; 9330 -2.5; 10263 -1.9; 11289 -0.1; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.7; 18182 -4.2; 20000 -9.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.7dB` and instead set Global volume in the UI for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.54 | 6.9 dB  |
| Peaking | 211 Hz   | 0.41 | -4.5 dB |
| Peaking | 2021 Hz  | 1.2  | 4.8 dB  |
| Peaking | 3668 Hz  | 5.48 | 3.9 dB  |
| Peaking | 6061 Hz  | 2.27 | -8.8 dB |
| Peaking | 7840 Hz  | 4.6  | 4.3 dB  |
| Peaking | 8698 Hz  | 1.49 | -3.1 dB |
| Peaking | 14658 Hz | 0.59 | 2.2 dB  |
| Peaking | 19927 Hz | 1.12 | -9.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20700/Sennheiser%20HD%20700.png)