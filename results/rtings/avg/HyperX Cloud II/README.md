# HyperX Cloud II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.7; 23 -3.0; 25 -3.4; 28 -3.9; 31 -4.3; 34 -4.5; 37 -4.7; 41 -4.8; 45 -4.8; 49 -4.8; 54 -4.7; 60 -4.8; 66 -4.9; 72 -5.1; 79 -5.3; 87 -5.7; 96 -6.0; 106 -6.4; 116 -6.7; 128 -6.8; 141 -6.5; 155 -6.3; 170 -6.0; 187 -5.3; 206 -4.5; 227 -3.7; 249 -3.0; 274 -2.6; 302 -2.5; 332 -2.6; 365 -2.7; 402 -2.7; 442 -2.6; 486 -2.7; 535 -2.8; 588 -2.7; 647 -2.5; 712 -2.2; 783 -1.8; 861 -1.5; 947 -0.5; 1042 0.2; 1146 -0.2; 1261 -0.8; 1387 -1.4; 1526 -2.1; 1678 -3.2; 1846 -4.2; 2031 -5.4; 2234 -5.4; 2457 -4.1; 2703 -2.9; 2973 -2.2; 3270 -1.5; 3597 1.3; 3957 6.0; 4353 4.8; 4788 -3.5; 5267 -3.2; 5793 -2.9; 6373 -4.8; 7010 -5.7; 7711 -6.9; 8482 -9.7; 9330 -10.1; 10263 -5.4; 11289 -1.2; 12418 -2.7; 13660 -7.3; 15026 -8.7; 16529 -6.9; 18182 -7.1; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.16 | -2.6 dB |
| Peaking | 120 Hz   | 0.42 | -6.1 dB |
| Peaking | 2096 Hz  | 2.81 | -5.7 dB |
| Peaking | 8571 Hz  | 2.67 | -9.0 dB |
| Peaking | 18803 Hz | 0.37 | -8.5 dB |
| Peaking | 607 Hz   | 3.08 | -1.5 dB |
| Peaking | 4101 Hz  | 4.77 | 9.9 dB  |
| Peaking | 4866 Hz  | 6.58 | -4.0 dB |
| Peaking | 8897 Hz  | 0.28 | -1.5 dB |
| Peaking | 11504 Hz | 4.35 | 5.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20II/HyperX%20Cloud%20II.png)