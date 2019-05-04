# SoundPeats QY8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.1; 23 -13.0; 25 -12.9; 28 -12.7; 31 -12.5; 34 -12.3; 37 -12.0; 41 -11.7; 45 -11.4; 49 -11.2; 54 -10.9; 60 -10.5; 66 -10.3; 72 -10.0; 79 -9.8; 87 -9.5; 96 -9.3; 106 -8.9; 116 -8.6; 128 -8.7; 141 -8.9; 155 -8.9; 170 -8.5; 187 -7.9; 206 -7.3; 227 -6.7; 249 -6.2; 274 -5.7; 302 -5.1; 332 -4.6; 365 -4.1; 402 -3.6; 442 -3.0; 486 -2.5; 535 -1.9; 588 -1.3; 647 -0.6; 712 -0.5; 783 -0.6; 861 -1.0; 947 -1.7; 1042 -2.6; 1146 -3.7; 1261 -4.2; 1387 -4.7; 1526 -5.2; 1678 -5.9; 1846 -7.5; 2031 -9.4; 2234 -10.1; 2457 -9.8; 2703 -8.8; 2973 -7.4; 3270 -7.0; 3597 -7.8; 3957 -9.8; 4353 -12.6; 4788 -12.9; 5267 -8.9; 5793 -4.8; 6373 -3.0; 7010 -5.2; 7711 -8.6; 8482 -6.9; 9330 -6.0; 10263 -6.4; 11289 -7.8; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats QY8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats QY8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.21 | -7.1 dB |
| Peaking | 161 Hz   | 1.77 | -1.8 dB |
| Peaking | 705 Hz   | 0.89 | 5.7 dB  |
| Peaking | 2247 Hz  | 2.47 | -5.1 dB |
| Peaking | 4535 Hz  | 4.9  | -8.1 dB |
| Peaking | 546 Hz   | 5.52 | -0.2 dB |
| Peaking | 5098 Hz  | 6.76 | -2.4 dB |
| Peaking | 6358 Hz  | 3.43 | 4.3 dB  |
| Peaking | 7764 Hz  | 5.96 | -3.8 dB |
| Peaking | 11062 Hz | 7.84 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | -3.8 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SoundPeats%20QY8/SoundPeats%20QY8.png)