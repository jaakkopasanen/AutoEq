# Etymotic mc3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.7; 66 5.4; 72 5.1; 79 4.6; 87 4.2; 96 3.7; 106 3.4; 116 3.2; 128 2.8; 141 2.5; 155 2.4; 170 2.2; 187 2.0; 206 2.0; 227 1.9; 249 1.9; 274 1.9; 302 1.9; 332 2.0; 365 1.9; 402 2.0; 442 2.1; 486 2.0; 535 2.0; 588 2.3; 647 2.2; 712 1.9; 783 1.8; 861 1.2; 947 0.5; 1042 -0.4; 1146 -1.1; 1261 -2.0; 1387 -3.1; 1526 -4.0; 1678 -4.4; 1846 -3.7; 2031 -3.2; 2234 -2.4; 2457 -0.9; 2703 0.5; 2973 2.6; 3270 4.4; 3597 5.6; 3957 5.5; 4353 3.9; 4788 3.8; 5267 5.6; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic mc3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.34 | 6.3 dB  |
| Peaking | 760 Hz  | 0.56 | 3.2 dB  |
| Peaking | 1671 Hz | 0.98 | -6.4 dB |
| Peaking | 3574 Hz | 2.02 | 6.6 dB  |
| Peaking | 5842 Hz | 3.33 | 5.9 dB  |
| Peaking | 6638 Hz | 9.03 | 1.8 dB  |
| Peaking | 7804 Hz | 2.54 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20mc3/Etymotic%20mc3.png)