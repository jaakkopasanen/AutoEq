# Santa Cruz Audio SC1000 Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.5; 25 5.3; 28 5.2; 31 5.0; 34 4.9; 37 4.7; 41 4.5; 45 4.4; 49 4.2; 54 4.0; 60 3.7; 66 3.2; 72 2.9; 79 2.6; 87 2.3; 96 1.8; 106 1.6; 116 1.3; 128 1.0; 141 0.7; 155 0.6; 170 0.4; 187 0.3; 206 0.3; 227 0.3; 249 0.3; 274 0.2; 302 0.2; 332 0.2; 365 0.3; 402 0.4; 442 0.7; 486 0.6; 535 0.7; 588 1.0; 647 1.0; 712 0.8; 783 0.9; 861 0.4; 947 0.1; 1042 0.0; 1146 -0.0; 1261 -0.2; 1387 -0.7; 1526 -1.3; 1678 -1.7; 1846 -1.8; 2031 -1.8; 2234 -1.9; 2457 -1.9; 2703 -2.2; 2973 -1.4; 3270 0.4; 3597 2.1; 3957 1.9; 4353 -0.8; 4788 -2.6; 5267 2.1; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.5; 9330 -2.1; 10263 -0.3; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Santa Cruz Audio SC1000 Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.64 | 4.9 dB  |
| Peaking | 50 Hz   | 0.71 | 2.8 dB  |
| Peaking | 3755 Hz | 2.95 | 9.1 dB  |
| Peaking | 4558 Hz | 0.96 | -9.8 dB |
| Peaking | 5951 Hz | 2.67 | 13.1 dB |
| Peaking | 656 Hz  | 1.64 | 1.2 dB  |
| Peaking | 1245 Hz | 3.47 | 0.7 dB  |
| Peaking | 1654 Hz | 2.19 | -0.8 dB |
| Peaking | 9027 Hz | 4.17 | -3.2 dB |
| Peaking | 9913 Hz | 1.33 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Santa%20Cruz%20Audio%20SC1000%20Active/Santa%20Cruz%20Audio%20SC1000%20Active.png)