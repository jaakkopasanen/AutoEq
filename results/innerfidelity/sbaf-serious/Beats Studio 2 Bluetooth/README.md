# Beats Studio 2 Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.8; 37 5.5; 41 5.1; 45 4.8; 49 4.7; 54 4.4; 60 4.3; 66 4.1; 72 3.8; 79 3.5; 87 3.1; 96 2.8; 106 2.8; 116 2.9; 128 2.9; 141 3.0; 155 3.1; 170 3.3; 187 3.5; 206 3.8; 227 4.2; 249 4.5; 274 5.1; 302 5.6; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 6.0; 535 6.0; 588 5.2; 647 3.3; 712 1.4; 783 0.3; 861 -0.5; 947 -0.5; 1042 0.7; 1146 1.1; 1261 0.4; 1387 0.7; 1526 1.5; 1678 2.3; 1846 3.5; 2031 4.6; 2234 5.3; 2457 5.8; 2703 5.4; 2973 4.4; 3270 1.8; 3597 1.2; 3957 1.9; 4353 4.9; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio 2 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.16 | 6.1 dB  |
| Peaking | 323 Hz  | 1.19 | 5.3 dB  |
| Peaking | 521 Hz  | 3.25 | 4.1 dB  |
| Peaking | 2374 Hz | 2.31 | 5.8 dB  |
| Peaking | 5398 Hz | 2.37 | 6.6 dB  |
| Peaking | 874 Hz  | 3.31 | -2.3 dB |
| Peaking | 1670 Hz | 0.17 | 0.4 dB  |
| Peaking | 3589 Hz | 7.23 | -1.9 dB |
| Peaking | 6540 Hz | 6.89 | 2.6 dB  |
| Peaking | 7705 Hz | 1.85 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Studio%202%20Bluetooth/Beats%20Studio%202%20Bluetooth.png)