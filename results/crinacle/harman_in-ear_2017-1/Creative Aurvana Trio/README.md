# Creative Aurvana Trio
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.6; 25 -8.8; 28 -9.0; 31 -9.3; 34 -9.5; 37 -9.6; 41 -9.8; 45 -10.0; 49 -10.1; 54 -10.3; 60 -10.5; 66 -10.8; 72 -11.0; 79 -11.3; 87 -11.6; 96 -12.0; 106 -12.2; 116 -12.4; 128 -12.6; 141 -12.8; 155 -12.7; 170 -12.7; 187 -12.6; 206 -12.4; 227 -12.1; 249 -11.8; 274 -11.4; 302 -10.9; 332 -10.3; 365 -9.7; 402 -9.2; 442 -8.6; 486 -8.0; 535 -7.4; 588 -6.8; 647 -6.1; 712 -5.4; 783 -4.7; 861 -4.1; 947 -3.7; 1042 -3.7; 1146 -3.9; 1261 -4.2; 1387 -4.1; 1526 -3.8; 1678 -3.5; 1846 -3.5; 2031 -3.9; 2234 -3.8; 2457 -3.2; 2703 -2.6; 2973 -1.8; 3270 -0.5; 3597 -0.5; 3957 -1.7; 4353 -4.9; 4788 -5.0; 5267 -2.1; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.7; 8482 -9.1; 9330 -9.2; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -11.8; 15026 -17.1; 16529 -14.0; 18182 -10.5; 20000 -16.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Trio GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Trio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 67 Hz    | 0.27 | -2.8 dB  |
| Peaking | 194 Hz   | 0.52 | -4.5 dB  |
| Peaking | 2114 Hz  | 0.35 | 4.0 dB   |
| Peaking | 6004 Hz  | 5    | 4.9 dB   |
| Peaking | 15725 Hz | 1.16 | -10.1 dB |
| Peaking | 2360 Hz  | 1.44 | -2.9 dB  |
| Peaking | 3725 Hz  | 1.18 | 5.0 dB   |
| Peaking | 4515 Hz  | 4.24 | -5.7 dB  |
| Peaking | 8722 Hz  | 3.17 | -3.9 dB  |
| Peaking | 12200 Hz | 3.95 | 3.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 16000 Hz | 1.41 | -10.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Creative%20Aurvana%20Trio/Creative%20Aurvana%20Trio.png)