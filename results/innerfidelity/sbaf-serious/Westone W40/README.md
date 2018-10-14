# Westone W40

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.3; 25 2.8; 28 2.1; 31 1.6; 34 1.1; 37 0.7; 41 0.2; 45 -0.2; 49 -0.6; 54 -1.0; 60 -1.6; 66 -2.0; 72 -2.5; 79 -3.0; 87 -3.5; 96 -4.1; 106 -4.5; 116 -4.7; 128 -5.1; 141 -5.4; 155 -5.5; 170 -5.7; 187 -5.8; 206 -5.8; 227 -5.7; 249 -5.7; 274 -5.5; 302 -5.4; 332 -5.1; 365 -4.8; 402 -4.5; 442 -3.9; 486 -3.6; 535 -3.1; 588 -2.3; 647 -1.7; 712 -1.2; 783 -0.5; 861 -0.2; 947 -0.0; 1042 0.0; 1146 -0.0; 1261 -0.1; 1387 -0.4; 1526 -0.4; 1678 -0.1; 1846 0.8; 2031 1.9; 2234 3.2; 2457 4.5; 2703 5.5; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.3; 9330 -3.9; 10263 -3.2; 11289 -0.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.88 | 4.5 dB  |
| Peaking | 103 Hz  | 0.86 | -1.9 dB |
| Peaking | 243 Hz  | 0.53 | -5.4 dB |
| Peaking | 4397 Hz | 0.72 | 7.1 dB  |
| Peaking | 9367 Hz | 2.61 | -6.6 dB |
| Peaking | 878 Hz  | 2.7  | 1.0 dB  |
| Peaking | 1644 Hz | 2.24 | -1.8 dB |
| Peaking | 2798 Hz | 2    | 2.5 dB  |
| Peaking | 3871 Hz | 0.86 | -1.3 dB |
| Peaking | 6122 Hz | 5.18 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W40/Westone%20W40.png)