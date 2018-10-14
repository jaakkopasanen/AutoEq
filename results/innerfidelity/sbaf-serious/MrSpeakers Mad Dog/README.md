# MrSpeakers Mad Dog

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.5; 72 5.2; 79 2.8; 87 0.2; 96 -0.8; 106 -0.7; 116 -0.4; 128 -0.1; 141 0.2; 155 0.9; 170 0.4; 187 0.5; 206 0.7; 227 1.1; 249 1.2; 274 1.3; 302 1.5; 332 1.6; 365 1.3; 402 1.3; 442 0.9; 486 0.0; 535 -0.3; 588 1.0; 647 1.6; 712 1.1; 783 -0.0; 861 -0.6; 947 -0.5; 1042 0.5; 1146 0.5; 1261 0.8; 1387 1.0; 1526 1.3; 1678 1.9; 1846 2.9; 2031 4.5; 2234 5.5; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 4.3; 7010 2.3; 7711 0.2; 8482 -1.7; 9330 -2.1; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Mad Dog ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.81 | 7.1 dB  |
| Peaking | 327 Hz  | 2.36 | 1.5 dB  |
| Peaking | 2531 Hz | 1.74 | 4.5 dB  |
| Peaking | 5141 Hz | 0.96 | 6.3 dB  |
| Peaking | 8604 Hz | 2.4  | -4.8 dB |
| Peaking | 38 Hz   | 2.73 | -1.8 dB |
| Peaking | 74 Hz   | 1.49 | 5.0 dB  |
| Peaking | 91 Hz   | 2.03 | -5.6 dB |
| Peaking | 660 Hz  | 6.01 | 1.5 dB  |
| Peaking | 877 Hz  | 3.61 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Mad%20Dog/MrSpeakers%20Mad%20Dog.png)