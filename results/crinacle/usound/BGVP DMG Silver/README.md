# BGVP DMG Silver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.6; 25 -6.9; 28 -7.2; 31 -7.5; 34 -7.7; 37 -7.9; 41 -8.1; 45 -8.3; 49 -8.4; 54 -8.5; 60 -8.7; 66 -8.9; 72 -9.2; 79 -9.4; 87 -9.6; 96 -9.8; 106 -10.0; 116 -10.1; 128 -10.1; 141 -10.1; 155 -10.1; 170 -9.9; 187 -9.6; 206 -9.3; 227 -8.9; 249 -8.5; 274 -8.0; 302 -7.5; 332 -7.0; 365 -6.4; 402 -5.9; 442 -5.3; 486 -4.7; 535 -4.1; 588 -3.5; 647 -2.9; 712 -2.2; 783 -1.4; 861 -0.9; 947 -0.5; 1042 -0.5; 1146 -0.9; 1261 -1.4; 1387 -1.9; 1526 -2.2; 1678 -2.4; 1846 -2.7; 2031 -3.1; 2234 -3.5; 2457 -4.0; 2703 -5.0; 2973 -5.0; 3270 -3.5; 3597 -4.1; 3957 -4.2; 4353 -3.9; 4788 -4.5; 5267 -5.2; 5793 -6.0; 6373 -4.7; 7010 -4.2; 7711 -7.1; 8482 -8.2; 9330 -6.9; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DMG Silver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DMG Silver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.49 | -1.9 dB |
| Peaking | 157 Hz  | 0.54 | -4.4 dB |
| Peaking | 980 Hz  | 0.84 | 5.0 dB  |
| Peaking | 5652 Hz | 0.55 | 0.5 dB  |
| Peaking | 8480 Hz | 4.34 | -3.8 dB |
| Peaking | 1913 Hz | 4.95 | 0.3 dB  |
| Peaking | 2853 Hz | 5.37 | -2.4 dB |
| Peaking | 3145 Hz | 2.43 | 1.3 dB  |
| Peaking | 5907 Hz | 4.59 | -1.6 dB |
| Peaking | 6705 Hz | 8.73 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/BGVP%20DMG%20Silver/BGVP%20DMG%20Silver.png)