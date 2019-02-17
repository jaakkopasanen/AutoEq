# AKG K280 Parabolic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.1; 54 -1.7; 60 -2.4; 66 -3.0; 72 -3.2; 79 -3.6; 87 -4.2; 96 -4.7; 106 -5.2; 116 -5.6; 128 -5.9; 141 -6.2; 155 -6.4; 170 -6.6; 187 -6.8; 206 -7.0; 227 -7.1; 249 -7.2; 274 -7.2; 302 -7.1; 332 -7.3; 365 -7.2; 402 -7.2; 442 -7.3; 486 -7.3; 535 -7.3; 588 -7.3; 647 -7.4; 712 -7.4; 783 -7.4; 861 -7.3; 947 -7.0; 1042 -5.9; 1146 -4.2; 1261 -3.2; 1387 -3.0; 1526 -3.6; 1678 -4.7; 1846 -5.8; 2031 -5.7; 2234 -4.2; 2457 -3.0; 2703 -2.7; 2973 -2.9; 3270 -3.7; 3597 -4.2; 3957 -2.6; 4353 -2.8; 4788 -4.2; 5267 -8.2; 5793 -4.4; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K280 Parabolic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K280 Parabolic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.69 | 6.7 dB  |
| Peaking | 1347 Hz  | 4.48 | 3.6 dB  |
| Peaking | 3103 Hz  | 1.43 | 3.7 dB  |
| Peaking | 6414 Hz  | 6.96 | 4.9 dB  |
| Peaking | 22050 Hz | 2.29 | 1.8 dB  |
| Peaking | 563 Hz   | 0.39 | -1.2 dB |
| Peaking | 1173 Hz  | 6    | 1.7 dB  |
| Peaking | 3461 Hz  | 4.11 | -4.4 dB |
| Peaking | 3785 Hz  | 1.69 | 3.6 dB  |
| Peaking | 5333 Hz  | 9.33 | -4.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K280%20Parabolic/AKG%20K280%20Parabolic.png)