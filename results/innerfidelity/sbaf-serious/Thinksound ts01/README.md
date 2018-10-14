# Thinksound ts01

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 21 -6.8; 23 -6.8; 25 -6.8; 28 -6.9; 31 -6.9; 34 -7.0; 37 -7.1; 41 -7.2; 45 -7.3; 49 -7.4; 54 -7.6; 60 -7.8; 66 -8.1; 72 -8.3; 79 -8.6; 87 -8.9; 96 -9.2; 106 -9.3; 116 -9.4; 128 -9.5; 141 -9.6; 155 -9.5; 170 -9.4; 187 -9.2; 206 -9.0; 227 -8.6; 249 -8.2; 274 -7.7; 302 -7.2; 332 -6.6; 365 -6.0; 402 -5.4; 442 -4.5; 486 -4.0; 535 -3.3; 588 -2.3; 647 -1.7; 712 -1.1; 783 -0.3; 861 -0.1; 947 0.1; 1042 -0.0; 1146 0.6; 1261 0.9; 1387 0.6; 1526 0.4; 1678 0.3; 1846 0.5; 2031 0.8; 2234 0.9; 2457 0.9; 2703 0.6; 2973 0.7; 3270 1.7; 3597 3.1; 3957 3.2; 4353 1.4; 4788 0.1; 5267 -1.7; 5793 -6.9; 6373 -6.5; 7010 -0.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.6dB` and instead set Global volume in the UI for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksound ts01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.2dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 0.19 | -6.5 dB  |
| Peaking | 156 Hz  | 0.67 | -5.6 dB  |
| Peaking | 326 Hz  | 1.21 | -3.1 dB  |
| Peaking | 4305 Hz | 0.77 | 2.8 dB   |
| Peaking | 6022 Hz | 4.84 | -11.0 dB |
| Peaking | 1125 Hz | 1.58 | 1.0 dB   |
| Peaking | 2939 Hz | 4.97 | -1.0 dB  |
| Peaking | 3744 Hz | 5.2  | 2.1 dB   |
| Peaking | 5108 Hz | 0.47 | -0.7 dB  |
| Peaking | 7303 Hz | 6.91 | 2.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Thinksound%20ts01/Thinksound%20ts01.png)