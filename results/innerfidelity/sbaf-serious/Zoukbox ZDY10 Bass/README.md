# Zoukbox ZDY10 Bass

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.2dB
GraphicEQ: 21 -7.3; 23 -7.4; 25 -7.6; 28 -7.8; 31 -7.9; 34 -8.0; 37 -8.1; 41 -8.2; 45 -8.4; 49 -8.5; 54 -8.6; 60 -8.8; 66 -9.0; 72 -9.1; 79 -9.4; 87 -9.6; 96 -9.8; 106 -9.8; 116 -9.7; 128 -9.7; 141 -9.6; 155 -9.4; 170 -9.2; 187 -8.9; 206 -8.5; 227 -8.0; 249 -7.6; 274 -7.0; 302 -6.4; 332 -5.8; 365 -5.1; 402 -4.5; 442 -3.7; 486 -3.2; 535 -2.5; 588 -1.3; 647 -1.0; 712 -0.6; 783 -0.1; 861 0.1; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.4; 1387 -0.8; 1526 -1.3; 1678 -1.7; 1846 -1.7; 2031 -2.0; 2234 -2.2; 2457 -2.5; 2703 -2.3; 2973 -2.3; 3270 -1.9; 3597 -2.2; 3957 -3.3; 4353 -5.8; 4788 -6.9; 5267 -6.6; 5793 -4.7; 6373 -3.2; 7010 -1.7; 7711 -1.9; 8482 -2.7; 9330 -3.7; 10263 -4.7; 11289 -3.0; 12418 -0.5; 13660 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.2dB` and instead set Global volume in the UI for both channels to **-1**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zoukbox ZDY10 Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.26 | -7.3 dB |
| Peaking | 141 Hz   | 0.67 | -5.5 dB |
| Peaking | 291 Hz   | 1.15 | -2.9 dB |
| Peaking | 4869 Hz  | 1.71 | -6.6 dB |
| Peaking | 10171 Hz | 3.54 | -4.5 dB |
| Peaking | 921 Hz   | 1.72 | 1.3 dB  |
| Peaking | 1661 Hz  | 4.39 | -0.3 dB |
| Peaking | 2795 Hz  | 0.82 | -2.1 dB |
| Peaking | 3599 Hz  | 2.56 | 2.7 dB  |
| Peaking | 6974 Hz  | 5.22 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Zoukbox%20ZDY10%20Bass/Zoukbox%20ZDY10%20Bass.png)