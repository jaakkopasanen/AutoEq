# Lime Ears Model X sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.5; 31 -1.7; 34 -1.9; 37 -2.0; 41 -2.2; 45 -2.4; 49 -2.7; 54 -2.9; 60 -3.2; 66 -3.5; 72 -3.8; 79 -4.2; 87 -4.6; 96 -5.1; 106 -5.5; 116 -6.0; 128 -6.3; 141 -6.6; 155 -6.8; 170 -7.0; 187 -7.2; 206 -7.4; 227 -7.5; 249 -7.5; 274 -7.5; 302 -7.4; 332 -7.3; 365 -7.0; 402 -6.9; 442 -6.8; 486 -6.5; 535 -6.3; 588 -6.0; 647 -5.7; 712 -5.3; 783 -4.9; 861 -4.5; 947 -4.5; 1042 -4.8; 1146 -5.4; 1261 -6.0; 1387 -6.3; 1526 -6.2; 1678 -6.1; 1846 -6.0; 2031 -5.8; 2234 -5.1; 2457 -3.6; 2703 -2.1; 2973 -1.3; 3270 -1.9; 3597 -3.4; 3957 -3.3; 4353 -4.6; 4788 -7.8; 5267 -6.7; 5793 -3.0; 6373 -1.3; 7010 -3.2; 7711 -5.7; 8482 -9.8; 9330 -12.6; 10263 -10.6; 11289 -5.9; 12418 -6.1; 13660 -13.6; 15026 -20.6; 16529 -23.3; 18182 -22.6; 20000 -17.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lime Ears Model X sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lime Ears Model X sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.77 | 5.0 dB   |
| Peaking | 3044 Hz  | 2.94 | 5.1 dB   |
| Peaking | 6545 Hz  | 4.16 | 6.3 dB   |
| Peaking | 9199 Hz  | 6.8  | -4.9 dB  |
| Peaking | 17688 Hz | 0.81 | -19.7 dB |
| Peaking | 255 Hz   | 0.93 | -2.0 dB  |
| Peaking | 878 Hz   | 3.47 | 1.6 dB   |
| Peaking | 9921 Hz  | 4.72 | -3.1 dB  |
| Peaking | 12093 Hz | 2.5  | 7.5 dB   |
| Peaking | 14996 Hz | 2.45 | -6.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.7 dB   |
| Peaking | 62 Hz    | 1.41 | 1.9 dB   |
| Peaking | 125 Hz   | 1.41 | -0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 16000 Hz | 1.41 | -21.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Lime%20Ears%20Model%20X%20sample%202/Lime%20Ears%20Model%20X%20sample%202.png)