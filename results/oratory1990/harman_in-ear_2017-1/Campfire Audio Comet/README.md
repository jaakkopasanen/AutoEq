# Campfire Audio Comet
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.0; 25 -4.2; 28 -4.4; 31 -4.6; 34 -4.7; 37 -4.8; 41 -5.0; 45 -5.2; 49 -5.4; 54 -5.6; 60 -5.9; 66 -6.2; 72 -6.5; 79 -6.9; 87 -7.4; 96 -7.8; 106 -8.2; 116 -8.6; 128 -8.9; 141 -9.2; 155 -9.4; 170 -9.5; 187 -9.7; 206 -9.7; 227 -9.7; 249 -9.9; 274 -10.2; 302 -10.3; 332 -10.0; 365 -9.6; 402 -9.4; 442 -9.1; 486 -8.8; 535 -8.5; 588 -8.1; 647 -7.7; 712 -7.3; 783 -6.9; 861 -6.6; 947 -6.5; 1042 -6.5; 1146 -6.4; 1261 -6.1; 1387 -5.6; 1526 -4.9; 1678 -4.1; 1846 -3.3; 2031 -2.5; 2234 -1.9; 2457 -1.8; 2703 -2.8; 2973 -4.8; 3270 -5.8; 3597 -4.2; 3957 -2.0; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -0.8; 6373 -3.5; 7010 -5.8; 7711 -6.2; 8482 -6.5; 9330 -8.0; 10263 -9.3; 11289 -7.1; 12418 -6.5; 13660 -6.8; 15026 -11.3; 16529 -14.0; 18182 -12.6; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Comet GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Comet ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.35 | 2.6 dB  |
| Peaking | 232 Hz   | 0.51 | -3.8 dB |
| Peaking | 2165 Hz  | 1.98 | 4.6 dB  |
| Peaking | 4996 Hz  | 2.19 | 6.8 dB  |
| Peaking | 17331 Hz | 1.01 | -7.8 dB |
| Peaking | 844 Hz   | 4.43 | 0.6 dB  |
| Peaking | 3261 Hz  | 4.99 | -3.9 dB |
| Peaking | 3409 Hz  | 2.14 | 2.0 dB  |
| Peaking | 10072 Hz | 4.41 | -2.8 dB |
| Peaking | 12907 Hz | 3.3  | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -7.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Campfire%20Audio%20Comet/Campfire%20Audio%20Comet.png)