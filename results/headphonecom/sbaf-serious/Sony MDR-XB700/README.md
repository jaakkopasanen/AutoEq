# Sony MDR-XB700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 21 -11.6; 23 -11.4; 25 -11.1; 28 -10.5; 31 -10.1; 34 -10.3; 37 -11.0; 41 -11.3; 45 -10.4; 49 -9.0; 54 -7.7; 60 -8.8; 66 -11.0; 72 -12.5; 79 -13.2; 87 -13.5; 96 -13.5; 106 -13.1; 116 -12.4; 128 -11.5; 141 -10.4; 155 -9.7; 170 -9.5; 187 -8.9; 206 -7.6; 227 -6.3; 249 -5.0; 274 -4.0; 302 -2.9; 332 -1.9; 365 -1.6; 402 -1.4; 442 -0.9; 486 -0.2; 535 0.9; 588 1.6; 647 3.7; 712 5.2; 783 4.8; 861 3.3; 947 1.3; 1042 -1.0; 1146 -2.6; 1261 -4.3; 1387 -5.7; 1526 -6.9; 1678 -7.4; 1846 -7.2; 2031 -6.7; 2234 -5.1; 2457 -2.9; 2703 -0.7; 2973 2.2; 3270 5.5; 3597 3.4; 3957 -3.2; 4353 -2.6; 4788 -4.0; 5267 -6.9; 5793 -8.8; 6373 0.4; 7010 2.1; 7711 0.2; 8482 -2.5; 9330 -5.7; 10263 -4.7; 11289 0.0; 12418 0.0; 13660 -0.7; 15026 -4.9; 16529 -1.4; 18182 0.0; 20000 -5.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.2dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.4dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 1.2  | -11.4 dB |
| Peaking | 19 Hz    | 0.2  | -8.1 dB  |
| Peaking | 113 Hz   | 0.86 | -9.7 dB  |
| Peaking | 1717 Hz  | 2.78 | -8.4 dB  |
| Peaking | 10221 Hz | 0.45 | -2.5 dB  |
| Peaking | 735 Hz   | 2.43 | 7.5 dB   |
| Peaking | 3312 Hz  | 4.16 | 10.1 dB  |
| Peaking | 5789 Hz  | 0.83 | -36.5 dB |
| Peaking | 6442 Hz  | 0.79 | 34.1 dB  |
| Peaking | 9500 Hz  | 6.35 | -5.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-XB700/Sony%20MDR-XB700.png)