# RHA T10i Reference Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -9.1; 23 -9.4; 25 -9.7; 28 -9.9; 31 -10.1; 34 -10.2; 37 -10.3; 41 -10.5; 45 -10.5; 49 -10.5; 54 -10.6; 60 -10.7; 66 -10.8; 72 -10.8; 79 -10.9; 87 -11.0; 96 -11.0; 106 -10.9; 116 -10.7; 128 -10.6; 141 -10.4; 155 -10.1; 170 -9.7; 187 -9.3; 206 -8.9; 227 -8.3; 249 -7.8; 274 -7.1; 302 -6.4; 332 -5.8; 365 -5.1; 402 -4.5; 442 -3.7; 486 -3.2; 535 -2.6; 588 -1.7; 647 -1.2; 712 -1.1; 783 -0.4; 861 0.0; 947 0.3; 1042 -0.2; 1146 -0.5; 1261 -0.9; 1387 -1.7; 1526 -2.7; 1678 -3.5; 1846 -4.2; 2031 -4.6; 2234 -4.7; 2457 -3.6; 2703 -1.8; 2973 0.3; 3270 1.1; 3597 1.1; 3957 2.5; 4353 4.5; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -4.7; 9330 -7.2; 10263 -9.7; 11289 -5.7; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T10i Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.24 | -10.0 dB |
| Peaking | 187 Hz   | 0.63 | -4.8 dB  |
| Peaking | 2110 Hz  | 2.07 | -5.7 dB  |
| Peaking | 5481 Hz  | 1.38 | 7.7 dB   |
| Peaking | 9859 Hz  | 2.69 | -11.5 dB |
| Peaking | 380 Hz   | 2.41 | -0.6 dB  |
| Peaking | 902 Hz   | 1.9  | 1.4 dB   |
| Peaking | 1564 Hz  | 4.72 | -1.1 dB  |
| Peaking | 10989 Hz | 7.55 | -3.7 dB  |
| Peaking | 12209 Hz | 3.18 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T10i%20Reference%20Filter/RHA%20T10i%20Reference%20Filter.png)