# qdc Neptune
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.2; 25 -4.3; 28 -4.4; 31 -4.6; 34 -4.7; 37 -4.8; 41 -4.9; 45 -5.1; 49 -5.3; 54 -5.4; 60 -5.7; 66 -5.9; 72 -6.2; 79 -6.6; 87 -7.0; 96 -7.4; 106 -7.7; 116 -8.0; 128 -8.3; 141 -8.6; 155 -8.8; 170 -8.9; 187 -8.9; 206 -8.9; 227 -8.9; 249 -8.8; 274 -8.6; 302 -8.4; 332 -8.1; 365 -7.8; 402 -7.6; 442 -7.3; 486 -7.1; 535 -6.7; 588 -6.3; 647 -5.8; 712 -5.3; 783 -4.8; 861 -4.3; 947 -4.1; 1042 -4.2; 1146 -4.8; 1261 -5.4; 1387 -5.7; 1526 -5.5; 1678 -5.0; 1846 -4.5; 2031 -4.4; 2234 -4.6; 2457 -5.1; 2703 -5.5; 2973 -4.9; 3270 -3.6; 3597 -2.4; 3957 -1.6; 4353 -2.1; 4788 -3.8; 5267 -4.8; 5793 -2.6; 6373 -0.5; 7010 -3.1; 7711 -5.9; 8482 -5.5; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Neptune GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Neptune ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.17 | 1.6 dB  |
| Peaking | 182 Hz  | 0.47 | -3.9 dB |
| Peaking | 907 Hz  | 1.82 | 2.1 dB  |
| Peaking | 3945 Hz | 3.09 | 4.1 dB  |
| Peaking | 6378 Hz | 6.03 | 5.1 dB  |
| Peaking | 1427 Hz | 3.47 | -0.9 dB |
| Peaking | 1998 Hz | 1.79 | 1.1 dB  |
| Peaking | 2693 Hz | 4.99 | -1.1 dB |
| Peaking | 7772 Hz | 9.62 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%20Neptune/qdc%20Neptune.png)