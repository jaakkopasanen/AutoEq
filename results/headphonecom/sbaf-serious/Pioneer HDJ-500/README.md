# Pioneer HDJ-500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.7; 31 4.4; 34 2.8; 37 1.4; 41 -0.1; 45 -1.2; 49 -1.9; 54 -2.5; 60 -2.9; 66 -3.0; 72 -2.9; 79 -2.7; 87 -3.0; 96 -3.2; 106 -3.3; 116 -3.3; 128 -3.7; 141 -4.0; 155 -4.2; 170 -4.3; 187 -4.6; 206 -4.6; 227 -4.8; 249 -4.6; 274 -4.3; 302 -4.6; 332 -4.7; 365 -5.3; 402 -5.5; 442 -4.7; 486 -4.4; 535 -3.4; 588 -2.3; 647 -1.5; 712 -1.1; 783 -0.9; 861 -0.5; 947 -0.4; 1042 0.3; 1146 1.1; 1261 1.6; 1387 2.0; 1526 2.6; 1678 3.2; 1846 4.4; 2031 5.8; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 2.0; 5267 -2.0; 5793 -0.5; 6373 5.2; 7010 0.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -2.0; 18182 -2.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.24 | 8.5 dB  |
| Peaking | 105 Hz   | 0.25 | -3.9 dB |
| Peaking | 393 Hz   | 1.28 | -3.2 dB |
| Peaking | 2379 Hz  | 1.14 | 6.4 dB  |
| Peaking | 3948 Hz  | 3.83 | 4.2 dB  |
| Peaking | 54 Hz    | 2.52 | -0.8 dB |
| Peaking | 87 Hz    | 2.49 | 0.7 dB  |
| Peaking | 5465 Hz  | 7.44 | -5.9 dB |
| Peaking | 6235 Hz  | 9.74 | 6.0 dB  |
| Peaking | 17529 Hz | 2.6  | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Pioneer%20HDJ-500/Pioneer%20HDJ-500.png)