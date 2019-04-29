# qdc 8SS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -1.7; 25 -1.9; 28 -2.1; 31 -2.4; 34 -2.6; 37 -2.8; 41 -3.0; 45 -3.2; 49 -3.4; 54 -3.7; 60 -4.0; 66 -4.4; 72 -4.8; 79 -5.2; 87 -5.6; 96 -6.2; 106 -6.6; 116 -7.1; 128 -7.4; 141 -7.8; 155 -8.1; 170 -8.4; 187 -8.5; 206 -8.7; 227 -8.7; 249 -8.7; 274 -8.8; 302 -8.7; 332 -8.7; 365 -8.6; 402 -8.5; 442 -8.5; 486 -8.4; 535 -8.3; 588 -8.2; 647 -8.2; 712 -8.1; 783 -8.0; 861 -8.0; 947 -8.2; 1042 -8.6; 1146 -9.3; 1261 -10.0; 1387 -10.2; 1526 -9.7; 1678 -8.6; 1846 -7.4; 2031 -6.2; 2234 -5.3; 2457 -4.3; 2703 -2.8; 2973 -1.6; 3270 -2.6; 3597 -3.1; 3957 -2.4; 4353 -2.4; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -3.9; 7010 -5.1; 7711 -6.8; 8482 -7.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.4; 15026 -6.6; 16529 -6.5; 18182 -7.7; 20000 -18.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc 8SS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc 8SS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.46 | 5.3 dB  |
| Peaking | 65 Hz   | 0.98 | 2.2 dB  |
| Peaking | 720 Hz  | 0.05 | -2.5 dB |
| Peaking | 2923 Hz | 2.2  | 5.9 dB  |
| Peaking | 5199 Hz | 1.84 | 8.0 dB  |
| Peaking | 883 Hz  | 1.15 | 1.3 dB  |
| Peaking | 1363 Hz | 2.1  | -2.6 dB |
| Peaking | 2041 Hz | 3.76 | 1.1 dB  |
| Peaking | 8242 Hz | 3.98 | -1.9 dB |
| Peaking | 9522 Hz | 1.59 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%208SS/qdc%208SS.png)