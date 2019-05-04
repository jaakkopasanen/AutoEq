# SoundPeats QY9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.3; 25 -4.7; 28 -5.3; 31 -5.9; 34 -6.3; 37 -6.7; 41 -7.2; 45 -7.7; 49 -8.0; 54 -8.5; 60 -9.0; 66 -9.5; 72 -10.0; 79 -10.5; 87 -11.0; 96 -11.5; 106 -12.0; 116 -12.3; 128 -12.7; 141 -12.9; 155 -13.0; 170 -13.2; 187 -13.5; 206 -13.5; 227 -13.4; 249 -13.2; 274 -12.9; 302 -12.5; 332 -12.0; 365 -11.4; 402 -10.7; 442 -9.9; 486 -8.9; 535 -7.7; 588 -6.5; 647 -5.3; 712 -4.6; 783 -4.3; 861 -4.2; 947 -3.8; 1042 -3.0; 1146 -2.4; 1261 -1.9; 1387 -1.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -1.3; 3270 -2.1; 3597 -2.8; 3957 -4.1; 4353 -5.8; 4788 -7.6; 5267 -8.8; 5793 -9.2; 6373 -7.9; 7010 -6.7; 7711 -6.7; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats QY9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats QY9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.1  | 3.3 dB  |
| Peaking | 127 Hz   | 0.58 | -4.9 dB |
| Peaking | 291 Hz   | 0.82 | -4.8 dB |
| Peaking | 2110 Hz  | 0.43 | 6.8 dB  |
| Peaking | 5405 Hz  | 1.67 | -5.9 dB |
| Peaking | 479 Hz   | 2.72 | -1.0 dB |
| Peaking | 711 Hz   | 1.41 | 1.5 dB  |
| Peaking | 923 Hz   | 2.1  | -1.3 dB |
| Peaking | 11400 Hz | 1.35 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -6.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SoundPeats%20QY9/SoundPeats%20QY9.png)