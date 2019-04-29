# Jomo Quatre Filterless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -9.2; 25 -9.3; 28 -9.4; 31 -9.6; 34 -9.7; 37 -9.8; 41 -10.0; 45 -10.1; 49 -10.3; 54 -10.4; 60 -10.7; 66 -11.0; 72 -11.2; 79 -11.5; 87 -11.9; 96 -12.3; 106 -12.6; 116 -12.8; 128 -13.1; 141 -13.2; 155 -13.4; 170 -13.4; 187 -13.4; 206 -13.3; 227 -13.1; 249 -12.9; 274 -12.7; 302 -12.3; 332 -11.9; 365 -11.5; 402 -11.2; 442 -10.7; 486 -10.2; 535 -9.6; 588 -9.0; 647 -8.5; 712 -7.8; 783 -7.0; 861 -6.5; 947 -6.1; 1042 -6.1; 1146 -6.3; 1261 -6.2; 1387 -5.4; 1526 -4.3; 1678 -3.6; 1846 -2.9; 2031 -2.3; 2234 -1.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.6; 4788 -5.6; 5267 -4.8; 5793 -1.0; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.3; 15026 -12.8; 16529 -17.1; 18182 -19.1; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Quatre Filterless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Quatre Filterless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.15 | -2.3 dB  |
| Peaking | 209 Hz   | 0.42 | -5.6 dB  |
| Peaking | 2906 Hz  | 1.08 | 4.6 dB   |
| Peaking | 6644 Hz  | 0.18 | 2.4 dB   |
| Peaking | 17838 Hz | 0.91 | -14.8 dB |
| Peaking | 4180 Hz  | 5.68 | 2.5 dB   |
| Peaking | 4979 Hz  | 4.09 | -5.1 dB  |
| Peaking | 6193 Hz  | 2.93 | 5.8 dB   |
| Peaking | 7580 Hz  | 1.9  | -3.0 dB  |
| Peaking | 12998 Hz | 5.3  | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -5.6 dB  |
| Peaking | 500 Hz   | 1.41 | -2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 16000 Hz | 1.41 | -11.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Quatre%20Filterless/Jomo%20Quatre%20Filterless.png)