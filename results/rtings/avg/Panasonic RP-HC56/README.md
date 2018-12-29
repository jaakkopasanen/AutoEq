# Panasonic RP-HC56
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.6; 25 5.3; 28 5.1; 31 4.9; 34 4.8; 37 4.7; 41 4.6; 45 4.6; 49 4.6; 54 4.5; 60 4.3; 66 4.1; 72 4.0; 79 3.9; 87 3.6; 96 3.5; 106 3.2; 116 3.0; 128 2.8; 141 2.7; 155 2.7; 170 2.8; 187 2.7; 206 2.7; 227 2.6; 249 2.5; 274 2.2; 302 1.7; 332 1.1; 365 0.3; 402 -0.7; 442 -1.6; 486 -2.7; 535 -3.6; 588 -3.9; 647 -3.5; 712 -2.4; 783 -1.0; 861 0.2; 947 0.3; 1042 -0.2; 1146 -0.5; 1261 0.1; 1387 0.6; 1526 1.4; 1678 2.4; 1846 3.3; 2031 4.2; 2234 5.6; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 5.3; 3957 5.2; 4353 4.9; 4788 4.2; 5267 1.1; 5793 -1.5; 6373 -1.0; 7010 -0.1; 7711 -2.7; 8482 -8.0; 9330 -11.6; 10263 -11.9; 11289 -9.2; 12418 -7.0; 13660 -6.3; 15026 -3.5; 16529 -2.4; 18182 -2.7; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC56 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC56 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.38 | 4.9 dB   |
| Peaking | 107 Hz   | 0.22 | 3.0 dB   |
| Peaking | 575 Hz   | 1.46 | -5.6 dB  |
| Peaking | 3334 Hz  | 0.8  | 7.2 dB   |
| Peaking | 10218 Hz | 1.32 | -13.0 dB |
| Peaking | 1257 Hz  | 4.2  | -1.5 dB  |
| Peaking | 2294 Hz  | 5.36 | 1.4 dB   |
| Peaking | 7024 Hz  | 2.01 | -3.6 dB  |
| Peaking | 7206 Hz  | 4.51 | 6.8 dB   |
| Peaking | 17763 Hz | 3.83 | -2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HC56/Panasonic%20RP-HC56.png)