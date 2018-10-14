# AKG K550

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 21 -0.9; 23 -1.1; 25 -1.2; 28 -1.4; 31 -1.5; 34 -1.6; 37 -1.5; 41 -1.4; 45 -1.2; 49 -1.0; 54 -0.9; 60 -0.7; 66 -0.0; 72 0.6; 79 0.9; 87 0.5; 96 -0.7; 106 -1.9; 116 -2.6; 128 -2.8; 141 -2.5; 155 -1.7; 170 -0.5; 187 -1.8; 206 -1.4; 227 -1.2; 249 -1.1; 274 -1.0; 302 -0.8; 332 -0.9; 365 -0.6; 402 -0.4; 442 0.1; 486 0.1; 535 0.5; 588 1.0; 647 1.3; 712 1.4; 783 1.6; 861 0.9; 947 0.3; 1042 -0.3; 1146 -0.9; 1261 -1.4; 1387 -1.7; 1526 -1.9; 1678 -1.6; 1846 -0.9; 2031 -0.2; 2234 -0.0; 2457 0.3; 2703 0.7; 2973 1.7; 3270 2.8; 3597 3.6; 3957 3.8; 4353 3.5; 4788 3.4; 5267 0.5; 5793 -0.7; 6373 -0.0; 7010 1.8; 7711 -1.0; 8482 -5.9; 9330 -6.5; 10263 -1.3; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.0dB` and instead set Global volume in the UI for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 142 Hz  | 1.21 | -2.3 dB |
| Peaking | 744 Hz  | 2.28 | 2.0 dB  |
| Peaking | 1459 Hz | 1.69 | -2.2 dB |
| Peaking | 3916 Hz | 1.99 | 4.3 dB  |
| Peaking | 8967 Hz | 5.26 | -8.2 dB |
| Peaking | 36 Hz   | 0.83 | -1.5 dB |
| Peaking | 79 Hz   | 2.6  | 2.2 dB  |
| Peaking | 114 Hz  | 4.51 | -1.1 dB |
| Peaking | 5765 Hz | 7.5  | -2.0 dB |
| Peaking | 7068 Hz | 9.59 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K550/AKG%20K550.png)