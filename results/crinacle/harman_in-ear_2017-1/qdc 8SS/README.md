# qdc 8SS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -2.8; 25 -3.0; 28 -3.3; 31 -3.5; 34 -3.7; 37 -3.9; 41 -4.2; 45 -4.4; 49 -4.6; 54 -4.8; 60 -5.1; 66 -5.5; 72 -5.9; 79 -6.4; 87 -6.7; 96 -7.3; 106 -7.8; 116 -8.2; 128 -8.6; 141 -9.0; 155 -9.3; 170 -9.5; 187 -9.7; 206 -9.8; 227 -9.9; 249 -9.9; 274 -9.9; 302 -9.8; 332 -9.6; 365 -9.5; 402 -9.4; 442 -9.3; 486 -9.2; 535 -9.0; 588 -8.9; 647 -8.9; 712 -8.8; 783 -8.7; 861 -8.7; 947 -8.9; 1042 -9.4; 1146 -10.1; 1261 -10.5; 1387 -10.4; 1526 -9.6; 1678 -8.4; 1846 -7.2; 2031 -5.7; 2234 -4.2; 2457 -2.6; 2703 -0.7; 2973 -0.5; 3270 -0.6; 3597 -1.1; 3957 -0.8; 4353 -1.2; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -8.0; 13660 -16.3; 15026 -22.5; 16529 -23.3; 18182 -24.0; 20000 -30.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc 8SS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc 8SS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.18 | 3.9 dB   |
| Peaking | 203 Hz   | 0.38 | -4.0 dB  |
| Peaking | 1368 Hz  | 1.5  | -4.3 dB  |
| Peaking | 3006 Hz  | 1.51 | 6.6 dB   |
| Peaking | 5346 Hz  | 2.63 | 5.5 dB   |
| Peaking | 354 Hz   | 5.22 | 0.2 dB   |
| Peaking | 7836 Hz  | 0.71 | 6.2 dB   |
| Peaking | 11718 Hz | 2.21 | 10.1 dB  |
| Peaking | 19985 Hz | 0.13 | -10.5 dB |
| Peaking | 20030 Hz | 0.13 | -10.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB   |
| Peaking | 62 Hz    | 1.41 | 1.1 dB   |
| Peaking | 125 Hz   | 1.41 | -1.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 16000 Hz | 1.41 | -23.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%208SS/qdc%208SS.png)