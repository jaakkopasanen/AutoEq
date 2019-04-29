# BGVP DMG Silver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.9; 25 -7.2; 28 -7.6; 31 -7.9; 34 -8.1; 37 -8.3; 41 -8.5; 45 -8.6; 49 -8.8; 54 -8.9; 60 -9.1; 66 -9.3; 72 -9.5; 79 -9.7; 87 -9.9; 96 -10.2; 106 -10.4; 116 -10.5; 128 -10.5; 141 -10.5; 155 -10.4; 170 -10.3; 187 -10.0; 206 -9.7; 227 -9.3; 249 -8.9; 274 -8.4; 302 -7.8; 332 -7.2; 365 -6.5; 402 -5.9; 442 -5.3; 486 -4.7; 535 -4.1; 588 -3.4; 647 -2.8; 712 -2.1; 783 -1.3; 861 -0.8; 947 -0.5; 1042 -0.6; 1146 -0.9; 1261 -1.2; 1387 -1.3; 1526 -1.4; 1678 -1.5; 1846 -1.7; 2031 -1.7; 2234 -1.6; 2457 -1.5; 2703 -2.1; 2973 -2.0; 3270 -0.5; 3597 -1.3; 3957 -1.8; 4353 -2.0; 4788 -2.9; 5267 -3.5; 5793 -4.2; 6373 -2.4; 7010 -2.0; 7711 -4.2; 8482 -5.7; 9330 -7.1; 10263 -6.5; 11289 -4.5; 12418 -4.5; 13660 -6.4; 15026 -13.7; 16529 -18.8; 18182 -17.1; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DMG Silver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DMG Silver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 45 Hz    | 0.4  | -3.0 dB  |
| Peaking | 166 Hz   | 0.53 | -5.0 dB  |
| Peaking | 904 Hz   | 1.01 | 3.7 dB   |
| Peaking | 3231 Hz  | 0.49 | 2.7 dB   |
| Peaking | 17314 Hz | 1.2  | -16.2 dB |
| Peaking | 5870 Hz  | 4.04 | -2.1 dB  |
| Peaking | 6677 Hz  | 5.77 | 3.4 dB   |
| Peaking | 9466 Hz  | 2.82 | -3.4 dB  |
| Peaking | 12902 Hz | 1.52 | 4.5 dB   |
| Peaking | 15373 Hz | 2.8  | -4.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 16000 Hz | 1.41 | -14.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/BGVP%20DMG%20Silver/BGVP%20DMG%20Silver.png)