# Sterling TE-400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 4.6; 66 2.7; 72 0.9; 79 -0.8; 87 -2.1; 96 -3.5; 106 -4.4; 116 -4.4; 128 -4.4; 141 -4.2; 155 -3.9; 170 -3.4; 187 -3.3; 206 -3.1; 227 -3.0; 249 -2.9; 274 -2.5; 302 -1.9; 332 -1.9; 365 -1.8; 402 -1.7; 442 -1.5; 486 -1.6; 535 -1.4; 588 0.1; 647 4.5; 712 6.0; 783 6.0; 861 3.9; 947 1.3; 1042 -0.7; 1146 -1.2; 1261 -0.6; 1387 0.2; 1526 1.4; 1678 2.4; 1846 3.5; 2031 4.8; 2234 5.0; 2457 4.8; 2703 3.8; 2973 3.0; 3270 3.1; 3597 5.6; 3957 2.5; 4353 -3.8; 4788 -2.2; 5267 3.5; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.4; 8482 -1.6; 9330 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sterling TE-400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 59 Hz   |  0.24 | 27.4 dB  |
| Peaking | 94 Hz   |  0.28 | -27.3 dB |
| Peaking | 737 Hz  |  3.3  | 8.9 dB   |
| Peaking | 2308 Hz |  1.66 | 5.9 dB   |
| Peaking | 6032 Hz |  5.59 | 6.7 dB   |
| Peaking | 3019 Hz |  3    | -0.9 dB  |
| Peaking | 3748 Hz |  4.49 | 7.7 dB   |
| Peaking | 4356 Hz |  3.95 | -7.8 dB  |
| Peaking | 5454 Hz | 10.32 | 3.9 dB   |
| Peaking | 8291 Hz |  9.39 | -2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sterling%20TE-400/Sterling%20TE-400.png)