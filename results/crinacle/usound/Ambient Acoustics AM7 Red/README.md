# Ambient Acoustics AM7 Red
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.8; 25 -8.1; 28 -8.5; 31 -8.8; 34 -9.0; 37 -9.2; 41 -9.4; 45 -9.5; 49 -9.7; 54 -9.9; 60 -10.1; 66 -10.2; 72 -10.4; 79 -10.6; 87 -10.9; 96 -11.0; 106 -11.3; 116 -11.4; 128 -11.5; 141 -11.5; 155 -11.5; 170 -11.4; 187 -11.3; 206 -11.1; 227 -10.8; 249 -10.4; 274 -10.0; 302 -9.6; 332 -9.2; 365 -8.7; 402 -8.1; 442 -7.5; 486 -6.9; 535 -6.3; 588 -5.6; 647 -4.9; 712 -4.2; 783 -3.5; 861 -2.9; 947 -2.5; 1042 -2.6; 1146 -3.1; 1261 -3.9; 1387 -4.8; 1526 -5.8; 1678 -7.3; 1846 -10.4; 2031 -11.9; 2234 -9.0; 2457 -6.0; 2703 -4.7; 2973 -5.7; 3270 -8.4; 3597 -4.0; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.5; 5793 -3.0; 6373 -4.8; 7010 -8.8; 7711 -10.4; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.4; 18182 -16.3; 20000 -16.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ambient Acoustics AM7 Red GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ambient Acoustics AM7 Red ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 0.49 | -2.0 dB  |
| Peaking | 173 Hz   | 0.51 | -4.5 dB  |
| Peaking | 938 Hz   | 1.12 | 4.7 dB   |
| Peaking | 1973 Hz  | 4.46 | -7.0 dB  |
| Peaking | 4482 Hz  | 2.98 | 7.0 dB   |
| Peaking | 3309 Hz  | 6.58 | -8.7 dB  |
| Peaking | 3386 Hz  | 2.48 | 5.5 dB   |
| Peaking | 5928 Hz  | 9.98 | 3.7 dB   |
| Peaking | 15188 Hz | 0.66 | 13.4 dB  |
| Peaking | 18654 Hz | 0.24 | -15.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ambient%20Acoustics%20AM7%20Red/Ambient%20Acoustics%20AM7%20Red.png)