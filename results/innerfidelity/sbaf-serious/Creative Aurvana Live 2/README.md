# Creative Aurvana Live 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.2; 23 -3.5; 25 -3.7; 28 -4.0; 31 -4.2; 34 -4.3; 37 -4.4; 41 -4.5; 45 -4.5; 49 -4.6; 54 -4.5; 60 -4.6; 66 -4.7; 72 -4.6; 79 -4.5; 87 -4.5; 96 -4.8; 106 -5.1; 116 -5.4; 128 -5.6; 141 -5.8; 155 -5.7; 170 -5.1; 187 -5.4; 206 -5.3; 227 -4.9; 249 -4.6; 274 -4.2; 302 -3.5; 332 -2.9; 365 -1.7; 402 -1.1; 442 -0.4; 486 -0.5; 535 -0.5; 588 -0.6; 647 -1.0; 712 -1.3; 783 -1.0; 861 -0.8; 947 -0.4; 1042 0.4; 1146 1.1; 1261 1.9; 1387 2.6; 1526 3.3; 1678 3.7; 1846 4.3; 2031 5.1; 2234 5.5; 2457 5.8; 2703 5.3; 2973 5.2; 3270 6.0; 3597 6.0; 3957 5.5; 4353 3.6; 4788 4.6; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.9; 9330 -4.0; 10263 -0.6; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Live 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.4  | -3.9 dB |
| Peaking | 176 Hz  | 0.69 | -4.8 dB |
| Peaking | 2667 Hz | 0.95 | 6.2 dB  |
| Peaking | 5682 Hz | 3.6  | 5.1 dB  |
| Peaking | 448 Hz  | 3.73 | 1.3 dB  |
| Peaking | 818 Hz  | 1.87 | -1.6 dB |
| Peaking | 2739 Hz | 0.4  | 0.9 dB  |
| Peaking | 2757 Hz | 4.93 | -2.1 dB |
| Peaking | 9124 Hz | 4.58 | -5.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Creative%20Aurvana%20Live%202/Creative%20Aurvana%20Live%202.png)