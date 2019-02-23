# Sony MDR-V6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -1.0; 41 -1.8; 45 -2.6; 49 -3.3; 54 -3.8; 60 -3.5; 66 -4.0; 72 -4.6; 79 -4.9; 87 -5.2; 96 -5.4; 106 -5.3; 116 -5.4; 128 -5.4; 141 -5.4; 155 -5.2; 170 -4.3; 187 -2.6; 206 -2.7; 227 -3.7; 249 -4.0; 274 -3.4; 302 -3.6; 332 -3.9; 365 -4.8; 402 -5.6; 442 -5.9; 486 -6.0; 535 -6.0; 588 -5.8; 647 -5.6; 712 -5.5; 783 -5.4; 861 -5.5; 947 -5.2; 1042 -5.4; 1146 -5.6; 1261 -6.3; 1387 -6.7; 1526 -7.9; 1678 -8.8; 1846 -9.2; 2031 -9.4; 2234 -9.4; 2457 -9.0; 2703 -9.6; 2973 -10.2; 3270 -9.3; 3597 -7.9; 3957 -7.7; 4353 -10.9; 4788 -9.7; 5267 -5.2; 5793 -2.4; 6373 -3.4; 7010 -7.1; 7711 -8.5; 8482 -10.7; 9330 -13.8; 10263 -12.4; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-V6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.8  | 6.4 dB  |
| Peaking | 249 Hz  | 1    | 3.1 dB  |
| Peaking | 3336 Hz | 0.77 | -3.4 dB |
| Peaking | 5945 Hz | 4.75 | 7.0 dB  |
| Peaking | 9482 Hz | 3.84 | -7.8 dB |
| Peaking | 138 Hz  | 4.47 | -0.6 dB |
| Peaking | 1049 Hz | 1.75 | 1.8 dB  |
| Peaking | 1815 Hz | 2.54 | -1.6 dB |
| Peaking | 3775 Hz | 6.17 | 2.7 dB  |
| Peaking | 4475 Hz | 8.83 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | 3.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-V6/Sony%20MDR-V6.png)