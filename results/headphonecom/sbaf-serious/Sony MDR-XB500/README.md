# Sony MDR-XB500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.2; 25 -11.4; 28 -11.5; 31 -11.7; 34 -11.8; 37 -11.8; 41 -11.9; 45 -11.9; 49 -12.1; 54 -12.1; 60 -12.1; 66 -12.0; 72 -12.1; 79 -12.7; 87 -13.4; 96 -13.6; 106 -13.2; 116 -13.8; 128 -14.4; 141 -15.1; 155 -15.3; 170 -14.3; 187 -14.2; 206 -15.1; 227 -15.4; 249 -14.9; 274 -14.6; 302 -14.3; 332 -13.8; 365 -13.4; 402 -12.6; 442 -11.9; 486 -10.8; 535 -9.4; 588 -7.8; 647 -6.0; 712 -3.8; 783 -2.0; 861 -0.8; 947 -1.1; 1042 -2.3; 1146 -3.4; 1261 -5.0; 1387 -6.5; 1526 -7.1; 1678 -6.6; 1846 -5.7; 2031 -4.4; 2234 -3.0; 2457 -1.3; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.3; 4788 -4.2; 5267 -3.5; 5793 -1.8; 6373 -1.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 57 Hz   | 0.07 | -4.6 dB |
| Peaking | 364 Hz  | 0.34 | -6.1 dB |
| Peaking | 886 Hz  | 0.99 | 13.5 dB |
| Peaking | 1601 Hz | 0.94 | -8.3 dB |
| Peaking | 2748 Hz | 0.72 | 9.1 dB  |
| Peaking | 66 Hz   | 5.11 | 0.7 dB  |
| Peaking | 4235 Hz | 6.02 | 2.0 dB  |
| Peaking | 4780 Hz | 5.16 | -2.5 dB |
| Peaking | 6333 Hz | 3.32 | 5.4 dB  |
| Peaking | 7373 Hz | 1.41 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -8.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-XB500/Sony%20MDR-XB500.png)