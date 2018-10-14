# HiFiMAN HE400S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.9; 49 5.5; 54 5.1; 60 4.5; 66 3.9; 72 3.4; 79 2.8; 87 2.3; 96 1.8; 106 1.6; 116 1.4; 128 1.0; 141 0.8; 155 0.7; 170 0.6; 187 0.5; 206 0.6; 227 0.6; 249 0.6; 274 0.6; 302 0.4; 332 0.2; 365 0.2; 402 0.0; 442 0.6; 486 1.1; 535 1.2; 588 1.2; 647 1.1; 712 0.8; 783 0.6; 861 0.2; 947 -0.1; 1042 -0.1; 1146 0.5; 1261 0.4; 1387 -0.1; 1526 0.1; 1678 0.4; 1846 1.0; 2031 1.5; 2234 2.0; 2457 2.6; 2703 2.6; 2973 2.2; 3270 2.5; 3597 2.4; 3957 2.2; 4353 -0.1; 4788 1.3; 5267 5.6; 5793 4.9; 6373 1.6; 7010 2.1; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE400S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 21 Hz   |  0.44 | 5.5 dB  |
| Peaking | 49 Hz   |  1.11 | 2.3 dB  |
| Peaking | 570 Hz  |  2.57 | 1.3 dB  |
| Peaking | 2751 Hz |  1.73 | 2.7 dB  |
| Peaking | 5506 Hz |  5.49 | 6.1 dB  |
| Peaking | 1481 Hz |  6.22 | -0.6 dB |
| Peaking | 3801 Hz |  6.21 | 1.2 dB  |
| Peaking | 4468 Hz |  9.85 | -2.3 dB |
| Peaking | 6944 Hz | 12.76 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE400S/HiFiMAN%20HE400S.png)