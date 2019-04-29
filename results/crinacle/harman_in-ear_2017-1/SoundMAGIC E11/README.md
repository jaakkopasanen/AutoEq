# SoundMAGIC E11
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.2; 25 -5.6; 28 -6.2; 31 -6.6; 34 -7.0; 37 -7.4; 41 -7.7; 45 -8.0; 49 -8.3; 54 -8.5; 60 -8.9; 66 -9.2; 72 -9.5; 79 -9.8; 87 -10.1; 96 -10.5; 106 -10.8; 116 -10.9; 128 -11.1; 141 -11.2; 155 -11.2; 170 -11.1; 187 -11.0; 206 -10.9; 227 -10.6; 249 -10.4; 274 -10.1; 302 -9.7; 332 -9.4; 365 -9.2; 402 -9.0; 442 -8.8; 486 -8.6; 535 -8.3; 588 -8.0; 647 -7.7; 712 -7.4; 783 -7.2; 861 -7.0; 947 -6.9; 1042 -7.2; 1146 -7.7; 1261 -8.0; 1387 -7.9; 1526 -7.3; 1678 -6.4; 1846 -5.2; 2031 -3.5; 2234 -1.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.9; 5267 -3.1; 5793 -5.9; 6373 -7.5; 7010 -6.6; 7711 -6.4; 8482 -8.5; 9330 -8.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.1; 15026 -20.7; 16529 -25.6; 18182 -21.0; 20000 -12.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundMAGIC E11 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundMAGIC E11 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.49 | 3.6 dB   |
| Peaking | 32 Hz    | 1.42 | -1.4 dB  |
| Peaking | 126 Hz   | 0.28 | -4.9 dB  |
| Peaking | 3420 Hz  | 1.12 | 7.3 dB   |
| Peaking | 17035 Hz | 1.38 | -21.0 dB |
| Peaking | 1423 Hz  | 2.71 | -2.3 dB  |
| Peaking | 2337 Hz  | 5.2  | 2.5 dB   |
| Peaking | 6354 Hz  | 7.39 | -2.2 dB  |
| Peaking | 12503 Hz | 2.37 | 7.0 dB   |
| Peaking | 17982 Hz | 0.33 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB   |
| Peaking | 62 Hz    | 1.41 | -2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 16000 Hz | 1.41 | -18.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/SoundMAGIC%20E11/SoundMAGIC%20E11.png)