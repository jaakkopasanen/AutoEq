# Shure KSE1500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.7; 25 -7.8; 28 -7.8; 31 -7.9; 34 -7.9; 37 -8.0; 41 -8.1; 45 -8.1; 49 -8.2; 54 -8.3; 60 -8.5; 66 -8.7; 72 -8.8; 79 -9.0; 87 -9.2; 96 -9.3; 106 -9.5; 116 -9.5; 128 -9.5; 141 -9.4; 155 -9.2; 170 -9.0; 187 -8.8; 206 -8.6; 227 -8.4; 249 -8.1; 274 -7.8; 302 -7.3; 332 -6.9; 365 -6.6; 402 -6.4; 442 -6.1; 486 -5.9; 535 -5.7; 588 -5.5; 647 -5.4; 712 -5.3; 783 -5.3; 861 -5.5; 947 -6.1; 1042 -6.8; 1146 -7.6; 1261 -8.1; 1387 -8.6; 1526 -8.8; 1678 -9.0; 1846 -9.0; 2031 -8.3; 2234 -6.5; 2457 -3.9; 2703 -1.4; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -10.0; 9330 -16.6; 10263 -18.5; 11289 -14.7; 12418 -9.9; 13660 -10.7; 15026 -16.7; 16529 -22.3; 18182 -26.4; 20000 -29.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure KSE1500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure KSE1500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 0.49 | -1.6 dB  |
| Peaking | 137 Hz   | 1.02 | -2.5 dB  |
| Peaking | 1761 Hz  | 1.99 | -5.5 dB  |
| Peaking | 4246 Hz  | 0.77 | 9.1 dB   |
| Peaking | 19824 Hz | 0.28 | -22.6 dB |
| Peaking | 2114 Hz  | 5.84 | -0.7 dB  |
| Peaking | 6628 Hz  | 3.08 | 3.5 dB   |
| Peaking | 10028 Hz | 2.77 | -10.5 dB |
| Peaking | 13066 Hz | 2.02 | 8.2 dB   |
| Peaking | 16945 Hz | 1.41 | -2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 10.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -22.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Shure%20KSE1500/Shure%20KSE1500.png)