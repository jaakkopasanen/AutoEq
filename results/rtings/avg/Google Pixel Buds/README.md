# Google Pixel Buds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -1.8; 60 -3.5; 66 -4.7; 72 -5.8; 79 -6.8; 87 -7.8; 96 -8.7; 106 -9.5; 116 -10.2; 128 -10.6; 141 -11.0; 155 -11.1; 170 -11.1; 187 -11.1; 206 -10.9; 227 -10.5; 249 -10.1; 274 -9.7; 302 -9.0; 332 -8.4; 365 -7.8; 402 -7.4; 442 -7.4; 486 -7.3; 535 -7.2; 588 -7.1; 647 -6.8; 712 -6.4; 783 -5.9; 861 -5.4; 947 -4.8; 1042 -4.0; 1146 -3.2; 1261 -2.1; 1387 -1.3; 1526 -0.6; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.7; 2457 -2.3; 2703 -4.2; 2973 -6.2; 3270 -7.5; 3597 -8.0; 3957 -7.9; 4353 -7.6; 4788 -7.4; 5267 -7.7; 5793 -6.8; 6373 -5.4; 7010 -4.3; 7711 -6.2; 8482 -7.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.2; 13660 -9.6; 15026 -9.4; 16529 -9.0; 18182 -8.7; 20000 -10.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Google Pixel Buds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Google Pixel Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.48 | 8.1 dB  |
| Peaking | 130 Hz   | 0.57 | -7.1 dB |
| Peaking | 1821 Hz  | 0.93 | 10.9 dB |
| Peaking | 7091 Hz  | 0.21 | -9.1 dB |
| Peaking | 8328 Hz  | 0.6  | 9.3 dB  |
| Peaking | 2368 Hz  | 5.92 | 1.5 dB  |
| Peaking | 3352 Hz  | 3.77 | -1.1 dB |
| Peaking | 6784 Hz  | 5.96 | 2.5 dB  |
| Peaking | 8206 Hz  | 3.67 | -1.7 dB |
| Peaking | 11373 Hz | 6.33 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -4.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Google%20Pixel%20Buds/Google%20Pixel%20Buds.png)