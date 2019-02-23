# SoundPeats QY9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.3; 34 -1.7; 37 -2.1; 41 -2.6; 45 -3.0; 49 -3.4; 54 -4.0; 60 -4.8; 66 -5.5; 72 -6.2; 79 -6.9; 87 -7.7; 96 -8.6; 106 -9.5; 116 -10.4; 128 -11.2; 141 -11.8; 155 -12.4; 170 -12.9; 187 -13.4; 206 -13.7; 227 -13.7; 249 -13.5; 274 -13.2; 302 -12.8; 332 -12.3; 365 -11.7; 402 -11.0; 442 -10.1; 486 -9.1; 535 -7.9; 588 -6.7; 647 -5.5; 712 -4.7; 783 -4.4; 861 -4.3; 947 -4.0; 1042 -3.1; 1146 -2.5; 1261 -2.0; 1387 -1.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -1.5; 3270 -2.5; 3597 -3.3; 3957 -4.6; 4353 -6.4; 4788 -7.5; 5267 -8.6; 5793 -9.5; 6373 -9.0; 7010 -6.9; 7711 -6.2; 8482 -7.2; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -7.1; 18182 -7.0; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats QY9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats QY9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.65 | 6.1 dB  |
| Peaking | 55 Hz    | 1.1  | 1.6 dB  |
| Peaking | 229 Hz   | 0.55 | -8.1 dB |
| Peaking | 2065 Hz  | 0.39 | 7.0 dB  |
| Peaking | 5436 Hz  | 1.42 | -6.3 dB |
| Peaking | 446 Hz   | 2.57 | -0.8 dB |
| Peaking | 716 Hz   | 1.82 | 1.6 dB  |
| Peaking | 910 Hz   | 2.28 | -1.3 dB |
| Peaking | 7362 Hz  | 9.41 | 1.5 dB  |
| Peaking | 18523 Hz | 0.18 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -7.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SoundPeats%20QY9/SoundPeats%20QY9.png)