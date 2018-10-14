# Meze 11 Neo

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 21 0.0; 23 2.2; 25 1.7; 28 1.0; 31 0.4; 34 -0.1; 37 -0.5; 41 -1.1; 45 -1.5; 49 -1.9; 54 -2.4; 60 -3.0; 66 -3.5; 72 -4.0; 79 -4.4; 87 -4.9; 96 -5.4; 106 -5.7; 116 -5.9; 128 -6.2; 141 -6.5; 155 -6.6; 170 -6.6; 187 -6.5; 206 -6.4; 227 -6.2; 249 -6.0; 274 -5.6; 302 -5.2; 332 -4.7; 365 -4.3; 402 -3.7; 442 -3.0; 486 -2.6; 535 -2.0; 588 -1.1; 647 -0.5; 712 -0.1; 783 0.2; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.8; 1387 -1.4; 1526 -2.1; 1678 -2.6; 1846 -3.0; 2031 -3.2; 2234 -3.5; 2457 -2.8; 2703 -1.7; 2973 0.5; 3270 2.4; 3597 3.4; 3957 2.8; 4353 0.7; 4788 -0.0; 5267 1.3; 5793 2.7; 6373 4.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.7dB` and instead set Global volume in the UI for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 11 Neo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.52 | 3.4 dB  |
| Peaking | 158 Hz  | 0.52 | -6.9 dB |
| Peaking | 2161 Hz | 2.01 | -3.9 dB |
| Peaking | 3541 Hz | 3.71 | 4.5 dB  |
| Peaking | 6372 Hz | 5.1  | 4.8 dB  |
| Peaking | 356 Hz  | 1.81 | -0.9 dB |
| Peaking | 658 Hz  | 2.94 | 0.5 dB  |
| Peaking | 844 Hz  | 1.72 | 1.3 dB  |
| Peaking | 1561 Hz | 4.22 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2011%20Neo/Meze%2011%20Neo.png)