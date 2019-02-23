# Sennheiser IE 80 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.9; 23 -13.0; 25 -13.0; 28 -13.0; 31 -13.1; 34 -13.1; 37 -13.1; 41 -13.2; 45 -13.2; 49 -13.3; 54 -13.4; 60 -13.5; 66 -13.7; 72 -13.8; 79 -14.0; 87 -14.1; 96 -14.3; 106 -14.4; 116 -14.4; 128 -14.4; 141 -14.3; 155 -14.1; 170 -13.9; 187 -13.5; 206 -13.1; 227 -12.7; 249 -12.1; 274 -11.6; 302 -10.9; 332 -10.2; 365 -9.4; 402 -8.7; 442 -8.1; 486 -7.3; 535 -6.5; 588 -5.8; 647 -5.0; 712 -4.2; 783 -3.5; 861 -2.9; 947 -2.4; 1042 -2.2; 1146 -2.1; 1261 -1.9; 1387 -1.7; 1526 -1.7; 1678 -1.8; 1846 -1.7; 2031 -1.2; 2234 -0.7; 2457 -0.5; 2703 -0.7; 2973 -1.2; 3270 -1.9; 3597 -2.7; 3957 -3.9; 4353 -5.9; 4788 -8.8; 5267 -8.8; 5793 -4.1; 6373 -0.8; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -6.2; 13660 -11.6; 15026 -16.6; 16529 -18.4; 18182 -17.7; 20000 -14.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 80 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 80 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.37 | -5.6 dB  |
| Peaking | 150 Hz   | 0.36 | -8.1 dB  |
| Peaking | 1465 Hz  | 0.38 | 5.4 dB   |
| Peaking | 17590 Hz | 0.88 | -14.2 dB |
| Peaking | 2832 Hz  | 2.78 | 1.6 dB   |
| Peaking | 5005 Hz  | 3.99 | -6.5 dB  |
| Peaking | 6334 Hz  | 5.08 | 5.7 dB   |
| Peaking | 12212 Hz | 2.06 | 4.1 dB   |
| Peaking | 14830 Hz | 2.52 | -4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.1 dB  |
| Peaking | 62 Hz    | 1.41 | -5.4 dB  |
| Peaking | 125 Hz   | 1.41 | -7.2 dB  |
| Peaking | 250 Hz   | 1.41 | -5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 16000 Hz | 1.41 | -15.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sennheiser%20IE%2080%20S/Sennheiser%20IE%2080%20S.png)