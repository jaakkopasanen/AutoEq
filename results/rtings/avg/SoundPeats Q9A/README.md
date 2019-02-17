# SoundPeats Q9A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.2; 25 -8.2; 28 -8.2; 31 -8.2; 34 -8.2; 37 -8.3; 41 -8.3; 45 -8.3; 49 -8.3; 54 -8.5; 60 -8.9; 66 -9.3; 72 -9.6; 79 -9.9; 87 -10.3; 96 -10.8; 106 -11.3; 116 -11.8; 128 -12.3; 141 -12.8; 155 -13.1; 170 -13.1; 187 -13.0; 206 -12.9; 227 -12.5; 249 -12.0; 274 -11.4; 302 -10.8; 332 -10.1; 365 -9.4; 402 -8.6; 442 -7.8; 486 -6.9; 535 -5.9; 588 -4.9; 647 -4.0; 712 -3.4; 783 -3.1; 861 -2.8; 947 -2.6; 1042 -2.9; 1146 -3.3; 1261 -3.9; 1387 -5.1; 1526 -6.8; 1678 -8.6; 1846 -9.8; 2031 -9.7; 2234 -7.6; 2457 -4.8; 2703 -2.3; 2973 -0.9; 3270 -0.5; 3597 -0.9; 3957 -1.9; 4353 -3.4; 4788 -5.1; 5267 -7.0; 5793 -6.7; 6373 -5.0; 7010 -4.0; 7711 -5.7; 8482 -5.9; 9330 -2.9; 10263 -2.7; 11289 -2.7; 12418 -2.7; 13660 -2.7; 15026 -2.7; 16529 -2.7; 18182 -2.7; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats Q9A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats Q9A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.13 | -5.1 dB |
| Peaking | 201 Hz   | 0.69 | -7.8 dB |
| Peaking | 1882 Hz  | 3.6  | -7.9 dB |
| Peaking | 5633 Hz  | 3.73 | -4.6 dB |
| Peaking | 21279 Hz | 2.18 | -1.0 dB |
| Peaking | 878 Hz   | 2.23 | 1.7 dB  |
| Peaking | 1547 Hz  | 6.61 | -1.7 dB |
| Peaking | 2225 Hz  | 6.9  | -2.4 dB |
| Peaking | 3202 Hz  | 2.73 | 3.3 dB  |
| Peaking | 8122 Hz  | 6.13 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -8.0 dB |
| Peaking | 250 Hz   | 1.41 | -8.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SoundPeats%20Q9A/SoundPeats%20Q9A.png)