# Astell & Kern Rosie Min
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.2; 25 -4.3; 28 -4.6; 31 -4.9; 34 -5.3; 37 -5.6; 41 -6.0; 45 -6.3; 49 -6.6; 54 -7.0; 60 -7.4; 66 -7.8; 72 -8.2; 79 -8.6; 87 -9.0; 96 -9.5; 106 -9.9; 116 -10.1; 128 -10.4; 141 -10.7; 155 -10.9; 170 -10.9; 187 -10.9; 206 -10.8; 227 -10.7; 249 -10.5; 274 -10.2; 302 -10.0; 332 -9.7; 365 -9.3; 402 -8.9; 442 -8.4; 486 -7.9; 535 -7.4; 588 -6.8; 647 -6.2; 712 -5.6; 783 -4.9; 861 -4.3; 947 -3.9; 1042 -4.0; 1146 -4.6; 1261 -5.6; 1387 -6.0; 1526 -5.7; 1678 -5.2; 1846 -4.7; 2031 -4.2; 2234 -3.2; 2457 -2.2; 2703 -1.4; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -3.1; 4353 -1.4; 4788 -2.2; 5267 -5.2; 5793 -3.2; 6373 -1.7; 7010 -6.1; 7711 -12.2; 8482 -14.0; 9330 -11.0; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.8; 20000 -20.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astell & Kern Rosie Min GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astell & Kern Rosie Min ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 190 Hz   | 0.6  | -4.7 dB |
| Peaking | 899 Hz   | 2.27 | 2.9 dB  |
| Peaking | 3270 Hz  | 1.23 | 6.2 dB  |
| Peaking | 6400 Hz  | 5.4  | 5.7 dB  |
| Peaking | 8257 Hz  | 3.42 | -9.4 dB |
| Peaking | 25 Hz    | 1.3  | 2.6 dB  |
| Peaking | 1097 Hz  | 6.78 | 0.8 dB  |
| Peaking | 1399 Hz  | 3.86 | -0.9 dB |
| Peaking | 9304 Hz  | 6.85 | -2.0 dB |
| Peaking | 10190 Hz | 3.52 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Astell%20&%20Kern%20Rosie%20Min/Astell%20&%20Kern%20Rosie%20Min.png)