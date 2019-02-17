# Sennheiser HD 600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.2; 34 -1.7; 37 -2.2; 41 -2.7; 45 -3.2; 49 -3.5; 54 -3.6; 60 -3.8; 66 -4.3; 72 -5.0; 79 -5.4; 87 -5.9; 96 -6.5; 106 -7.0; 116 -7.4; 128 -7.6; 141 -7.8; 155 -7.9; 170 -7.9; 187 -7.8; 206 -7.8; 227 -7.7; 249 -7.5; 274 -7.2; 302 -7.0; 332 -6.7; 365 -6.4; 402 -6.2; 442 -6.1; 486 -6.0; 535 -5.9; 588 -5.8; 647 -5.7; 712 -5.7; 783 -5.6; 861 -5.6; 947 -6.3; 1042 -6.6; 1146 -6.8; 1261 -7.1; 1387 -7.1; 1526 -6.8; 1678 -6.5; 1846 -6.8; 2031 -6.5; 2234 -6.2; 2457 -6.7; 2703 -7.6; 2973 -8.2; 3270 -8.5; 3597 -7.2; 3957 -4.8; 4353 -3.6; 4788 -5.8; 5267 -6.6; 5793 -8.7; 6373 -6.1; 7010 -4.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -10.8; 13660 -12.3; 15026 -9.7; 16529 -11.5; 18182 -14.9; 20000 -12.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 25 Hz    |  1.29 | 6.5 dB  |
| Peaking | 54 Hz    |  2.84 | 2.0 dB  |
| Peaking | 13198 Hz |  2.84 | -7.3 dB |
| Peaking | 13281 Hz |  0.77 | 3.6 dB  |
| Peaking | 18629 Hz |  0.64 | -9.4 dB |
| Peaking | 173 Hz   |  1.24 | -1.7 dB |
| Peaking | 626 Hz   |  1.65 | 1.0 dB  |
| Peaking | 3225 Hz  |  3.29 | -2.6 dB |
| Peaking | 4208 Hz  |  5    | 3.6 dB  |
| Peaking | 5794 Hz  | 10.18 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -7.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)