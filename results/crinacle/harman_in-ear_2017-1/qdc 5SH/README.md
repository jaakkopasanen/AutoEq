# qdc 5SH
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.1; 25 -8.2; 28 -8.5; 31 -8.7; 34 -8.8; 37 -8.9; 41 -9.1; 45 -9.3; 49 -9.4; 54 -9.5; 60 -9.7; 66 -10.0; 72 -10.2; 79 -10.5; 87 -10.7; 96 -11.2; 106 -11.4; 116 -11.6; 128 -11.8; 141 -11.9; 155 -11.9; 170 -11.8; 187 -11.7; 206 -11.5; 227 -11.2; 249 -10.9; 274 -10.6; 302 -10.1; 332 -9.6; 365 -9.1; 402 -8.7; 442 -8.4; 486 -8.0; 535 -7.6; 588 -7.4; 647 -7.3; 712 -7.2; 783 -7.3; 861 -7.5; 947 -7.9; 1042 -8.4; 1146 -8.8; 1261 -8.8; 1387 -8.3; 1526 -7.4; 1678 -6.6; 1846 -5.9; 2031 -5.5; 2234 -5.0; 2457 -3.8; 2703 -1.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.8; 4788 -3.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.7; 9330 -8.3; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -18.9; 15026 -28.6; 16529 -28.7; 18182 -27.8; 20000 -33.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc 5SH GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc 5SH ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 63 Hz    | 0.38 | -2.4 dB  |
| Peaking | 173 Hz   | 0.73 | -4.0 dB  |
| Peaking | 4397 Hz  | 0.43 | 20.2 dB  |
| Peaking | 12002 Hz | 0.78 | 25.8 dB  |
| Peaking | 15146 Hz | 0.19 | -40.0 dB |
| Peaking | 1274 Hz  | 3.54 | -1.9 dB  |
| Peaking | 2865 Hz  | 5.1  | 2.7 dB   |
| Peaking | 4615 Hz  | 7.23 | -3.7 dB  |
| Peaking | 6128 Hz  | 4.81 | 3.0 dB   |
| Peaking | 14919 Hz | 6.48 | -2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 16000 Hz | 1.41 | -30.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%205SH/qdc%205SH.png)