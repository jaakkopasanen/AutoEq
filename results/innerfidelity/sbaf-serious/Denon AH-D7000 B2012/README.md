# Denon AH-D7000 B2012

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 21 0.0; 23 0.9; 25 0.1; 28 -0.6; 31 -1.1; 34 -1.4; 37 -1.6; 41 -1.7; 45 -1.6; 49 -1.5; 54 -1.5; 60 -1.4; 66 -1.2; 72 -1.4; 79 -1.7; 87 -2.1; 96 -2.4; 106 -2.5; 116 -2.7; 128 -2.8; 141 -3.0; 155 -3.0; 170 -2.9; 187 -3.0; 206 -2.9; 227 -2.7; 249 -2.5; 274 -2.2; 302 -2.0; 332 -1.7; 365 -1.5; 402 -1.2; 442 -0.7; 486 -0.5; 535 -0.2; 588 0.2; 647 0.1; 712 -0.2; 783 -0.5; 861 -0.7; 947 0.4; 1042 -0.1; 1146 0.1; 1261 0.4; 1387 0.1; 1526 -0.4; 1678 -0.7; 1846 -0.7; 2031 -0.6; 2234 0.4; 2457 2.1; 2703 1.2; 2973 1.1; 3270 0.8; 3597 -0.2; 3957 -0.0; 4353 0.0; 4788 0.0; 5267 1.7; 5793 0.9; 6373 0.0; 7010 -0.4; 7711 0.2; 8482 0.0; 9330 -1.4; 10263 -0.9; 11289 0.0; 12418 0.0; 13660 -0.2; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.4dB` and instead set Global volume in the UI for both channels to **-24**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7000 B2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 1.37 | 3.6 dB  |
| Peaking | 34 Hz   | 1.03 | -1.9 dB |
| Peaking | 163 Hz  | 0.66 | -3.1 dB |
| Peaking | 2553 Hz | 6.31 | 2.2 dB  |
| Peaking | 5362 Hz | 8.03 | 1.8 dB  |
| Peaking | 1442 Hz | 1.36 | 0.8 dB  |
| Peaking | 1742 Hz | 2.38 | -1.5 dB |
| Peaking | 3092 Hz | 8.88 | 0.8 dB  |
| Peaking | 9706 Hz | 8.17 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D7000%20B2012/Denon%20AH-D7000%20B2012.png)