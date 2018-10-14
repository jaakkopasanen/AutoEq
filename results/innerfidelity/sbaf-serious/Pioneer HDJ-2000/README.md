# Pioneer HDJ-2000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.8; 54 4.5; 60 2.8; 66 1.5; 72 0.4; 79 -0.7; 87 -1.8; 96 -2.3; 106 -2.5; 116 -2.3; 128 -2.1; 141 -2.2; 155 -2.2; 170 -1.9; 187 -2.0; 206 -2.0; 227 -1.9; 249 -1.9; 274 -1.7; 302 -1.4; 332 -1.3; 365 -1.1; 402 -1.1; 442 -0.8; 486 -0.6; 535 -0.7; 588 -0.6; 647 -0.6; 712 -1.0; 783 -1.0; 861 -0.5; 947 0.0; 1042 -0.4; 1146 -1.1; 1261 -1.1; 1387 -1.4; 1526 -1.6; 1678 -1.4; 1846 -0.7; 2031 0.8; 2234 3.1; 2457 5.4; 2703 6.0; 2973 6.0; 3270 5.7; 3597 3.5; 3957 0.7; 4353 2.4; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.2; 10263 -0.2; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 44 Hz   |  0.45 | 9.4 dB  |
| Peaking | 90 Hz   |  0.74 | -7.1 dB |
| Peaking | 934 Hz  |  0.06 | -1.2 dB |
| Peaking | 2805 Hz |  2.48 | 7.6 dB  |
| Peaking | 5590 Hz |  2.31 | 7.4 dB  |
| Peaking | 1365 Hz |  0.75 | 1.8 dB  |
| Peaking | 1594 Hz |  1.48 | -3.1 dB |
| Peaking | 2310 Hz |  6.48 | 1.5 dB  |
| Peaking | 4081 Hz |  9.37 | -2.6 dB |
| Peaking | 4699 Hz | 10.19 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20HDJ-2000/Pioneer%20HDJ-2000.png)