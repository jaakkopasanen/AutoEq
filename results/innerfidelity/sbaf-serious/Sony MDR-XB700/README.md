# Sony MDR-XB700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.8; 25 -10.0; 28 -10.3; 31 -10.5; 34 -10.6; 37 -10.5; 41 -10.2; 45 -10.1; 49 -10.0; 54 -9.9; 60 -10.7; 66 -11.6; 72 -12.3; 79 -13.1; 87 -13.6; 96 -14.0; 106 -14.2; 116 -14.2; 128 -14.1; 141 -14.1; 155 -13.5; 170 -13.6; 187 -13.1; 206 -12.4; 227 -11.5; 249 -10.5; 274 -9.1; 302 -8.0; 332 -6.8; 365 -6.0; 402 -5.3; 442 -4.2; 486 -3.2; 535 -2.0; 588 -0.9; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -1.2; 1042 -3.3; 1146 -4.9; 1261 -6.6; 1387 -8.4; 1526 -9.7; 1678 -10.5; 1846 -11.0; 2031 -10.8; 2234 -9.4; 2457 -6.6; 2703 -3.9; 2973 -0.7; 3270 -0.5; 3597 -2.6; 3957 -4.7; 4353 -3.5; 4788 -4.1; 5267 -4.2; 5793 -9.1; 6373 -6.9; 7010 -4.0; 7711 -6.2; 8482 -7.4; 9330 -9.7; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 1.34 | -2.7 dB  |
| Peaking | 136 Hz  | 0.52 | -8.6 dB  |
| Peaking | 786 Hz  | 0.67 | 10.6 dB  |
| Peaking | 1928 Hz | 0.77 | -11.9 dB |
| Peaking | 3051 Hz | 1.54 | 11.5 dB  |
| Peaking | 55 Hz   | 5.23 | 0.7 dB   |
| Peaking | 5195 Hz | 4.7  | 3.0 dB   |
| Peaking | 6017 Hz | 6.09 | -6.7 dB  |
| Peaking | 6694 Hz | 6.14 | 5.2 dB   |
| Peaking | 9195 Hz | 7.24 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -7.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | 5.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-XB700/Sony%20MDR-XB700.png)