# E-Mu Teak 2016

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 21 -1.8; 23 -2.2; 25 -2.6; 28 -3.1; 31 -3.4; 34 -3.5; 37 -3.6; 41 -3.7; 45 -3.8; 49 -3.8; 54 -3.9; 60 -3.8; 66 -3.6; 72 -3.5; 79 -3.7; 87 -4.2; 96 -4.2; 106 -4.3; 116 -4.3; 128 -4.4; 141 -4.4; 155 -4.3; 170 -3.9; 187 -3.9; 206 -3.7; 227 -3.1; 249 -2.7; 274 -2.2; 302 -1.9; 332 -1.7; 365 -1.3; 402 -0.9; 442 -0.5; 486 -0.3; 535 -0.1; 588 0.2; 647 0.1; 712 -0.2; 783 -0.2; 861 0.1; 947 0.2; 1042 -0.0; 1146 0.3; 1261 0.5; 1387 0.4; 1526 0.2; 1678 0.4; 1846 0.8; 2031 1.5; 2234 2.1; 2457 2.8; 2703 3.2; 2973 3.6; 3270 3.7; 3597 2.7; 3957 2.5; 4353 2.2; 4788 1.0; 5267 0.8; 5793 1.2; 6373 2.0; 7010 2.4; 7711 0.3; 8482 0.0; 9330 -0.3; 10263 -0.8; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.0dB` and instead set Global volume in the UI for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `E-Mu Teak 2016 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -3.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.47 | -3.3 dB |
| Peaking | 157 Hz  | 0.83 | -3.5 dB |
| Peaking | 3046 Hz | 1.51 | 3.8 dB  |
| Peaking | 6751 Hz | 6.74 | 2.4 dB  |
| Peaking | 590 Hz  | 3.15 | 0.7 dB  |
| Peaking | 726 Hz  | 4.94 | -0.3 dB |
| Peaking | 9998 Hz | 6.34 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/E-Mu%20Teak%202016/E-Mu%20Teak%202016.png)