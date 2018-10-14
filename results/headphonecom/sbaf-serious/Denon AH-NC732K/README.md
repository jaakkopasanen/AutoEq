# Denon AH-NC732K

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.7dB
GraphicEQ: 21 0.0; 23 5.3; 25 4.7; 28 4.2; 31 3.8; 34 3.4; 37 3.1; 41 3.3; 45 3.5; 49 3.7; 54 4.0; 60 4.3; 66 4.7; 72 4.8; 79 4.5; 87 4.6; 96 4.6; 106 4.8; 116 4.9; 128 5.0; 141 5.2; 155 5.5; 170 5.3; 187 5.4; 206 5.4; 227 5.4; 249 5.4; 274 5.6; 302 5.6; 332 5.5; 365 5.4; 402 5.3; 442 5.2; 486 4.7; 535 4.4; 588 4.0; 647 3.6; 712 3.6; 783 3.4; 861 2.1; 947 0.6; 1042 -0.3; 1146 -0.8; 1261 -2.5; 1387 -3.9; 1526 -0.8; 1678 -0.5; 1846 1.3; 2031 5.2; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.1; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.7dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-NC732K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.54 | 5.7 dB  |
| Peaking | 92 Hz   | 0.37 | 3.8 dB  |
| Peaking | 393 Hz  | 0.49 | 4.0 dB  |
| Peaking | 1362 Hz | 1.96 | -7.7 dB |
| Peaking | 3121 Hz | 0.64 | 7.1 dB  |
| Peaking | 1792 Hz | 8.97 | -3.3 dB |
| Peaking | 2079 Hz | 2.42 | 2.5 dB  |
| Peaking | 2998 Hz | 1.46 | -1.4 dB |
| Peaking | 6142 Hz | 1.92 | 5.4 dB  |
| Peaking | 7557 Hz | 1.41 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-NC732K/Denon%20AH-NC732K.png)