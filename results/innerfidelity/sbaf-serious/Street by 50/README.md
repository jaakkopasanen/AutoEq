# Street by 50

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 0.0; 23 -0.1; 25 -0.8; 28 -1.9; 31 -2.9; 34 -3.7; 37 -4.5; 41 -5.4; 45 -6.2; 49 -6.9; 54 -7.6; 60 -8.4; 66 -9.0; 72 -9.5; 79 -9.9; 87 -10.3; 96 -10.6; 106 -10.8; 116 -10.8; 128 -10.8; 141 -10.7; 155 -10.6; 170 -10.1; 187 -9.7; 206 -9.1; 227 -8.7; 249 -10.0; 274 -9.4; 302 -8.6; 332 -7.9; 365 -7.1; 402 -6.8; 442 -6.3; 486 -6.0; 535 -4.3; 588 -0.4; 647 1.5; 712 2.6; 783 2.3; 861 1.1; 947 0.2; 1042 -0.2; 1146 -0.8; 1261 -0.8; 1387 0.4; 1526 -0.2; 1678 -2.2; 1846 -3.8; 2031 -5.1; 2234 -5.8; 2457 -5.8; 2703 -5.4; 2973 -4.4; 3270 -3.3; 3597 -1.5; 3957 0.5; 4353 2.8; 4788 5.8; 5267 4.4; 5793 -0.9; 6373 3.2; 7010 1.8; 7711 0.3; 8482 -0.2; 9330 -3.8; 10263 -4.6; 11289 -1.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.9dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Street by 50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 73 Hz   |  0.74 | -7.6 dB |
| Peaking | 154 Hz  |  0.94 | -6.8 dB |
| Peaking | 318 Hz  |  1.55 | -6.1 dB |
| Peaking | 2482 Hz |  1.99 | -6.6 dB |
| Peaking | 4817 Hz |  4.46 | 7.0 dB  |
| Peaking | 18 Hz   |  2.57 | 2.0 dB  |
| Peaking | 495 Hz  |  3.65 | -4.2 dB |
| Peaking | 694 Hz  |  2.26 | 4.8 dB  |
| Peaking | 6704 Hz | 10.63 | 4.4 dB  |
| Peaking | 9972 Hz |  5.05 | -5.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Street%20by%2050/Street%20by%2050.png)