# Howard Leight Sync

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.5; 66 3.4; 72 1.5; 79 0.0; 87 -1.3; 96 -3.6; 106 -6.0; 116 -8.2; 128 -10.0; 141 -10.6; 155 -11.5; 170 -11.0; 187 -11.5; 206 -10.9; 227 -10.4; 249 -10.0; 274 -9.4; 302 -8.6; 332 -7.1; 365 -6.4; 402 -6.1; 442 -5.0; 486 -5.2; 535 -4.9; 588 -4.4; 647 -4.2; 712 -3.6; 783 -2.8; 861 -1.8; 947 -0.5; 1042 -0.0; 1146 0.1; 1261 0.2; 1387 -0.2; 1526 -1.9; 1678 -5.1; 1846 -8.5; 2031 -11.2; 2234 -13.5; 2457 -10.7; 2703 -9.8; 2973 -7.9; 3270 -1.4; 3597 0.0; 3957 -2.2; 4353 -2.0; 4788 -3.5; 5267 -7.3; 5793 -13.7; 6373 -15.7; 7010 -13.2; 7711 -12.4; 8482 -14.9; 9330 -17.3; 10263 -16.3; 11289 -13.0; 12418 -11.4; 13660 -13.5; 15026 -14.5; 16529 -10.8; 18182 -7.5; 20000 -6.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Howard Leight Sync ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.1dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 207 Hz   | 0.87 | -12.2 dB |
| Peaking | 2223 Hz  | 3.27 | -13.2 dB |
| Peaking | 8142 Hz  | 1.11 | -12.2 dB |
| Peaking | 14763 Hz | 0.72 | -10.9 dB |
| Peaking | 21967 Hz | 1.93 | -15.5 dB |
| Peaking | 28 Hz    | 0.48 | 6.4 dB   |
| Peaking | 56 Hz    | 2.29 | 3.7 dB   |
| Peaking | 125 Hz   | 2.51 | -5.0 dB  |
| Peaking | 4213 Hz  | 2.55 | 4.1 dB   |
| Peaking | 6042 Hz  | 6.96 | -7.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Howard%20Leight%20Sync/Howard%20Leight%20Sync.png)