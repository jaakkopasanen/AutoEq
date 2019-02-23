# Sony MDR-ZX110NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.8; 25 -3.5; 28 -4.5; 31 -5.3; 34 -5.9; 37 -6.5; 41 -7.1; 45 -7.7; 49 -8.2; 54 -8.7; 60 -9.3; 66 -9.8; 72 -10.2; 79 -10.6; 87 -10.9; 96 -11.1; 106 -11.2; 116 -11.3; 128 -11.2; 141 -11.1; 155 -10.9; 170 -10.7; 187 -10.4; 206 -10.1; 227 -9.8; 249 -9.4; 274 -9.2; 302 -9.0; 332 -8.4; 365 -7.3; 402 -5.9; 442 -5.4; 486 -5.7; 535 -5.8; 588 -5.8; 647 -5.9; 712 -5.9; 783 -5.7; 861 -5.4; 947 -5.3; 1042 -6.1; 1146 -7.4; 1261 -8.0; 1387 -8.3; 1526 -8.0; 1678 -7.3; 1846 -6.2; 2031 -5.1; 2234 -3.7; 2457 -2.3; 2703 -2.0; 2973 -2.5; 3270 -2.8; 3597 -1.7; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -3.3; 7010 -6.9; 7711 -9.5; 8482 -12.0; 9330 -12.6; 10263 -8.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -6.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX110NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX110NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.43 | 4.9 dB  |
| Peaking | 115 Hz   | 0.64 | -5.1 dB |
| Peaking | 3708 Hz  | 1.18 | 4.9 dB  |
| Peaking | 5559 Hz  | 2.53 | 4.8 dB  |
| Peaking | 8690 Hz  | 2.72 | -7.8 dB |
| Peaking | 455 Hz   | 4.05 | 2.0 dB  |
| Peaking | 916 Hz   | 1.56 | 3.7 dB  |
| Peaking | 1265 Hz  | 1    | -3.8 dB |
| Peaking | 2401 Hz  | 3.49 | 2.8 dB  |
| Peaking | 11030 Hz | 6.89 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-ZX110NC/Sony%20MDR-ZX110NC.png)