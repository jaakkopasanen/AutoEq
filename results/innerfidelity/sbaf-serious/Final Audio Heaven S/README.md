# Final Audio Heaven S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.8dB
GraphicEQ: 21 0.0; 23 2.5; 25 2.3; 28 2.1; 31 2.0; 34 1.8; 37 1.7; 41 1.5; 45 1.3; 49 1.1; 54 0.9; 60 0.5; 66 0.1; 72 -0.2; 79 -0.6; 87 -1.0; 96 -1.5; 106 -1.8; 116 -1.9; 128 -2.2; 141 -2.5; 155 -2.7; 170 -2.8; 187 -2.9; 206 -2.9; 227 -2.8; 249 -2.8; 274 -2.6; 302 -2.5; 332 -2.3; 365 -2.1; 402 -1.9; 442 -1.4; 486 -1.2; 535 -0.9; 588 -0.3; 647 -0.0; 712 0.1; 783 0.5; 861 0.4; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.6; 1387 -1.0; 1526 -1.5; 1678 -1.7; 1846 -1.7; 2031 -1.6; 2234 -1.9; 2457 -1.9; 2703 -2.3; 2973 -1.5; 3270 0.7; 3597 3.1; 3957 3.6; 4353 2.3; 4788 1.7; 5267 1.2; 5793 -1.4; 6373 -6.7; 7010 -5.6; 7711 -4.6; 8482 -4.7; 9330 -1.7; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.8dB` and instead set Global volume in the UI for both channels to **-38**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Heaven S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.4dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.46 | 2.6 dB   |
| Peaking | 189 Hz   | 0.6  | -3.2 dB  |
| Peaking | 2678 Hz  | 0.92 | -10.3 dB |
| Peaking | 4030 Hz  | 0.63 | 12.7 dB  |
| Peaking | 6832 Hz  | 1.47 | -12.2 dB |
| Peaking | 387 Hz   | 2.42 | -0.5 dB  |
| Peaking | 799 Hz   | 1.65 | 0.9 dB   |
| Peaking | 1760 Hz  | 1.42 | -1.2 dB  |
| Peaking | 2139 Hz  | 3.23 | 1.5 dB   |
| Peaking | 15992 Hz | 1.88 | -0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Final%20Audio%20Heaven%20S/Final%20Audio%20Heaven%20S.png)