# InEar ProPhile-8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.2; 25 -7.4; 28 -7.7; 31 -7.9; 34 -8.0; 37 -8.1; 41 -8.2; 45 -8.3; 49 -8.5; 54 -8.7; 60 -9.1; 66 -9.4; 72 -9.5; 79 -9.8; 87 -9.8; 96 -9.6; 106 -9.9; 116 -9.7; 128 -9.8; 141 -9.5; 155 -9.3; 170 -9.1; 187 -8.9; 206 -8.6; 227 -8.2; 249 -7.9; 274 -7.6; 302 -7.2; 332 -6.8; 365 -6.4; 402 -6.2; 442 -6.1; 486 -5.9; 535 -5.7; 588 -5.6; 647 -5.3; 712 -5.1; 783 -4.8; 861 -4.7; 947 -4.7; 1042 -5.2; 1146 -5.8; 1261 -6.4; 1387 -6.5; 1526 -6.1; 1678 -5.5; 1846 -4.7; 2031 -3.7; 2234 -2.5; 2457 -1.3; 2703 -0.5; 2973 -0.5; 3270 -1.1; 3597 -1.1; 3957 -0.9; 4353 -0.8; 4788 -1.4; 5267 -3.2; 5793 -4.6; 6373 -3.3; 7010 -3.7; 7711 -5.1; 8482 -5.3; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -8.8; 15026 -17.9; 16529 -24.5; 18182 -28.5; 20000 -28.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar ProPhile-8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar ProPhile-8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 65 Hz    | 0.45 | -3.4 dB  |
| Peaking | 155 Hz   | 0.84 | -2.3 dB  |
| Peaking | 3802 Hz  | 0.58 | 11.0 dB  |
| Peaking | 12328 Hz | 0.54 | 24.0 dB  |
| Peaking | 17601 Hz | 0.16 | -34.1 dB |
| Peaking | 919 Hz   | 1.34 | 2.7 dB   |
| Peaking | 1475 Hz  | 0.83 | -3.8 dB  |
| Peaking | 2891 Hz  | 0.91 | 4.2 dB   |
| Peaking | 3502 Hz  | 2.14 | -3.6 dB  |
| Peaking | 5579 Hz  | 7.26 | -2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 16000 Hz | 1.41 | -22.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/InEar%20ProPhile-8/InEar%20ProPhile-8.png)