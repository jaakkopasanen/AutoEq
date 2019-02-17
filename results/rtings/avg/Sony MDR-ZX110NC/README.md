# Sony MDR-ZX110NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.7; 25 -4.4; 28 -5.3; 31 -6.1; 34 -6.8; 37 -7.3; 41 -8.0; 45 -8.6; 49 -9.0; 54 -9.6; 60 -10.1; 66 -10.7; 72 -11.1; 79 -11.4; 87 -11.8; 96 -12.0; 106 -12.1; 116 -12.2; 128 -12.1; 141 -11.9; 155 -11.8; 170 -11.5; 187 -11.3; 206 -10.9; 227 -10.6; 249 -10.3; 274 -10.1; 302 -9.8; 332 -9.2; 365 -8.2; 402 -6.8; 442 -6.3; 486 -6.6; 535 -6.7; 588 -6.7; 647 -6.7; 712 -6.7; 783 -6.6; 861 -6.2; 947 -6.2; 1042 -7.0; 1146 -8.3; 1261 -8.8; 1387 -9.2; 1526 -8.9; 1678 -8.2; 1846 -7.0; 2031 -5.9; 2234 -4.5; 2457 -3.2; 2703 -2.9; 2973 -3.4; 3270 -3.6; 3597 -2.6; 3957 -1.5; 4353 -0.9; 4788 -0.5; 5267 -0.5; 5793 -0.7; 6373 -4.2; 7010 -7.8; 7711 -10.4; 8482 -12.9; 9330 -13.4; 10263 -9.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.6; 18182 -7.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX110NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX110NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 1.45 | 4.2 dB  |
| Peaking | 103 Hz   | 0.61 | -5.6 dB |
| Peaking | 233 Hz   | 1.56 | -1.7 dB |
| Peaking | 4957 Hz  | 1.21 | 7.4 dB  |
| Peaking | 8595 Hz  | 2.35 | -9.4 dB |
| Peaking | 1007 Hz  | 0.95 | 2.3 dB  |
| Peaking | 1376 Hz  | 1.4  | -4.8 dB |
| Peaking | 2500 Hz  | 3.49 | 2.7 dB  |
| Peaking | 11231 Hz | 6.03 | 1.8 dB  |
| Peaking | 17508 Hz | 2.96 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-ZX110NC/Sony%20MDR-ZX110NC.png)