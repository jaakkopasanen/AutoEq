# Noble Sage
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.2; 25 -6.4; 28 -6.6; 31 -6.7; 34 -6.9; 37 -7.0; 41 -7.2; 45 -7.4; 49 -7.6; 54 -7.8; 60 -8.1; 66 -8.4; 72 -8.8; 79 -9.1; 87 -9.5; 96 -10.0; 106 -10.3; 116 -10.6; 128 -10.9; 141 -11.2; 155 -11.4; 170 -11.5; 187 -11.5; 206 -11.4; 227 -11.3; 249 -11.2; 274 -11.0; 302 -10.6; 332 -10.2; 365 -9.8; 402 -9.4; 442 -9.0; 486 -8.6; 535 -8.0; 588 -7.5; 647 -7.0; 712 -6.5; 783 -5.9; 861 -5.5; 947 -5.3; 1042 -5.5; 1146 -5.9; 1261 -6.3; 1387 -6.3; 1526 -6.0; 1678 -5.6; 1846 -5.2; 2031 -4.6; 2234 -3.8; 2457 -2.8; 2703 -1.6; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -2.5; 4788 -4.8; 5267 -4.7; 5793 -3.0; 6373 -2.5; 7010 -4.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -16.3; 16529 -18.1; 18182 -8.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble Sage GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble Sage ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 145 Hz   |  0.71 | -4.3 dB  |
| Peaking | 297 Hz   |  1.25 | -2.5 dB  |
| Peaking | 3291 Hz  |  1.43 | 6.5 dB   |
| Peaking | 6227 Hz  |  5.91 | 3.3 dB   |
| Peaking | 15997 Hz |  2.71 | -14.4 dB |
| Peaking | 18 Hz    |  1.33 | 0.5 dB   |
| Peaking | 897 Hz   |  3.72 | 1.5 dB   |
| Peaking | 4950 Hz  | 10.15 | -1.5 dB  |
| Peaking | 13257 Hz |  4.41 | 2.9 dB   |
| Peaking | 16960 Hz |  6.15 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB   |
| Peaking | 62 Hz    | 1.41 | -1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 16000 Hz | 1.41 | -10.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Noble%20Sage/Noble%20Sage.png)