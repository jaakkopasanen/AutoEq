# Sony MDR-EX57LP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -2.1; 31 -2.6; 34 -3.0; 37 -3.4; 41 -3.9; 45 -4.3; 49 -4.7; 54 -5.1; 60 -5.6; 66 -6.0; 72 -6.5; 79 -6.8; 87 -7.1; 96 -7.4; 106 -7.7; 116 -7.9; 128 -8.2; 141 -8.3; 155 -8.3; 170 -8.3; 187 -8.2; 206 -8.0; 227 -7.7; 249 -7.4; 274 -7.0; 302 -6.5; 332 -6.0; 365 -5.3; 402 -4.7; 442 -4.2; 486 -3.6; 535 -3.0; 588 -2.4; 647 -1.9; 712 -1.6; 783 -1.2; 861 -0.6; 947 -1.0; 1042 -1.4; 1146 -1.9; 1261 -2.6; 1387 -3.4; 1526 -4.5; 1678 -5.2; 1846 -5.4; 2031 -4.8; 2234 -4.5; 2457 -4.7; 2703 -5.2; 2973 -5.3; 3270 -4.0; 3597 -2.8; 3957 -3.5; 4353 -6.1; 4788 -8.6; 5267 -9.7; 5793 -5.7; 6373 -1.1; 7010 -1.9; 7711 -4.1; 8482 -4.4; 9330 -4.4; 10263 -4.4; 11289 -5.0; 12418 -4.4; 13660 -4.4; 15026 -4.4; 16529 -4.4; 18182 -4.4; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX57LP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX57LP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.89 | 4.3 dB  |
| Peaking | 151 Hz  | 0.57 | -4.2 dB |
| Peaking | 791 Hz  | 1.3  | 4.2 dB  |
| Peaking | 5165 Hz | 4.66 | -6.4 dB |
| Peaking | 6548 Hz | 5.87 | 5.3 dB  |
| Peaking | 747 Hz  | 5.23 | -1.2 dB |
| Peaking | 1706 Hz | 2.61 | -2.8 dB |
| Peaking | 1817 Hz | 0.61 | 1.8 dB  |
| Peaking | 3265 Hz | 1.28 | -3.0 dB |
| Peaking | 3635 Hz | 3.91 | 4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-EX57LP/Sony%20MDR-EX57LP.png)