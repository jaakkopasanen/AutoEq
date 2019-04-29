# Jomo Flamenco sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -3.3; 25 -3.8; 28 -4.5; 31 -4.9; 34 -5.3; 37 -5.6; 41 -5.9; 45 -6.3; 49 -6.6; 54 -7.0; 60 -7.3; 66 -7.7; 72 -8.1; 79 -8.5; 87 -8.9; 96 -9.4; 106 -9.8; 116 -10.2; 128 -10.5; 141 -10.7; 155 -10.8; 170 -11.0; 187 -11.1; 206 -11.2; 227 -11.1; 249 -10.9; 274 -10.8; 302 -10.6; 332 -10.3; 365 -9.9; 402 -9.6; 442 -9.1; 486 -8.6; 535 -8.1; 588 -7.4; 647 -6.7; 712 -5.8; 783 -4.9; 861 -4.0; 947 -3.4; 1042 -3.3; 1146 -3.7; 1261 -4.2; 1387 -4.6; 1526 -4.6; 1678 -4.6; 1846 -4.7; 2031 -5.2; 2234 -5.4; 2457 -4.8; 2703 -3.6; 2973 -3.1; 3270 -3.5; 3597 -4.1; 3957 -2.5; 4353 -0.5; 4788 -0.9; 5267 -5.2; 5793 -4.9; 6373 -3.2; 7010 -4.8; 7711 -6.0; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Flamenco sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Flamenco sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.51 | 5.5 dB  |
| Peaking | 207 Hz  | 0.42 | -4.9 dB |
| Peaking | 972 Hz  | 1.36 | 4.0 dB  |
| Peaking | 3496 Hz | 0.84 | 2.4 dB  |
| Peaking | 4490 Hz | 4.98 | 4.3 dB  |
| Peaking | 2278 Hz | 7.02 | -0.9 dB |
| Peaking | 2906 Hz | 7.6  | 1.0 dB  |
| Peaking | 5535 Hz | 8.29 | -3.2 dB |
| Peaking | 6221 Hz | 2.86 | 3.3 dB  |
| Peaking | 7399 Hz | 1.24 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Flamenco%20sample%202/Jomo%20Flamenco%20sample%202.png)