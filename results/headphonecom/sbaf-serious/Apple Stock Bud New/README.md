# Apple Stock Bud New
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -1.1; 155 -2.3; 170 -3.4; 187 -4.3; 206 -4.8; 227 -5.2; 249 -5.5; 274 -5.7; 302 -5.8; 332 -5.8; 365 -5.8; 402 -5.7; 442 -5.3; 486 -5.7; 535 -5.5; 588 -5.9; 647 -6.0; 712 -6.1; 783 -6.2; 861 -6.3; 947 -6.5; 1042 -6.6; 1146 -6.7; 1261 -6.8; 1387 -7.2; 1526 -7.9; 1678 -8.6; 1846 -9.2; 2031 -10.1; 2234 -11.6; 2457 -13.7; 2703 -15.5; 2973 -15.8; 3270 -14.1; 3597 -11.7; 3957 -11.0; 4353 -12.2; 4788 -12.7; 5267 -12.3; 5793 -12.7; 6373 -12.6; 7010 -11.9; 7711 -11.3; 8482 -11.0; 9330 -9.3; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -10.1; 15026 -11.1; 16529 -6.7; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple Stock Bud New GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple Stock Bud New ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 50 Hz    | 0.32 | 6.7 dB  |
| Peaking | 902 Hz   | 1.45 | 0.4 dB  |
| Peaking | 2796 Hz  | 1.99 | -8.5 dB |
| Peaking | 6118 Hz  | 1.24 | -5.9 dB |
| Peaking | 14558 Hz | 4.29 | -5.4 dB |
| Peaking | 18 Hz    | 2.45 | 1.2 dB  |
| Peaking | 130 Hz   | 3.06 | 2.0 dB  |
| Peaking | 224 Hz   | 1.63 | -1.3 dB |
| Peaking | 8710 Hz  | 4.51 | -1.9 dB |
| Peaking | 10798 Hz | 2.58 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | 5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | -6.5 dB |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Apple%20Stock%20Bud%20New/Apple%20Stock%20Bud%20New.png)