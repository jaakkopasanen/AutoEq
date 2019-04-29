# Astell & Kern Rosie 2 o’clock
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.2; 25 -6.5; 28 -6.8; 31 -7.1; 34 -7.4; 37 -7.7; 41 -8.0; 45 -8.2; 49 -8.4; 54 -8.6; 60 -9.0; 66 -9.3; 72 -9.6; 79 -10.0; 87 -10.3; 96 -10.7; 106 -11.0; 116 -11.2; 128 -11.4; 141 -11.6; 155 -11.7; 170 -11.7; 187 -11.6; 206 -11.4; 227 -11.2; 249 -11.0; 274 -10.6; 302 -10.3; 332 -10.0; 365 -9.5; 402 -9.1; 442 -8.6; 486 -8.1; 535 -7.6; 588 -7.0; 647 -6.4; 712 -5.7; 783 -4.9; 861 -4.3; 947 -3.9; 1042 -3.9; 1146 -4.4; 1261 -5.5; 1387 -6.0; 1526 -5.7; 1678 -5.1; 1846 -4.6; 2031 -4.2; 2234 -3.5; 2457 -2.9; 2703 -2.3; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -1.8; 4353 -0.6; 4788 -1.1; 5267 -4.1; 5793 -2.3; 6373 -0.9; 7010 -5.7; 7711 -12.2; 8482 -12.8; 9330 -8.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.8; 20000 -16.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astell & Kern Rosie 2 o’clock GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astell & Kern Rosie 2 o’clock ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 164 Hz  | 0.45 | -5.3 dB |
| Peaking | 897 Hz  | 1.98 | 3.1 dB  |
| Peaking | 3590 Hz | 1.09 | 6.3 dB  |
| Peaking | 6401 Hz | 5.34 | 5.7 dB  |
| Peaking | 8059 Hz | 3.75 | -9.1 dB |
| Peaking | 19 Hz   | 1.65 | 0.9 dB  |
| Peaking | 1101 Hz | 6.51 | 0.7 dB  |
| Peaking | 1391 Hz | 4.56 | -0.9 dB |
| Peaking | 4687 Hz | 9.48 | 1.8 dB  |
| Peaking | 5292 Hz | 8.44 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Astell%20&%20Kern%20Rosie%202%20o%E2%80%99clock/Astell%20&%20Kern%20Rosie%202%20o%E2%80%99clock.png)