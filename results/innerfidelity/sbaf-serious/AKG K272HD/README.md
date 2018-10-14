# AKG K272HD

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.8; 37 5.2; 41 4.3; 45 3.4; 49 2.7; 54 2.1; 60 1.4; 66 0.5; 72 -0.2; 79 -1.0; 87 -1.1; 96 1.2; 106 4.0; 116 3.1; 128 0.2; 141 -0.8; 155 -0.7; 170 -0.0; 187 -0.5; 206 -0.5; 227 -1.0; 249 -1.3; 274 -1.5; 302 -1.5; 332 -1.6; 365 -1.6; 402 -1.7; 442 -1.6; 486 -1.7; 535 -1.9; 588 -2.1; 647 -3.0; 712 0.2; 783 0.4; 861 0.5; 947 0.5; 1042 -0.3; 1146 -0.3; 1261 -1.1; 1387 -1.8; 1526 -2.8; 1678 -2.8; 1846 -1.6; 2031 1.3; 2234 2.3; 2457 3.9; 2703 4.4; 2973 5.0; 3270 4.6; 3597 5.5; 3957 6.0; 4353 5.3; 4788 5.7; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.0; 8482 -4.1; 9330 -6.5; 10263 -3.2; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K272HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 1.67 | 4.6 dB   |
| Peaking | 34 Hz   | 1.63 | 4.6 dB   |
| Peaking | 1591 Hz | 2.28 | -5.0 dB  |
| Peaking | 4790 Hz | 0.59 | 7.0 dB   |
| Peaking | 9123 Hz | 2.8  | -10.4 dB |
| Peaking | 85 Hz   | 4.17 | -2.3 dB  |
| Peaking | 108 Hz  | 5.84 | 5.0 dB   |
| Peaking | 360 Hz  | 0.78 | -1.8 dB  |
| Peaking | 648 Hz  | 3.82 | -4.2 dB  |
| Peaking | 716 Hz  | 2.37 | 2.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K272HD/AKG%20K272HD.png)