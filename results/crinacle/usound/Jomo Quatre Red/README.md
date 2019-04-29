# Jomo Quatre Red
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.8; 25 -9.9; 28 -10.0; 31 -10.1; 34 -10.2; 37 -10.2; 41 -10.4; 45 -10.5; 49 -10.6; 54 -10.7; 60 -10.8; 66 -11.0; 72 -11.3; 79 -11.6; 87 -11.9; 96 -12.1; 106 -12.3; 116 -12.6; 128 -12.7; 141 -12.8; 155 -12.9; 170 -12.8; 187 -12.7; 206 -12.5; 227 -12.4; 249 -12.1; 274 -11.8; 302 -11.5; 332 -11.2; 365 -10.8; 402 -10.5; 442 -10.0; 486 -9.5; 535 -9.0; 588 -8.4; 647 -7.8; 712 -7.1; 783 -6.3; 861 -5.4; 947 -5.0; 1042 -4.8; 1146 -4.8; 1261 -4.6; 1387 -4.0; 1526 -3.2; 1678 -2.9; 1846 -2.8; 2031 -2.9; 2234 -2.8; 2457 -1.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.7; 4788 -6.9; 5267 -5.8; 5793 -2.0; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Quatre Red GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Quatre Red ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.74 | -2.3 dB |
| Peaking | 172 Hz  | 0.32 | -6.3 dB |
| Peaking | 889 Hz  | 2.13 | 1.1 dB  |
| Peaking | 2292 Hz | 0.47 | 3.8 dB  |
| Peaking | 3248 Hz | 2.3  | 3.3 dB  |
| Peaking | 4021 Hz | 6.82 | 2.6 dB  |
| Peaking | 4786 Hz | 4.19 | -3.8 dB |
| Peaking | 5138 Hz | 6.66 | -1.5 dB |
| Peaking | 6238 Hz | 3.09 | 6.5 dB  |
| Peaking | 7440 Hz | 1.58 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Quatre%20Red/Jomo%20Quatre%20Red.png)