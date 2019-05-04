# Sennheiser HD 600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.0; 34 -1.6; 37 -2.1; 41 -2.6; 45 -3.0; 49 -3.3; 54 -3.5; 60 -3.8; 66 -4.4; 72 -4.9; 79 -5.4; 87 -5.8; 96 -6.5; 106 -7.1; 116 -7.5; 128 -7.7; 141 -7.9; 155 -8.1; 170 -8.1; 187 -8.0; 206 -8.0; 227 -8.0; 249 -7.8; 274 -7.5; 302 -7.2; 332 -7.0; 365 -6.7; 402 -6.5; 442 -6.4; 486 -6.3; 535 -6.1; 588 -6.0; 647 -6.0; 712 -6.0; 783 -5.8; 861 -5.6; 947 -6.2; 1042 -6.7; 1146 -6.9; 1261 -7.2; 1387 -7.1; 1526 -6.8; 1678 -6.5; 1846 -6.4; 2031 -6.0; 2234 -5.7; 2457 -6.2; 2703 -7.2; 2973 -8.0; 3270 -8.3; 3597 -7.1; 3957 -4.7; 4353 -3.5; 4788 -5.9; 5267 -6.9; 5793 -8.2; 6373 -5.3; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -10.6; 13660 -11.6; 15026 -9.1; 16529 -11.7; 18182 -15.2; 20000 -11.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.34 | 6.5 dB  |
| Peaking | 51 Hz    | 2.52 | 2.1 dB  |
| Peaking | 7242 Hz  | 1.79 | 1.7 dB  |
| Peaking | 18610 Hz | 0.55 | -8.3 dB |
| Peaking | 22050 Hz | 0.67 | -4.2 dB |
| Peaking | 174 Hz   | 1.36 | -2.0 dB |
| Peaking | 3333 Hz  | 3.64 | -3.6 dB |
| Peaking | 4175 Hz  | 2.32 | 3.8 dB  |
| Peaking | 5468 Hz  | 4.35 | -3.0 dB |
| Peaking | 18373 Hz | 2.11 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -7.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)