# Sony MDR-EX56LP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -10.2; 25 -10.5; 28 -10.9; 31 -11.2; 34 -11.5; 37 -11.7; 41 -12.0; 45 -12.2; 49 -12.4; 54 -12.6; 60 -12.9; 66 -13.0; 72 -13.2; 79 -13.3; 87 -13.4; 96 -13.4; 106 -13.3; 116 -13.2; 128 -13.1; 141 -12.9; 155 -12.7; 170 -12.4; 187 -12.0; 206 -11.6; 227 -11.1; 249 -10.6; 274 -10.1; 302 -9.6; 332 -9.0; 365 -8.3; 402 -7.8; 442 -7.4; 486 -7.2; 535 -6.8; 588 -6.5; 647 -6.2; 712 -6.4; 783 -6.7; 861 -6.8; 947 -3.2; 1042 -2.7; 1146 -4.3; 1261 -5.6; 1387 -6.9; 1526 -8.3; 1678 -9.3; 1846 -10.2; 2031 -10.7; 2234 -10.5; 2457 -9.5; 2703 -7.7; 2973 -5.8; 3270 -4.1; 3597 -2.8; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX56LP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX56LP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 59 Hz   | 0.4  | -5.9 dB |
| Peaking | 167 Hz  | 0.83 | -3.1 dB |
| Peaking | 1037 Hz | 3.84 | 4.8 dB  |
| Peaking | 2112 Hz | 1.77 | -5.7 dB |
| Peaking | 4644 Hz | 1.35 | 7.4 dB  |
| Peaking | 608 Hz  | 2.29 | 0.8 dB  |
| Peaking | 845 Hz  | 9.04 | -1.5 dB |
| Peaking | 4834 Hz | 6.67 | -1.3 dB |
| Peaking | 6385 Hz | 2.77 | 3.9 dB  |
| Peaking | 7561 Hz | 1.93 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.2 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.7 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-EX56LP/Sony%20MDR-EX56LP.png)