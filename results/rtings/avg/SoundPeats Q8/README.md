# SoundPeats Q8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.2; 23 -14.5; 25 -14.7; 28 -14.9; 31 -15.1; 34 -15.2; 37 -15.2; 41 -15.3; 45 -15.3; 49 -15.2; 54 -15.1; 60 -14.8; 66 -14.5; 72 -14.3; 79 -13.9; 87 -13.6; 96 -13.1; 106 -12.6; 116 -12.0; 128 -11.2; 141 -10.4; 155 -10.0; 170 -9.5; 187 -8.7; 206 -8.0; 227 -7.2; 249 -6.6; 274 -6.0; 302 -5.3; 332 -4.5; 365 -3.8; 402 -3.0; 442 -2.5; 486 -2.1; 535 -1.4; 588 -0.8; 647 -0.5; 712 -0.5; 783 -0.8; 861 -1.3; 947 -1.5; 1042 -1.6; 1146 -1.7; 1261 -1.7; 1387 -1.9; 1526 -1.6; 1678 -1.1; 1846 -0.8; 2031 -0.8; 2234 -1.6; 2457 -3.0; 2703 -4.8; 2973 -6.6; 3270 -6.5; 3597 -4.8; 3957 -2.9; 4353 -1.1; 4788 -1.3; 5267 -2.2; 5793 -2.6; 6373 -2.6; 7010 -7.8; 7711 -13.6; 8482 -9.6; 9330 -4.4; 10263 -4.4; 11289 -4.4; 12418 -7.0; 13660 -12.2; 15026 -16.9; 16529 -18.1; 18182 -17.2; 20000 -14.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats Q8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats Q8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 43 Hz    | 0.22 | -10.8 dB |
| Peaking | 692 Hz   | 0.4  | 4.4 dB   |
| Peaking | 15632 Hz | 1.94 | -8.7 dB  |
| Peaking | 18784 Hz | 0.67 | -12.2 dB |
| Peaking | 2071 Hz  | 3.77 | 2.1 dB   |
| Peaking | 3171 Hz  | 2.65 | -5.3 dB  |
| Peaking | 4999 Hz  | 1.1  | 4.2 dB   |
| Peaking | 7715 Hz  | 4.68 | -11.6 dB |
| Peaking | 10429 Hz | 2.16 | 3.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.9 dB |
| Peaking | 62 Hz    | 1.41 | -8.1 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 3.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -16.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SoundPeats%20Q8/SoundPeats%20Q8.png)