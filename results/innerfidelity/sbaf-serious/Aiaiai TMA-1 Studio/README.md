# Aiaiai TMA-1 Studio

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.2; 31 4.1; 34 3.1; 37 2.2; 41 1.1; 45 0.3; 49 -0.4; 54 -1.0; 60 -1.5; 66 -1.9; 72 -2.2; 79 -2.5; 87 -2.6; 96 -2.8; 106 -2.6; 116 -2.6; 128 -2.8; 141 -3.2; 155 -3.4; 170 -3.1; 187 -3.0; 206 -3.0; 227 -2.9; 249 -2.8; 274 -2.5; 302 -1.9; 332 -1.6; 365 -1.9; 402 -1.6; 442 -1.4; 486 -1.3; 535 -0.8; 588 0.2; 647 1.0; 712 1.6; 783 1.8; 861 1.2; 947 0.3; 1042 -0.1; 1146 0.1; 1261 1.2; 1387 1.3; 1526 1.7; 1678 2.5; 1846 3.6; 2031 4.7; 2234 5.7; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 5.3; 3957 5.2; 4353 5.9; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.4; 7010 1.3; 7711 0.2; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aiaiai TMA-1 Studio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.92 | 8.0 dB  |
| Peaking | 102 Hz  | 0.23 | -3.5 dB |
| Peaking | 717 Hz  | 3.31 | 2.5 dB  |
| Peaking | 2699 Hz | 1.18 | 6.2 dB  |
| Peaking | 5312 Hz | 2.35 | 5.2 dB  |
| Peaking | 1090 Hz | 7.48 | -0.9 dB |
| Peaking | 2074 Hz | 5.83 | 0.6 dB  |
| Peaking | 6308 Hz | 5.49 | 0.8 dB  |
| Peaking | 6389 Hz | 7.32 | 2.3 dB  |
| Peaking | 7396 Hz | 2.16 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aiaiai%20TMA-1%20Studio/Aiaiai%20TMA-1%20Studio.png)