# Sony MDR-DS3000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.6; 106 -1.1; 116 -1.4; 128 -1.8; 141 -2.0; 155 -2.3; 170 -2.2; 187 -2.2; 206 -2.3; 227 -2.0; 249 -2.0; 274 -1.8; 302 -1.7; 332 -1.5; 365 -1.9; 402 -2.6; 442 -3.0; 486 -3.3; 535 -3.5; 588 -3.8; 647 -4.1; 712 -4.6; 783 -5.1; 861 -5.0; 947 -6.0; 1042 -6.6; 1146 -6.8; 1261 -6.9; 1387 -7.1; 1526 -8.3; 1678 -9.8; 1846 -11.9; 2031 -12.4; 2234 -10.6; 2457 -8.6; 2703 -8.0; 2973 -6.6; 3270 -4.9; 3597 -4.3; 3957 -5.3; 4353 -7.3; 4788 -6.5; 5267 -2.4; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-DS3000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-DS3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.24 | 6.2 dB  |
| Peaking | 364 Hz  | 0.78 | 3.4 dB  |
| Peaking | 1971 Hz | 2.56 | -6.4 dB |
| Peaking | 3450 Hz | 5.78 | 2.7 dB  |
| Peaking | 5983 Hz | 4.04 | 6.8 dB  |
| Peaking | 157 Hz  | 4.9  | -0.3 dB |
| Peaking | 4605 Hz | 7.32 | -4.6 dB |
| Peaking | 4869 Hz | 2.85 | 2.0 dB  |
| Peaking | 8107 Hz | 3.84 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | 3.3 dB  |
| Peaking | 250 Hz   | 1.41 | 3.7 dB  |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-DS3000/Sony%20MDR-DS3000.png)