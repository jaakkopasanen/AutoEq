# Fischer Audio SBA-03

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.5; 25 4.3; 28 4.1; 31 3.9; 34 3.7; 37 3.5; 41 3.2; 45 3.0; 49 2.7; 54 2.4; 60 2.1; 66 1.7; 72 1.3; 79 0.9; 87 0.4; 96 -0.0; 106 -0.3; 116 -0.6; 128 -0.9; 141 -1.2; 155 -1.5; 170 -1.6; 187 -1.7; 206 -1.9; 227 -1.8; 249 -1.9; 274 -1.8; 302 -1.7; 332 -1.5; 365 -1.4; 402 -1.2; 442 -0.8; 486 -0.7; 535 -0.4; 588 0.1; 647 0.2; 712 0.2; 783 0.6; 861 0.4; 947 0.2; 1042 -0.0; 1146 -0.3; 1261 -0.6; 1387 -1.2; 1526 -1.7; 1678 -2.2; 1846 -2.5; 2031 -2.8; 2234 -3.6; 2457 -4.2; 2703 -3.4; 2973 0.9; 3270 5.2; 3597 6.0; 3957 6.0; 4353 4.7; 4788 1.5; 5267 -2.0; 5793 -4.5; 6373 1.1; 7010 2.5; 7711 0.3; 8482 -1.6; 9330 -1.2; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio SBA-03 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 24 Hz   |  1.39 | 4.7 dB   |
| Peaking | 46 Hz   |  2.16 | 2.3 dB   |
| Peaking | 2625 Hz |  1.48 | -10.0 dB |
| Peaking | 3461 Hz |  1.57 | 12.1 dB  |
| Peaking | 5555 Hz |  6.99 | -7.5 dB  |
| Peaking | 73 Hz   |  1.39 | 1.3 dB   |
| Peaking | 349 Hz  |  0.31 | -2.5 dB  |
| Peaking | 712 Hz  |  0.87 | 2.6 dB   |
| Peaking | 6820 Hz | 10.3  | 3.2 dB   |
| Peaking | 8856 Hz |  6.52 | -2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fischer%20Audio%20SBA-03/Fischer%20Audio%20SBA-03.png)