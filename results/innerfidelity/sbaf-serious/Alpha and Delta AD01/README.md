# Alpha and Delta AD01

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -8.1; 23 -8.1; 25 -8.1; 28 -8.1; 31 -8.1; 34 -8.1; 37 -8.0; 41 -7.9; 45 -7.8; 49 -7.7; 54 -7.6; 60 -7.5; 66 -7.5; 72 -7.4; 79 -7.4; 87 -7.4; 96 -7.3; 106 -7.1; 116 -6.9; 128 -6.7; 141 -6.5; 155 -6.2; 170 -5.8; 187 -5.4; 206 -5.0; 227 -4.6; 249 -4.2; 274 -3.7; 302 -3.2; 332 -2.7; 365 -2.2; 402 -1.8; 442 -1.2; 486 -0.9; 535 -0.5; 588 0.2; 647 0.5; 712 0.6; 783 0.9; 861 0.6; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -0.9; 1387 -1.6; 1526 -2.4; 1678 -3.3; 1846 -3.8; 2031 -4.3; 2234 -4.5; 2457 -3.6; 2703 -1.9; 2973 1.1; 3270 4.3; 3597 5.4; 3957 3.1; 4353 -0.4; 4788 -1.2; 5267 3.3; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.0; 9330 -1.7; 10263 -0.5; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Alpha and Delta AD01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 42 Hz   |  0.19 | -8.2 dB |
| Peaking | 2149 Hz |  1.99 | -5.1 dB |
| Peaking | 3454 Hz |  4.71 | 7.0 dB  |
| Peaking | 6070 Hz |  4.33 | 6.8 dB  |
| Peaking | 9336 Hz |  3.92 | -1.8 dB |
| Peaking | 205 Hz  |  1.27 | -0.7 dB |
| Peaking | 721 Hz  |  1.38 | 1.8 dB  |
| Peaking | 1562 Hz |  4.35 | -1.1 dB |
| Peaking | 4640 Hz | 10.79 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Alpha%20and%20Delta%20AD01/Alpha%20and%20Delta%20AD01.png)