# SteelSeries Siberia 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.5dB
GraphicEQ: 21 -1.6; 23 -2.2; 25 -2.6; 28 -3.3; 31 -3.8; 34 -4.1; 37 -4.3; 41 -4.5; 45 -4.6; 49 -4.6; 54 -4.6; 60 -4.7; 66 -4.8; 72 -4.9; 79 -4.9; 87 -4.9; 96 -5.0; 106 -5.1; 116 -5.1; 128 -5.2; 141 -5.1; 155 -5.0; 170 -4.7; 187 -4.7; 206 -4.8; 227 -4.9; 249 -5.2; 274 -5.1; 302 -4.9; 332 -4.6; 365 -4.3; 402 -4.1; 442 -4.0; 486 -3.5; 535 -2.9; 588 -1.6; 647 0.0; 712 1.5; 783 1.9; 861 1.5; 947 0.1; 1042 0.3; 1146 -0.7; 1261 -0.8; 1387 -0.6; 1526 -0.4; 1678 -1.3; 1846 -2.9; 2031 -4.3; 2234 -4.3; 2457 -3.7; 2703 -3.8; 2973 -3.4; 3270 1.6; 3597 -0.8; 3957 -1.8; 4353 -0.5; 4788 0.1; 5267 -1.6; 5793 -2.7; 6373 -2.9; 7010 -3.1; 7711 -5.7; 8482 -7.3; 9330 -5.6; 10263 -1.5; 11289 -0.0; 12418 -1.1; 13660 -0.8; 15026 0.0; 16529 0.0; 18182 -0.2; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SteelSeries Siberia 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-24**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SteelSeries Siberia 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.66 | -3.1 dB |
| Peaking | 231 Hz   | 0.3  | -5.0 dB |
| Peaking | 776 Hz   | 2.04 | 4.8 dB  |
| Peaking | 2285 Hz  | 2.5  | -4.3 dB |
| Peaking | 8362 Hz  | 2.69 | -7.4 dB |
| Peaking | 1513 Hz  | 7.31 | 1.1 dB  |
| Peaking | 4750 Hz  | 6.89 | 1.2 dB  |
| Peaking | 5825 Hz  | 5.55 | -1.6 dB |
| Peaking | 10887 Hz | 7.8  | 1.9 dB  |
| Peaking | 19874 Hz | 4.06 | -6.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SteelSeries%20Siberia%20200/SteelSeries%20Siberia%20200.png)