# Lime Ears Model X Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.4; 25 -6.6; 28 -6.8; 31 -7.0; 34 -7.1; 37 -7.3; 41 -7.4; 45 -7.6; 49 -7.8; 54 -8.0; 60 -8.3; 66 -8.6; 72 -8.9; 79 -9.3; 87 -9.6; 96 -10.1; 106 -10.5; 116 -10.8; 128 -11.1; 141 -11.4; 155 -11.5; 170 -11.7; 187 -11.8; 206 -11.8; 227 -11.8; 249 -11.6; 274 -11.5; 302 -11.3; 332 -10.9; 365 -10.5; 402 -10.2; 442 -9.8; 486 -9.3; 535 -8.8; 588 -8.2; 647 -7.7; 712 -7.0; 783 -6.3; 861 -5.6; 947 -5.3; 1042 -5.2; 1146 -5.5; 1261 -5.7; 1387 -5.5; 1526 -5.0; 1678 -4.5; 1846 -4.0; 2031 -3.5; 2234 -2.8; 2457 -1.3; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -0.7; 4353 -1.8; 4788 -4.3; 5267 -3.8; 5793 -1.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.5; 9330 -8.0; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -10.1; 15026 -16.9; 16529 -19.4; 18182 -18.1; 20000 -11.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lime Ears Model X Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lime Ears Model X Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 155 Hz   | 0.62 | -4.7 dB  |
| Peaking | 335 Hz   | 1.15 | -2.5 dB  |
| Peaking | 3130 Hz  | 0.97 | 6.4 dB   |
| Peaking | 6238 Hz  | 5.34 | 4.9 dB   |
| Peaking | 17355 Hz | 1.02 | -14.5 dB |
| Peaking | 926 Hz   | 4.35 | 1.4 dB   |
| Peaking | 8206 Hz  | 1.67 | -0.4 dB  |
| Peaking | 8919 Hz  | 4.38 | -1.7 dB  |
| Peaking | 12855 Hz | 1.65 | 4.9 dB   |
| Peaking | 14969 Hz | 2.58 | -5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.8 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -14.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Lime%20Ears%20Model%20X%20Bass/Lime%20Ears%20Model%20X%20Bass.png)