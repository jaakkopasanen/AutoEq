# Meze 12 Classics
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.5; 28 -2.1; 31 -2.6; 34 -3.0; 37 -3.4; 41 -3.9; 45 -4.3; 49 -4.6; 54 -5.1; 60 -5.5; 66 -5.9; 72 -6.4; 79 -6.8; 87 -7.3; 96 -7.9; 106 -8.3; 116 -8.6; 128 -9.0; 141 -9.2; 155 -9.4; 170 -9.5; 187 -9.5; 206 -9.5; 227 -9.4; 249 -9.3; 274 -9.1; 302 -8.7; 332 -8.2; 365 -7.7; 402 -7.2; 442 -6.7; 486 -6.1; 535 -5.5; 588 -4.9; 647 -4.3; 712 -3.8; 783 -3.1; 861 -2.5; 947 -2.4; 1042 -2.3; 1146 -2.0; 1261 -2.5; 1387 -2.9; 1526 -2.8; 1678 -2.6; 1846 -2.6; 2031 -2.7; 2234 -3.0; 2457 -4.1; 2703 -5.4; 2973 -5.2; 3270 -3.5; 3597 -2.7; 3957 -3.0; 4353 -4.1; 4788 -7.4; 5267 -11.7; 5793 -7.6; 6373 -2.4; 7010 -2.8; 7711 -5.0; 8482 -5.3; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -12.2; 15026 -24.3; 16529 -27.2; 18182 -21.6; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 12 Classics GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 12 Classics ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 13 Hz    |  0.48 | 6.0 dB   |
| Peaking | 215 Hz   |  0.49 | -5.7 dB  |
| Peaking | 2886 Hz  |  0.1  | 3.6 dB   |
| Peaking | 5249 Hz  |  6.09 | -9.5 dB  |
| Peaking | 16658 Hz |  1.34 | -26.1 dB |
| Peaking | 910 Hz   |  3.35 | 1.1 dB   |
| Peaking | 2755 Hz  |  4.09 | -3.4 dB  |
| Peaking | 6592 Hz  | 10.1  | 3.4 dB   |
| Peaking | 12788 Hz |  2.51 | 7.5 dB   |
| Peaking | 14890 Hz |  2.97 | -8.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB   |
| Peaking | 62 Hz    | 1.41 | -0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 16000 Hz | 1.41 | -23.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Meze%2012%20Classics/Meze%2012%20Classics.png)