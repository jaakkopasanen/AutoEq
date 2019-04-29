# Oriveti New Primacy
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -5.0; 25 -5.3; 28 -5.7; 31 -6.0; 34 -6.3; 37 -6.5; 41 -6.7; 45 -7.0; 49 -7.2; 54 -7.4; 60 -7.7; 66 -8.0; 72 -8.3; 79 -8.6; 87 -8.9; 96 -9.3; 106 -9.7; 116 -10.0; 128 -10.2; 141 -10.4; 155 -10.6; 170 -10.7; 187 -10.7; 206 -10.7; 227 -10.8; 249 -10.7; 274 -10.6; 302 -10.4; 332 -10.3; 365 -10.1; 402 -10.0; 442 -9.8; 486 -9.6; 535 -9.4; 588 -9.2; 647 -8.8; 712 -8.3; 783 -7.6; 861 -7.0; 947 -6.4; 1042 -6.1; 1146 -6.1; 1261 -6.3; 1387 -6.2; 1526 -5.8; 1678 -5.5; 1846 -4.9; 2031 -3.6; 2234 -1.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.2; 4788 -4.8; 5267 -4.4; 5793 -2.4; 6373 -2.9; 7010 -8.1; 7711 -9.1; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oriveti New Primacy GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oriveti New Primacy ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.56 | 3.0 dB  |
| Peaking | 215 Hz  | 0.39 | -4.4 dB |
| Peaking | 2417 Hz | 4.15 | 2.7 dB  |
| Peaking | 3470 Hz | 1.02 | 6.0 dB  |
| Peaking | 7502 Hz | 6.98 | -4.8 dB |
| Peaking | 605 Hz  | 2.58 | -0.6 dB |
| Peaking | 979 Hz  | 3.04 | 1.1 dB  |
| Peaking | 1645 Hz | 3.08 | -0.5 dB |
| Peaking | 4940 Hz | 9.55 | -2.9 dB |
| Peaking | 6057 Hz | 7.35 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Oriveti%20New%20Primacy/Oriveti%20New%20Primacy.png)