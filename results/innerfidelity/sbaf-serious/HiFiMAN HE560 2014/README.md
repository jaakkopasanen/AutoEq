# HiFiMAN HE560 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 0.0; 23 2.0; 25 2.1; 28 2.1; 31 2.2; 34 2.2; 37 2.2; 41 2.2; 45 2.3; 49 2.2; 54 2.1; 60 2.0; 66 1.8; 72 1.5; 79 1.2; 87 1.0; 96 0.6; 106 0.3; 116 -0.0; 128 -0.3; 141 -0.6; 155 -0.8; 170 -0.9; 187 -1.1; 206 -1.3; 227 -1.3; 249 -1.5; 274 -1.2; 302 -1.1; 332 -1.4; 365 -1.8; 402 -2.1; 442 -1.9; 486 -1.1; 535 1.0; 588 1.7; 647 0.6; 712 0.1; 783 -0.4; 861 -0.5; 947 -0.0; 1042 0.2; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 0.2; 1678 1.4; 1846 2.5; 2031 2.9; 2234 2.1; 2457 1.8; 2703 1.0; 2973 -0.3; 3270 -1.5; 3597 -2.4; 3957 -2.6; 4353 -4.5; 4788 -3.7; 5267 0.8; 5793 -0.0; 6373 -2.5; 7010 -1.5; 7711 -1.4; 8482 -3.3; 9330 -2.8; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.1dB` and instead set Global volume in the UI for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE560 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.53 | 2.5 dB  |
| Peaking | 242 Hz  | 0.78 | -1.8 dB |
| Peaking | 2063 Hz | 3.04 | 3.3 dB  |
| Peaking | 4286 Hz | 3.5  | -4.6 dB |
| Peaking | 8728 Hz | 4.85 | -3.8 dB |
| Peaking | 431 Hz  | 3.99 | -1.6 dB |
| Peaking | 569 Hz  | 5.36 | 2.7 dB  |
| Peaking | 1320 Hz | 6.31 | -1.0 dB |
| Peaking | 5418 Hz | 8.98 | 2.5 dB  |
| Peaking | 6523 Hz | 7.63 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE560%202014/HiFiMAN%20HE560%202014.png)