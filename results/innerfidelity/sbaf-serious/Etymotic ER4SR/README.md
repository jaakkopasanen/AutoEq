# Etymotic ER4SR

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.9; 60 5.5; 66 5.1; 72 4.8; 79 4.3; 87 3.8; 96 3.3; 106 3.0; 116 2.8; 128 2.4; 141 2.1; 155 1.9; 170 1.7; 187 1.5; 206 1.4; 227 1.3; 249 1.3; 274 1.3; 302 1.2; 332 1.3; 365 1.3; 402 1.4; 442 1.6; 486 1.6; 535 1.7; 588 1.9; 647 1.7; 712 1.5; 783 1.4; 861 1.0; 947 0.4; 1042 -0.3; 1146 -1.0; 1261 -1.8; 1387 -2.7; 1526 -3.7; 1678 -4.4; 1846 -4.8; 2031 -4.9; 2234 -4.9; 2457 -4.1; 2703 -2.8; 2973 -0.4; 3270 2.0; 3597 3.1; 3957 2.7; 4353 1.1; 4788 1.3; 5267 3.5; 5793 5.5; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4SR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.38 | 6.3 dB  |
| Peaking | 843 Hz  | 0.64 | 3.9 dB  |
| Peaking | 2226 Hz | 0.57 | -8.0 dB |
| Peaking | 3490 Hz | 2.06 | 8.1 dB  |
| Peaking | 6014 Hz | 2.99 | 7.6 dB  |
| Peaking | 166 Hz  | 2.63 | -0.1 dB |
| Peaking | 6874 Hz | 7.64 | 0.9 dB  |
| Peaking | 7503 Hz | 5.89 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20ER4SR/Etymotic%20ER4SR.png)