# Shure SE530

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.1; 25 2.0; 28 1.9; 31 1.8; 34 1.7; 37 1.5; 41 1.3; 45 1.2; 49 1.0; 54 0.7; 60 0.4; 66 0.0; 72 -0.3; 79 -0.7; 87 -1.1; 96 -1.6; 106 -2.0; 116 -2.2; 128 -2.6; 141 -2.8; 155 -3.0; 170 -3.2; 187 -3.2; 206 -3.4; 227 -3.3; 249 -3.4; 274 -3.2; 302 -3.1; 332 -2.9; 365 -2.7; 402 -2.4; 442 -2.0; 486 -1.8; 535 -1.5; 588 -0.9; 647 -0.5; 712 -0.3; 783 0.1; 861 0.2; 947 0.1; 1042 0.0; 1146 -0.2; 1261 -0.4; 1387 -0.9; 1526 -1.3; 1678 -1.7; 1846 -1.8; 2031 -1.8; 2234 -1.2; 2457 0.4; 2703 2.3; 2973 4.0; 3270 5.4; 3597 5.9; 3957 5.5; 4353 4.4; 4788 4.9; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE530 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.54 | 2.2 dB  |
| Peaking | 204 Hz  | 0.59 | -3.7 dB |
| Peaking | 2015 Hz | 2.13 | -3.2 dB |
| Peaking | 3480 Hz | 1.77 | 6.0 dB  |
| Peaking | 5737 Hz | 3.05 | 5.5 dB  |
| Peaking | 461 Hz  | 1.1  | -1.7 dB |
| Peaking | 614 Hz  | 0.65 | 1.6 dB  |
| Peaking | 1488 Hz | 2.8  | -0.8 dB |
| Peaking | 6580 Hz | 7.8  | 2.1 dB  |
| Peaking | 7766 Hz | 2.2  | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE530/Shure%20SE530.png)