# Paradigm Shift E3m

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -7.6; 23 -7.6; 25 -7.6; 28 -7.7; 31 -7.8; 34 -7.9; 37 -8.0; 41 -8.1; 45 -8.3; 49 -8.5; 54 -8.7; 60 -8.9; 66 -9.2; 72 -9.5; 79 -9.9; 87 -10.3; 96 -10.6; 106 -10.8; 116 -11.1; 128 -11.3; 141 -11.5; 155 -11.6; 170 -11.6; 187 -11.5; 206 -11.5; 227 -11.2; 249 -11.0; 274 -10.6; 302 -10.2; 332 -9.7; 365 -9.1; 402 -8.4; 442 -7.6; 486 -6.8; 535 -5.9; 588 -4.7; 647 -3.7; 712 -2.7; 783 -1.6; 861 -0.9; 947 -0.3; 1042 0.4; 1146 0.7; 1261 0.8; 1387 0.4; 1526 -0.5; 1678 1.1; 1846 1.1; 2031 2.0; 2234 3.7; 2457 5.8; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.5; 4788 3.8; 5267 3.2; 5793 1.9; 6373 1.8; 7010 2.4; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Paradigm Shift E3m ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.18 | -7.4 dB |
| Peaking | 179 Hz  | 0.63 | -6.7 dB |
| Peaking | 380 Hz  | 1.19 | -4.3 dB |
| Peaking | 2516 Hz | 4.24 | 2.9 dB  |
| Peaking | 3585 Hz | 1.21 | 6.2 dB  |
| Peaking | 557 Hz  | 3.82 | -0.8 dB |
| Peaking | 1097 Hz | 2    | 1.4 dB  |
| Peaking | 1531 Hz | 7.16 | -1.5 dB |
| Peaking | 8993 Hz | 3.09 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Paradigm%20Shift%20E3m/Paradigm%20Shift%20E3m.png)