# Fidue A91 Sirius custom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.9; 34 -1.4; 37 -1.9; 41 -2.6; 45 -3.1; 49 -3.6; 54 -4.0; 60 -4.4; 66 -4.8; 72 -5.2; 79 -5.7; 87 -6.1; 96 -6.5; 106 -7.0; 116 -7.4; 128 -7.7; 141 -8.0; 155 -8.1; 170 -8.4; 187 -8.5; 206 -8.8; 227 -8.8; 249 -8.7; 274 -8.8; 302 -8.8; 332 -8.6; 365 -8.4; 402 -8.3; 442 -8.2; 486 -8.1; 535 -8.0; 588 -7.8; 647 -7.7; 712 -7.6; 783 -7.5; 861 -7.5; 947 -7.8; 1042 -8.6; 1146 -9.8; 1261 -10.8; 1387 -11.1; 1526 -10.6; 1678 -9.4; 1846 -7.9; 2031 -6.2; 2234 -4.6; 2457 -3.6; 2703 -3.2; 2973 -3.4; 3270 -3.7; 3597 -3.5; 3957 -3.6; 4353 -4.1; 4788 -3.4; 5267 -1.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.6; 10263 -7.1; 11289 -6.5; 12418 -7.3; 13660 -14.8; 15026 -21.0; 16529 -21.4; 18182 -18.1; 20000 -13.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A91 Sirius custom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A91 Sirius custom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.86 | 6.4 dB   |
| Peaking | 1865 Hz  | 0.24 | -23.3 dB |
| Peaking | 2413 Hz  | 2.38 | 4.5 dB   |
| Peaking | 4225 Hz  | 0.13 | 23.9 dB  |
| Peaking | 16235 Hz | 0.54 | -25.9 dB |
| Peaking | 847 Hz   | 2.02 | 1.9 dB   |
| Peaking | 1347 Hz  | 4.23 | -1.9 dB  |
| Peaking | 6119 Hz  | 3.01 | 5.9 dB   |
| Peaking | 7011 Hz  | 1.2  | -3.9 dB  |
| Peaking | 11921 Hz | 4.26 | 4.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB   |
| Peaking | 62 Hz    | 1.41 | 1.0 dB   |
| Peaking | 125 Hz   | 1.41 | -1.2 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 16000 Hz | 1.41 | -18.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Fidue%20A91%20Sirius%20custom/Fidue%20A91%20Sirius%20custom.png)