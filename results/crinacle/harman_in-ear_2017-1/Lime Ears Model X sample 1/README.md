# Lime Ears Model X sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.6; 25 -2.7; 28 -2.9; 31 -3.0; 34 -3.1; 37 -3.2; 41 -3.4; 45 -3.6; 49 -3.7; 54 -3.9; 60 -4.2; 66 -4.5; 72 -4.9; 79 -5.3; 87 -5.7; 96 -6.2; 106 -6.6; 116 -7.0; 128 -7.4; 141 -7.7; 155 -8.0; 170 -8.2; 187 -8.3; 206 -8.4; 227 -8.5; 249 -8.5; 274 -8.5; 302 -8.4; 332 -8.2; 365 -8.0; 402 -7.8; 442 -7.6; 486 -7.4; 535 -7.1; 588 -6.7; 647 -6.4; 712 -6.0; 783 -5.5; 861 -5.2; 947 -5.1; 1042 -5.3; 1146 -5.8; 1261 -6.3; 1387 -6.3; 1526 -6.0; 1678 -5.6; 1846 -5.2; 2031 -4.7; 2234 -4.2; 2457 -3.5; 2703 -2.5; 2973 -1.2; 3270 -0.6; 3597 -0.5; 3957 -0.6; 4353 -2.0; 4788 -4.4; 5267 -4.9; 5793 -3.6; 6373 -3.1; 7010 -5.0; 7711 -7.7; 8482 -7.7; 9330 -7.4; 10263 -6.5; 11289 -5.8; 12418 -5.8; 13660 -11.4; 15026 -18.3; 16529 -20.2; 18182 -18.1; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lime Ears Model X sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lime Ears Model X sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.28 | 3.4 dB   |
| Peaking | 212 Hz   | 0.59 | -3.2 dB  |
| Peaking | 3638 Hz  | 1.28 | 6.0 dB   |
| Peaking | 12214 Hz | 1.87 | 8.1 dB   |
| Peaking | 16439 Hz | 0.71 | -16.4 dB |
| Peaking | 923 Hz   | 2.74 | 1.4 dB   |
| Peaking | 1398 Hz  | 1.95 | -1.1 dB  |
| Peaking | 5017 Hz  | 4.92 | -2.8 dB  |
| Peaking | 6512 Hz  | 2.27 | 3.8 dB   |
| Peaking | 7723 Hz  | 3.54 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB   |
| Peaking | 62 Hz    | 1.41 | 1.4 dB   |
| Peaking | 125 Hz   | 1.41 | -1.4 dB  |
| Peaking | 250 Hz   | 1.41 | -2.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 16000 Hz | 1.41 | -15.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Lime%20Ears%20Model%20X%20sample%201/Lime%20Ears%20Model%20X%20sample%201.png)