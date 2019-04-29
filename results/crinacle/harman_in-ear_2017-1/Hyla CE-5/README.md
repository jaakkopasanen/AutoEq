# Hyla CE-5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.0; 25 -8.0; 28 -8.0; 31 -8.0; 34 -8.0; 37 -7.9; 41 -7.9; 45 -7.8; 49 -7.7; 54 -7.6; 60 -7.6; 66 -7.5; 72 -7.5; 79 -7.5; 87 -7.5; 96 -7.5; 106 -7.4; 116 -7.4; 128 -7.2; 141 -7.0; 155 -6.8; 170 -6.5; 187 -6.4; 206 -6.0; 227 -5.6; 249 -5.2; 274 -4.9; 302 -4.4; 332 -3.9; 365 -3.5; 402 -3.2; 442 -3.0; 486 -2.8; 535 -2.6; 588 -2.4; 647 -2.3; 712 -2.2; 783 -2.1; 861 -2.2; 947 -2.5; 1042 -3.3; 1146 -4.4; 1261 -5.4; 1387 -6.0; 1526 -6.3; 1678 -6.3; 1846 -6.2; 2031 -5.7; 2234 -4.8; 2457 -3.6; 2703 -2.4; 2973 -1.5; 3270 -1.2; 3597 -1.7; 3957 -2.9; 4353 -4.0; 4788 -4.2; 5267 -2.6; 5793 -0.8; 6373 -0.5; 7010 -1.6; 7711 -3.6; 8482 -3.9; 9330 -5.6; 10263 -6.8; 11289 -3.9; 12418 -4.1; 13660 -14.5; 15026 -23.3; 16529 -17.7; 18182 -7.7; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hyla CE-5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hyla CE-5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.4  | -4.1 dB  |
| Peaking | 129 Hz   | 1.18 | -2.3 dB  |
| Peaking | 6399 Hz  | 1.82 | 4.4 dB   |
| Peaking | 12240 Hz | 3.23 | 8.8 dB   |
| Peaking | 15118 Hz | 1.56 | -22.0 dB |
| Peaking | 837 Hz   | 0.97 | 3.6 dB   |
| Peaking | 1598 Hz  | 0.87 | -4.4 dB  |
| Peaking | 3110 Hz  | 1.64 | 4.1 dB   |
| Peaking | 4585 Hz  | 4.25 | -2.3 dB  |
| Peaking | 13295 Hz | 8.8  | 0.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 16000 Hz | 1.41 | -18.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Hyla%20CE-5/Hyla%20CE-5.png)