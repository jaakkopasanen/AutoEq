# AudioFly AF180

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.6; 25 2.4; 28 2.2; 31 2.0; 34 1.8; 37 1.6; 41 1.4; 45 1.2; 49 0.9; 54 0.7; 60 0.3; 66 0.0; 72 -0.3; 79 -0.7; 87 -1.2; 96 -1.7; 106 -2.0; 116 -2.2; 128 -2.4; 141 -2.7; 155 -2.9; 170 -3.1; 187 -3.0; 206 -3.2; 227 -3.1; 249 -3.1; 274 -2.9; 302 -2.8; 332 -2.7; 365 -2.4; 402 -2.2; 442 -1.8; 486 -1.7; 535 -1.3; 588 -0.7; 647 -0.4; 712 -0.2; 783 0.2; 861 0.1; 947 -0.0; 1042 -0.1; 1146 -0.1; 1261 -0.1; 1387 -0.2; 1526 -0.3; 1678 0.0; 1846 0.7; 2031 1.8; 2234 2.6; 2457 4.1; 2703 5.1; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.7; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.2; 10263 -3.4; 11289 -0.7; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioFly AF180 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.78 | 0.8 dB  |
| Peaking | 21 Hz    | 0.28 | 2.4 dB  |
| Peaking | 187 Hz   | 0.45 | -3.5 dB |
| Peaking | 4280 Hz  | 0.84 | 6.9 dB  |
| Peaking | 10075 Hz | 2.59 | -4.2 dB |
| Peaking | 1642 Hz  | 2.61 | -1.6 dB |
| Peaking | 2856 Hz  | 2.6  | 1.9 dB  |
| Peaking | 4369 Hz  | 1.67 | -1.9 dB |
| Peaking | 6603 Hz  | 1.67 | 3.0 dB  |
| Peaking | 7489 Hz  | 4.2  | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioFly%20AF180/AudioFly%20AF180.png)