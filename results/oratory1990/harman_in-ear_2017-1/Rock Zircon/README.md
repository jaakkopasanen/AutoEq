# Rock Zircon
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.4; 25 -3.7; 28 -4.0; 31 -4.2; 34 -4.5; 37 -4.7; 41 -4.9; 45 -5.2; 49 -5.4; 54 -5.7; 60 -6.1; 66 -6.4; 72 -6.8; 79 -7.2; 87 -7.6; 96 -8.0; 106 -8.4; 116 -8.7; 128 -8.8; 141 -8.8; 155 -8.5; 170 -7.2; 187 -8.6; 206 -8.7; 227 -8.0; 249 -7.3; 274 -6.5; 302 -5.6; 332 -4.7; 365 -3.9; 402 -3.2; 442 -2.5; 486 -1.9; 535 -1.4; 588 -1.0; 647 -0.7; 712 -0.5; 783 -0.5; 861 -0.7; 947 -1.2; 1042 -1.9; 1146 -2.7; 1261 -3.3; 1387 -3.9; 1526 -4.3; 1678 -4.7; 1846 -4.6; 2031 -4.1; 2234 -3.6; 2457 -3.9; 2703 -4.1; 2973 -4.9; 3270 -4.6; 3597 -4.0; 3957 -3.6; 4353 -4.2; 4788 -6.1; 5267 -9.7; 5793 -13.4; 6373 -10.7; 7010 -9.3; 7711 -9.8; 8482 -7.8; 9330 -5.2; 10263 -5.2; 11289 -5.2; 12418 -6.8; 13660 -19.1; 15026 -28.8; 16529 -31.2; 18182 -27.6; 20000 -18.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rock Zircon GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rock Zircon ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 114 Hz   | 1.36 | -3.1 dB  |
| Peaking | 226 Hz   | 1.21 | -3.7 dB  |
| Peaking | 654 Hz   | 0.61 | 4.9 dB   |
| Peaking | 5835 Hz  | 6.55 | -7.1 dB  |
| Peaking | 17122 Hz | 1.19 | -28.9 dB |
| Peaking | 22 Hz    | 1.39 | 2.2 dB   |
| Peaking | 1515 Hz  | 3.54 | -1.2 dB  |
| Peaking | 3961 Hz  | 4.39 | 2.6 dB   |
| Peaking | 11835 Hz | 2.03 | 11.4 dB  |
| Peaking | 14799 Hz | 2    | -12.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB   |
| Peaking | 62 Hz    | 1.41 | -0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 4.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 16000 Hz | 1.41 | -30.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Rock%20Zircon/Rock%20Zircon.png)