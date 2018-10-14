# Soul Combat

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.8; 25 2.6; 28 1.1; 31 -0.2; 34 -1.2; 37 -2.1; 41 -3.0; 45 -3.7; 49 -4.1; 54 -4.6; 60 -5.0; 66 -5.3; 72 -5.6; 79 -5.9; 87 -6.3; 96 -6.5; 106 -6.8; 116 -7.1; 128 -7.4; 141 -7.9; 155 -8.4; 170 -8.5; 187 -8.7; 206 -9.0; 227 -9.5; 249 -9.9; 274 -10.4; 302 -10.9; 332 -11.3; 365 -11.6; 402 -11.9; 442 -12.6; 486 -12.7; 535 -11.7; 588 -9.2; 647 -6.2; 712 -3.0; 783 0.0; 861 1.6; 947 1.1; 1042 -1.0; 1146 -2.9; 1261 -3.3; 1387 -2.3; 1526 -1.6; 1678 -2.9; 1846 -4.0; 2031 -2.7; 2234 -0.2; 2457 2.8; 2703 4.6; 2973 5.6; 3270 5.4; 3597 5.5; 3957 5.8; 4353 4.6; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -3.1; 10263 -4.2; 11289 -0.8; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul Combat ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 2.42 | 6.3 dB  |
| Peaking | 163 Hz  | 0.38 | -8.1 dB |
| Peaking | 442 Hz  | 1.71 | -9.0 dB |
| Peaking | 3256 Hz | 2.65 | 5.9 dB  |
| Peaking | 5367 Hz | 2.51 | 6.4 dB  |
| Peaking | 580 Hz  | 3.57 | -3.3 dB |
| Peaking | 872 Hz  | 2.06 | 5.8 dB  |
| Peaking | 1189 Hz | 3.22 | -3.8 dB |
| Peaking | 1860 Hz | 5.29 | -4.5 dB |
| Peaking | 9956 Hz | 4.95 | -5.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20Combat/Soul%20Combat.png)