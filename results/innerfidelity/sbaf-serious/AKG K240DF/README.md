# AKG K240DF

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.9; 66 5.5; 72 5.0; 79 4.7; 87 4.2; 96 3.4; 106 2.8; 116 2.1; 128 1.1; 141 0.3; 155 -0.2; 170 -0.3; 187 -0.8; 206 -1.2; 227 -1.3; 249 -1.5; 274 -1.4; 302 -1.5; 332 -1.5; 365 -1.9; 402 -1.8; 442 -1.4; 486 -1.7; 535 -1.3; 588 -0.7; 647 -0.6; 712 -0.6; 783 -0.3; 861 -0.2; 947 -0.1; 1042 0.1; 1146 0.3; 1261 0.3; 1387 -0.2; 1526 -1.1; 1678 -1.7; 1846 -1.8; 2031 -1.5; 2234 -1.0; 2457 0.3; 2703 0.9; 2973 2.2; 3270 0.7; 3597 -2.4; 3957 -2.1; 4353 -1.1; 4788 0.4; 5267 4.5; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.2; 8482 -3.3; 9330 -5.5; 10263 -4.1; 11289 -0.1; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240DF ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 39 Hz   |  0.66 | 7.0 dB  |
| Peaking | 1846 Hz |  2.33 | -2.8 dB |
| Peaking | 4277 Hz |  2.07 | -9.7 dB |
| Peaking | 5511 Hz |  0.93 | 10.8 dB |
| Peaking | 9081 Hz |  2.19 | -9.6 dB |
| Peaking | 41 Hz   |  2.68 | -1.5 dB |
| Peaking | 84 Hz   |  1    | 2.2 dB  |
| Peaking | 271 Hz  |  0.44 | -2.4 dB |
| Peaking | 1214 Hz |  0.33 | 0.6 dB  |
| Peaking | 3636 Hz | 13.22 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K240DF/AKG%20K240DF.png)