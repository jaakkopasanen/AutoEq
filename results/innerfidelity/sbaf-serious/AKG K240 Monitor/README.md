# AKG K240 Monitor

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.4; 37 4.6; 41 3.6; 45 2.7; 49 1.9; 54 1.1; 60 0.3; 66 -0.2; 72 -0.4; 79 -0.7; 87 -1.3; 96 -1.7; 106 -2.2; 116 -2.7; 128 -3.1; 141 -3.4; 155 -3.5; 170 -3.3; 187 -3.5; 206 -3.5; 227 -3.3; 249 -3.2; 274 -3.0; 302 -3.0; 332 -3.1; 365 -3.1; 402 -2.8; 442 -2.4; 486 -2.4; 535 -2.0; 588 -1.4; 647 -1.0; 712 -0.7; 783 -0.4; 861 -0.3; 947 -0.0; 1042 0.1; 1146 0.3; 1261 0.4; 1387 -0.0; 1526 -0.8; 1678 -1.4; 1846 -1.5; 2031 -1.4; 2234 -0.4; 2457 1.2; 2703 1.5; 2973 3.0; 3270 1.1; 3597 -3.7; 3957 -2.5; 4353 0.0; 4788 2.0; 5267 5.2; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -2.2; 9330 -3.5; 10263 -1.8; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 Monitor ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.82 | 6.8 dB  |
| Peaking | 188 Hz  | 0.45 | -3.8 dB |
| Peaking | 3855 Hz | 6.77 | -5.3 dB |
| Peaking | 5892 Hz | 2.21 | 6.7 dB  |
| Peaking | 9069 Hz | 3.31 | -4.7 dB |
| Peaking | 458 Hz  | 2.41 | -0.7 dB |
| Peaking | 1262 Hz | 1.05 | 1.2 dB  |
| Peaking | 1802 Hz | 2.28 | -2.6 dB |
| Peaking | 3044 Hz | 3.59 | 3.5 dB  |
| Peaking | 3522 Hz | 8.64 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K240%20Monitor/AKG%20K240%20Monitor.png)