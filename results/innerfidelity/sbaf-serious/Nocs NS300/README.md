# Nocs NS300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.4; 45 4.7; 49 4.1; 54 3.6; 60 3.1; 66 2.7; 72 2.3; 79 2.1; 87 2.3; 96 2.4; 106 3.1; 116 4.0; 128 3.8; 141 3.3; 155 3.4; 170 4.4; 187 4.7; 206 5.8; 227 6.0; 249 6.0; 274 6.0; 302 5.5; 332 3.1; 365 2.2; 402 1.7; 442 1.3; 486 0.9; 535 0.6; 588 0.6; 647 0.3; 712 -0.2; 783 -0.3; 861 -0.5; 947 -0.4; 1042 0.5; 1146 1.8; 1261 2.9; 1387 3.0; 1526 4.3; 1678 4.2; 1846 4.8; 2031 4.8; 2234 4.2; 2457 3.9; 2703 2.9; 2973 2.6; 3270 2.0; 3597 3.4; 3957 4.8; 4353 6.0; 4788 4.7; 5267 4.8; 5793 6.0; 6373 5.2; 7010 2.3; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.1  | 2.4 dB  |
| Peaking | 28 Hz   | 1.01 | 4.0 dB  |
| Peaking | 237 Hz  | 1.52 | 5.7 dB  |
| Peaking | 1865 Hz | 1.71 | 4.7 dB  |
| Peaking | 4975 Hz | 1.56 | 5.7 dB  |
| Peaking | 120 Hz  | 7.54 | 1.3 dB  |
| Peaking | 943 Hz  | 1.58 | -2.1 dB |
| Peaking | 1230 Hz | 2.67 | 2.1 dB  |
| Peaking | 6287 Hz | 5.42 | 3.3 dB  |
| Peaking | 7592 Hz | 1.53 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS300/Nocs%20NS300.png)