# Sony MDR-SA5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.5; 72 -2.3; 79 -3.2; 87 -4.3; 96 -4.6; 106 -4.8; 116 -4.8; 128 -4.8; 141 -4.7; 155 -4.6; 170 -4.2; 187 -4.1; 206 -4.0; 227 -3.9; 249 -3.6; 274 -3.5; 302 -3.2; 332 -3.6; 365 -4.3; 402 -4.1; 442 -4.3; 486 -4.8; 535 -5.4; 588 -6.2; 647 -6.7; 712 -7.3; 783 -8.0; 861 -8.6; 947 -9.1; 1042 -8.3; 1146 -6.3; 1261 -4.9; 1387 -4.4; 1526 -4.7; 1678 -5.3; 1846 -6.6; 2031 -7.8; 2234 -8.6; 2457 -11.8; 2703 -15.4; 2973 -14.3; 3270 -11.6; 3597 -8.1; 3957 -7.6; 4353 -10.2; 4788 -8.2; 5267 -0.5; 5793 -0.5; 6373 -2.2; 7010 -7.9; 7711 -12.0; 8482 -13.0; 9330 -13.4; 10263 -10.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -11.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-SA5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-SA5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 34 Hz    |  0.55 | 6.6 dB  |
| Peaking | 290 Hz   |  1.34 | 3.0 dB  |
| Peaking | 2824 Hz  |  3.48 | -9.6 dB |
| Peaking | 5828 Hz  |  4.2  | 9.0 dB  |
| Peaking | 8569 Hz  |  2.35 | -8.0 dB |
| Peaking | 943 Hz   |  2.6  | -3.6 dB |
| Peaking | 1379 Hz  |  2.2  | 3.3 dB  |
| Peaking | 4597 Hz  |  6.39 | -5.6 dB |
| Peaking | 5115 Hz  | 10.23 | 5.3 dB  |
| Peaking | 11486 Hz |  5.63 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.0 dB |
| Peaking | 250 Hz   | 1.41 | 3.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-SA5000/Sony%20MDR-SA5000.png)