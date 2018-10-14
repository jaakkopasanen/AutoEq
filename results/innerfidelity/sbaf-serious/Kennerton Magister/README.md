# Kennerton Magister

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.8dB
GraphicEQ: 21 0.0; 23 5.7; 25 5.2; 28 4.6; 31 4.2; 34 3.9; 37 3.6; 41 3.5; 45 3.4; 49 3.3; 54 3.1; 60 2.5; 66 2.4; 72 2.5; 79 2.3; 87 1.1; 96 0.6; 106 -0.4; 116 -1.2; 128 -1.8; 141 -2.0; 155 -1.9; 170 -1.3; 187 -2.2; 206 -2.0; 227 -1.5; 249 -0.8; 274 0.5; 302 2.1; 332 3.4; 365 3.9; 402 3.2; 442 2.6; 486 1.7; 535 1.2; 588 1.0; 647 0.5; 712 0.4; 783 0.6; 861 0.5; 947 -0.0; 1042 -0.1; 1146 -0.4; 1261 -1.1; 1387 -2.1; 1526 -3.2; 1678 -4.0; 1846 -4.7; 2031 -4.1; 2234 -3.9; 2457 -2.9; 2703 -2.1; 2973 -0.9; 3270 -0.5; 3597 -0.1; 3957 -0.2; 4353 0.6; 4788 1.9; 5267 5.7; 5793 6.0; 6373 4.7; 7010 2.4; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.8dB` and instead set Global volume in the UI for both channels to **-67**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kennerton Magister ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.27 | 6.1 dB  |
| Peaking | 52 Hz   | 2.07 | 2.7 dB  |
| Peaking | 381 Hz  | 3.05 | 4.2 dB  |
| Peaking | 1943 Hz | 1.79 | -4.9 dB |
| Peaking | 5728 Hz | 3.39 | 7.0 dB  |
| Peaking | 79 Hz   | 2.36 | 2.3 dB  |
| Peaking | 179 Hz  | 0.64 | -2.6 dB |
| Peaking | 313 Hz  | 4.03 | 2.4 dB  |
| Peaking | 611 Hz  | 1.07 | 1.1 dB  |
| Peaking | 8250 Hz | 5.16 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Kennerton%20Magister/Kennerton%20Magister.png)