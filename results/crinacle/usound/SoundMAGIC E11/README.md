# SoundMAGIC E11
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -4.0; 25 -4.5; 28 -5.0; 31 -5.5; 34 -5.9; 37 -6.2; 41 -6.6; 45 -6.9; 49 -7.1; 54 -7.4; 60 -7.7; 66 -8.0; 72 -8.3; 79 -8.7; 87 -9.0; 96 -9.3; 106 -9.6; 116 -9.7; 128 -9.9; 141 -10.0; 155 -10.0; 170 -10.0; 187 -9.9; 206 -9.8; 227 -9.5; 249 -9.3; 274 -9.0; 302 -8.6; 332 -8.4; 365 -8.4; 402 -8.1; 442 -8.0; 486 -7.8; 535 -7.5; 588 -7.3; 647 -7.1; 712 -6.7; 783 -6.5; 861 -6.3; 947 -6.1; 1042 -6.4; 1146 -7.0; 1261 -7.5; 1387 -7.7; 1526 -7.4; 1678 -6.6; 1846 -5.4; 2031 -4.0; 2234 -2.6; 2457 -1.3; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.7; 5267 -4.0; 5793 -7.0; 6373 -9.0; 7010 -9.0; 7711 -9.3; 8482 -10.2; 9330 -7.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundMAGIC E11 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundMAGIC E11 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 14 Hz   | 0.72 | 4.3 dB   |
| Peaking | 158 Hz  | 0.45 | -3.6 dB  |
| Peaking | 1511 Hz | 1.75 | -4.2 dB  |
| Peaking | 4212 Hz | 0.53 | 10.1 dB  |
| Peaking | 6870 Hz | 1.11 | -10.3 dB |
| Peaking | 2600 Hz | 4.91 | 1.1 dB   |
| Peaking | 4461 Hz | 1.09 | -1.6 dB  |
| Peaking | 4691 Hz | 2.73 | 2.4 dB   |
| Peaking | 5997 Hz | 4.64 | -0.5 dB  |
| Peaking | 7147 Hz | 9.01 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/SoundMAGIC%20E11/SoundMAGIC%20E11.png)