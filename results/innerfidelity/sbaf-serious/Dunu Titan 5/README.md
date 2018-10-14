# Dunu Titan 5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.1dB
GraphicEQ: 21 -4.2; 23 -4.3; 25 -4.3; 28 -4.4; 31 -4.4; 34 -4.5; 37 -4.6; 41 -4.6; 45 -4.7; 49 -4.7; 54 -4.8; 60 -5.0; 66 -5.1; 72 -5.3; 79 -5.4; 87 -5.6; 96 -5.8; 106 -5.7; 116 -5.7; 128 -5.7; 141 -5.5; 155 -5.4; 170 -5.2; 187 -4.8; 206 -4.5; 227 -4.1; 249 -3.7; 274 -3.3; 302 -2.8; 332 -2.3; 365 -1.9; 402 -1.6; 442 -1.1; 486 -0.3; 535 -0.3; 588 0.3; 647 0.8; 712 0.7; 783 1.0; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.2; 1387 -2.0; 1526 -2.8; 1678 -3.5; 1846 -3.9; 2031 -4.1; 2234 -4.4; 2457 -4.1; 2703 -3.5; 2973 -1.7; 3270 0.7; 3597 2.0; 3957 1.4; 4353 -1.2; 4788 -3.5; 5267 -5.9; 5793 -8.4; 6373 -4.0; 7010 0.0; 7711 0.3; 8482 0.0; 9330 -0.0; 10263 -1.7; 11289 -0.2; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.1dB` and instead set Global volume in the UI for both channels to **-21**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Titan 5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.34 | -4.2 dB |
| Peaking | 120 Hz  | 0.9  | -3.7 dB |
| Peaking | 227 Hz  | 1.51 | -2.2 dB |
| Peaking | 2048 Hz | 2.11 | -4.8 dB |
| Peaking | 5668 Hz | 5.32 | -9.0 dB |
| Peaking | 743 Hz  | 2.42 | 1.6 dB  |
| Peaking | 2734 Hz | 5.3  | -1.6 dB |
| Peaking | 3641 Hz | 3.15 | 4.9 dB  |
| Peaking | 4567 Hz | 0.84 | -1.8 dB |
| Peaking | 7311 Hz | 4.36 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20Titan%205/Dunu%20Titan%205.png)