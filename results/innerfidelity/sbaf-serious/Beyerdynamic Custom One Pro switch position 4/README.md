# Beyerdynamic Custom One Pro switch position 4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.0; 25 -0.4; 28 -1.0; 31 -1.4; 34 -1.7; 37 -2.0; 41 -2.3; 45 -2.5; 49 -2.7; 54 -2.7; 60 -2.8; 66 -2.9; 72 -3.0; 79 -3.0; 87 -1.3; 96 0.5; 106 -0.3; 116 -2.9; 128 -4.6; 141 -5.5; 155 -5.1; 170 -3.6; 187 -4.8; 206 -3.9; 227 -2.6; 249 -1.9; 274 -1.3; 302 -0.8; 332 -0.7; 365 -0.5; 402 -0.6; 442 -0.5; 486 -0.8; 535 -0.9; 588 -0.6; 647 -0.6; 712 -0.8; 783 0.2; 861 0.4; 947 0.1; 1042 0.1; 1146 0.2; 1261 -0.1; 1387 -0.7; 1526 -1.5; 1678 -2.2; 1846 -2.5; 2031 -2.4; 2234 -1.6; 2457 0.5; 2703 2.4; 2973 4.2; 3270 5.0; 3597 5.9; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom One Pro switch position 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 1.46 | -2.8 dB |
| Peaking | 163 Hz  | 1.55 | -5.0 dB |
| Peaking | 1731 Hz | 3.05 | -2.8 dB |
| Peaking | 2137 Hz | 3.94 | -3.2 dB |
| Peaking | 4269 Hz | 1.09 | 7.0 dB  |
| Peaking | 79 Hz   | 4.18 | -2.0 dB |
| Peaking | 99 Hz   | 3.6  | 3.3 dB  |
| Peaking | 126 Hz  | 4.96 | -2.0 dB |
| Peaking | 6308 Hz | 3.35 | 4.6 dB  |
| Peaking | 7340 Hz | 1.51 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%204/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%204.png)