# Sony MDR-ZX550BN
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.6; 128 -1.1; 141 -1.4; 155 -1.3; 170 -1.0; 187 -1.0; 206 -1.3; 227 -1.3; 249 -0.6; 274 -0.5; 302 -0.7; 332 -1.8; 365 -3.0; 402 -3.8; 442 -4.4; 486 -5.1; 535 -5.5; 588 -5.8; 647 -6.0; 712 -6.1; 783 -6.3; 861 -6.5; 947 -6.6; 1042 -6.4; 1146 -6.2; 1261 -6.2; 1387 -6.4; 1526 -6.0; 1678 -5.0; 1846 -4.0; 2031 -2.8; 2234 -1.6; 2457 -0.9; 2703 -1.2; 2973 -1.2; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.1; 7711 -10.7; 8482 -13.9; 9330 -11.3; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.0; 16529 -14.8; 18182 -16.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX550BN GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX550BN ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 48 Hz    | 0.24 | 6.4 dB   |
| Peaking | 273 Hz   | 1.89 | 3.8 dB   |
| Peaking | 6104 Hz  | 0.52 | 9.6 dB   |
| Peaking | 8453 Hz  | 2.32 | -15.7 dB |
| Peaking | 17699 Hz | 1.54 | -13.0 dB |
| Peaking | 19 Hz    | 2.45 | 0.9 dB   |
| Peaking | 1441 Hz  | 0.86 | -2.0 dB  |
| Peaking | 2316 Hz  | 1.92 | 2.9 dB   |
| Peaking | 4664 Hz  | 5.05 | -1.0 dB  |
| Peaking | 14798 Hz | 7.33 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.6 dB  |
| Peaking | 125 Hz   | 1.41 | 3.9 dB  |
| Peaking | 250 Hz   | 1.41 | 5.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | -6.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-ZX550BN/Sony%20MDR-ZX550BN.png)