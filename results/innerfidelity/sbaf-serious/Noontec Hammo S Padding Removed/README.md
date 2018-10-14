# Noontec Hammo S Padding Removed

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.3; 25 3.1; 28 2.8; 31 2.6; 34 2.4; 37 2.3; 41 2.2; 45 2.1; 49 2.0; 54 1.8; 60 1.6; 66 1.4; 72 1.3; 79 1.1; 87 1.1; 96 1.0; 106 1.1; 116 0.8; 128 0.2; 141 -0.4; 155 -0.8; 170 -0.1; 187 -0.6; 206 -0.6; 227 -0.5; 249 -0.0; 274 0.7; 302 1.2; 332 1.6; 365 1.7; 402 2.1; 442 2.2; 486 2.4; 535 2.4; 588 1.9; 647 1.0; 712 0.4; 783 0.6; 861 0.7; 947 0.6; 1042 -0.3; 1146 -0.9; 1261 -1.4; 1387 -1.9; 1526 -2.1; 1678 -2.0; 1846 -1.4; 2031 -0.2; 2234 1.1; 2457 2.9; 2703 4.3; 2973 5.0; 3270 4.6; 3597 0.7; 3957 3.2; 4353 1.6; 4788 5.2; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Hammo S Padding Removed ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.45 | 3.3 dB  |
| Peaking | 480 Hz  | 1.68 | 2.6 dB  |
| Peaking | 1581 Hz | 1.93 | -2.9 dB |
| Peaking | 2849 Hz | 2.85 | 5.2 dB  |
| Peaking | 5590 Hz | 2.7  | 6.6 dB  |
| Peaking | 186 Hz  | 1.08 | -3.7 dB |
| Peaking | 196 Hz  | 0.62 | 2.6 dB  |
| Peaking | 467 Hz  | 4.12 | -0.7 dB |
| Peaking | 6560 Hz | 7.24 | 2.4 dB  |
| Peaking | 7639 Hz | 2.12 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Hammo%20S%20Padding%20Removed/Noontec%20Hammo%20S%20Padding%20Removed.png)