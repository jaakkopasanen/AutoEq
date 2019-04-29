# Vision Ears Erlkönig 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.8; 25 -7.0; 28 -7.4; 31 -7.6; 34 -7.8; 37 -8.0; 41 -8.2; 45 -8.4; 49 -8.6; 54 -8.8; 60 -9.1; 66 -9.4; 72 -9.7; 79 -10.0; 87 -10.3; 96 -10.6; 106 -10.9; 116 -11.2; 128 -11.4; 141 -11.4; 155 -11.4; 170 -11.4; 187 -11.3; 206 -11.2; 227 -11.0; 249 -10.7; 274 -10.4; 302 -10.0; 332 -9.5; 365 -9.0; 402 -8.5; 442 -8.1; 486 -7.6; 535 -7.0; 588 -6.4; 647 -5.8; 712 -5.2; 783 -4.6; 861 -4.1; 947 -3.9; 1042 -4.1; 1146 -4.5; 1261 -4.9; 1387 -4.8; 1526 -4.4; 1678 -3.8; 1846 -3.2; 2031 -2.8; 2234 -2.6; 2457 -2.4; 2703 -2.0; 2973 -1.0; 3270 -1.1; 3597 -1.6; 3957 -1.8; 4353 -1.8; 4788 -2.0; 5267 -1.5; 5793 -0.5; 6373 -0.5; 7010 -3.1; 7711 -5.3; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -9.4; 15026 -19.3; 16529 -22.4; 18182 -12.0; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vision Ears Erlkönig 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vision Ears Erlkönig 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 103 Hz   | 0.44 | -4.3 dB  |
| Peaking | 238 Hz   | 0.81 | -3.0 dB  |
| Peaking | 3655 Hz  | 0.43 | 4.0 dB   |
| Peaking | 6090 Hz  | 5.37 | 2.9 dB   |
| Peaking | 16297 Hz | 1.96 | -19.6 dB |
| Peaking | 894 Hz   | 2.78 | 1.4 dB   |
| Peaking | 1381 Hz  | 2.98 | -1.2 dB  |
| Peaking | 8009 Hz  | 5.01 | -1.8 dB  |
| Peaking | 12652 Hz | 5.38 | 3.6 dB   |
| Peaking | 22048 Hz | 2.02 | -0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 16000 Hz | 1.41 | -16.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Vision%20Ears%20Erlk%C3%B6nig%202/Vision%20Ears%20Erlk%C3%B6nig%202.png)