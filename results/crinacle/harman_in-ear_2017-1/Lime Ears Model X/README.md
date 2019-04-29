# Lime Ears Model X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.0; 25 -1.2; 28 -1.4; 31 -1.6; 34 -1.8; 37 -1.9; 41 -2.1; 45 -2.3; 49 -2.5; 54 -2.7; 60 -3.0; 66 -3.3; 72 -3.6; 79 -4.0; 87 -4.5; 96 -4.9; 106 -5.3; 116 -5.8; 128 -6.1; 141 -6.4; 155 -6.7; 170 -6.9; 187 -7.1; 206 -7.2; 227 -7.3; 249 -7.3; 274 -7.3; 302 -7.2; 332 -7.0; 365 -6.8; 402 -6.7; 442 -6.5; 486 -6.2; 535 -6.0; 588 -5.7; 647 -5.3; 712 -4.9; 783 -4.5; 861 -4.1; 947 -4.1; 1042 -4.3; 1146 -4.9; 1261 -5.4; 1387 -5.6; 1526 -5.4; 1678 -5.2; 1846 -4.9; 2031 -4.6; 2234 -3.9; 2457 -2.9; 2703 -1.6; 2973 -0.5; 3270 -0.5; 3597 -1.2; 3957 -1.3; 4353 -2.6; 4788 -5.4; 5267 -5.1; 5793 -2.6; 6373 -1.5; 7010 -2.7; 7711 -5.8; 8482 -8.1; 9330 -9.3; 10263 -7.8; 11289 -5.1; 12418 -5.1; 13660 -11.8; 15026 -18.8; 16529 -21.0; 18182 -19.6; 20000 -12.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lime Ears Model X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lime Ears Model X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.94 | 4.3 dB   |
| Peaking | 3190 Hz  | 2.5  | 4.5 dB   |
| Peaking | 9472 Hz  | 2.71 | -9.8 dB  |
| Peaking | 10978 Hz | 0.64 | 17.0 dB  |
| Peaking | 16156 Hz | 0.5  | -23.9 dB |
| Peaking | 256 Hz   | 0.8  | -2.5 dB  |
| Peaking | 917 Hz   | 2.34 | 1.5 dB   |
| Peaking | 1415 Hz  | 2.4  | -1.1 dB  |
| Peaking | 5059 Hz  | 8.59 | -2.9 dB  |
| Peaking | 6421 Hz  | 5.93 | 2.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB   |
| Peaking | 62 Hz    | 1.41 | 1.7 dB   |
| Peaking | 125 Hz   | 1.41 | -1.0 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 16000 Hz | 1.41 | -18.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Lime%20Ears%20Model%20X/Lime%20Ears%20Model%20X.png)