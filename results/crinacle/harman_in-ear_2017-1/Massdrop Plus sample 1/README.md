# Massdrop Plus sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.7; 25 -8.0; 28 -8.4; 31 -8.7; 34 -8.9; 37 -9.1; 41 -9.3; 45 -9.5; 49 -9.7; 54 -10.0; 60 -10.2; 66 -10.5; 72 -10.8; 79 -11.1; 87 -11.5; 96 -11.8; 106 -12.1; 116 -12.4; 128 -12.6; 141 -12.8; 155 -12.8; 170 -12.8; 187 -12.7; 206 -12.6; 227 -12.4; 249 -12.1; 274 -11.8; 302 -11.4; 332 -10.9; 365 -10.3; 402 -9.9; 442 -9.4; 486 -8.9; 535 -8.4; 588 -7.9; 647 -7.4; 712 -6.9; 783 -6.4; 861 -6.1; 947 -6.0; 1042 -6.4; 1146 -7.2; 1261 -7.9; 1387 -8.2; 1526 -8.1; 1678 -7.7; 1846 -7.3; 2031 -6.5; 2234 -5.4; 2457 -4.1; 2703 -3.0; 2973 -1.9; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -12.2; 16529 -13.0; 18182 -8.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop Plus sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop Plus sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 100 Hz   | 0.44 | -4.4 dB |
| Peaking | 232 Hz   | 0.8  | -3.5 dB |
| Peaking | 1643 Hz  | 2.2  | -2.8 dB |
| Peaking | 4213 Hz  | 0.94 | 6.9 dB  |
| Peaking | 16260 Hz | 2.03 | -7.8 dB |
| Peaking | 857 Hz   | 3.17 | 1.4 dB  |
| Peaking | 2854 Hz  | 0.08 | -0.2 dB |
| Peaking | 6349 Hz  | 3.41 | 3.9 dB  |
| Peaking | 7488 Hz  | 2.08 | -2.9 dB |
| Peaking | 13446 Hz | 5.55 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -6.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Massdrop%20Plus%20sample%201/Massdrop%20Plus%20sample%201.png)