# HZSOUND HZ3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.5dB
GraphicEQ: 21 0.0; 23 0.4; 25 0.1; 28 -0.2; 31 -0.4; 34 -0.7; 37 -0.9; 41 -1.1; 45 -1.3; 49 -1.5; 54 -1.8; 60 -2.1; 66 -2.4; 72 -2.8; 79 -3.1; 87 -3.6; 96 -3.9; 106 -4.1; 116 -4.3; 128 -4.6; 141 -4.8; 155 -4.9; 170 -5.0; 187 -4.9; 206 -4.9; 227 -4.8; 249 -4.7; 274 -4.4; 302 -4.2; 332 -4.0; 365 -3.7; 402 -3.4; 442 -2.9; 486 -2.7; 535 -2.4; 588 -1.7; 647 -1.4; 712 -1.1; 783 -0.8; 861 -0.9; 947 0.4; 1042 -0.4; 1146 -0.7; 1261 -0.2; 1387 0.1; 1526 -0.7; 1678 -0.9; 1846 -0.8; 2031 -0.5; 2234 -0.3; 2457 0.1; 2703 0.6; 2973 1.3; 3270 2.2; 3597 1.8; 3957 1.3; 4353 -0.4; 4788 -4.8; 5267 -8.4; 5793 -5.4; 6373 -0.3; 7010 2.0; 7711 0.3; 8482 -0.3; 9330 -1.5; 10263 -0.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.5dB` and instead set Global volume in the UI for both channels to **-24**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HZSOUND HZ3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.1dB.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 120 Hz  |  0.65 | -3.4 dB  |
| Peaking | 282 Hz  |  0.68 | -3.2 dB  |
| Peaking | 3998 Hz |  1.96 | 4.6 dB   |
| Peaking | 5302 Hz |  2.71 | -11.1 dB |
| Peaking | 6688 Hz |  4.31 | 5.0 dB   |
| Peaking | 14 Hz   |  1.63 | 0.9 dB   |
| Peaking | 966 Hz  | 12.18 | 1.3 dB   |
| Peaking | 1830 Hz |  3.5  | -0.8 dB  |
| Peaking | 3201 Hz |  8.35 | 0.9 dB   |
| Peaking | 9296 Hz | 10.34 | -1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HZSOUND%20HZ3/HZSOUND%20HZ3.png)