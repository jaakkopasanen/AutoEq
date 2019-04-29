# Geek Wold GK3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.0; 23 -12.3; 25 -12.6; 28 -12.9; 31 -13.1; 34 -13.2; 37 -13.3; 41 -13.3; 45 -13.4; 49 -13.4; 54 -13.4; 60 -13.5; 66 -13.5; 72 -13.5; 79 -13.5; 87 -13.6; 96 -13.6; 106 -13.6; 116 -13.5; 128 -13.4; 141 -13.3; 155 -13.0; 170 -12.7; 187 -12.4; 206 -12.0; 227 -11.6; 249 -11.2; 274 -10.7; 302 -10.2; 332 -9.7; 365 -9.1; 402 -8.7; 442 -8.2; 486 -7.8; 535 -7.3; 588 -6.9; 647 -6.5; 712 -6.1; 783 -5.8; 861 -5.6; 947 -5.8; 1042 -6.4; 1146 -7.2; 1261 -6.8; 1387 -7.4; 1526 -7.7; 1678 -7.9; 1846 -8.6; 2031 -9.7; 2234 -11.0; 2457 -11.3; 2703 -9.8; 2973 -8.8; 3270 -9.6; 3597 -12.5; 3957 -12.1; 4353 -6.9; 4788 -2.9; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.0; 16529 -13.8; 18182 -17.3; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Geek Wold GK3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Geek Wold GK3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 44 Hz    | 0.31 | -6.7 dB  |
| Peaking | 175 Hz   | 0.8  | -3.5 dB  |
| Peaking | 3982 Hz  | 1.1  | -11.4 dB |
| Peaking | 5237 Hz  | 1.59 | 14.1 dB  |
| Peaking | 18078 Hz | 1.54 | -12.3 dB |
| Peaking | 843 Hz   | 2.32 | 1.8 dB   |
| Peaking | 2311 Hz  | 3.82 | -2.5 dB  |
| Peaking | 3007 Hz  | 6.39 | 2.9 dB   |
| Peaking | 7999 Hz  | 6.02 | -1.5 dB  |
| Peaking | 14257 Hz | 3.51 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.4 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 16000 Hz | 1.41 | -6.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Geek%20Wold%20GK3/Geek%20Wold%20GK3.png)