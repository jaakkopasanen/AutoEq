# Audeze LCD-3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 21 0.0; 23 3.4; 25 3.1; 28 2.4; 31 1.8; 34 1.6; 37 1.5; 41 1.4; 45 1.4; 49 1.1; 54 0.7; 60 0.6; 66 0.5; 72 0.3; 79 0.0; 87 -0.3; 96 -0.7; 106 -0.9; 116 -1.1; 128 -1.4; 141 -1.7; 155 -1.8; 170 -2.0; 187 -2.2; 206 -2.3; 227 -2.2; 249 -2.2; 274 -2.2; 302 -2.1; 332 -2.0; 365 -1.8; 402 -1.9; 442 -2.0; 486 -2.2; 535 -2.2; 588 -1.9; 647 -1.8; 712 -1.8; 783 -1.3; 861 -1.1; 947 -0.4; 1042 0.3; 1146 0.5; 1261 0.8; 1387 0.3; 1526 -0.2; 1678 0.1; 1846 0.9; 2031 1.3; 2234 1.1; 2457 1.4; 2703 1.4; 2973 1.3; 3270 1.6; 3597 3.8; 3957 5.2; 4353 5.0; 4788 4.3; 5267 3.1; 5793 0.9; 6373 2.7; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.1; 16529 -2.5; 18182 -5.3; 20000 -3.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.5dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.33 | 4.2 dB  |
| Peaking | 267 Hz   | 0.45 | -2.4 dB |
| Peaking | 4274 Hz  | 1.62 | 5.1 dB  |
| Peaking | 15119 Hz | 1.83 | 2.2 dB  |
| Peaking | 18450 Hz | 1.06 | -6.0 dB |
| Peaking | 688 Hz   | 2.31 | -0.8 dB |
| Peaking | 1146 Hz  | 3.56 | 1.1 dB  |
| Peaking | 2190 Hz  | 2.62 | 0.8 dB  |
| Peaking | 3279 Hz  | 3.86 | -1.7 dB |
| Peaking | 3703 Hz  | 5    | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3/Audeze%20LCD-3.png)