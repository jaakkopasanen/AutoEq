# Jomo Flamenco Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.3; 28 -1.8; 31 -2.1; 34 -2.4; 37 -2.7; 41 -3.0; 45 -3.3; 49 -3.6; 54 -3.9; 60 -4.2; 66 -4.6; 72 -5.0; 79 -5.4; 87 -5.9; 96 -6.4; 106 -6.8; 116 -7.2; 128 -7.6; 141 -7.9; 155 -8.2; 170 -8.3; 187 -8.4; 206 -8.5; 227 -8.5; 249 -8.4; 274 -8.3; 302 -8.1; 332 -7.8; 365 -7.4; 402 -7.1; 442 -6.8; 486 -6.3; 535 -5.8; 588 -5.2; 647 -4.6; 712 -3.9; 783 -3.2; 861 -2.6; 947 -2.4; 1042 -2.6; 1146 -3.3; 1261 -4.0; 1387 -4.5; 1526 -4.7; 1678 -5.0; 1846 -5.5; 2031 -6.2; 2234 -6.4; 2457 -5.6; 2703 -4.3; 2973 -3.6; 3270 -4.3; 3597 -5.1; 3957 -4.7; 4353 -5.5; 4788 -8.1; 5267 -10.6; 5793 -10.5; 6373 -10.3; 7010 -11.0; 7711 -9.3; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -11.7; 15026 -24.2; 16529 -28.7; 18182 -24.0; 20000 -15.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Flamenco Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Flamenco Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.98 | 5.5 dB   |
| Peaking | 937 Hz   | 2.26 | 4.0 dB   |
| Peaking | 6602 Hz  | 1.49 | -8.5 dB  |
| Peaking | 10894 Hz | 0.39 | 19.6 dB  |
| Peaking | 16311 Hz | 0.57 | -35.8 dB |
| Peaking | 214 Hz   | 1.04 | -2.6 dB  |
| Peaking | 4960 Hz  | 1.59 | 3.4 dB   |
| Peaking | 5138 Hz  | 4.03 | -5.3 dB  |
| Peaking | 12961 Hz | 3.36 | 9.3 dB   |
| Peaking | 13439 Hz | 1.29 | -5.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB   |
| Peaking | 62 Hz    | 1.41 | 1.4 dB   |
| Peaking | 125 Hz   | 1.41 | -1.4 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 16000 Hz | 1.41 | -22.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Flamenco%20Treble/Jomo%20Flamenco%20Treble.png)