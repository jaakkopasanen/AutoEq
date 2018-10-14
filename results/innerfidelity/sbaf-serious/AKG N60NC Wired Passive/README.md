# AKG N60NC Wired Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 -2.9; 23 -2.8; 25 -2.8; 28 -2.7; 31 -2.7; 34 -2.6; 37 -2.5; 41 -2.5; 45 -2.6; 49 -2.7; 54 -2.7; 60 -2.7; 66 -2.7; 72 -2.7; 79 -3.0; 87 -3.6; 96 -4.1; 106 -4.1; 116 -4.0; 128 -4.3; 141 -4.4; 155 -4.2; 170 -4.0; 187 -3.7; 206 -3.0; 227 -2.3; 249 -2.2; 274 -2.4; 302 -2.6; 332 -1.7; 365 -1.3; 402 -1.1; 442 -0.9; 486 -1.9; 535 -0.9; 588 -0.3; 647 -0.1; 712 -0.1; 783 0.2; 861 0.1; 947 0.0; 1042 -0.0; 1146 -0.0; 1261 -0.0; 1387 -0.6; 1526 -1.0; 1678 -1.6; 1846 -1.8; 2031 -1.8; 2234 -2.1; 2457 -1.8; 2703 -1.9; 2973 -1.8; 3270 -1.6; 3597 -1.7; 3957 -1.0; 4353 -0.0; 4788 3.0; 5267 1.2; 5793 4.3; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.8dB` and instead set Global volume in the UI for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N60NC Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.6  | -2.0 dB |
| Peaking | 38 Hz   | 0.18 | -0.7 dB |
| Peaking | 138 Hz  | 0.67 | -3.7 dB |
| Peaking | 2554 Hz | 1.27 | -2.3 dB |
| Peaking | 6149 Hz | 3.81 | 6.0 dB  |
| Peaking | 497 Hz  | 9.37 | -1.4 dB |
| Peaking | 830 Hz  | 1.59 | 0.6 dB  |
| Peaking | 4662 Hz | 2.51 | -1.4 dB |
| Peaking | 4778 Hz | 8.42 | 4.0 dB  |
| Peaking | 8026 Hz | 6.48 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20N60NC%20Wired%20Passive/AKG%20N60NC%20Wired%20Passive.png)