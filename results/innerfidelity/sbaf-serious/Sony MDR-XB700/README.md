# Sony MDR-XB700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.1; 23 -12.3; 25 -12.4; 28 -12.7; 31 -12.9; 34 -13.1; 37 -13.0; 41 -12.6; 45 -12.5; 49 -12.4; 54 -12.3; 60 -13.1; 66 -14.1; 72 -14.8; 79 -15.6; 87 -16.0; 96 -16.4; 106 -16.7; 116 -16.6; 128 -16.5; 141 -16.6; 155 -16.0; 170 -16.0; 187 -15.6; 206 -14.9; 227 -14.0; 249 -13.0; 274 -11.6; 302 -10.4; 332 -9.3; 365 -8.5; 402 -7.7; 442 -6.6; 486 -5.7; 535 -4.5; 588 -3.4; 647 -1.8; 712 -0.5; 783 -0.5; 861 -2.1; 947 -3.7; 1042 -5.7; 1146 -7.4; 1261 -9.1; 1387 -10.8; 1526 -12.2; 1678 -13.0; 1846 -13.4; 2031 -13.2; 2234 -11.9; 2457 -9.1; 2703 -6.4; 2973 -3.0; 3270 -0.7; 3597 -5.0; 3957 -7.1; 4353 -6.0; 4788 -6.5; 5267 -6.6; 5793 -11.5; 6373 -9.3; 7010 -3.4; 7711 -4.7; 8482 -9.6; 9330 -12.2; 10263 -8.4; 11289 -5.0; 12418 -4.9; 13660 -4.9; 15026 -5.7; 16529 -4.9; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.28 | -7.4 dB |
| Peaking | 151 Hz   | 0.89 | -8.6 dB |
| Peaking | 1819 Hz  | 2.5  | -9.7 dB |
| Peaking | 9250 Hz  | 4.3  | -7.8 dB |
| Peaking | 22050 Hz | 2.23 | -4.2 dB |
| Peaking | 741 Hz   | 2.44 | 6.3 dB  |
| Peaking | 1333 Hz  | 3.92 | -3.0 dB |
| Peaking | 2265 Hz  | 7.68 | -2.7 dB |
| Peaking | 3211 Hz  | 6.94 | 5.9 dB  |
| Peaking | 5965 Hz  | 9.19 | -8.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.4 dB  |
| Peaking | 62 Hz    | 1.41 | -5.8 dB  |
| Peaking | 125 Hz   | 1.41 | -10.8 dB |
| Peaking | 250 Hz   | 1.41 | -7.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -9.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-XB700/Sony%20MDR-XB700.png)