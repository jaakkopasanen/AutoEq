# Sony MDR-DS6000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.8; 54 -1.9; 60 -2.9; 66 -4.3; 72 -5.7; 79 -6.9; 87 -7.9; 96 -8.7; 106 -9.2; 116 -9.6; 128 -9.7; 141 -9.6; 155 -9.5; 170 -9.1; 187 -9.1; 206 -8.5; 227 -8.4; 249 -8.4; 274 -8.1; 302 -7.7; 332 -7.5; 365 -7.3; 402 -7.1; 442 -6.6; 486 -6.9; 535 -7.3; 588 -7.5; 647 -7.8; 712 -8.3; 783 -8.5; 861 -8.1; 947 -6.8; 1042 -7.4; 1146 -8.5; 1261 -9.6; 1387 -9.8; 1526 -10.6; 1678 -11.5; 1846 -12.1; 2031 -12.6; 2234 -11.7; 2457 -9.7; 2703 -7.3; 2973 -5.5; 3270 -3.6; 3597 -1.4; 3957 -0.9; 4353 -2.6; 4788 -1.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-DS6000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-DS6000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.43 | 9.2 dB  |
| Peaking | 104 Hz  | 0.64 | -8.2 dB |
| Peaking | 1993 Hz | 1.27 | -6.9 dB |
| Peaking | 3666 Hz | 1.91 | 6.5 dB  |
| Peaking | 5751 Hz | 2.95 | 5.8 dB  |
| Peaking | 34 Hz   | 3.52 | -0.5 dB |
| Peaking | 444 Hz  | 3.44 | 0.9 dB  |
| Peaking | 798 Hz  | 2.17 | -1.4 dB |
| Peaking | 969 Hz  | 5.59 | 2.0 dB  |
| Peaking | 8202 Hz | 4.77 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -7.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-DS6000/Sony%20MDR-DS6000.png)