# Earsonics Grace
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.2; 25 -7.5; 28 -7.9; 31 -8.2; 34 -8.4; 37 -8.7; 41 -8.9; 45 -9.2; 49 -9.4; 54 -9.6; 60 -9.8; 66 -10.1; 72 -10.4; 79 -10.5; 87 -10.7; 96 -10.9; 106 -11.2; 116 -11.2; 128 -11.3; 141 -11.0; 155 -10.7; 170 -10.3; 187 -9.9; 206 -9.5; 227 -8.9; 249 -8.2; 274 -7.7; 302 -7.3; 332 -7.0; 365 -6.9; 402 -6.9; 442 -7.0; 486 -7.2; 535 -7.4; 588 -7.6; 647 -7.8; 712 -7.9; 783 -7.9; 861 -8.1; 947 -8.5; 1042 -9.2; 1146 -10.3; 1261 -11.4; 1387 -11.8; 1526 -11.3; 1678 -9.8; 1846 -7.5; 2031 -5.2; 2234 -3.1; 2457 -1.4; 2703 -0.5; 2973 -0.5; 3270 -0.7; 3597 -2.9; 3957 -4.4; 4353 -1.8; 4788 -0.5; 5267 -0.5; 5793 -2.9; 6373 -5.9; 7010 -10.6; 7711 -7.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -9.9; 16529 -14.0; 18182 -9.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics Grace GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics Grace ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 101 Hz   |  0.6  | -4.8 dB |
| Peaking | 1417 Hz  |  1.66 | -6.5 dB |
| Peaking | 2716 Hz  |  1.74 | 7.4 dB  |
| Peaking | 5012 Hz  |  4.42 | 6.1 dB  |
| Peaking | 16694 Hz |  2.11 | -8.2 dB |
| Peaking | 36 Hz    |  2.19 | -0.7 dB |
| Peaking | 338 Hz   |  3.31 | 0.9 dB  |
| Peaking | 5624 Hz  | 10.36 | 2.0 dB  |
| Peaking | 7122 Hz  |  7.93 | -5.3 dB |
| Peaking | 13735 Hz |  4.04 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -5.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Earsonics%20Grace/Earsonics%20Grace.png)