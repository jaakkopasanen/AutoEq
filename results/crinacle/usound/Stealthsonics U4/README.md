# Stealthsonics U4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -8.9; 25 -9.0; 28 -9.1; 31 -9.2; 34 -9.3; 37 -9.4; 41 -9.6; 45 -9.7; 49 -9.8; 54 -10.0; 60 -10.2; 66 -10.5; 72 -10.8; 79 -11.0; 87 -11.3; 96 -11.8; 106 -12.1; 116 -12.3; 128 -12.5; 141 -12.7; 155 -12.9; 170 -12.8; 187 -12.8; 206 -12.7; 227 -12.4; 249 -12.2; 274 -11.9; 302 -11.5; 332 -11.0; 365 -10.6; 402 -10.1; 442 -9.6; 486 -8.9; 535 -8.2; 588 -7.5; 647 -6.7; 712 -5.8; 783 -4.9; 861 -4.0; 947 -3.4; 1042 -3.2; 1146 -3.4; 1261 -3.8; 1387 -3.8; 1526 -3.7; 1678 -3.6; 1846 -3.6; 2031 -2.9; 2234 -1.7; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.8; 3597 -1.0; 3957 -1.4; 4353 -2.3; 4788 -2.5; 5267 -4.3; 5793 -8.8; 6373 -12.1; 7010 -10.9; 7711 -6.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stealthsonics U4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stealthsonics U4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.12 | -2.0 dB |
| Peaking | 198 Hz   | 0.44 | -5.2 dB |
| Peaking | 936 Hz   | 1.56 | 3.4 dB  |
| Peaking | 3297 Hz  | 0.76 | 6.4 dB  |
| Peaking | 6432 Hz  | 3.66 | -8.9 dB |
| Peaking | 1972 Hz  | 4.7  | -1.0 dB |
| Peaking | 2467 Hz  | 2.25 | 1.3 dB  |
| Peaking | 3221 Hz  | 1.4  | -0.8 dB |
| Peaking | 4933 Hz  | 7.32 | 1.4 dB  |
| Peaking | 11381 Hz | 1.77 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Stealthsonics%20U4/Stealthsonics%20U4.png)