# Sony MDR-ZX550BN
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.3; 96 -2.2; 106 -3.1; 116 -4.0; 128 -4.7; 141 -5.1; 155 -5.0; 170 -4.7; 187 -4.6; 206 -5.0; 227 -5.1; 249 -4.3; 274 -3.2; 302 -4.2; 332 -5.8; 365 -6.8; 402 -7.5; 442 -8.2; 486 -8.9; 535 -9.4; 588 -9.7; 647 -9.9; 712 -10.1; 783 -10.3; 861 -10.4; 947 -10.5; 1042 -10.4; 1146 -10.2; 1261 -10.2; 1387 -10.4; 1526 -10.1; 1678 -9.1; 1846 -8.2; 2031 -7.1; 2234 -6.3; 2457 -5.6; 2703 -5.6; 2973 -5.1; 3270 -3.0; 3597 -0.8; 3957 -0.5; 4353 -0.5; 4788 -2.6; 5267 -4.1; 5793 -4.2; 6373 -1.1; 7010 -7.1; 7711 -15.1; 8482 -17.3; 9330 -13.5; 10263 -10.9; 11289 -11.6; 12418 -9.6; 13660 -6.5; 15026 -8.9; 16529 -18.3; 18182 -20.9; 20000 -8.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX550BN GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX550BN ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.27 | 6.3 dB   |
| Peaking | 1254 Hz  | 0.56 | -6.2 dB  |
| Peaking | 6446 Hz  | 0.48 | 14.8 dB  |
| Peaking | 8344 Hz  | 1.52 | -23.4 dB |
| Peaking | 17818 Hz | 1.31 | -17.2 dB |
| Peaking | 282 Hz   | 5.87 | 3.2 dB   |
| Peaking | 5287 Hz  | 4.41 | -7.9 dB  |
| Peaking | 5407 Hz  | 1.95 | 4.6 dB   |
| Peaking | 11591 Hz | 4.21 | -3.3 dB  |
| Peaking | 14046 Hz | 4.01 | 4.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | 2.6 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | -4.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.9 dB |
| Peaking | 16000 Hz | 1.41 | -9.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-ZX550BN/Sony%20MDR-ZX550BN.png)