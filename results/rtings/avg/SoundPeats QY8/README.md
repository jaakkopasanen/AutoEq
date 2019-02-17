# SoundPeats QY8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.3; 25 -8.2; 28 -8.0; 31 -7.8; 34 -7.5; 37 -7.3; 41 -7.0; 45 -6.7; 49 -6.4; 54 -6.2; 60 -6.2; 66 -6.1; 72 -6.1; 79 -6.1; 87 -6.2; 96 -6.2; 106 -6.4; 116 -6.5; 128 -7.1; 141 -7.8; 155 -8.1; 170 -7.9; 187 -7.4; 206 -7.0; 227 -6.5; 249 -6.0; 274 -5.5; 302 -5.0; 332 -4.5; 365 -4.0; 402 -3.5; 442 -3.0; 486 -2.5; 535 -1.9; 588 -1.4; 647 -0.7; 712 -0.5; 783 -0.6; 861 -0.9; 947 -1.7; 1042 -2.7; 1146 -3.6; 1261 -4.2; 1387 -4.7; 1526 -5.1; 1678 -5.9; 1846 -7.4; 2031 -9.2; 2234 -9.4; 2457 -9.1; 2703 -8.4; 2973 -7.5; 3270 -7.3; 3597 -8.2; 3957 -10.2; 4353 -13.1; 4788 -12.8; 5267 -8.7; 5793 -5.0; 6373 -4.1; 7010 -5.2; 7711 -8.0; 8482 -7.4; 9330 -5.8; 10263 -6.7; 11289 -7.0; 12418 -4.8; 13660 -3.5; 15026 -3.3; 16529 -2.6; 18182 -2.2; 20000 -2.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats QY8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats QY8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 13 Hz   | 0.2  | -6.3 dB  |
| Peaking | 170 Hz  | 1.12 | -5.1 dB  |
| Peaking | 2253 Hz | 1.8  | -7.0 dB  |
| Peaking | 4472 Hz | 3.18 | -10.4 dB |
| Peaking | 9805 Hz | 1.18 | -4.5 dB  |
| Peaking | 329 Hz  | 1.89 | -1.0 dB  |
| Peaking | 768 Hz  | 1.41 | 3.0 dB   |
| Peaking | 1203 Hz | 1.55 | -1.4 dB  |
| Peaking | 6269 Hz | 5.9  | 2.2 dB   |
| Peaking | 7833 Hz | 8.33 | -2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | -7.1 dB |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SoundPeats%20QY8/SoundPeats%20QY8.png)