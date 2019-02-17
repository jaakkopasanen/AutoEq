# Sony MDR-7550
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -2.8; 25 -3.0; 28 -3.3; 31 -3.5; 34 -3.7; 37 -3.9; 41 -4.1; 45 -4.4; 49 -4.6; 54 -4.8; 60 -5.3; 66 -5.7; 72 -5.9; 79 -6.3; 87 -6.6; 96 -6.9; 106 -7.1; 116 -7.4; 128 -7.7; 141 -8.0; 155 -8.2; 170 -8.4; 187 -8.5; 206 -8.6; 227 -8.6; 249 -8.4; 274 -8.4; 302 -8.3; 332 -7.9; 365 -7.8; 402 -7.4; 442 -7.3; 486 -7.0; 535 -6.9; 588 -6.6; 647 -6.2; 712 -6.0; 783 -6.1; 861 -6.2; 947 -6.5; 1042 -6.3; 1146 -6.8; 1261 -8.0; 1387 -9.0; 1526 -10.0; 1678 -10.5; 1846 -10.3; 2031 -9.6; 2234 -8.1; 2457 -6.0; 2703 -3.5; 2973 -0.9; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -4.0; 4788 -8.4; 5267 -8.2; 5793 -2.0; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.49 | 3.9 dB  |
| Peaking | 196 Hz  | 0.88 | -2.4 dB |
| Peaking | 1791 Hz | 2.22 | -5.1 dB |
| Peaking | 3302 Hz | 2.59 | 7.5 dB  |
| Peaking | 6289 Hz | 7.06 | 6.1 dB  |
| Peaking | 866 Hz  | 1.61 | 0.9 dB  |
| Peaking | 1415 Hz | 5.42 | -1.0 dB |
| Peaking | 4044 Hz | 7.35 | 3.4 dB  |
| Peaking | 5031 Hz | 4.77 | -5.5 dB |
| Peaking | 5747 Hz | 7.62 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7550/Sony%20MDR-7550.png)