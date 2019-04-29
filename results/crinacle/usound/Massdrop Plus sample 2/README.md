# Massdrop Plus sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.0; 25 -5.3; 28 -5.6; 31 -5.9; 34 -6.1; 37 -6.2; 41 -6.4; 45 -6.7; 49 -6.9; 54 -7.1; 60 -7.4; 66 -7.6; 72 -7.9; 79 -8.2; 87 -8.6; 96 -8.9; 106 -9.3; 116 -9.6; 128 -9.8; 141 -10.0; 155 -10.0; 170 -10.1; 187 -10.1; 206 -10.1; 227 -9.9; 249 -9.6; 274 -9.4; 302 -9.2; 332 -8.8; 365 -8.4; 402 -8.0; 442 -7.7; 486 -7.2; 535 -6.8; 588 -6.4; 647 -5.9; 712 -5.3; 783 -4.8; 861 -4.4; 947 -4.3; 1042 -4.6; 1146 -5.5; 1261 -6.5; 1387 -7.3; 1526 -7.8; 1678 -7.8; 1846 -7.9; 2031 -7.8; 2234 -7.6; 2457 -7.1; 2703 -6.2; 2973 -5.3; 3270 -4.5; 3597 -3.8; 3957 -3.2; 4353 -2.7; 4788 -1.8; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.5; 8482 -8.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop Plus sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop Plus sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.56 | 2.4 dB  |
| Peaking | 176 Hz  | 0.52 | -3.9 dB |
| Peaking | 914 Hz  | 1.32 | 3.2 dB  |
| Peaking | 1652 Hz | 1.52 | -2.6 dB |
| Peaking | 5273 Hz | 1.89 | 6.4 dB  |
| Peaking | 2372 Hz | 3.76 | -0.9 dB |
| Peaking | 3666 Hz | 1.66 | 1.5 dB  |
| Peaking | 4885 Hz | 2.57 | -1.6 dB |
| Peaking | 6380 Hz | 4.74 | 2.4 dB  |
| Peaking | 8257 Hz | 4.28 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Massdrop%20Plus%20sample%202/Massdrop%20Plus%20sample%202.png)