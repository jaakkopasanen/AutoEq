# Meze Classic 99

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.5; 31 4.7; 34 3.9; 37 3.4; 41 2.8; 45 2.4; 49 2.2; 54 1.9; 60 1.7; 66 1.5; 72 1.4; 79 1.3; 87 1.4; 96 1.2; 106 1.5; 116 1.6; 128 1.1; 141 0.5; 155 0.5; 170 1.1; 187 0.8; 206 0.7; 227 0.9; 249 0.9; 274 1.0; 302 0.9; 332 0.7; 365 0.4; 402 0.1; 442 0.1; 486 -0.4; 535 -0.7; 588 -0.6; 647 -0.6; 712 -0.6; 783 -0.4; 861 -0.5; 947 -0.2; 1042 0.3; 1146 0.2; 1261 -0.1; 1387 -0.2; 1526 -0.4; 1678 -0.5; 1846 -0.2; 2031 0.4; 2234 0.8; 2457 1.5; 2703 2.2; 2973 3.0; 3270 4.4; 3597 5.5; 3957 6.0; 4353 3.0; 4788 3.3; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze Classic 99 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.82 | 6.1 dB  |
| Peaking | 105 Hz  | 1.65 | 1.0 dB  |
| Peaking | 261 Hz  | 2.76 | 1.0 dB  |
| Peaking | 3621 Hz | 2.72 | 5.5 dB  |
| Peaking | 5794 Hz | 3.27 | 6.1 dB  |
| Peaking | 631 Hz  | 2.23 | -0.8 dB |
| Peaking | 1658 Hz | 3.86 | -0.8 dB |
| Peaking | 2637 Hz | 5.25 | 0.7 dB  |
| Peaking | 6638 Hz | 8.27 | 2.1 dB  |
| Peaking | 7715 Hz | 2.26 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%20Classic%2099/Meze%20Classic%2099.png)