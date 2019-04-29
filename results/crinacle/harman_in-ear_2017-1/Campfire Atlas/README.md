# Campfire Atlas
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.6; 23 -12.8; 25 -12.9; 28 -13.0; 31 -13.1; 34 -13.1; 37 -13.1; 41 -13.1; 45 -13.1; 49 -13.1; 54 -13.1; 60 -13.2; 66 -13.3; 72 -13.4; 79 -13.5; 87 -13.6; 96 -13.7; 106 -13.9; 116 -13.9; 128 -13.8; 141 -13.7; 155 -13.6; 170 -13.3; 187 -13.0; 206 -12.6; 227 -12.1; 249 -11.6; 274 -11.1; 302 -10.4; 332 -9.7; 365 -9.0; 402 -8.3; 442 -7.7; 486 -7.1; 535 -6.5; 588 -5.8; 647 -5.3; 712 -4.7; 783 -4.1; 861 -3.8; 947 -3.7; 1042 -3.9; 1146 -4.5; 1261 -4.9; 1387 -4.9; 1526 -4.6; 1678 -4.1; 1846 -3.4; 2031 -2.5; 2234 -1.5; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.3; 4353 -2.5; 4788 -4.8; 5267 -8.1; 5793 -7.9; 6373 -3.3; 7010 -4.0; 7711 -6.2; 8482 -8.3; 9330 -8.9; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -9.3; 15026 -17.3; 16529 -21.4; 18182 -19.0; 20000 -14.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Atlas GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Atlas ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.25 | -6.0 dB  |
| Peaking | 163 Hz   | 0.56 | -5.4 dB  |
| Peaking | 798 Hz   | 1.29 | 3.0 dB   |
| Peaking | 2973 Hz  | 1.15 | 6.6 dB   |
| Peaking | 17440 Hz | 1.07 | -16.1 dB |
| Peaking | 4187 Hz  | 2.84 | 2.2 dB   |
| Peaking | 5518 Hz  | 4.19 | -4.6 dB  |
| Peaking | 6617 Hz  | 4.79 | 5.7 dB   |
| Peaking | 12358 Hz | 2.35 | 6.1 dB   |
| Peaking | 19098 Hz | 0.08 | -2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.7 dB  |
| Peaking | 125 Hz   | 1.41 | -6.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 16000 Hz | 1.41 | -15.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Campfire%20Atlas/Campfire%20Atlas.png)