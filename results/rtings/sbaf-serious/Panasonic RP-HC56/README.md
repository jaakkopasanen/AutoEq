# Panasonic RP-HC56

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.6; 28 5.2; 31 5.0; 34 4.7; 37 4.6; 41 4.4; 45 4.3; 49 4.3; 54 4.2; 60 4.0; 66 3.9; 72 4.0; 79 4.0; 87 4.0; 96 3.9; 106 3.7; 116 3.5; 128 3.3; 141 3.2; 155 3.3; 170 3.4; 187 3.3; 206 3.2; 227 3.1; 249 3.0; 274 2.9; 302 2.5; 332 2.0; 365 1.3; 402 0.4; 442 -0.5; 486 -1.5; 535 -2.4; 588 -2.8; 647 -2.5; 712 -1.5; 783 -0.5; 861 0.3; 947 0.3; 1042 -0.2; 1146 -0.3; 1261 0.3; 1387 0.6; 1526 1.1; 1678 2.0; 1846 3.3; 2031 4.7; 2234 5.9; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.8; 5267 4.1; 5793 2.4; 6373 2.7; 7010 2.4; 7711 -0.4; 8482 -7.0; 9330 -11.5; 10263 -10.2; 11289 -3.9; 12418 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC56 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC56 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.3  | 5.8 dB   |
| Peaking | 106 Hz   | 1.02 | 2.4 dB   |
| Peaking | 227 Hz   | 2.13 | 2.6 dB   |
| Peaking | 3690 Hz  | 0.8  | 7.0 dB   |
| Peaking | 9559 Hz  | 3.41 | -14.6 dB |
| Peaking | 591 Hz   | 3.03 | -3.6 dB  |
| Peaking | 1284 Hz  | 2    | -1.3 dB  |
| Peaking | 2205 Hz  | 4.11 | 2.3 dB   |
| Peaking | 6942 Hz  | 8.82 | 2.2 dB   |
| Peaking | 21287 Hz | 2.55 | 1.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Panasonic%20RP-HC56/Panasonic%20RP-HC56.png)