# Zero Audio Duoza ZH-DWX10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.5; 25 -8.6; 28 -8.8; 31 -8.9; 34 -9.0; 37 -9.1; 41 -9.3; 45 -9.4; 49 -9.5; 54 -9.7; 60 -9.9; 66 -10.1; 72 -10.4; 79 -10.7; 87 -11.0; 96 -11.3; 106 -11.5; 116 -11.8; 128 -11.8; 141 -11.9; 155 -11.9; 170 -11.7; 187 -11.6; 206 -11.3; 227 -10.9; 249 -10.5; 274 -10.1; 302 -9.6; 332 -9.1; 365 -8.5; 402 -7.9; 442 -7.3; 486 -6.6; 535 -6.0; 588 -5.3; 647 -4.6; 712 -3.8; 783 -3.0; 861 -2.3; 947 -1.9; 1042 -1.8; 1146 -2.1; 1261 -2.5; 1387 -2.7; 1526 -3.1; 1678 -3.7; 1846 -4.4; 2031 -5.6; 2234 -7.0; 2457 -8.3; 2703 -7.8; 2973 -5.7; 3270 -3.6; 3597 -2.5; 3957 -2.4; 4353 -3.1; 4788 -3.6; 5267 -2.4; 5793 -0.5; 6373 -0.8; 7010 -4.2; 7711 -9.4; 8482 -8.6; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -10.6; 15026 -17.8; 16529 -16.4; 18182 -13.5; 20000 -15.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Zero Audio Duoza ZH-DWX10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zero Audio Duoza ZH-DWX10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 131 Hz   | 0.37 | -5.6 dB  |
| Peaking | 962 Hz   | 1.11 | 5.4 dB   |
| Peaking | 3878 Hz  | 4.08 | 3.9 dB   |
| Peaking | 5951 Hz  | 3.88 | 6.8 dB   |
| Peaking | 16824 Hz | 0.94 | -11.1 dB |
| Peaking | 23 Hz    | 1.76 | -1.2 dB  |
| Peaking | 2509 Hz  | 5.8  | -3.5 dB  |
| Peaking | 7948 Hz  | 6.12 | -5.0 dB  |
| Peaking | 13121 Hz | 1.1  | 5.2 dB   |
| Peaking | 14907 Hz | 2.99 | -8.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 16000 Hz | 1.41 | -12.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Zero%20Audio%20Duoza%20ZH-DWX10/Zero%20Audio%20Duoza%20ZH-DWX10.png)