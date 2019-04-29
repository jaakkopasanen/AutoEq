# BGVP DM6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.8; 25 -5.3; 28 -5.9; 31 -6.4; 34 -6.8; 37 -7.1; 41 -7.5; 45 -7.9; 49 -8.3; 54 -8.7; 60 -9.0; 66 -9.4; 72 -9.8; 79 -10.2; 87 -10.7; 96 -11.1; 106 -11.5; 116 -11.8; 128 -12.1; 141 -12.4; 155 -12.4; 170 -12.5; 187 -12.6; 206 -12.6; 227 -12.4; 249 -12.1; 274 -11.9; 302 -11.6; 332 -11.1; 365 -10.6; 402 -10.2; 442 -9.7; 486 -9.2; 535 -8.6; 588 -8.0; 647 -7.3; 712 -6.6; 783 -5.9; 861 -5.3; 947 -5.0; 1042 -5.0; 1146 -5.3; 1261 -5.4; 1387 -5.1; 1526 -4.5; 1678 -3.7; 1846 -2.8; 2031 -1.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.0; 4353 -3.9; 4788 -3.0; 5267 -2.5; 5793 -6.0; 6373 -10.3; 7010 -9.6; 7711 -8.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.2; 15026 -29.8; 16529 -35.9; 18182 -29.0; 20000 -11.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DM6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DM6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 187 Hz   | 0.46 | -6.4 dB  |
| Peaking | 5460 Hz  | 0.36 | 12.0 dB  |
| Peaking | 6546 Hz  | 3.17 | -7.7 dB  |
| Peaking | 12398 Hz | 1.84 | 14.0 dB  |
| Peaking | 16200 Hz | 0.71 | -36.8 dB |
| Peaking | 21 Hz    | 1.88 | 2.7 dB   |
| Peaking | 1454 Hz  | 2.12 | -2.8 dB  |
| Peaking | 1885 Hz  | 0.56 | 1.5 dB   |
| Peaking | 4373 Hz  | 7.51 | -3.4 dB  |
| Peaking | 17682 Hz | 4.45 | -4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB   |
| Peaking | 62 Hz    | 1.41 | -2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -5.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 16000 Hz | 1.41 | -29.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/BGVP%20DM6/BGVP%20DM6.png)