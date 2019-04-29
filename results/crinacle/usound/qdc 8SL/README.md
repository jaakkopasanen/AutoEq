# qdc 8SL
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.8; 25 -7.1; 28 -7.4; 31 -7.6; 34 -7.7; 37 -7.8; 41 -7.9; 45 -8.1; 49 -8.2; 54 -8.4; 60 -8.5; 66 -8.7; 72 -8.9; 79 -9.0; 87 -9.2; 96 -9.4; 106 -9.6; 116 -9.7; 128 -9.7; 141 -9.6; 155 -9.5; 170 -9.3; 187 -9.1; 206 -8.9; 227 -8.5; 249 -8.1; 274 -7.7; 302 -7.3; 332 -6.9; 365 -6.5; 402 -6.2; 442 -6.0; 486 -5.8; 535 -5.7; 588 -5.8; 647 -5.8; 712 -5.9; 783 -6.0; 861 -6.3; 947 -6.6; 1042 -7.3; 1146 -8.1; 1261 -8.8; 1387 -9.0; 1526 -8.7; 1678 -8.0; 1846 -7.3; 2031 -6.8; 2234 -6.3; 2457 -5.9; 2703 -4.9; 2973 -3.8; 3270 -3.7; 3597 -4.1; 3957 -4.3; 4353 -5.3; 4788 -2.1; 5267 -0.5; 5793 -0.5; 6373 -2.7; 7010 -4.9; 7711 -7.7; 8482 -9.0; 9330 -7.2; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -8.3; 15026 -6.5; 16529 -6.5; 18182 -6.6; 20000 -13.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc 8SL GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc 8SL ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 77 Hz    | 0.73 | -2.2 dB |
| Peaking | 157 Hz   | 1.36 | -2.2 dB |
| Peaking | 1415 Hz  | 2.8  | -2.9 dB |
| Peaking | 3156 Hz  | 3.04 | 2.8 dB  |
| Peaking | 5490 Hz  | 3.59 | 6.8 dB  |
| Peaking | 564 Hz   | 1.79 | 1.1 dB  |
| Peaking | 6221 Hz  | 8.23 | 1.3 dB  |
| Peaking | 6906 Hz  | 4.49 | 0.7 dB  |
| Peaking | 8293 Hz  | 4.1  | -3.4 dB |
| Peaking | 19890 Hz | 2.26 | -7.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%208SL/qdc%208SL.png)