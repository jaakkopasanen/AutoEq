# Unique Melody Merlin V2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.4; 25 -6.5; 28 -6.7; 31 -6.8; 34 -7.0; 37 -7.1; 41 -7.3; 45 -7.5; 49 -7.6; 54 -7.8; 60 -8.1; 66 -8.4; 72 -8.8; 79 -9.1; 87 -9.5; 96 -10.0; 106 -10.4; 116 -10.6; 128 -11.0; 141 -11.2; 155 -11.5; 170 -11.6; 187 -11.7; 206 -11.7; 227 -11.6; 249 -11.5; 274 -11.4; 302 -11.1; 332 -10.8; 365 -10.5; 402 -10.2; 442 -9.9; 486 -9.5; 535 -9.2; 588 -8.6; 647 -8.2; 712 -7.7; 783 -7.2; 861 -6.8; 947 -6.6; 1042 -6.7; 1146 -7.1; 1261 -7.4; 1387 -7.4; 1526 -7.0; 1678 -6.4; 1846 -5.6; 2031 -4.4; 2234 -2.9; 2457 -1.4; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.5; 4788 -1.3; 5267 -0.5; 5793 -0.8; 6373 -2.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -10.6; 11289 -10.1; 12418 -9.8; 13660 -17.9; 15026 -24.6; 16529 -19.3; 18182 -7.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody Merlin V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody Merlin V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 110 Hz   | 0.94 | -1.2 dB  |
| Peaking | 232 Hz   | 0.51 | -4.8 dB  |
| Peaking | 2974 Hz  | 1.71 | 5.8 dB   |
| Peaking | 5395 Hz  | 1.54 | 5.6 dB   |
| Peaking | 15220 Hz | 1.87 | -19.9 dB |
| Peaking | 896 Hz   | 3.06 | 0.9 dB   |
| Peaking | 1412 Hz  | 3.14 | -1.4 dB  |
| Peaking | 12361 Hz | 6.54 | 4.1 dB   |
| Peaking | 16853 Hz | 0.67 | -2.3 dB  |
| Peaking | 18523 Hz | 1.6  | 4.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB   |
| Peaking | 62 Hz    | 1.41 | -1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 16000 Hz | 1.41 | -18.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Unique%20Melody%20Merlin%20V2/Unique%20Melody%20Merlin%20V2.png)