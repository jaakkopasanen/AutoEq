# JH Audio 16v2 2 o’clock
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.6; 25 -7.8; 28 -8.1; 31 -8.3; 34 -8.5; 37 -8.7; 41 -8.9; 45 -9.1; 49 -9.3; 54 -9.6; 60 -9.9; 66 -10.3; 72 -10.6; 79 -10.9; 87 -11.3; 96 -11.8; 106 -12.1; 116 -12.4; 128 -12.7; 141 -12.9; 155 -13.0; 170 -13.1; 187 -13.1; 206 -13.0; 227 -12.9; 249 -12.7; 274 -12.5; 302 -12.2; 332 -11.9; 365 -11.6; 402 -11.2; 442 -10.8; 486 -10.4; 535 -9.9; 588 -9.4; 647 -8.8; 712 -8.1; 783 -7.3; 861 -6.6; 947 -6.0; 1042 -5.9; 1146 -6.1; 1261 -6.2; 1387 -5.8; 1526 -4.8; 1678 -3.6; 1846 -2.4; 2031 -1.7; 2234 -1.5; 2457 -1.5; 2703 -1.2; 2973 -1.0; 3270 -1.1; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.8; 9330 -8.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.1; 20000 -15.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio 16v2 2 o’clock GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio 16v2 2 o’clock ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 59 Hz    | 0.45 | -1.8 dB |
| Peaking | 125 Hz   | 0.85 | -2.1 dB |
| Peaking | 271 Hz   | 0.5  | -5.2 dB |
| Peaking | 4064 Hz  | 0.49 | 6.8 dB  |
| Peaking | 8728 Hz  | 2.54 | -6.0 dB |
| Peaking | 937 Hz   | 2.08 | 2.0 dB  |
| Peaking | 1672 Hz  | 0.78 | -3.3 dB |
| Peaking | 1951 Hz  | 1.74 | 4.0 dB  |
| Peaking | 6104 Hz  | 5.29 | 1.8 dB  |
| Peaking | 19909 Hz | 1.75 | -8.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/JH%20Audio%2016v2%202%20o%E2%80%99clock/JH%20Audio%2016v2%202%20o%E2%80%99clock.png)