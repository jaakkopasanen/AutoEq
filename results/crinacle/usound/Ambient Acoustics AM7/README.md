# Ambient Acoustics AM7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.8; 28 -1.2; 31 -1.7; 34 -2.1; 37 -2.4; 41 -2.7; 45 -3.1; 49 -3.4; 54 -3.8; 60 -4.1; 66 -4.5; 72 -4.9; 79 -5.3; 87 -5.8; 96 -6.2; 106 -6.7; 116 -7.1; 128 -7.4; 141 -7.7; 155 -7.9; 170 -8.0; 187 -8.2; 206 -8.2; 227 -8.2; 249 -8.1; 274 -7.9; 302 -7.8; 332 -7.6; 365 -7.3; 402 -7.0; 442 -6.7; 486 -6.3; 535 -5.9; 588 -5.5; 647 -5.1; 712 -4.6; 783 -4.1; 861 -3.8; 947 -3.7; 1042 -4.1; 1146 -4.9; 1261 -6.0; 1387 -7.0; 1526 -7.9; 1678 -9.3; 1846 -12.3; 2031 -13.7; 2234 -10.6; 2457 -7.5; 2703 -6.1; 2973 -6.9; 3270 -9.2; 3597 -5.1; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -4.3; 5793 -5.0; 6373 -7.3; 7010 -11.4; 7711 -12.6; 8482 -8.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -13.2; 20000 -18.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ambient Acoustics AM7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ambient Acoustics AM7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.91 | 6.0 dB  |
| Peaking | 912 Hz  | 2.18 | 3.4 dB  |
| Peaking | 1976 Hz | 3.52 | -7.8 dB |
| Peaking | 4434 Hz | 3.24 | 7.3 dB  |
| Peaking | 7455 Hz | 4.67 | -7.3 dB |
| Peaking | 61 Hz   | 1.67 | 1.2 dB  |
| Peaking | 195 Hz  | 0.94 | -2.1 dB |
| Peaking | 2736 Hz | 4.74 | 2.0 dB  |
| Peaking | 3325 Hz | 5.09 | -4.6 dB |
| Peaking | 3821 Hz | 9.02 | 3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ambient%20Acoustics%20AM7/Ambient%20Acoustics%20AM7.png)