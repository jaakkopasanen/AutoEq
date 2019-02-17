# SoundPeats QY9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.7; 25 -3.1; 28 -3.7; 31 -4.2; 34 -4.7; 37 -5.1; 41 -5.5; 45 -6.0; 49 -6.4; 54 -6.9; 60 -7.8; 66 -8.5; 72 -9.1; 79 -9.9; 87 -10.7; 96 -11.6; 106 -12.5; 116 -13.3; 128 -14.1; 141 -14.8; 155 -15.3; 170 -15.8; 187 -16.3; 206 -16.6; 227 -16.7; 249 -16.5; 274 -16.1; 302 -15.7; 332 -15.2; 365 -14.6; 402 -13.9; 442 -13.1; 486 -12.1; 535 -10.9; 588 -9.7; 647 -8.4; 712 -7.6; 783 -7.3; 861 -7.3; 947 -6.9; 1042 -6.1; 1146 -5.4; 1261 -4.9; 1387 -4.5; 1526 -3.3; 1678 -2.1; 1846 -0.8; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -1.7; 2973 -4.4; 3270 -5.5; 3597 -6.3; 3957 -7.6; 4353 -9.3; 4788 -10.4; 5267 -11.5; 5793 -12.4; 6373 -12.0; 7010 -9.9; 7711 -9.2; 8482 -10.2; 9330 -8.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -9.4; 16529 -10.1; 18182 -10.0; 20000 -9.7
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

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.48 | 4.8 dB   |
| Peaking | 216 Hz   | 0.53 | -10.7 dB |
| Peaking | 2136 Hz  | 1.04 | 7.4 dB   |
| Peaking | 5536 Hz  | 1.3  | -6.7 dB  |
| Peaking | 18315 Hz | 0.84 | -4.1 dB  |
| Peaking | 418 Hz   | 2.76 | -1.0 dB  |
| Peaking | 692 Hz   | 3.08 | 1.4 dB   |
| Peaking | 1421 Hz  | 6.01 | -0.7 dB  |
| Peaking | 8831 Hz  | 6.12 | -2.8 dB  |
| Peaking | 10599 Hz | 1.83 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -9.8 dB |
| Peaking | 500 Hz   | 1.41 | -3.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -3.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SoundPeats%20QY9/SoundPeats%20QY9.png)