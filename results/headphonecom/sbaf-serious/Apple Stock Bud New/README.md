# Apple Stock Bud New
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -1.2; 170 -2.3; 187 -3.2; 206 -3.7; 227 -4.1; 249 -4.4; 274 -4.6; 302 -4.7; 332 -4.7; 365 -4.7; 402 -4.6; 442 -4.2; 486 -4.6; 535 -4.4; 588 -4.8; 647 -4.9; 712 -5.0; 783 -5.1; 861 -5.2; 947 -5.4; 1042 -5.6; 1146 -5.6; 1261 -5.7; 1387 -6.2; 1526 -6.8; 1678 -7.5; 1846 -8.1; 2031 -9.0; 2234 -10.5; 2457 -12.6; 2703 -14.4; 2973 -14.7; 3270 -13.0; 3597 -10.6; 3957 -9.9; 4353 -11.1; 4788 -11.6; 5267 -11.2; 5793 -11.6; 6373 -11.5; 7010 -10.8; 7711 -10.2; 8482 -9.9; 9330 -8.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.0; 15026 -10.0; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple Stock Bud New GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple Stock Bud New ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 51 Hz    | 0.26 | 6.5 dB  |
| Peaking | 856 Hz   | 0.79 | 1.3 dB  |
| Peaking | 2802 Hz  | 2.22 | -8.0 dB |
| Peaking | 6018 Hz  | 1.33 | -4.9 dB |
| Peaking | 14667 Hz | 4.83 | -4.3 dB |
| Peaking | 21 Hz    | 2.59 | 0.7 dB  |
| Peaking | 139 Hz   | 3.16 | 1.5 dB  |
| Peaking | 227 Hz   | 2.01 | -1.0 dB |
| Peaking | 8657 Hz  | 4.06 | -1.9 dB |
| Peaking | 10228 Hz | 2.21 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 5.4 dB  |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | -5.5 dB |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Apple%20Stock%20Bud%20New/Apple%20Stock%20Bud%20New.png)