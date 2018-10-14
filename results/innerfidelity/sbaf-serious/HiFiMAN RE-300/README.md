# HiFiMAN RE-300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.1; 23 -0.2; 25 -0.3; 28 -0.4; 31 -0.5; 34 -0.7; 37 -0.8; 41 -0.9; 45 -1.0; 49 -1.2; 54 -1.5; 60 -1.8; 66 -2.1; 72 -2.4; 79 -2.7; 87 -3.0; 96 -3.5; 106 -3.7; 116 -3.9; 128 -4.0; 141 -4.3; 155 -4.3; 170 -4.4; 187 -4.3; 206 -4.2; 227 -4.0; 249 -3.8; 274 -3.5; 302 -3.2; 332 -2.8; 365 -2.4; 402 -1.9; 442 -1.3; 486 -1.0; 535 -0.5; 588 0.2; 647 0.6; 712 0.7; 783 1.1; 861 0.8; 947 0.4; 1042 -0.4; 1146 -0.5; 1261 -0.8; 1387 -2.4; 1526 -3.5; 1678 -3.3; 1846 -1.7; 2031 1.3; 2234 4.7; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.9; 6373 2.4; 7010 2.2; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 100 Hz  | 0.77 | -1.3 dB |
| Peaking | 200 Hz  | 0.56 | -3.8 dB |
| Peaking | 685 Hz  | 1.9  | 1.5 dB  |
| Peaking | 1622 Hz | 2.25 | -7.6 dB |
| Peaking | 3096 Hz | 0.72 | 7.6 dB  |
| Peaking | 1958 Hz | 6.41 | -1.0 dB |
| Peaking | 2335 Hz | 4.6  | 1.9 dB  |
| Peaking | 3200 Hz | 2.7  | -1.1 dB |
| Peaking | 5544 Hz | 2.72 | 3.6 dB  |
| Peaking | 7563 Hz | 1.1  | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-300/HiFiMAN%20RE-300.png)