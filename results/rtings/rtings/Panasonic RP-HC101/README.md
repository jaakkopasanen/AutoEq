# Panasonic RP-HC101

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.9; 37 5.1; 41 3.6; 45 2.4; 49 1.3; 54 0.2; 60 -0.7; 66 -1.5; 72 -1.9; 79 -2.3; 87 -2.7; 96 -3.1; 106 -3.4; 116 -3.7; 128 -4.0; 141 -4.1; 155 -4.2; 170 -4.3; 187 -4.2; 206 -4.1; 227 -3.9; 249 -3.9; 274 -4.1; 302 -4.2; 332 -4.5; 365 -5.5; 402 -6.3; 442 -6.9; 486 -7.0; 535 -6.5; 588 -5.7; 647 -4.7; 712 -3.6; 783 -2.4; 861 -1.3; 947 -0.4; 1042 0.2; 1146 0.4; 1261 0.2; 1387 -0.5; 1526 -1.4; 1678 -2.8; 1846 -3.7; 2031 -3.5; 2234 -1.7; 2457 0.7; 2703 2.7; 2973 3.2; 3270 3.1; 3597 4.1; 3957 5.9; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.8; 6373 1.9; 7010 -2.5; 7711 -4.7; 8482 -2.6; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.4; 16529 -4.4; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC101 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC101 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.73 | 9.1 dB   |
| Peaking | 98 Hz    | 0.3  | -4.9 dB  |
| Peaking | 490 Hz   | 1.55 | -5.8 dB  |
| Peaking | 4480 Hz  | 2.13 | 7.3 dB   |
| Peaking | 18830 Hz | 0.87 | -5.3 dB  |
| Peaking | 1242 Hz  | 1.13 | 6.2 dB   |
| Peaking | 2160 Hz  | 0.72 | -10.7 dB |
| Peaking | 2727 Hz  | 1.89 | 9.1 dB   |
| Peaking | 6836 Hz  | 1.08 | 7.9 dB   |
| Peaking | 7547 Hz  | 2.74 | -12.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Panasonic%20RP-HC101/Panasonic%20RP-HC101.png)