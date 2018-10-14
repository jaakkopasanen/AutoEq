# Music Hall DeBe

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.8; 37 5.5; 41 5.0; 45 4.6; 49 4.3; 54 3.8; 60 3.4; 66 2.9; 72 2.5; 79 2.0; 87 1.3; 96 0.8; 106 0.3; 116 -0.1; 128 -0.7; 141 -1.1; 155 -1.6; 170 -1.8; 187 -1.8; 206 -2.3; 227 -2.6; 249 -2.9; 274 -2.8; 302 -2.6; 332 -2.8; 365 -2.6; 402 -2.3; 442 -2.2; 486 -1.8; 535 -0.7; 588 1.0; 647 2.2; 712 2.1; 783 1.6; 861 0.8; 947 0.3; 1042 0.0; 1146 0.1; 1261 0.1; 1387 0.3; 1526 1.0; 1678 2.2; 1846 3.8; 2031 5.6; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 2.5; 5267 3.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Music Hall DeBe ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.36 | 6.3 dB  |
| Peaking | 421 Hz  | 0.27 | -3.9 dB |
| Peaking | 689 Hz  | 1.74 | 5.5 dB  |
| Peaking | 2198 Hz | 1.8  | 4.7 dB  |
| Peaking | 3860 Hz | 0.91 | 5.6 dB  |
| Peaking | 5021 Hz | 7.46 | -4.8 dB |
| Peaking | 6196 Hz | 2.2  | 5.9 dB  |
| Peaking | 7449 Hz | 1.63 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Music%20Hall%20DeBe/Music%20Hall%20DeBe.png)