# Bluedio R2-WH

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 -0.1; 25 -0.8; 28 -1.8; 31 -2.5; 34 -3.1; 37 -3.6; 41 -4.1; 45 -4.3; 49 -4.5; 54 -4.7; 60 -4.9; 66 -4.9; 72 -5.0; 79 -5.0; 87 -4.8; 96 -5.0; 106 -5.5; 116 -5.7; 128 -5.7; 141 -6.2; 155 -6.3; 170 -6.0; 187 -6.1; 206 -5.8; 227 -5.6; 249 -5.0; 274 -5.6; 302 -5.1; 332 -4.4; 365 -4.4; 402 -3.5; 442 -2.7; 486 -2.4; 535 -1.4; 588 0.4; 647 1.6; 712 2.5; 783 3.0; 861 2.0; 947 0.5; 1042 -0.2; 1146 -0.2; 1261 0.0; 1387 0.1; 1526 0.1; 1678 -0.4; 1846 -0.9; 2031 -1.2; 2234 -0.2; 2457 -0.1; 2703 0.1; 2973 1.4; 3270 3.5; 3597 3.8; 3957 5.8; 4353 6.0; 4788 5.2; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio R2-WH ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.57 | 3.7 dB  |
| Peaking | 37 Hz   | 0.89 | -2.8 dB |
| Peaking | 276 Hz  | 0.19 | -6.4 dB |
| Peaking | 734 Hz  | 1.15 | 7.8 dB  |
| Peaking | 4727 Hz | 1.4  | 7.0 dB  |
| Peaking | 1477 Hz | 3.07 | 2.4 dB  |
| Peaking | 1580 Hz | 1.52 | -1.4 dB |
| Peaking | 6376 Hz | 4.32 | 3.7 dB  |
| Peaking | 7551 Hz | 1.78 | -2.6 dB |
| Peaking | 7566 Hz | 1.85 | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bluedio%20R2-WH/Bluedio%20R2-WH.png)