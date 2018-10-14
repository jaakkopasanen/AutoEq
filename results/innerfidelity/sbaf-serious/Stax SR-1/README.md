# Stax SR-1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 5.5; 96 3.3; 106 1.4; 116 0.5; 128 -0.1; 141 -0.4; 155 -0.4; 170 -0.8; 187 -0.9; 206 -0.5; 227 -0.2; 249 0.2; 274 0.5; 302 0.7; 332 1.0; 365 1.1; 402 1.1; 442 1.5; 486 1.4; 535 1.4; 588 1.7; 647 1.7; 712 1.6; 783 1.4; 861 0.9; 947 0.6; 1042 0.2; 1146 0.9; 1261 1.6; 1387 1.5; 1526 0.5; 1678 0.3; 1846 0.7; 2031 1.4; 2234 1.6; 2457 1.6; 2703 1.6; 2973 2.4; 3270 3.7; 3597 5.4; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -3.8; 10263 -2.0; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.66 | 7.1 dB  |
| Peaking | 616 Hz  | 1.48 | 1.7 dB  |
| Peaking | 4164 Hz | 1.55 | 5.9 dB  |
| Peaking | 5991 Hz | 3.45 | 4.1 dB  |
| Peaking | 9524 Hz | 5.28 | -5.2 dB |
| Peaking | 17 Hz   | 1.15 | 3.0 dB  |
| Peaking | 38 Hz   | 1.7  | -1.8 dB |
| Peaking | 81 Hz   | 2.46 | 3.5 dB  |
| Peaking | 133 Hz  | 1.26 | -2.5 dB |
| Peaking | 1301 Hz | 7.12 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-1/Stax%20SR-1.png)