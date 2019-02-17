# Sennheiser HD 540 reference-II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.2; 31 -1.9; 34 -2.5; 37 -3.0; 41 -3.5; 45 -4.0; 49 -4.4; 54 -4.9; 60 -5.3; 66 -5.5; 72 -5.8; 79 -6.9; 87 -8.1; 96 -9.0; 106 -9.6; 116 -10.3; 128 -10.8; 141 -11.2; 155 -11.5; 170 -11.7; 187 -11.8; 206 -11.9; 227 -11.9; 249 -11.8; 274 -11.6; 302 -11.3; 332 -11.0; 365 -10.7; 402 -10.4; 442 -10.2; 486 -10.0; 535 -9.7; 588 -9.3; 647 -9.0; 712 -8.7; 783 -8.5; 861 -7.9; 947 -6.4; 1042 -6.5; 1146 -6.7; 1261 -6.4; 1387 -5.8; 1526 -5.1; 1678 -4.5; 1846 -4.2; 2031 -4.6; 2234 -5.5; 2457 -6.4; 2703 -7.3; 2973 -7.6; 3270 -6.9; 3597 -5.5; 3957 -7.4; 4353 -7.7; 4788 -10.4; 5267 -9.5; 5793 -9.6; 6373 -12.2; 7010 -7.9; 7711 -8.8; 8482 -8.5; 9330 -6.5; 10263 -6.5; 11289 -9.4; 12418 -15.7; 13660 -14.8; 15026 -9.5; 16529 -8.9; 18182 -12.2; 20000 -13.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 540 reference-II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 540 reference-II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.15 | 6.5 dB   |
| Peaking | 172 Hz   | 0.38 | -6.7 dB  |
| Peaking | 1733 Hz  | 2.2  | 2.9 dB   |
| Peaking | 6017 Hz  | 2.58 | -4.4 dB  |
| Peaking | 13137 Hz | 2.71 | -10.4 dB |
| Peaking | 840 Hz   | 2.34 | -1.1 dB  |
| Peaking | 952 Hz   | 4.32 | 2.0 dB   |
| Peaking | 2845 Hz  | 6.78 | -1.2 dB  |
| Peaking | 10242 Hz | 4.58 | 2.8 dB   |
| Peaking | 19277 Hz | 1.08 | -7.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -6.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20540%20reference-II/Sennheiser%20HD%20540%20reference-II.png)