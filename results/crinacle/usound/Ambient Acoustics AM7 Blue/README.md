# Ambient Acoustics AM7 Blue
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.5; 25 -4.9; 28 -5.4; 31 -5.8; 34 -6.1; 37 -6.3; 41 -6.6; 45 -6.8; 49 -7.0; 54 -7.3; 60 -7.5; 66 -7.8; 72 -8.0; 79 -8.3; 87 -8.7; 96 -9.0; 106 -9.3; 116 -9.6; 128 -9.8; 141 -10.0; 155 -10.0; 170 -10.0; 187 -10.0; 206 -9.9; 227 -9.8; 249 -9.5; 274 -9.2; 302 -8.9; 332 -8.5; 365 -8.1; 402 -7.6; 442 -7.1; 486 -6.5; 535 -5.9; 588 -5.3; 647 -4.6; 712 -3.9; 783 -3.3; 861 -2.9; 947 -2.9; 1042 -3.3; 1146 -4.3; 1261 -5.4; 1387 -6.3; 1526 -7.1; 1678 -8.5; 1846 -11.3; 2031 -12.6; 2234 -9.7; 2457 -6.6; 2703 -5.3; 2973 -6.3; 3270 -9.1; 3597 -4.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -3.3; 5793 -3.6; 6373 -5.6; 7010 -9.8; 7711 -11.3; 8482 -7.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.9; 18182 -18.8; 20000 -14.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ambient Acoustics AM7 Blue GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ambient Acoustics AM7 Blue ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 909 Hz   | 2.33 | 4.3 dB   |
| Peaking | 1977 Hz  | 4.15 | -7.1 dB  |
| Peaking | 4536 Hz  | 2.56 | 7.0 dB   |
| Peaking | 7519 Hz  | 5.57 | -5.9 dB  |
| Peaking | 18811 Hz | 1.5  | -14.6 dB |
| Peaking | 19 Hz    | 1.48 | 2.7 dB   |
| Peaking | 130 Hz   | 0.85 | -3.1 dB  |
| Peaking | 246 Hz   | 1.55 | -2.0 dB  |
| Peaking | 13123 Hz | 1.96 | 1.1 dB   |
| Peaking | 15611 Hz | 5.04 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -3.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ambient%20Acoustics%20AM7%20Blue/Ambient%20Acoustics%20AM7%20Blue.png)