# Jomo Haka
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.4; 25 -6.5; 28 -6.6; 31 -6.8; 34 -6.9; 37 -7.0; 41 -7.1; 45 -7.3; 49 -7.4; 54 -7.5; 60 -7.7; 66 -8.0; 72 -8.4; 79 -8.7; 87 -9.0; 96 -9.4; 106 -9.6; 116 -10.0; 128 -10.2; 141 -10.3; 155 -10.7; 170 -10.9; 187 -10.8; 206 -10.7; 227 -10.5; 249 -10.4; 274 -10.1; 302 -9.7; 332 -9.5; 365 -9.0; 402 -8.6; 442 -8.1; 486 -7.5; 535 -7.0; 588 -6.3; 647 -5.7; 712 -4.9; 783 -4.1; 861 -3.4; 947 -2.9; 1042 -2.8; 1146 -3.0; 1261 -3.2; 1387 -3.1; 1526 -2.6; 1678 -1.8; 1846 -1.1; 2031 -0.7; 2234 -0.7; 2457 -1.6; 2703 -3.2; 2973 -4.5; 3270 -3.9; 3597 -2.1; 3957 -0.7; 4353 -0.5; 4788 -2.3; 5267 -7.1; 5793 -8.2; 6373 -3.9; 7010 -4.9; 7711 -5.3; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Haka GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Haka ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 137 Hz  | 0.06 | -0.7 dB |
| Peaking | 240 Hz  | 0.38 | -5.6 dB |
| Peaking | 462 Hz  | 0.69 | 1.9 dB  |
| Peaking | 883 Hz  | 1.93 | 2.5 dB  |
| Peaking | 2064 Hz | 0.72 | 4.5 dB  |
| Peaking | 1450 Hz | 4.21 | -0.8 dB |
| Peaking | 2233 Hz | 2.06 | 1.4 dB  |
| Peaking | 2986 Hz | 2.76 | -3.8 dB |
| Peaking | 4227 Hz | 2.31 | 4.4 dB  |
| Peaking | 5488 Hz | 6.54 | -6.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Haka/Jomo%20Haka.png)