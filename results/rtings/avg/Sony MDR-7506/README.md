# Sony MDR-7506
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.6; 25 -7.1; 28 -7.7; 31 -8.2; 34 -8.6; 37 -8.7; 41 -8.8; 45 -8.8; 49 -8.8; 54 -8.7; 60 -8.5; 66 -8.3; 72 -8.1; 79 -7.8; 87 -7.8; 96 -7.7; 106 -7.7; 116 -7.4; 128 -6.9; 141 -6.4; 155 -5.9; 170 -5.2; 187 -4.3; 206 -3.3; 227 -2.0; 249 -0.5; 274 -1.2; 302 -3.5; 332 -4.2; 365 -4.4; 402 -4.6; 442 -4.6; 486 -4.6; 535 -4.5; 588 -4.3; 647 -3.9; 712 -3.6; 783 -3.4; 861 -2.9; 947 -2.6; 1042 -2.8; 1146 -3.2; 1261 -3.5; 1387 -3.9; 1526 -4.7; 1678 -5.4; 1846 -6.2; 2031 -7.0; 2234 -6.6; 2457 -6.2; 2703 -7.1; 2973 -8.3; 3270 -8.2; 3597 -7.3; 3957 -7.9; 4353 -10.3; 4788 -8.0; 5267 -4.0; 5793 -1.1; 6373 -1.7; 7010 -3.8; 7711 -5.7; 8482 -7.7; 9330 -10.0; 10263 -11.0; 11289 -7.5; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7506 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7506 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 53 Hz    | 0.49 | -3.7 dB |
| Peaking | 250 Hz   | 2.39 | 5.0 dB  |
| Peaking | 4584 Hz  | 1.5  | -7.3 dB |
| Peaking | 5832 Hz  | 2.38 | 9.1 dB  |
| Peaking | 9852 Hz  | 3.1  | -6.5 dB |
| Peaking | 997 Hz   | 1.49 | 2.6 dB  |
| Peaking | 1986 Hz  | 5.19 | -1.5 dB |
| Peaking | 3436 Hz  | 2.1  | -1.9 dB |
| Peaking | 3722 Hz  | 6.13 | 3.5 dB  |
| Peaking | 12263 Hz | 6.17 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | 3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-7506/Sony%20MDR-7506.png)