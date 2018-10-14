# Skullcandy Navigator

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.4; 23 -2.4; 25 -2.5; 28 -2.5; 31 -2.5; 34 -2.5; 37 -2.5; 41 -2.5; 45 -2.5; 49 -2.5; 54 -2.6; 60 -2.8; 66 -2.9; 72 -3.0; 79 -3.2; 87 -3.5; 96 -3.8; 106 -3.9; 116 -4.0; 128 -4.3; 141 -4.4; 155 -4.3; 170 -4.2; 187 -3.9; 206 -4.3; 227 -4.3; 249 -4.2; 274 -3.8; 302 -3.3; 332 -3.0; 365 -2.6; 402 -2.0; 442 -1.2; 486 -0.7; 535 -0.1; 588 0.7; 647 1.0; 712 1.1; 783 1.6; 861 0.8; 947 0.4; 1042 0.2; 1146 0.2; 1261 -0.1; 1387 -0.0; 1526 -0.3; 1678 0.4; 1846 0.9; 2031 1.6; 2234 2.5; 2457 3.4; 2703 3.9; 2973 4.3; 3270 4.9; 3597 5.2; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Navigator ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.38 | -2.2 dB |
| Peaking | 118 Hz  | 0.8  | -2.7 dB |
| Peaking | 254 Hz  | 0.84 | -3.0 dB |
| Peaking | 673 Hz  | 2.24 | 2.0 dB  |
| Peaking | 4315 Hz | 1.09 | 6.7 dB  |
| Peaking | 1515 Hz | 2.72 | -1.0 dB |
| Peaking | 2553 Hz | 2.93 | 1.2 dB  |
| Peaking | 4328 Hz | 3.56 | -0.8 dB |
| Peaking | 6334 Hz | 2.88 | 4.6 dB  |
| Peaking | 7391 Hz | 1.59 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Navigator/Skullcandy%20Navigator.png)