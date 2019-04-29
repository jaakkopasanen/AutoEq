# JH Audio 13v2 2 o’clock
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -7.7; 25 -7.7; 28 -7.8; 31 -7.9; 34 -8.0; 37 -8.1; 41 -8.2; 45 -8.4; 49 -8.5; 54 -8.7; 60 -8.9; 66 -9.1; 72 -9.3; 79 -9.6; 87 -9.9; 96 -10.2; 106 -10.5; 116 -10.5; 128 -10.7; 141 -10.8; 155 -10.8; 170 -10.8; 187 -10.6; 206 -10.4; 227 -10.2; 249 -9.9; 274 -9.7; 302 -9.3; 332 -9.0; 365 -8.7; 402 -8.3; 442 -7.9; 486 -7.5; 535 -7.1; 588 -6.6; 647 -6.2; 712 -5.6; 783 -5.1; 861 -4.7; 947 -4.7; 1042 -4.8; 1146 -5.0; 1261 -5.4; 1387 -5.7; 1526 -5.6; 1678 -5.4; 1846 -5.3; 2031 -5.6; 2234 -6.1; 2457 -6.5; 2703 -5.3; 2973 -1.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.7; 5793 -4.4; 6373 -5.5; 7010 -11.3; 7711 -15.7; 8482 -11.6; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -11.2; 18182 -18.2; 20000 -16.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio 13v2 2 o’clock GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio 13v2 2 o’clock ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 101 Hz   | 0.57 | -3.4 dB  |
| Peaking | 221 Hz   | 1.1  | -2.3 dB  |
| Peaking | 4487 Hz  | 1    | 7.0 dB   |
| Peaking | 7624 Hz  | 4.15 | -12.6 dB |
| Peaking | 18966 Hz | 1.24 | -14.2 dB |
| Peaking | 917 Hz   | 2.11 | 2.0 dB   |
| Peaking | 2557 Hz  | 3.15 | -3.2 dB  |
| Peaking | 3077 Hz  | 4.88 | 3.2 dB   |
| Peaking | 14720 Hz | 2.67 | 2.3 dB   |
| Peaking | 22049 Hz | 1.87 | 0.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.4 dB |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/JH%20Audio%2013v2%202%20o%E2%80%99clock/JH%20Audio%2013v2%202%20o%E2%80%99clock.png)