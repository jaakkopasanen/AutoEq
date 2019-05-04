# 1MORE Quad Driver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.7; 28 -2.5; 31 -3.1; 34 -3.7; 37 -4.2; 41 -4.8; 45 -5.3; 49 -5.8; 54 -6.3; 60 -6.9; 66 -7.5; 72 -8.0; 79 -8.5; 87 -9.0; 96 -9.5; 106 -10.0; 116 -10.4; 128 -10.7; 141 -10.9; 155 -11.0; 170 -11.1; 187 -11.0; 206 -10.8; 227 -10.7; 249 -10.6; 274 -10.4; 302 -10.1; 332 -9.6; 365 -9.1; 402 -8.5; 442 -7.8; 486 -7.1; 535 -6.0; 588 -5.1; 647 -4.4; 712 -3.9; 783 -3.8; 861 -4.1; 947 -4.5; 1042 -4.7; 1146 -5.0; 1261 -4.8; 1387 -4.6; 1526 -4.7; 1678 -5.0; 1846 -5.3; 2031 -5.7; 2234 -5.8; 2457 -5.4; 2703 -5.1; 2973 -4.8; 3270 -5.1; 3597 -6.0; 3957 -7.9; 4353 -10.0; 4788 -9.4; 5267 -5.5; 5793 -1.8; 6373 -1.0; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -7.0; 12418 -9.8; 13660 -10.9; 15026 -9.5; 16529 -6.8; 18182 -7.9; 20000 -14.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Quad Driver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Quad Driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.75 | 6.4 dB  |
| Peaking | 190 Hz   | 0.55 | -6.0 dB |
| Peaking | 2182 Hz  | 0.11 | 2.5 dB  |
| Peaking | 4389 Hz  | 4.68 | -6.6 dB |
| Peaking | 13642 Hz | 1.53 | -5.9 dB |
| Peaking | 381 Hz   | 2.32 | -1.0 dB |
| Peaking | 705 Hz   | 2.44 | 1.9 dB  |
| Peaking | 2142 Hz  | 1.66 | -1.5 dB |
| Peaking | 6354 Hz  | 5.21 | 5.3 dB  |
| Peaking | 8006 Hz  | 2.75 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/1MORE%20Quad%20Driver/1MORE%20Quad%20Driver.png)