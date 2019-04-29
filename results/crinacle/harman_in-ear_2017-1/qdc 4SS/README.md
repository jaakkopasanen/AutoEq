# qdc 4SS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.6; 25 -5.8; 28 -6.0; 31 -6.2; 34 -6.3; 37 -6.4; 41 -6.6; 45 -6.8; 49 -6.9; 54 -7.1; 60 -7.3; 66 -7.6; 72 -8.0; 79 -8.4; 87 -8.8; 96 -9.3; 106 -9.7; 116 -10.0; 128 -10.4; 141 -10.7; 155 -11.1; 170 -11.3; 187 -11.4; 206 -11.4; 227 -11.4; 249 -11.3; 274 -11.2; 302 -10.9; 332 -10.6; 365 -10.2; 402 -9.9; 442 -9.5; 486 -9.1; 535 -8.7; 588 -8.2; 647 -7.7; 712 -7.1; 783 -6.6; 861 -6.2; 947 -6.0; 1042 -6.2; 1146 -6.6; 1261 -7.0; 1387 -6.9; 1526 -6.5; 1678 -5.8; 1846 -5.0; 2031 -3.8; 2234 -2.4; 2457 -1.2; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -2.2; 3957 -2.5; 4353 -1.5; 4788 -2.0; 5267 -1.5; 5793 -0.6; 6373 -2.7; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -17.2; 15026 -26.1; 16529 -27.6; 18182 -27.5; 20000 -26.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc 4SS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc 4SS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.23 | 1.2 dB   |
| Peaking | 205 Hz   | 0.52 | -5.1 dB  |
| Peaking | 4137 Hz  | 0.31 | 19.9 dB  |
| Peaking | 12344 Hz | 0.67 | 27.2 dB  |
| Peaking | 14960 Hz | 0.2  | -43.7 dB |
| Peaking | 894 Hz   | 1.54 | 2.5 dB   |
| Peaking | 2169 Hz  | 0.51 | -4.6 dB  |
| Peaking | 2593 Hz  | 1.26 | 6.1 dB   |
| Peaking | 3802 Hz  | 6.3  | -2.0 dB  |
| Peaking | 5862 Hz  | 4.74 | 3.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB   |
| Peaking | 62 Hz    | 1.41 | -0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 16000 Hz | 1.41 | -27.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%204SS/qdc%204SS.png)