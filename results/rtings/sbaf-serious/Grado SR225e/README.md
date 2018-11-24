# Grado SR225e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.7; 37 5.1; 41 4.1; 45 3.3; 49 2.6; 54 2.0; 60 1.4; 66 0.9; 72 0.7; 79 0.6; 87 0.4; 96 0.2; 106 0.1; 116 -0.1; 128 -0.3; 141 -0.3; 155 -0.3; 170 -0.3; 187 -0.2; 206 -0.1; 227 0.1; 249 0.3; 274 -0.3; 302 -0.1; 332 0.3; 365 0.4; 402 0.4; 442 0.4; 486 0.5; 535 0.5; 588 0.4; 647 0.6; 712 0.5; 783 0.4; 861 0.1; 947 0.1; 1042 0.0; 1146 0.1; 1261 -0.2; 1387 -1.0; 1526 -2.0; 1678 -2.9; 1846 -6.0; 2031 -8.7; 2234 -8.3; 2457 -6.6; 2703 -4.4; 2973 -2.5; 3270 -1.0; 3597 1.3; 3957 1.3; 4353 -5.1; 4788 -3.7; 5267 -1.6; 5793 -1.5; 6373 0.8; 7010 1.9; 7711 -1.2; 8482 -6.1; 9330 -9.6; 10263 -9.3; 11289 -5.1; 12418 -0.9; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 1.08 | 6.7 dB   |
| Peaking | 2141 Hz  | 3    | -9.5 dB  |
| Peaking | 4552 Hz  | 9.35 | -5.5 dB  |
| Peaking | 7015 Hz  | 4.82 | 4.4 dB   |
| Peaking | 9638 Hz  | 2.82 | -11.1 dB |
| Peaking | 745 Hz   | 1.01 | 0.7 dB   |
| Peaking | 2660 Hz  | 5.33 | -1.3 dB  |
| Peaking | 3833 Hz  | 5.5  | 5.7 dB   |
| Peaking | 4131 Hz  | 3.24 | -2.5 dB  |
| Peaking | 13301 Hz | 4.73 | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Grado%20SR225e/Grado%20SR225e.png)