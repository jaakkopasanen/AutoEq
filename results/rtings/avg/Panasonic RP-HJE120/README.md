# Panasonic RP-HJE120
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.8dB
GraphicEQ: 21 -1.8; 23 -2.1; 25 -2.4; 28 -2.8; 31 -3.1; 34 -3.3; 37 -3.5; 41 -3.7; 45 -3.9; 49 -4.1; 54 -4.4; 60 -4.9; 66 -5.4; 72 -5.8; 79 -6.3; 87 -6.8; 96 -7.4; 106 -7.9; 116 -8.4; 128 -8.9; 141 -9.2; 155 -9.5; 170 -9.5; 187 -9.4; 206 -9.3; 227 -8.9; 249 -8.4; 274 -7.8; 302 -7.3; 332 -6.9; 365 -6.3; 402 -5.6; 442 -4.8; 486 -3.9; 535 -2.9; 588 -1.9; 647 -0.7; 712 0.3; 783 0.7; 861 0.6; 947 0.1; 1042 -0.1; 1146 -0.4; 1261 -0.6; 1387 -0.7; 1526 -0.9; 1678 -1.2; 1846 -1.6; 2031 -2.0; 2234 -1.8; 2457 -1.4; 2703 -1.5; 2973 -1.7; 3270 -1.8; 3597 -1.8; 3957 -2.3; 4353 -3.5; 4788 -4.7; 5267 -6.1; 5793 -4.7; 6373 -1.6; 7010 1.7; 7711 0.3; 8482 0.0; 9330 -2.0; 10263 -0.9; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.1; 16529 -3.8; 18182 -2.6; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HJE120 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HJE120 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 79 Hz    | 0.43 | -4.5 dB |
| Peaking | 181 Hz   | 0.91 | -6.7 dB |
| Peaking | 350 Hz   | 1.86 | -3.4 dB |
| Peaking | 2475 Hz  | 1.4  | -1.6 dB |
| Peaking | 5182 Hz  | 3.42 | -6.2 dB |
| Peaking | 498 Hz   | 3.59 | -1.0 dB |
| Peaking | 772 Hz   | 2.72 | 2.1 dB  |
| Peaking | 6321 Hz  | 2.76 | -1.4 dB |
| Peaking | 7009 Hz  | 5.09 | 3.8 dB  |
| Peaking | 20811 Hz | 0.63 | -6.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HJE120/Panasonic%20RP-HJE120.png)