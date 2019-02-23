# SoundPeats Q9A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -7.8; 25 -7.9; 28 -7.9; 31 -7.9; 34 -7.9; 37 -7.9; 41 -7.9; 45 -7.9; 49 -8.0; 54 -8.1; 60 -8.5; 66 -8.9; 72 -9.2; 79 -9.6; 87 -10.0; 96 -10.4; 106 -10.9; 116 -11.4; 128 -11.9; 141 -12.4; 155 -12.7; 170 -12.7; 187 -12.7; 206 -12.5; 227 -12.2; 249 -11.6; 274 -11.1; 302 -10.4; 332 -9.7; 365 -9.0; 402 -8.3; 442 -7.4; 486 -6.5; 535 -5.6; 588 -4.6; 647 -3.7; 712 -3.1; 783 -2.7; 861 -2.5; 947 -2.3; 1042 -2.5; 1146 -3.0; 1261 -3.6; 1387 -4.7; 1526 -6.4; 1678 -8.3; 1846 -9.4; 2031 -9.3; 2234 -7.2; 2457 -4.5; 2703 -2.0; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -1.5; 4353 -3.0; 4788 -4.7; 5267 -6.7; 5793 -6.4; 6373 -4.6; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats Q9A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats Q9A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 188 Hz  | 0.52 | -6.7 dB |
| Peaking | 885 Hz  | 0.73 | 5.6 dB  |
| Peaking | 1905 Hz | 2.22 | -6.8 dB |
| Peaking | 3198 Hz | 1.83 | 7.0 dB  |
| Peaking | 6843 Hz | 9.75 | 2.1 dB  |
| Peaking | 24 Hz   | 1.48 | -1.1 dB |
| Peaking | 4055 Hz | 6.32 | 1.1 dB  |
| Peaking | 5403 Hz | 8.05 | -2.2 dB |
| Peaking | 8748 Hz | 3.81 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SoundPeats%20Q9A/SoundPeats%20Q9A.png)