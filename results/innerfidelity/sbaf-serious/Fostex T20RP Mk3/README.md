# Fostex T20RP Mk3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.6; 45 4.3; 49 2.9; 54 1.3; 60 -0.3; 66 -1.8; 72 -3.0; 79 -4.1; 87 -4.9; 96 -5.5; 106 -5.5; 116 -5.4; 128 -5.1; 141 -4.7; 155 -4.3; 170 -3.7; 187 -3.2; 206 -2.6; 227 -2.3; 249 -2.1; 274 -1.7; 302 -2.0; 332 -1.5; 365 -0.2; 402 0.2; 442 0.4; 486 2.4; 535 2.1; 588 2.4; 647 3.0; 712 2.7; 783 2.9; 861 1.4; 947 0.8; 1042 0.1; 1146 -0.3; 1261 0.9; 1387 -0.3; 1526 1.5; 1678 1.7; 1846 1.7; 2031 2.8; 2234 2.4; 2457 2.7; 2703 2.7; 2973 2.2; 3270 1.8; 3597 1.0; 3957 -0.8; 4353 -1.5; 4788 0.5; 5267 5.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -3.6; 9330 -6.2; 10263 -3.8; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T20RP Mk3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 38 Hz   | 0.51 | 11.1 dB  |
| Peaking | 86 Hz   | 0.56 | -10.9 dB |
| Peaking | 631 Hz  | 1.19 | 3.4 dB   |
| Peaking | 5985 Hz | 3.06 | 7.0 dB   |
| Peaking | 9282 Hz | 4.14 | -7.4 dB  |
| Peaking | 774 Hz  | 5.16 | 0.9 dB   |
| Peaking | 1123 Hz | 1.4  | -2.0 dB  |
| Peaking | 2672 Hz | 0.74 | 3.4 dB   |
| Peaking | 4451 Hz | 2.17 | -5.2 dB  |
| Peaking | 5194 Hz | 7.88 | 4.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T20RP%20Mk3/Fostex%20T20RP%20Mk3.png)