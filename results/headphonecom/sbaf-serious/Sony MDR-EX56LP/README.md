# Sony MDR-EX56LP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.1; 23 -14.4; 25 -14.8; 28 -15.2; 31 -15.5; 34 -15.8; 37 -16.0; 41 -16.3; 45 -16.5; 49 -16.7; 54 -16.9; 60 -17.2; 66 -17.3; 72 -17.5; 79 -17.6; 87 -17.7; 96 -17.7; 106 -17.6; 116 -17.5; 128 -17.3; 141 -17.2; 155 -17.0; 170 -16.7; 187 -16.3; 206 -15.9; 227 -15.4; 249 -14.9; 274 -14.4; 302 -13.9; 332 -13.3; 365 -12.6; 402 -12.1; 442 -11.7; 486 -11.5; 535 -11.1; 588 -10.7; 647 -10.5; 712 -10.7; 783 -11.0; 861 -11.1; 947 -7.5; 1042 -7.0; 1146 -8.6; 1261 -9.9; 1387 -11.2; 1526 -12.6; 1678 -13.6; 1846 -14.5; 2031 -15.0; 2234 -14.8; 2457 -13.7; 2703 -12.0; 2973 -10.1; 3270 -8.4; 3597 -7.1; 3957 -4.3; 4353 -0.8; 4788 -0.5; 5267 -0.5; 5793 -1.1; 6373 -5.3; 7010 -6.2; 7711 -6.2; 8482 -6.5; 9330 -8.8; 10263 -10.3; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -8.2; 16529 -9.4; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX56LP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX56LP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.31 | -6.5 dB |
| Peaking | 153 Hz   | 0.34 | -8.4 dB |
| Peaking | 2119 Hz  | 1.41 | -8.9 dB |
| Peaking | 4824 Hz  | 2.48 | 8.3 dB  |
| Peaking | 867 Hz   | 3.64 | -3.7 dB |
| Peaking | 978 Hz   | 4.04 | 5.0 dB  |
| Peaking | 1520 Hz  | 5.06 | -1.1 dB |
| Peaking | 9947 Hz  | 5.58 | -4.4 dB |
| Peaking | 16165 Hz | 3.43 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.5 dB  |
| Peaking | 62 Hz    | 1.41 | -8.2 dB  |
| Peaking | 125 Hz   | 1.41 | -8.9 dB  |
| Peaking | 250 Hz   | 1.41 | -6.3 dB  |
| Peaking | 500 Hz   | 1.41 | -3.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -10.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -2.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-EX56LP/Sony%20MDR-EX56LP.png)