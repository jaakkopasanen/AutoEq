# Taobao 3 driver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.8; 45 -1.3; 49 -1.7; 54 -1.9; 60 -2.3; 66 -2.8; 72 -3.3; 79 -3.8; 87 -4.4; 96 -5.0; 106 -5.5; 116 -5.9; 128 -6.4; 141 -6.8; 155 -7.2; 170 -7.4; 187 -7.6; 206 -7.8; 227 -7.9; 249 -8.0; 274 -8.0; 302 -8.0; 332 -8.0; 365 -7.8; 402 -7.8; 442 -7.7; 486 -7.6; 535 -7.5; 588 -7.3; 647 -7.0; 712 -6.7; 783 -6.4; 861 -6.1; 947 -6.1; 1042 -6.4; 1146 -7.0; 1261 -7.6; 1387 -7.8; 1526 -7.4; 1678 -6.7; 1846 -6.2; 2031 -6.3; 2234 -6.1; 2457 -5.0; 2703 -3.8; 2973 -3.4; 3270 -4.0; 3597 -5.7; 3957 -7.1; 4353 -7.6; 4788 -8.3; 5267 -8.7; 5793 -6.9; 6373 -3.9; 7010 -6.7; 7711 -8.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Taobao 3 driver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Taobao 3 driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.38 | 6.3 dB  |
| Peaking | 207 Hz  | 0.57 | -2.2 dB |
| Peaking | 1384 Hz | 5.15 | -1.4 dB |
| Peaking | 2942 Hz | 3.19 | 3.6 dB  |
| Peaking | 4833 Hz | 3.92 | -2.5 dB |
| Peaking | 890 Hz  | 4.61 | 0.9 dB  |
| Peaking | 6423 Hz | 8.95 | 3.5 dB  |
| Peaking | 7547 Hz | 8.14 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Taobao%203%20driver/Taobao%203%20driver.png)