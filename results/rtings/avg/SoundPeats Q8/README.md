# SoundPeats Q8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.8; 25 -10.0; 28 -10.2; 31 -10.3; 34 -10.4; 37 -10.5; 41 -10.5; 45 -10.5; 49 -10.5; 54 -10.5; 60 -10.4; 66 -10.4; 72 -10.4; 79 -10.2; 87 -10.2; 96 -10.1; 106 -10.0; 116 -9.8; 128 -9.5; 141 -9.2; 155 -9.3; 170 -9.0; 187 -8.4; 206 -8.0; 227 -7.3; 249 -6.7; 274 -6.1; 302 -5.4; 332 -4.7; 365 -3.9; 402 -3.1; 442 -2.6; 486 -2.2; 535 -1.5; 588 -0.8; 647 -0.5; 712 -0.5; 783 -0.9; 861 -1.3; 947 -1.5; 1042 -1.7; 1146 -1.6; 1261 -1.7; 1387 -1.8; 1526 -1.5; 1678 -1.0; 1846 -0.6; 2031 -0.5; 2234 -0.9; 2457 -2.3; 2703 -4.4; 2973 -6.7; 3270 -6.8; 3597 -5.1; 3957 -3.3; 4353 -1.6; 4788 -0.9; 5267 -2.0; 5793 -2.8; 6373 -3.9; 7010 -8.0; 7711 -12.9; 8482 -9.9; 9330 -4.3; 10263 -4.3; 11289 -4.3; 12418 -7.1; 13660 -13.5; 15026 -17.6; 16529 -18.3; 18182 -17.4; 20000 -14.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats Q8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats Q8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 43 Hz    | 0.25 | -6.1 dB  |
| Peaking | 209 Hz   | 0.58 | -5.3 dB  |
| Peaking | 465 Hz   | 0.29 | 5.3 dB   |
| Peaking | 15411 Hz | 2.08 | -8.5 dB  |
| Peaking | 18663 Hz | 0.66 | -12.7 dB |
| Peaking | 2180 Hz  | 2.95 | 2.9 dB   |
| Peaking | 3167 Hz  | 2.34 | -5.6 dB  |
| Peaking | 4783 Hz  | 1.49 | 4.3 dB   |
| Peaking | 7791 Hz  | 4.39 | -10.2 dB |
| Peaking | 10515 Hz | 2.37 | 3.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 3.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -17.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SoundPeats%20Q8/SoundPeats%20Q8.png)