# Ambient Acoustics AM24
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.5; 25 -5.8; 28 -6.2; 31 -6.5; 34 -6.7; 37 -6.9; 41 -7.1; 45 -7.3; 49 -7.5; 54 -7.7; 60 -7.9; 66 -8.2; 72 -8.4; 79 -8.7; 87 -9.1; 96 -9.4; 106 -9.6; 116 -10.0; 128 -10.2; 141 -10.3; 155 -10.4; 170 -10.6; 187 -10.6; 206 -10.7; 227 -10.6; 249 -10.5; 274 -10.4; 302 -10.3; 332 -10.0; 365 -9.7; 402 -9.5; 442 -9.4; 486 -9.1; 535 -8.9; 588 -8.6; 647 -8.3; 712 -8.0; 783 -7.7; 861 -7.5; 947 -7.6; 1042 -8.1; 1146 -8.8; 1261 -9.6; 1387 -10.0; 1526 -9.6; 1678 -8.5; 1846 -6.7; 2031 -4.1; 2234 -1.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.9; 3957 -2.5; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -1.1; 6373 -8.7; 7010 -10.4; 7711 -7.1; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.0; 15026 -22.9; 16529 -28.3; 18182 -25.4; 20000 -13.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ambient Acoustics AM24 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ambient Acoustics AM24 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 212 Hz   | 0.42 | -4.3 dB  |
| Peaking | 1570 Hz  | 1.28 | -9.9 dB  |
| Peaking | 2369 Hz  | 0.72 | 10.2 dB  |
| Peaking | 5128 Hz  | 4.73 | 4.4 dB   |
| Peaking | 17233 Hz | 1.26 | -24.6 dB |
| Peaking | 19 Hz    | 1.68 | 1.7 dB   |
| Peaking | 5785 Hz  | 9.25 | 3.6 dB   |
| Peaking | 6718 Hz  | 4.92 | -6.7 dB  |
| Peaking | 12711 Hz | 1.38 | 8.4 dB   |
| Peaking | 15023 Hz | 1.96 | -9.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB   |
| Peaking | 62 Hz    | 1.41 | -1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -22.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ambient%20Acoustics%20AM24/Ambient%20Acoustics%20AM24.png)