# Oppo PM3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.6; 28 1.5; 31 1.5; 34 1.5; 37 1.4; 41 1.4; 45 1.5; 49 1.5; 54 1.5; 60 1.3; 66 1.3; 72 1.2; 79 1.1; 87 1.1; 96 0.7; 106 0.2; 116 0.0; 128 -0.2; 141 -0.4; 155 -0.5; 170 0.4; 187 -0.1; 206 0.0; 227 0.6; 249 1.2; 274 1.9; 302 2.6; 332 2.9; 365 3.0; 402 2.8; 442 2.4; 486 1.7; 535 1.1; 588 1.0; 647 0.6; 712 0.3; 783 0.4; 861 0.3; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.5; 1387 -1.1; 1526 -1.7; 1678 -2.2; 1846 -3.1; 2031 -2.8; 2234 -3.1; 2457 -2.1; 2703 -1.3; 2973 -0.2; 3270 0.5; 3597 0.5; 3957 0.7; 4353 1.0; 4788 3.5; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.69 | 1.8 dB  |
| Peaking | 368 Hz  | 1.76 | 3.2 dB  |
| Peaking | 2052 Hz | 1.69 | -3.5 dB |
| Peaking | 3183 Hz | 4.74 | 0.9 dB  |
| Peaking | 5666 Hz | 2.86 | 7.0 dB  |
| Peaking | 84 Hz   | 1.92 | 0.9 dB  |
| Peaking | 132 Hz  | 1.11 | -0.9 dB |
| Peaking | 290 Hz  | 5.13 | 0.7 dB  |
| Peaking | 6659 Hz | 7.85 | 2.3 dB  |
| Peaking | 7647 Hz | 2.27 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM3/Oppo%20PM3.png)