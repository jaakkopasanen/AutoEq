# qdc 8SH
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.0; 25 -6.1; 28 -6.4; 31 -6.6; 34 -6.7; 37 -6.9; 41 -7.0; 45 -7.2; 49 -7.3; 54 -7.4; 60 -7.6; 66 -7.9; 72 -8.2; 79 -8.5; 87 -8.7; 96 -9.0; 106 -9.2; 116 -9.4; 128 -9.4; 141 -9.7; 155 -9.8; 170 -9.6; 187 -9.4; 206 -9.2; 227 -8.9; 249 -8.7; 274 -8.3; 302 -7.9; 332 -7.5; 365 -7.0; 402 -6.8; 442 -6.6; 486 -6.4; 535 -6.2; 588 -6.2; 647 -6.4; 712 -6.6; 783 -7.1; 861 -7.8; 947 -8.7; 1042 -9.8; 1146 -10.8; 1261 -11.2; 1387 -10.8; 1526 -9.8; 1678 -8.7; 1846 -7.7; 2031 -6.7; 2234 -5.6; 2457 -4.5; 2703 -3.0; 2973 -1.6; 3270 -1.6; 3597 -2.1; 3957 -2.7; 4353 -4.5; 4788 -2.9; 5267 -0.5; 5793 -0.5; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -14.7; 15026 -22.7; 16529 -24.3; 18182 -24.1; 20000 -26.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc 8SH GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc 8SH ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 112 Hz   | 0.97 | -2.5 dB  |
| Peaking | 197 Hz   | 1.63 | -1.9 dB  |
| Peaking | 1296 Hz  | 2    | -5.3 dB  |
| Peaking | 3146 Hz  | 2.21 | 5.3 dB   |
| Peaking | 5693 Hz  | 3.38 | 6.4 dB   |
| Peaking | 19 Hz    | 1.75 | 0.9 dB   |
| Peaking | 517 Hz   | 3.11 | 0.7 dB   |
| Peaking | 670 Hz   | 3.19 | 0.7 dB   |
| Peaking | 11076 Hz | 0.37 | 19.7 dB  |
| Peaking | 16608 Hz | 0.27 | -30.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB   |
| Peaking | 62 Hz    | 1.41 | -0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.2 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB   |
| Peaking | 1000 Hz  | 1.41 | -3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 16000 Hz | 1.41 | -22.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%208SH/qdc%208SH.png)