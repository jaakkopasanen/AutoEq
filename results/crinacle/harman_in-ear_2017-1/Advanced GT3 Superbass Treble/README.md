# Advanced GT3 Superbass Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.1; 25 -11.2; 28 -11.2; 31 -11.2; 34 -11.1; 37 -11.1; 41 -11.0; 45 -10.9; 49 -10.8; 54 -10.6; 60 -10.5; 66 -10.5; 72 -10.6; 79 -10.7; 87 -10.7; 96 -11.0; 106 -11.1; 116 -11.3; 128 -11.4; 141 -11.5; 155 -11.7; 170 -11.7; 187 -11.7; 206 -11.8; 227 -11.8; 249 -11.7; 274 -11.7; 302 -11.6; 332 -11.4; 365 -11.2; 402 -11.0; 442 -10.9; 486 -10.6; 535 -10.6; 588 -10.3; 647 -9.7; 712 -9.2; 783 -8.8; 861 -8.5; 947 -8.2; 1042 -8.1; 1146 -8.2; 1261 -8.1; 1387 -7.6; 1526 -6.6; 1678 -5.5; 1846 -4.2; 2031 -2.9; 2234 -1.4; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -1.2; 3597 -2.7; 3957 -4.9; 4353 -6.1; 4788 -3.9; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -14.2; 15026 -26.0; 16529 -31.6; 18182 -31.6; 20000 -27.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced GT3 Superbass Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced GT3 Superbass Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.7  | -4.0 dB  |
| Peaking | 252 Hz   | 0.23 | -5.1 dB  |
| Peaking | 2623 Hz  | 1.67 | 6.0 dB   |
| Peaking | 9990 Hz  | 0.27 | 24.0 dB  |
| Peaking | 17111 Hz | 0.28 | -41.6 dB |
| Peaking | 4341 Hz  | 4.45 | -4.5 dB  |
| Peaking | 5885 Hz  | 1.88 | 6.3 dB   |
| Peaking | 7935 Hz  | 1.55 | -5.1 dB  |
| Peaking | 12723 Hz | 3.18 | 7.1 dB   |
| Peaking | 15003 Hz | 3.16 | -5.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 8.0 dB   |
| Peaking | 16000 Hz | 1.41 | -30.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Advanced%20GT3%20Superbass%20Treble/Advanced%20GT3%20Superbass%20Treble.png)