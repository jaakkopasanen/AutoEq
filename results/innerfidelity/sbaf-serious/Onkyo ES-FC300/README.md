# Onkyo ES-FC300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.5; 23 -4.7; 25 -4.9; 28 -5.0; 31 -5.0; 34 -4.9; 37 -5.0; 41 -5.1; 45 -5.3; 49 -5.5; 54 -5.4; 60 -5.0; 66 -4.5; 72 -4.0; 79 -4.7; 87 -5.6; 96 -5.8; 106 -5.2; 116 -5.5; 128 -5.9; 141 -5.8; 155 -5.4; 170 -4.6; 187 -4.1; 206 -2.7; 227 -1.5; 249 -0.3; 274 -0.1; 302 -1.4; 332 -2.2; 365 -2.8; 402 -3.0; 442 -2.8; 486 -2.6; 535 -2.3; 588 -1.8; 647 -1.6; 712 -1.3; 783 -0.8; 861 -0.5; 947 -0.1; 1042 0.1; 1146 0.4; 1261 0.7; 1387 0.7; 1526 0.3; 1678 0.0; 1846 0.1; 2031 0.5; 2234 0.7; 2457 0.9; 2703 0.5; 2973 1.2; 3270 1.8; 3597 2.3; 3957 5.4; 4353 5.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Onkyo ES-FC300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.65 | -4.0 dB |
| Peaking | 68 Hz   | 0.72 | -3.2 dB |
| Peaking | 138 Hz  | 1.63 | -4.2 dB |
| Peaking | 461 Hz  | 1.85 | -2.8 dB |
| Peaking | 5037 Hz | 1.71 | 6.8 dB  |
| Peaking | 261 Hz  | 6.92 | 1.9 dB  |
| Peaking | 2830 Hz | 4.22 | -0.2 dB |
| Peaking | 6246 Hz | 6.06 | 1.8 dB  |
| Peaking | 6669 Hz | 5.18 | 1.9 dB  |
| Peaking | 7507 Hz | 1.99 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Onkyo%20ES-FC300/Onkyo%20ES-FC300.png)