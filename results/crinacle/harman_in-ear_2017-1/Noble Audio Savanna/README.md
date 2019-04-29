# Noble Audio Savanna
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.8; 34 -1.3; 37 -1.7; 41 -2.3; 45 -2.8; 49 -3.2; 54 -3.6; 60 -4.2; 66 -4.7; 72 -5.3; 79 -5.8; 87 -6.4; 96 -7.0; 106 -7.5; 116 -8.0; 128 -8.5; 141 -8.9; 155 -9.3; 170 -9.6; 187 -9.8; 206 -10.0; 227 -10.1; 249 -10.1; 274 -10.1; 302 -10.0; 332 -9.9; 365 -9.7; 402 -9.6; 442 -9.5; 486 -9.2; 535 -9.0; 588 -8.7; 647 -8.4; 712 -8.0; 783 -7.6; 861 -7.2; 947 -7.1; 1042 -7.2; 1146 -7.7; 1261 -7.9; 1387 -7.7; 1526 -7.1; 1678 -6.2; 1846 -5.3; 2031 -4.4; 2234 -3.6; 2457 -3.0; 2703 -1.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -0.5; 5267 -0.6; 5793 -5.0; 6373 -8.6; 7010 -8.6; 7711 -7.9; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.2; 15026 -16.5; 16529 -23.8; 18182 -25.5; 20000 -18.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble Audio Savanna GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble Audio Savanna ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.5  | 6.6 dB   |
| Peaking | 74 Hz    | 0.85 | 1.7 dB   |
| Peaking | 187 Hz   | 0.27 | -4.1 dB  |
| Peaking | 3669 Hz  | 1.15 | 7.2 dB   |
| Peaking | 18115 Hz | 1.06 | -21.7 dB |
| Peaking | 1373 Hz  | 4.86 | -1.5 dB  |
| Peaking | 5270 Hz  | 4.76 | 4.8 dB   |
| Peaking | 6404 Hz  | 2.51 | -5.1 dB  |
| Peaking | 13265 Hz | 1.22 | 6.5 dB   |
| Peaking | 15870 Hz | 1.9  | -7.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 1.4 dB   |
| Peaking | 125 Hz   | 1.41 | -1.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -17.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Noble%20Audio%20Savanna/Noble%20Audio%20Savanna.png)