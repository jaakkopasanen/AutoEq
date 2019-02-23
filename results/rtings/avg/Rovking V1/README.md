# Rovking V1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.6; 23 -17.6; 25 -17.5; 28 -17.5; 31 -17.4; 34 -17.4; 37 -17.3; 41 -17.2; 45 -17.2; 49 -17.1; 54 -17.1; 60 -17.0; 66 -17.0; 72 -17.0; 79 -16.9; 87 -16.8; 96 -16.7; 106 -16.7; 116 -16.6; 128 -16.4; 141 -16.0; 155 -15.5; 170 -14.9; 187 -14.2; 206 -13.5; 227 -13.0; 249 -12.6; 274 -12.1; 302 -11.3; 332 -10.4; 365 -9.5; 402 -8.4; 442 -7.3; 486 -6.2; 535 -5.2; 588 -4.2; 647 -3.6; 712 -3.3; 783 -2.9; 861 -2.4; 947 -2.1; 1042 -1.8; 1146 -1.4; 1261 -1.3; 1387 -1.3; 1526 -1.0; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -1.1; 3270 -2.7; 3597 -4.0; 3957 -5.5; 4353 -7.0; 4788 -9.3; 5267 -9.0; 5793 -7.2; 6373 -5.7; 7010 -5.0; 7711 -9.0; 8482 -8.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.2; 13660 -9.6; 15026 -7.1; 16529 -6.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rovking V1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rovking V1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.25 | -10.2 dB |
| Peaking | 170 Hz   | 0.33 | -9.7 dB  |
| Peaking | 1476 Hz  | 0.18 | 7.5 dB   |
| Peaking | 4818 Hz  | 2.42 | -6.8 dB  |
| Peaking | 9918 Hz  | 0.49 | -3.2 dB  |
| Peaking | 6793 Hz  | 9.09 | 2.5 dB   |
| Peaking | 7918 Hz  | 6.37 | -3.8 dB  |
| Peaking | 11502 Hz | 1.72 | 2.4 dB   |
| Peaking | 13054 Hz | 3.66 | -4.5 dB  |
| Peaking | 16499 Hz | 0.85 | 0.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.3 dB |
| Peaking | 62 Hz    | 1.41 | -7.4 dB  |
| Peaking | 125 Hz   | 1.41 | -8.1 dB  |
| Peaking | 250 Hz   | 1.41 | -5.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Rovking%20V1/Rovking%20V1.png)