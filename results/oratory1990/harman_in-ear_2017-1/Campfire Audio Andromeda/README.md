# Campfire Audio Andromeda
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.2; 25 -5.5; 28 -5.9; 31 -6.2; 34 -6.5; 37 -6.7; 41 -6.9; 45 -7.2; 49 -7.4; 54 -7.7; 60 -8.0; 66 -8.4; 72 -8.7; 79 -9.1; 87 -9.5; 96 -9.9; 106 -10.2; 116 -10.5; 128 -10.8; 141 -11.0; 155 -11.1; 170 -11.2; 187 -11.1; 206 -11.1; 227 -11.0; 249 -10.9; 274 -11.0; 302 -11.0; 332 -10.6; 365 -10.3; 402 -9.9; 442 -9.6; 486 -9.2; 535 -8.8; 588 -8.3; 647 -7.8; 712 -7.4; 783 -6.9; 861 -6.6; 947 -6.5; 1042 -6.6; 1146 -6.6; 1261 -6.7; 1387 -6.5; 1526 -6.3; 1678 -5.9; 1846 -5.0; 2031 -3.7; 2234 -1.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -2.9; 4788 -2.7; 5267 -1.9; 5793 -3.9; 6373 -4.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.5; 15026 -24.5; 16529 -24.2; 18182 -18.0; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Andromeda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Andromeda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.49 | 2.4 dB   |
| Peaking | 168 Hz   | 0.69 | -1.3 dB  |
| Peaking | 221 Hz   | 0.31 | -3.6 dB  |
| Peaking | 3799 Hz  | 0.56 | 6.0 dB   |
| Peaking | 16293 Hz | 1.33 | -20.8 dB |
| Peaking | 1625 Hz  | 1.44 | -5.4 dB  |
| Peaking | 1922 Hz  | 0.69 | 3.9 dB   |
| Peaking | 4450 Hz  | 4.76 | -2.1 dB  |
| Peaking | 11926 Hz | 2.64 | 7.1 dB   |
| Peaking | 19784 Hz | 0.09 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB   |
| Peaking | 62 Hz    | 1.41 | -1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 16000 Hz | 1.41 | -20.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Campfire%20Audio%20Andromeda/Campfire%20Audio%20Andromeda.png)