# Sony MDR-ZX550BN
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.6; 87 -1.5; 96 -2.4; 106 -3.4; 116 -4.3; 128 -4.9; 141 -5.3; 155 -5.2; 170 -4.8; 187 -4.8; 206 -5.1; 227 -5.2; 249 -4.4; 274 -3.2; 302 -4.3; 332 -5.7; 365 -6.8; 402 -7.6; 442 -8.2; 486 -8.9; 535 -9.3; 588 -9.6; 647 -9.8; 712 -10.0; 783 -10.1; 861 -10.3; 947 -10.4; 1042 -10.3; 1146 -10.0; 1261 -10.0; 1387 -10.2; 1526 -9.9; 1678 -8.8; 1846 -7.9; 2031 -6.6; 2234 -5.4; 2457 -4.7; 2703 -5.0; 2973 -5.0; 3270 -3.0; 3597 -0.8; 3957 -0.5; 4353 -0.5; 4788 -2.5; 5267 -3.2; 5793 -4.8; 6373 -1.2; 7010 -7.4; 7711 -14.5; 8482 -17.7; 9330 -15.2; 10263 -11.2; 11289 -10.3; 12418 -9.2; 13660 -6.6; 15026 -9.7; 16529 -18.7; 18182 -20.8; 20000 -8.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX550BN GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX550BN ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.3  | 6.3 dB   |
| Peaking | 1266 Hz  | 0.57 | -6.3 dB  |
| Peaking | 6379 Hz  | 0.39 | 12.2 dB  |
| Peaking | 8529 Hz  | 1.7  | -21.8 dB |
| Peaking | 17725 Hz | 1.22 | -17.6 dB |
| Peaking | 133 Hz   | 3.62 | -1.7 dB  |
| Peaking | 281 Hz   | 4.94 | 3.2 dB   |
| Peaking | 4211 Hz  | 2.8  | 4.5 dB   |
| Peaking | 5013 Hz  | 1.37 | -4.0 dB  |
| Peaking | 6451 Hz  | 8.12 | 5.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB   |
| Peaking | 62 Hz    | 1.41 | 5.8 dB   |
| Peaking | 125 Hz   | 1.41 | 0.4 dB   |
| Peaking | 250 Hz   | 1.41 | 2.6 dB   |
| Peaking | 500 Hz   | 1.41 | -2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -7.1 dB  |
| Peaking | 16000 Hz | 1.41 | -10.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-ZX550BN/Sony%20MDR-ZX550BN.png)