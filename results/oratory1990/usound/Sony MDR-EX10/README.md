# Sony MDR-EX10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -10.0; 25 -10.1; 28 -10.2; 31 -10.3; 34 -10.3; 37 -10.3; 41 -10.3; 45 -10.3; 49 -10.3; 54 -10.3; 60 -10.3; 66 -10.3; 72 -10.4; 79 -10.4; 87 -10.4; 96 -10.4; 106 -10.4; 116 -10.3; 128 -10.2; 141 -9.9; 155 -9.6; 170 -9.2; 187 -8.7; 206 -8.0; 227 -7.8; 249 -8.2; 274 -7.6; 302 -6.9; 332 -6.3; 365 -5.7; 402 -5.1; 442 -4.6; 486 -4.0; 535 -3.5; 588 -3.0; 647 -2.6; 712 -2.1; 783 -1.7; 861 -1.5; 947 -1.5; 1042 -1.8; 1146 -2.1; 1261 -2.1; 1387 -2.2; 1526 -2.1; 1678 -1.8; 1846 -1.7; 2031 -2.1; 2234 -2.4; 2457 -2.5; 2703 -3.0; 2973 -3.5; 3270 -3.7; 3597 -3.7; 3957 -4.0; 4353 -4.1; 4788 -3.9; 5267 -3.3; 5793 -2.0; 6373 -0.5; 7010 -1.9; 7711 -4.1; 8482 -4.4; 9330 -6.4; 10263 -4.8; 11289 -4.4; 12418 -4.4; 13660 -4.4; 15026 -5.2; 16529 -6.9; 18182 -4.5; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.5  | -4.4 dB |
| Peaking | 114 Hz   | 0.4  | -5.3 dB |
| Peaking | 804 Hz   | 0.89 | 3.2 dB  |
| Peaking | 1933 Hz  | 1.54 | 1.9 dB  |
| Peaking | 6425 Hz  | 5.3  | 4.3 dB  |
| Peaking | 213 Hz   | 5.57 | 0.8 dB  |
| Peaking | 252 Hz   | 5.01 | -0.7 dB |
| Peaking | 5669 Hz  | 4.06 | 0.3 dB  |
| Peaking | 9409 Hz  | 6.84 | -2.4 dB |
| Peaking | 16366 Hz | 3.53 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sony%20MDR-EX10/Sony%20MDR-EX10.png)