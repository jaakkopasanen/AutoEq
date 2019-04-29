# Jomo Haka
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.6; 25 -8.7; 28 -8.9; 31 -9.0; 34 -9.1; 37 -9.2; 41 -9.4; 45 -9.5; 49 -9.6; 54 -9.8; 60 -10.0; 66 -10.2; 72 -10.6; 79 -10.9; 87 -11.2; 96 -11.6; 106 -11.9; 116 -12.2; 128 -12.4; 141 -12.6; 155 -12.9; 170 -13.1; 187 -13.0; 206 -12.9; 227 -12.8; 249 -12.6; 274 -12.3; 302 -11.9; 332 -11.5; 365 -10.9; 402 -10.5; 442 -10.0; 486 -9.3; 535 -8.8; 588 -8.1; 647 -7.4; 712 -6.6; 783 -5.9; 861 -5.2; 947 -4.8; 1042 -4.7; 1146 -4.8; 1261 -4.8; 1387 -4.4; 1526 -3.6; 1678 -2.7; 1846 -1.9; 2031 -1.2; 2234 -0.6; 2457 -0.9; 2703 -2.2; 2973 -3.3; 3270 -2.7; 3597 -1.2; 3957 -0.5; 4353 -0.6; 4788 -2.5; 5267 -7.3; 5793 -8.2; 6373 -3.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.4; 16529 -13.6; 18182 -11.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Haka GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Haka ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 71 Hz    | 0.28 | -2.7 dB |
| Peaking | 217 Hz   | 0.6  | -4.9 dB |
| Peaking | 2117 Hz  | 0.87 | 5.2 dB  |
| Peaking | 4120 Hz  | 4.26 | 4.8 dB  |
| Peaking | 17044 Hz | 1.92 | -7.9 dB |
| Peaking | 902 Hz   | 3.13 | 1.4 dB  |
| Peaking | 1381 Hz  | 3.72 | -1.0 dB |
| Peaking | 5556 Hz  | 8.69 | -4.9 dB |
| Peaking | 6560 Hz  | 7.3  | 3.5 dB  |
| Peaking | 14046 Hz | 4.83 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -5.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Haka/Jomo%20Haka.png)