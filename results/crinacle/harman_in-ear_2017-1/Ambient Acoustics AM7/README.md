# Ambient Acoustics AM7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.3; 25 -1.8; 28 -2.4; 31 -2.9; 34 -3.2; 37 -3.5; 41 -3.9; 45 -4.2; 49 -4.6; 54 -4.9; 60 -5.3; 66 -5.6; 72 -6.0; 79 -6.5; 87 -6.9; 96 -7.3; 106 -7.8; 116 -8.2; 128 -8.5; 141 -8.8; 155 -9.0; 170 -9.2; 187 -9.3; 206 -9.4; 227 -9.3; 249 -9.2; 274 -9.1; 302 -8.9; 332 -8.5; 365 -8.2; 402 -7.9; 442 -7.5; 486 -7.1; 535 -6.6; 588 -6.2; 647 -5.7; 712 -5.2; 783 -4.8; 861 -4.5; 947 -4.5; 1042 -4.9; 1146 -5.7; 1261 -6.5; 1387 -7.2; 1526 -7.8; 1678 -9.2; 1846 -12.1; 2031 -13.1; 2234 -9.5; 2457 -5.8; 2703 -4.0; 2973 -4.6; 3270 -7.0; 3597 -3.1; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -3.4; 5793 -3.9; 6373 -5.8; 7010 -9.1; 7711 -9.6; 8482 -6.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.0; 15026 -18.5; 16529 -24.8; 18182 -29.6; 20000 -29.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ambient Acoustics AM7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ambient Acoustics AM7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.48 | 6.4 dB   |
| Peaking | 186 Hz   | 0.89 | -3.3 dB  |
| Peaking | 1964 Hz  | 4.99 | -8.0 dB  |
| Peaking | 4416 Hz  | 1.75 | 6.9 dB   |
| Peaking | 18867 Hz | 0.91 | -27.2 dB |
| Peaking | 869 Hz   | 2.54 | 2.5 dB   |
| Peaking | 6185 Hz  | 5.8  | 1.1 dB   |
| Peaking | 7176 Hz  | 3.83 | -4.3 dB  |
| Peaking | 12927 Hz | 1.2  | 10.0 dB  |
| Peaking | 15950 Hz | 1.17 | -10.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB   |
| Peaking | 62 Hz    | 1.41 | 0.6 dB   |
| Peaking | 125 Hz   | 1.41 | -1.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 16000 Hz | 1.41 | -20.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ambient%20Acoustics%20AM7/Ambient%20Acoustics%20AM7.png)