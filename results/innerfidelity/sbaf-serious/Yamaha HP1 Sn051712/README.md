# Yamaha HP1 Sn051712

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.0; 25 4.7; 28 4.1; 31 3.7; 34 3.4; 37 3.1; 41 2.8; 45 2.5; 49 2.2; 54 1.9; 60 1.8; 66 1.6; 72 1.4; 79 1.2; 87 1.0; 96 0.5; 106 0.0; 116 -0.2; 128 -0.5; 141 -0.7; 155 -0.9; 170 -0.9; 187 -1.1; 206 -1.2; 227 -1.2; 249 -1.2; 274 -1.0; 302 -1.0; 332 -1.2; 365 -1.1; 402 -1.3; 442 -1.0; 486 -1.3; 535 -1.4; 588 -1.3; 647 -1.3; 712 -1.4; 783 -1.1; 861 -0.8; 947 -0.3; 1042 0.4; 1146 1.4; 1261 2.6; 1387 3.3; 1526 3.3; 1678 3.5; 1846 3.1; 2031 2.2; 2234 0.9; 2457 1.0; 2703 1.8; 2973 2.6; 3270 4.0; 3597 4.4; 3957 4.1; 4353 3.6; 4788 4.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HP1 Sn051712 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.2  | 5.1 dB  |
| Peaking | 51 Hz   | 1.8  | 1.5 dB  |
| Peaking | 1575 Hz | 2.77 | 3.8 dB  |
| Peaking | 3560 Hz | 2.73 | 3.8 dB  |
| Peaking | 5630 Hz | 2.72 | 6.2 dB  |
| Peaking | 80 Hz   | 2.27 | 1.0 dB  |
| Peaking | 376 Hz  | 0.34 | -1.5 dB |
| Peaking | 1253 Hz | 4.04 | 1.7 dB  |
| Peaking | 6553 Hz | 7.66 | 2.1 dB  |
| Peaking | 7818 Hz | 2.61 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20HP1%20Sn051712/Yamaha%20HP1%20Sn051712.png)