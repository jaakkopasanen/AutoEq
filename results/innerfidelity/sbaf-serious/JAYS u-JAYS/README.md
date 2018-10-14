# JAYS u-JAYS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.2; 25 2.9; 28 2.5; 31 2.3; 34 2.1; 37 1.9; 41 1.7; 45 1.6; 49 1.5; 54 1.5; 60 1.1; 66 0.9; 72 0.7; 79 0.6; 87 0.4; 96 0.4; 106 0.5; 116 0.6; 128 0.6; 141 0.1; 155 0.1; 170 0.6; 187 0.4; 206 0.6; 227 1.0; 249 1.4; 274 2.3; 302 3.2; 332 3.7; 365 3.7; 402 3.4; 442 3.0; 486 2.5; 535 2.2; 588 2.1; 647 1.7; 712 1.2; 783 1.0; 861 0.5; 947 0.2; 1042 -0.0; 1146 0.1; 1261 0.1; 1387 -0.0; 1526 -0.2; 1678 -0.2; 1846 0.5; 2031 1.3; 2234 2.2; 2457 3.4; 2703 4.1; 2973 4.2; 3270 3.7; 3597 4.4; 3957 6.0; 4353 5.4; 4788 5.7; 5267 4.7; 5793 2.9; 6373 2.2; 7010 1.0; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JAYS u-JAYS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.91 | 3.6 dB  |
| Peaking | 51 Hz   | 1.76 | 0.8 dB  |
| Peaking | 377 Hz  | 1.4  | 3.8 dB  |
| Peaking | 2720 Hz | 3.13 | 3.0 dB  |
| Peaking | 4422 Hz | 1.86 | 5.9 dB  |
| Peaking | 658 Hz  | 1.91 | 1.2 dB  |
| Peaking | 980 Hz  | 0.62 | -1.2 dB |
| Peaking | 1632 Hz | 4.22 | -1.0 dB |
| Peaking | 1643 Hz | 0.59 | 0.8 dB  |
| Peaking | 8617 Hz | 2.66 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JAYS%20u-JAYS/JAYS%20u-JAYS.png)