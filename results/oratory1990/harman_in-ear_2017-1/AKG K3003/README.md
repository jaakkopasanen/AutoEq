# AKG K3003
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.3; 25 -10.4; 28 -10.4; 31 -10.4; 34 -10.3; 37 -10.3; 41 -10.4; 45 -10.6; 49 -10.8; 54 -10.9; 60 -11.1; 66 -11.3; 72 -11.5; 79 -11.9; 87 -12.2; 96 -12.5; 106 -12.8; 116 -13.0; 128 -13.2; 141 -13.3; 155 -13.4; 170 -13.4; 187 -13.4; 206 -13.2; 227 -13.0; 249 -12.8; 274 -12.5; 302 -12.0; 332 -11.5; 365 -11.0; 402 -10.5; 442 -10.1; 486 -9.5; 535 -9.0; 588 -8.5; 647 -7.9; 712 -7.4; 783 -6.9; 861 -6.6; 947 -6.5; 1042 -6.5; 1146 -6.5; 1261 -6.3; 1387 -6.0; 1526 -5.5; 1678 -4.9; 1846 -4.4; 2031 -3.7; 2234 -2.7; 2457 -1.4; 2703 -0.5; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -4.6; 5267 -6.3; 5793 -7.3; 6373 -6.3; 7010 -6.9; 7711 -8.4; 8482 -7.7; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -16.5; 15026 -26.3; 16529 -24.2; 18182 -15.4; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.16 | -3.5 dB  |
| Peaking | 131 Hz   | 0.76 | -3.3 dB  |
| Peaking | 273 Hz   | 0.74 | -4.1 dB  |
| Peaking | 3188 Hz  | 1.19 | 6.9 dB   |
| Peaking | 15903 Hz | 1.85 | -22.5 dB |
| Peaking | 4379 Hz  | 5.37 | 4.1 dB   |
| Peaking | 5078 Hz  | 2.46 | -3.1 dB  |
| Peaking | 7757 Hz  | 5.95 | -1.8 dB  |
| Peaking | 12361 Hz | 1.83 | 7.1 dB   |
| Peaking | 14256 Hz | 3.23 | -8.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -5.6 dB  |
| Peaking | 250 Hz   | 1.41 | -5.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 16000 Hz | 1.41 | -20.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/AKG%20K3003/AKG%20K3003.png)