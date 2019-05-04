# Google Pixel Buds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.8; 54 -3.5; 60 -5.1; 66 -6.5; 72 -7.6; 79 -8.7; 87 -9.7; 96 -10.6; 106 -11.2; 116 -11.6; 128 -11.9; 141 -11.9; 155 -11.8; 170 -11.4; 187 -10.8; 206 -10.1; 227 -9.3; 249 -8.5; 274 -7.9; 302 -7.5; 332 -7.4; 365 -7.4; 402 -7.3; 442 -7.0; 486 -6.7; 535 -6.2; 588 -5.6; 647 -4.9; 712 -4.1; 783 -3.2; 861 -2.1; 947 -1.3; 1042 -0.7; 1146 -0.5; 1261 -0.5; 1387 -1.2; 1526 -2.8; 1678 -4.7; 1846 -6.6; 2031 -7.6; 2234 -7.7; 2457 -7.5; 2703 -7.1; 2973 -6.0; 3270 -4.9; 3597 -4.7; 3957 -5.0; 4353 -6.3; 4788 -8.3; 5267 -8.7; 5793 -6.4; 6373 -4.5; 7010 -6.8; 7711 -9.2; 8482 -7.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.3; 13660 -9.6; 15026 -7.1; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Google Pixel Buds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Google Pixel Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.54 | 8.3 dB  |
| Peaking | 112 Hz   | 0.66 | -7.9 dB |
| Peaking | 1221 Hz  | 1.04 | 10.2 dB |
| Peaking | 2264 Hz  | 0.6  | -6.4 dB |
| Peaking | 3398 Hz  | 1.96 | 5.5 dB  |
| Peaking | 5149 Hz  | 5.31 | -2.6 dB |
| Peaking | 6330 Hz  | 4.7  | 3.2 dB  |
| Peaking | 7680 Hz  | 5.26 | -3.4 dB |
| Peaking | 10442 Hz | 0.56 | 1.0 dB  |
| Peaking | 13641 Hz | 3.39 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Google%20Pixel%20Buds/Google%20Pixel%20Buds.png)