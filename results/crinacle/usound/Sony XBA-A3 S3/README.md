# Sony XBA-A3 S3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.6; 25 -5.8; 28 -6.1; 31 -6.2; 34 -6.4; 37 -6.5; 41 -6.7; 45 -6.8; 49 -6.9; 54 -7.0; 60 -7.3; 66 -7.6; 72 -7.8; 79 -8.0; 87 -8.3; 96 -8.6; 106 -8.9; 116 -9.1; 128 -9.3; 141 -9.3; 155 -9.2; 170 -9.1; 187 -8.9; 206 -8.7; 227 -8.3; 249 -8.0; 274 -7.6; 302 -7.2; 332 -7.0; 365 -6.7; 402 -6.4; 442 -6.2; 486 -6.0; 535 -5.6; 588 -5.4; 647 -5.1; 712 -4.8; 783 -4.4; 861 -4.2; 947 -4.1; 1042 -4.4; 1146 -5.1; 1261 -5.7; 1387 -6.0; 1526 -5.8; 1678 -5.2; 1846 -4.5; 2031 -3.9; 2234 -3.2; 2457 -2.7; 2703 -2.5; 2973 -2.6; 3270 -2.3; 3597 -3.0; 3957 -3.2; 4353 -4.3; 4788 -5.4; 5267 -3.5; 5793 -0.5; 6373 -1.0; 7010 -2.6; 7711 -4.8; 8482 -5.0; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -6.2; 15026 -5.7; 16529 -5.4; 18182 -5.5; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-A3 S3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-A3 S3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 68 Hz    | 1.59 | 0.8 dB  |
| Peaking | 82 Hz    | 0.59 | -2.8 dB |
| Peaking | 181 Hz   | 0.82 | -2.7 dB |
| Peaking | 2878 Hz  | 1.97 | 2.9 dB  |
| Peaking | 6134 Hz  | 4.58 | 4.9 dB  |
| Peaking | 900 Hz   | 2.54 | 1.3 dB  |
| Peaking | 1387 Hz  | 3.45 | -1.5 dB |
| Peaking | 4688 Hz  | 2.23 | 1.5 dB  |
| Peaking | 4739 Hz  | 5.71 | -3.1 dB |
| Peaking | 14177 Hz | 2.78 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20XBA-A3%20S3/Sony%20XBA-A3%20S3.png)