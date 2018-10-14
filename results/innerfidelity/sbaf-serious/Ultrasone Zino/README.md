# Ultrasone Zino

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.8; 28 5.1; 31 4.1; 34 3.2; 37 2.4; 41 1.4; 45 0.6; 49 -0.1; 54 -0.8; 60 -1.5; 66 -1.9; 72 -2.3; 79 -2.4; 87 -2.4; 96 -2.2; 106 -2.1; 116 -1.8; 128 -1.5; 141 -1.1; 155 -0.6; 170 0.1; 187 0.6; 206 1.3; 227 2.2; 249 2.5; 274 3.1; 302 4.4; 332 4.9; 365 5.0; 402 4.3; 442 4.0; 486 4.4; 535 5.2; 588 6.0; 647 6.0; 712 6.0; 783 6.0; 861 4.5; 947 1.6; 1042 -1.2; 1146 -3.3; 1261 -4.3; 1387 -5.7; 1526 -7.1; 1678 -8.3; 1846 -9.1; 2031 -9.6; 2234 -8.3; 2457 -3.1; 2703 0.2; 2973 0.9; 3270 2.6; 3597 3.6; 3957 5.2; 4353 -1.3; 4788 1.1; 5267 1.9; 5793 -2.3; 6373 -2.4; 7010 -0.2; 7711 0.3; 8482 -0.7; 9330 -2.5; 10263 -2.7; 11289 -0.7; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Zino ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 24 Hz    |  1.26 | 7.0 dB   |
| Peaking | 319 Hz   |  0.66 | 10.1 dB  |
| Peaking | 744 Hz   |  1.24 | 11.0 dB  |
| Peaking | 2049 Hz  |  0.24 | -39.7 dB |
| Peaking | 3000 Hz  |  0.3  | 34.6 dB  |
| Peaking | 3864 Hz  | 16.58 | 4.2 dB   |
| Peaking | 6155 Hz  |  6.97 | -3.6 dB  |
| Peaking | 7571 Hz  |  4.93 | 1.5 dB   |
| Peaking | 9819 Hz  |  3.53 | -2.9 dB  |
| Peaking | 14522 Hz |  0.73 | 1.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20Zino/Ultrasone%20Zino.png)