# Sennheiser HD 800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 21 0.0; 23 2.9; 25 2.6; 28 2.1; 31 1.8; 34 1.5; 37 1.3; 41 1.2; 45 1.4; 49 1.5; 54 1.2; 60 0.6; 66 0.4; 72 -0.4; 79 -1.1; 87 -1.6; 96 -1.9; 106 -2.2; 116 -2.5; 128 -2.8; 141 -3.1; 155 -3.3; 170 -3.2; 187 -3.5; 206 -3.5; 227 -3.5; 249 -3.5; 274 -3.4; 302 -3.2; 332 -2.9; 365 -2.7; 402 -2.6; 442 -2.4; 486 -2.1; 535 -1.9; 588 -1.6; 647 -1.3; 712 -1.1; 783 -0.8; 861 -0.7; 947 -0.1; 1042 0.1; 1146 1.1; 1261 1.3; 1387 1.5; 1526 1.1; 1678 1.3; 1846 1.5; 2031 1.6; 2234 1.3; 2457 2.4; 2703 2.5; 2973 1.5; 3270 1.4; 3597 0.9; 3957 -1.8; 4353 -2.3; 4788 -2.1; 5267 -3.5; 5793 -7.0; 6373 -7.4; 7010 -2.5; 7711 -1.4; 8482 -2.9; 9330 -5.6; 10263 -2.6; 11289 0.0; 12418 0.0; 13660 -2.7; 15026 -4.4; 16529 -3.0; 18182 -2.2; 20000 -2.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.6dB` and instead set Global volume in the UI for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.24 | 3.2 dB  |
| Peaking | 192 Hz   | 0.55 | -3.9 dB |
| Peaking | 6044 Hz  | 3.98 | -8.4 dB |
| Peaking | 15495 Hz | 1.39 | -3.7 dB |
| Peaking | 20291 Hz | 1.44 | -2.3 dB |
| Peaking | 1305 Hz  | 3.78 | 1.4 dB  |
| Peaking | 2807 Hz  | 1.13 | 2.6 dB  |
| Peaking | 4193 Hz  | 4.67 | -2.9 dB |
| Peaking | 9466 Hz  | 5.09 | -6.0 dB |
| Peaking | 11440 Hz | 2.72 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20800/Sennheiser%20HD%20800.png)