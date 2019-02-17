# Sennheiser IE 80 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.6; 23 -13.7; 25 -13.7; 28 -13.7; 31 -13.8; 34 -13.8; 37 -13.8; 41 -13.9; 45 -13.9; 49 -14.0; 54 -14.1; 60 -14.2; 66 -14.4; 72 -14.5; 79 -14.7; 87 -14.9; 96 -15.0; 106 -15.1; 116 -15.2; 128 -15.1; 141 -15.0; 155 -14.9; 170 -14.6; 187 -14.3; 206 -13.8; 227 -13.4; 249 -12.9; 274 -12.3; 302 -11.7; 332 -10.9; 365 -10.1; 402 -9.5; 442 -8.8; 486 -8.0; 535 -7.2; 588 -6.5; 647 -5.7; 712 -4.9; 783 -4.2; 861 -3.6; 947 -3.1; 1042 -2.9; 1146 -2.8; 1261 -2.6; 1387 -2.4; 1526 -2.4; 1678 -2.5; 1846 -2.4; 2031 -2.0; 2234 -1.4; 2457 -1.2; 2703 -1.4; 2973 -1.9; 3270 -2.6; 3597 -3.4; 3957 -4.6; 4353 -6.6; 4788 -9.6; 5267 -9.5; 5793 -4.9; 6373 -1.1; 7010 -0.5; 7711 -2.6; 8482 -2.9; 9330 -2.9; 10263 -2.9; 11289 -3.2; 12418 -6.2; 13660 -12.3; 15026 -17.3; 16529 -19.2; 18182 -18.4; 20000 -14.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 80 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 80 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.19 | -10.4 dB |
| Peaking | 158 Hz   | 0.68 | -6.4 dB  |
| Peaking | 341 Hz   | 1.19 | -3.5 dB  |
| Peaking | 4941 Hz  | 6.74 | -7.7 dB  |
| Peaking | 17615 Hz | 0.91 | -18.6 dB |
| Peaking | 1232 Hz  | 1.89 | 1.0 dB   |
| Peaking | 2461 Hz  | 3.1  | 2.2 dB   |
| Peaking | 6794 Hz  | 6.62 | 4.3 dB   |
| Peaking | 11137 Hz | 1.8  | 4.6 dB   |
| Peaking | 14753 Hz | 2.29 | -6.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.8 dB |
| Peaking | 62 Hz    | 1.41 | -7.9 dB  |
| Peaking | 125 Hz   | 1.41 | -10.0 dB |
| Peaking | 250 Hz   | 1.41 | -8.1 dB  |
| Peaking | 500 Hz   | 1.41 | -3.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 4000 Hz  | 1.41 | -3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 16000 Hz | 1.41 | -21.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sennheiser%20IE%2080%20S/Sennheiser%20IE%2080%20S.png)