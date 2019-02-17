# 1MORE Piston Fit
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -1.2; 79 -2.2; 87 -3.3; 96 -4.5; 106 -5.7; 116 -6.9; 128 -8.0; 141 -9.0; 155 -9.8; 170 -10.4; 187 -10.9; 206 -11.3; 227 -11.6; 249 -11.8; 274 -11.9; 302 -11.8; 332 -11.7; 365 -11.5; 402 -11.2; 442 -10.8; 486 -10.4; 535 -9.8; 588 -9.0; 647 -8.2; 712 -7.5; 783 -6.9; 861 -6.5; 947 -6.3; 1042 -7.0; 1146 -7.7; 1261 -8.0; 1387 -8.2; 1526 -8.2; 1678 -8.7; 1846 -10.1; 2031 -11.1; 2234 -10.9; 2457 -9.2; 2703 -6.6; 2973 -10.0; 3270 -12.8; 3597 -13.5; 3957 -13.8; 4353 -14.5; 4788 -15.0; 5267 -15.5; 5793 -14.3; 6373 -12.1; 7010 -9.1; 7711 -6.8; 8482 -8.0; 9330 -11.8; 10263 -11.4; 11289 -7.0; 12418 -6.5; 13660 -6.8; 15026 -8.3; 16529 -6.8; 18182 -6.5; 20000 -6.5
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

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 47 Hz    | 0.39 | 7.5 dB  |
| Peaking | 217 Hz   | 0.6  | -7.4 dB |
| Peaking | 4151 Hz  | 0.5  | -2.7 dB |
| Peaking | 4798 Hz  | 1.63 | -6.5 dB |
| Peaking | 15260 Hz | 3.08 | -1.3 dB |
| Peaking | 902 Hz   | 2.91 | 2.1 dB  |
| Peaking | 2514 Hz  | 1.76 | -3.9 dB |
| Peaking | 2688 Hz  | 5.34 | 7.5 dB  |
| Peaking | 7723 Hz  | 4.93 | 3.8 dB  |
| Peaking | 9643 Hz  | 5.77 | -5.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 6.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | -7.9 dB |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/1MORE%20Piston%20Fit/1MORE%20Piston%20Fit.png)