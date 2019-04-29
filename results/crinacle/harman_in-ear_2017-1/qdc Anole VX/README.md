# qdc Anole VX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.0; 25 -7.2; 28 -7.5; 31 -7.8; 34 -7.9; 37 -8.1; 41 -8.3; 45 -8.4; 49 -8.6; 54 -8.8; 60 -8.9; 66 -9.1; 72 -9.3; 79 -9.5; 87 -9.7; 96 -9.8; 106 -10.0; 116 -10.1; 128 -10.1; 141 -10.1; 155 -10.0; 170 -9.8; 187 -9.6; 206 -9.4; 227 -9.1; 249 -8.8; 274 -8.5; 302 -8.2; 332 -7.8; 365 -7.5; 402 -7.3; 442 -7.1; 486 -7.0; 535 -7.0; 588 -7.1; 647 -7.2; 712 -7.3; 783 -7.5; 861 -7.8; 947 -8.2; 1042 -8.8; 1146 -9.4; 1261 -9.6; 1387 -9.2; 1526 -8.4; 1678 -7.5; 1846 -6.6; 2031 -5.6; 2234 -4.4; 2457 -3.1; 2703 -2.0; 2973 -1.5; 3270 -1.2; 3597 -1.7; 3957 -3.1; 4353 -4.6; 4788 -1.9; 5267 -0.5; 5793 -0.8; 6373 -5.7; 7010 -8.1; 7711 -6.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -15.2; 15026 -24.1; 16529 -28.3; 18182 -26.3; 20000 -18.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole VX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole VX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 121 Hz   | 0.46 | -3.7 dB  |
| Peaking | 1390 Hz  | 0.86 | -8.9 dB  |
| Peaking | 4082 Hz  | 0.28 | 11.9 dB  |
| Peaking | 12163 Hz | 1.46 | 13.7 dB  |
| Peaking | 16137 Hz | 0.37 | -27.6 dB |
| Peaking | 4371 Hz  | 4.25 | -5.8 dB  |
| Peaking | 5066 Hz  | 1.9  | 4.7 dB   |
| Peaking | 5808 Hz  | 6.88 | 2.3 dB   |
| Peaking | 6814 Hz  | 2.87 | -5.0 dB  |
| Peaking | 8431 Hz  | 2.54 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB   |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 16000 Hz | 1.41 | -25.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%20Anole%20VX/qdc%20Anole%20VX.png)