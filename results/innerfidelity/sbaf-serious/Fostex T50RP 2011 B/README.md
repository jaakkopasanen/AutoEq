# Fostex T50RP 2011 B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.3; 106 4.2; 116 3.4; 128 2.5; 141 1.7; 155 1.2; 170 0.9; 187 0.3; 206 0.0; 227 -0.1; 249 -0.1; 274 -0.1; 302 -0.1; 332 0.2; 365 0.8; 402 0.5; 442 0.4; 486 0.2; 535 0.4; 588 0.6; 647 0.8; 712 0.0; 783 0.4; 861 -0.4; 947 -0.4; 1042 0.3; 1146 0.1; 1261 -0.2; 1387 -0.5; 1526 -1.2; 1678 -0.7; 1846 0.1; 2031 1.3; 2234 3.0; 2457 5.1; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50RP 2011 B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 53 Hz   | 0.24 | 6.8 dB  |
| Peaking | 189 Hz  | 0.88 | -3.9 dB |
| Peaking | 1526 Hz | 1.99 | -2.8 dB |
| Peaking | 1863 Hz | 4.92 | -1.3 dB |
| Peaking | 3621 Hz | 0.8  | 7.0 dB  |
| Peaking | 2607 Hz | 4.35 | 2.0 dB  |
| Peaking | 3421 Hz | 1.15 | -1.1 dB |
| Peaking | 6272 Hz | 2.17 | 5.5 dB  |
| Peaking | 7401 Hz | 1.51 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50RP%202011%20B/Fostex%20T50RP%202011%20B.png)