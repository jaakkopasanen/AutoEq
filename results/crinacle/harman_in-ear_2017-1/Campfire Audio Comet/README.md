# Campfire Audio Comet
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.5; 25 -6.6; 28 -6.7; 31 -6.8; 34 -6.9; 37 -6.9; 41 -7.0; 45 -7.1; 49 -7.2; 54 -7.4; 60 -7.6; 66 -7.9; 72 -8.1; 79 -8.3; 87 -8.7; 96 -9.3; 106 -9.8; 116 -10.0; 128 -10.4; 141 -10.5; 155 -10.8; 170 -10.9; 187 -10.9; 206 -10.7; 227 -10.9; 249 -10.8; 274 -10.6; 302 -10.5; 332 -10.1; 365 -9.7; 402 -9.5; 442 -9.2; 486 -8.9; 535 -8.3; 588 -7.7; 647 -7.3; 712 -6.8; 783 -6.0; 861 -5.5; 947 -5.2; 1042 -5.3; 1146 -5.6; 1261 -5.8; 1387 -5.5; 1526 -4.8; 1678 -3.9; 1846 -3.1; 2031 -2.3; 2234 -1.8; 2457 -2.0; 2703 -3.4; 2973 -6.1; 3270 -7.1; 3597 -4.1; 3957 -1.0; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.1; 6373 -6.0; 7010 -6.3; 7711 -6.2; 8482 -6.5; 9330 -9.3; 10263 -7.6; 11289 -6.5; 12418 -6.5; 13660 -8.1; 15026 -16.1; 16529 -21.1; 18182 -21.7; 20000 -17.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Comet GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Comet ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 196 Hz   | 0.59 | -4.7 dB  |
| Peaking | 2063 Hz  | 2.07 | 4.3 dB   |
| Peaking | 5206 Hz  | 1.67 | 7.4 dB   |
| Peaking | 6593 Hz  | 6.02 | -4.0 dB  |
| Peaking | 18095 Hz | 0.89 | -17.4 dB |
| Peaking | 919 Hz   | 3.33 | 1.7 dB   |
| Peaking | 3214 Hz  | 7.08 | -3.8 dB  |
| Peaking | 4010 Hz  | 7.17 | 2.3 dB   |
| Peaking | 12974 Hz | 2.87 | 5.4 dB   |
| Peaking | 15656 Hz | 2.58 | -4.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB   |
| Peaking | 62 Hz    | 1.41 | -0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 16000 Hz | 1.41 | -15.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Campfire%20Audio%20Comet/Campfire%20Audio%20Comet.png)