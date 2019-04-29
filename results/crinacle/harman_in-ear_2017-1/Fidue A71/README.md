# Fidue A71
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.7; 23 -17.7; 25 -17.7; 28 -17.7; 31 -17.7; 34 -17.6; 37 -17.6; 41 -17.5; 45 -17.4; 49 -17.4; 54 -17.3; 60 -17.2; 66 -17.1; 72 -17.1; 79 -17.1; 87 -17.0; 96 -17.0; 106 -16.9; 116 -16.7; 128 -16.6; 141 -16.4; 155 -16.0; 170 -15.6; 187 -15.2; 206 -14.7; 227 -14.1; 249 -13.6; 274 -13.0; 302 -12.3; 332 -11.5; 365 -10.7; 402 -10.0; 442 -9.5; 486 -8.8; 535 -8.1; 588 -7.6; 647 -7.1; 712 -6.5; 783 -6.0; 861 -5.6; 947 -5.5; 1042 -5.6; 1146 -6.0; 1261 -6.4; 1387 -6.6; 1526 -6.6; 1678 -6.6; 1846 -6.4; 2031 -5.9; 2234 -5.2; 2457 -4.3; 2703 -2.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -5.1; 7711 -6.9; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.1; 15026 -18.0; 16529 -19.5; 18182 -17.2; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A71 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A71 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 47 Hz    | 0.18 | -11.5 dB |
| Peaking | 3486 Hz  | 1.47 | 6.2 dB   |
| Peaking | 5717 Hz  | 2.12 | 6.0 dB   |
| Peaking | 12468 Hz | 1.4  | 9.8 dB   |
| Peaking | 15954 Hz | 0.67 | -16.6 dB |
| Peaking | 214 Hz   | 1.31 | -1.1 dB  |
| Peaking | 860 Hz   | 1.06 | 2.2 dB   |
| Peaking | 1661 Hz  | 1.66 | -1.5 dB  |
| Peaking | 16184 Hz | 5.98 | 0.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.6 dB |
| Peaking | 62 Hz    | 1.41 | -7.4 dB  |
| Peaking | 125 Hz   | 1.41 | -8.2 dB  |
| Peaking | 250 Hz   | 1.41 | -5.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -14.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Fidue%20A71/Fidue%20A71.png)