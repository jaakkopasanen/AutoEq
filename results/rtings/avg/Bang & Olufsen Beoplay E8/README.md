# Bang & Olufsen Beoplay E8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 21 0.0; 23 2.5; 25 2.3; 28 1.9; 31 1.5; 34 1.3; 37 1.2; 41 1.2; 45 1.4; 49 1.6; 54 1.8; 60 1.9; 66 2.1; 72 2.3; 79 2.4; 87 2.4; 96 2.3; 106 1.9; 116 1.5; 128 0.8; 141 0.2; 155 -0.5; 170 -1.3; 187 -2.1; 206 -2.8; 227 -3.4; 249 -3.7; 274 -4.0; 302 -4.0; 332 -4.0; 365 -3.7; 402 -3.4; 442 -3.0; 486 -2.4; 535 -1.8; 588 -1.1; 647 -0.2; 712 0.6; 783 1.2; 861 1.2; 947 0.5; 1042 -0.4; 1146 -1.3; 1261 -1.7; 1387 -1.9; 1526 -1.9; 1678 -1.8; 1846 -1.2; 2031 0.9; 2234 3.4; 2457 4.1; 2703 3.7; 2973 2.9; 3270 2.3; 3597 2.5; 3957 2.8; 4353 2.1; 4788 1.4; 5267 0.2; 5793 -2.1; 6373 -6.8; 7010 -10.4; 7711 -7.9; 8482 -5.0; 9330 -6.7; 10263 -9.3; 11289 -6.8; 12418 -1.3; 13660 0.0; 15026 0.0; 16529 -3.1; 18182 -7.2; 20000 -1.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay E8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay E8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 315 Hz   | 1.41 | -4.6 dB  |
| Peaking | 4538 Hz  | 0.93 | 8.4 dB   |
| Peaking | 7173 Hz  | 1.03 | -13.0 dB |
| Peaking | 18297 Hz | 3.04 | -7.2 dB  |
| Peaking | 20947 Hz | 2.36 | -4.1 dB  |
| Peaking | 14 Hz    | 0.5  | 3.2 dB   |
| Peaking | 85 Hz    | 1.65 | 2.6 dB   |
| Peaking | 1489 Hz  | 3.57 | -2.9 dB  |
| Peaking | 10672 Hz | 3.69 | -9.3 dB  |
| Peaking | 11682 Hz | 1.22 | 4.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%20E8/Bang%20&%20Olufsen%20Beoplay%20E8.png)