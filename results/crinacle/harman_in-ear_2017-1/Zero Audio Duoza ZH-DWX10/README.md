# Zero Audio Duoza ZH-DWX10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.8; 25 -9.9; 28 -10.1; 31 -10.2; 34 -10.4; 37 -10.5; 41 -10.6; 45 -10.7; 49 -10.9; 54 -11.0; 60 -11.2; 66 -11.5; 72 -11.7; 79 -12.0; 87 -12.3; 96 -12.7; 106 -12.9; 116 -13.1; 128 -13.2; 141 -13.2; 155 -13.2; 170 -13.1; 187 -12.9; 206 -12.6; 227 -12.3; 249 -11.9; 274 -11.4; 302 -10.8; 332 -10.2; 365 -9.5; 402 -8.9; 442 -8.3; 486 -7.6; 535 -6.9; 588 -6.1; 647 -5.4; 712 -4.6; 783 -3.9; 861 -3.2; 947 -2.9; 1042 -2.8; 1146 -3.0; 1261 -3.1; 1387 -3.1; 1526 -3.2; 1678 -3.8; 1846 -4.4; 2031 -5.2; 2234 -6.0; 2457 -6.8; 2703 -5.9; 2973 -3.6; 3270 -1.5; 3597 -0.7; 3957 -1.0; 4353 -2.1; 4788 -2.9; 5267 -1.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.7; 8482 -7.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -19.7; 15026 -34.3; 16529 -35.4; 18182 -30.1; 20000 -27.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Zero Audio Duoza ZH-DWX10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zero Audio Duoza ZH-DWX10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 62 Hz    | 0.29 | -4.2 dB  |
| Peaking | 202 Hz   | 0.69 | -4.8 dB  |
| Peaking | 6087 Hz  | 0.23 | 26.5 dB  |
| Peaking | 12246 Hz | 1.89 | 17.8 dB  |
| Peaking | 15451 Hz | 0.27 | -49.1 dB |
| Peaking | 1021 Hz  | 1.78 | 2.1 dB   |
| Peaking | 2510 Hz  | 2.59 | -4.4 dB  |
| Peaking | 3493 Hz  | 2.67 | 2.8 dB   |
| Peaking | 4758 Hz  | 4.01 | -1.9 dB  |
| Peaking | 5918 Hz  | 6.05 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 10.0 dB  |
| Peaking | 16000 Hz | 1.41 | -36.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Zero%20Audio%20Duoza%20ZH-DWX10/Zero%20Audio%20Duoza%20ZH-DWX10.png)