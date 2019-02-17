# Sony MDR-EX57LP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.4; 25 -2.9; 28 -3.5; 31 -4.0; 34 -4.5; 37 -4.9; 41 -5.3; 45 -5.7; 49 -6.1; 54 -6.5; 60 -7.1; 66 -7.5; 72 -7.9; 79 -8.2; 87 -8.6; 96 -8.9; 106 -9.1; 116 -9.4; 128 -9.6; 141 -9.7; 155 -9.8; 170 -9.7; 187 -9.7; 206 -9.4; 227 -9.2; 249 -8.9; 274 -8.5; 302 -8.0; 332 -7.4; 365 -6.8; 402 -6.2; 442 -5.6; 486 -5.1; 535 -4.5; 588 -3.8; 647 -3.3; 712 -3.0; 783 -2.6; 861 -2.0; 947 -2.5; 1042 -2.8; 1146 -3.3; 1261 -4.0; 1387 -4.9; 1526 -5.9; 1678 -6.7; 1846 -6.8; 2031 -6.2; 2234 -5.9; 2457 -6.1; 2703 -6.6; 2973 -6.7; 3270 -5.4; 3597 -4.2; 3957 -5.0; 4353 -7.5; 4788 -10.0; 5267 -11.1; 5793 -7.2; 6373 -2.5; 7010 -0.5; 7711 -2.5; 8482 -2.7; 9330 -2.8; 10263 -3.5; 11289 -6.4; 12418 -4.8; 13660 -2.8; 15026 -2.8; 16529 -2.8; 18182 -2.8; 20000 -2.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX57LP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX57LP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 109 Hz   | 0.58 | -5.9 dB |
| Peaking | 248 Hz   | 1.06 | -3.6 dB |
| Peaking | 1762 Hz  | 2.95 | -3.8 dB |
| Peaking | 2764 Hz  | 2.82 | -3.4 dB |
| Peaking | 5049 Hz  | 4.37 | -8.9 dB |
| Peaking | 20 Hz    | 2.5  | 1.7 dB  |
| Peaking | 855 Hz   | 3.57 | 1.6 dB  |
| Peaking | 5610 Hz  | 8.11 | -2.3 dB |
| Peaking | 6790 Hz  | 4.65 | 3.6 dB  |
| Peaking | 11460 Hz | 4.85 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | -4.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-EX57LP/Sony%20MDR-EX57LP.png)