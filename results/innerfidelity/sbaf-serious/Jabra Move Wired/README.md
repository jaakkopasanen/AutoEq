# Jabra Move Wired

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.9; 23 -4.0; 25 -4.1; 28 -4.1; 31 -4.0; 34 -3.9; 37 -3.7; 41 -3.4; 45 -2.6; 49 -1.8; 54 -2.0; 60 -3.0; 66 -2.8; 72 -2.3; 79 -1.6; 87 -1.8; 96 -3.2; 106 -4.1; 116 -4.1; 128 -3.9; 141 -4.1; 155 -3.5; 170 -3.1; 187 -2.6; 206 -1.6; 227 -0.4; 249 -0.3; 274 -1.3; 302 -1.9; 332 -1.9; 365 -1.7; 402 -1.6; 442 -1.8; 486 -2.0; 535 -2.1; 588 -2.0; 647 -1.9; 712 -1.3; 783 -0.7; 861 -1.5; 947 -0.7; 1042 0.6; 1146 0.0; 1261 0.0; 1387 0.1; 1526 0.2; 1678 0.5; 1846 1.4; 2031 2.4; 2234 3.5; 2457 4.5; 2703 5.0; 2973 4.5; 3270 5.6; 3597 6.0; 3957 6.0; 4353 5.2; 4788 4.6; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Move Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.67 | -4.1 dB |
| Peaking | 128 Hz  | 1.51 | -3.9 dB |
| Peaking | 540 Hz  | 0.95 | -2.1 dB |
| Peaking | 3328 Hz | 1.21 | 5.9 dB  |
| Peaking | 5792 Hz | 3.47 | 4.8 dB  |
| Peaking | 100 Hz  | 6.19 | -0.3 dB |
| Peaking | 1685 Hz | 2.16 | -1.8 dB |
| Peaking | 2309 Hz | 0.96 | 1.6 dB  |
| Peaking | 3036 Hz | 5    | -2.1 dB |
| Peaking | 8434 Hz | 2.95 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Jabra%20Move%20Wired/Jabra%20Move%20Wired.png)