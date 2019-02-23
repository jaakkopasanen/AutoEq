# Campfire Audio Comet
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.2; 25 -4.4; 28 -4.6; 31 -4.8; 34 -4.9; 37 -5.0; 41 -5.2; 45 -5.3; 49 -5.6; 54 -5.8; 60 -6.1; 66 -6.4; 72 -6.7; 79 -7.1; 87 -7.6; 96 -8.0; 106 -8.4; 116 -8.8; 128 -9.1; 141 -9.4; 155 -9.6; 170 -9.7; 187 -9.9; 206 -9.9; 227 -9.9; 249 -10.0; 274 -10.3; 302 -10.4; 332 -10.1; 365 -9.8; 402 -9.6; 442 -9.3; 486 -9.0; 535 -8.7; 588 -8.3; 647 -7.9; 712 -7.5; 783 -7.0; 861 -6.8; 947 -6.7; 1042 -6.7; 1146 -6.6; 1261 -6.3; 1387 -5.8; 1526 -5.1; 1678 -4.2; 1846 -3.4; 2031 -2.6; 2234 -2.0; 2457 -2.0; 2703 -3.0; 2973 -4.9; 3270 -6.0; 3597 -4.3; 3957 -2.2; 4353 -0.7; 4788 -0.5; 5267 -0.5; 5793 -1.0; 6373 -3.7; 7010 -6.0; 7711 -6.2; 8482 -6.5; 9330 -8.1; 10263 -9.4; 11289 -7.2; 12418 -6.5; 13660 -6.9; 15026 -11.5; 16529 -14.1; 18182 -12.7; 20000 -9.2
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
| Peaking | 13 Hz    | 0.24 | 2.7 dB  |
| Peaking | 234 Hz   | 0.5  | -3.9 dB |
| Peaking | 2171 Hz  | 2.07 | 4.5 dB  |
| Peaking | 4993 Hz  | 2.26 | 6.8 dB  |
| Peaking | 17346 Hz | 0.99 | -8.0 dB |
| Peaking | 840 Hz   | 4.6  | 0.5 dB  |
| Peaking | 3247 Hz  | 4.96 | -3.9 dB |
| Peaking | 3390 Hz  | 2.09 | 2.0 dB  |
| Peaking | 10067 Hz | 4.43 | -2.9 dB |
| Peaking | 12883 Hz | 3.35 | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -7.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Campfire%20Audio%20Comet/Campfire%20Audio%20Comet.png)