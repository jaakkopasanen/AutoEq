# Noble Audio Khan
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.8; 25 -7.9; 28 -8.0; 31 -8.1; 34 -8.1; 37 -8.1; 41 -8.2; 45 -8.1; 49 -8.1; 54 -8.1; 60 -8.1; 66 -8.1; 72 -8.2; 79 -8.2; 87 -8.3; 96 -8.3; 106 -8.4; 116 -8.4; 128 -8.4; 141 -8.5; 155 -8.4; 170 -8.3; 187 -8.2; 206 -8.1; 227 -8.0; 249 -7.9; 274 -7.9; 302 -7.9; 332 -7.7; 365 -7.7; 402 -7.8; 442 -8.0; 486 -8.1; 535 -8.2; 588 -8.3; 647 -8.4; 712 -8.5; 783 -8.4; 861 -8.4; 947 -8.4; 1042 -8.6; 1146 -9.0; 1261 -9.3; 1387 -9.1; 1526 -8.5; 1678 -7.7; 1846 -6.7; 2031 -5.6; 2234 -4.5; 2457 -3.5; 2703 -2.5; 2973 -1.6; 3270 -0.7; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.8; 5793 -3.5; 6373 -5.2; 7010 -5.5; 7711 -6.2; 8482 -8.7; 9330 -10.6; 10263 -8.8; 11289 -6.6; 12418 -9.4; 13660 -17.0; 15026 -24.4; 16529 -28.0; 18182 -27.0; 20000 -21.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble Audio Khan GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble Audio Khan ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 116 Hz   | 0.09 | -1.7 dB  |
| Peaking | 1366 Hz  | 1.4  | -3.0 dB  |
| Peaking | 3858 Hz  | 0.92 | 7.3 dB   |
| Peaking | 16020 Hz | 1.71 | -13.9 dB |
| Peaking | 18845 Hz | 0.73 | -18.0 dB |
| Peaking | 5232 Hz  | 5.32 | 3.0 dB   |
| Peaking | 5493 Hz  | 2.3  | -1.6 dB  |
| Peaking | 9350 Hz  | 4.03 | -3.9 dB  |
| Peaking | 11670 Hz | 2.56 | 5.5 dB   |
| Peaking | 14272 Hz | 3.81 | -3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 16000 Hz | 1.41 | -26.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Noble%20Audio%20Khan/Noble%20Audio%20Khan.png)