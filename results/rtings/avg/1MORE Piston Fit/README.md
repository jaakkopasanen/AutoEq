# 1MORE Piston Fit
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -1.0; 106 -2.2; 116 -3.4; 128 -4.5; 141 -5.5; 155 -6.3; 170 -6.9; 187 -7.4; 206 -7.7; 227 -8.1; 249 -8.3; 274 -8.3; 302 -8.3; 332 -8.1; 365 -8.0; 402 -7.7; 442 -7.3; 486 -6.8; 535 -6.2; 588 -5.5; 647 -4.7; 712 -3.9; 783 -3.3; 861 -2.9; 947 -2.8; 1042 -3.4; 1146 -4.1; 1261 -4.4; 1387 -4.6; 1526 -4.7; 1678 -5.2; 1846 -6.5; 2031 -7.5; 2234 -7.4; 2457 -5.7; 2703 -3.0; 2973 -6.4; 3270 -9.2; 3597 -9.9; 3957 -10.3; 4353 -11.0; 4788 -11.5; 5267 -12.0; 5793 -10.7; 6373 -8.5; 7010 -5.6; 7711 -6.2; 8482 -6.5; 9330 -8.2; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Piston Fit GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Piston Fit ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 63 Hz   | 0.26 | 7.6 dB  |
| Peaking | 220 Hz  | 0.62 | -6.3 dB |
| Peaking | 899 Hz  | 1.26 | 4.2 dB  |
| Peaking | 2710 Hz | 8.96 | 5.0 dB  |
| Peaking | 4573 Hz | 1.57 | -5.5 dB |
| Peaking | 21 Hz   | 2.81 | 1.1 dB  |
| Peaking | 91 Hz   | 6.44 | 1.1 dB  |
| Peaking | 5654 Hz | 5.46 | -2.0 dB |
| Peaking | 7199 Hz | 3.3  | 2.5 dB  |
| Peaking | 9707 Hz | 8.27 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.8 dB  |
| Peaking | 125 Hz   | 1.41 | 2.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.6 dB |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/1MORE%20Piston%20Fit/1MORE%20Piston%20Fit.png)