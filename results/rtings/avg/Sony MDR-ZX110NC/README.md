# Sony MDR-ZX110NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.6; 25 -3.3; 28 -4.3; 31 -5.1; 34 -5.7; 37 -6.3; 41 -6.9; 45 -7.5; 49 -8.0; 54 -8.5; 60 -9.1; 66 -9.6; 72 -10.0; 79 -10.3; 87 -10.6; 96 -10.9; 106 -11.0; 116 -11.0; 128 -11.0; 141 -10.9; 155 -10.7; 170 -10.5; 187 -10.2; 206 -9.9; 227 -9.7; 249 -9.3; 274 -9.1; 302 -8.9; 332 -8.3; 365 -7.3; 402 -5.9; 442 -5.4; 486 -5.8; 535 -5.9; 588 -5.9; 647 -6.0; 712 -6.0; 783 -5.8; 861 -5.4; 947 -5.4; 1042 -6.3; 1146 -7.5; 1261 -8.2; 1387 -8.5; 1526 -8.3; 1678 -7.4; 1846 -6.4; 2031 -5.5; 2234 -4.5; 2457 -3.3; 2703 -2.6; 2973 -2.6; 3270 -2.5; 3597 -1.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.4; 7010 -7.1; 7711 -10.3; 8482 -11.7; 9330 -10.9; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -6.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX110NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX110NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.41 | 5.0 dB  |
| Peaking | 99 Hz   | 0.77 | -4.5 dB |
| Peaking | 207 Hz  | 1.59 | -2.0 dB |
| Peaking | 5166 Hz | 0.94 | 8.1 dB  |
| Peaking | 8259 Hz | 2.15 | -9.4 dB |
| Peaking | 326 Hz  | 2.66 | -2.2 dB |
| Peaking | 411 Hz  | 1.62 | 2.3 dB  |
| Peaking | 937 Hz  | 2.49 | 2.1 dB  |
| Peaking | 1374 Hz | 1.49 | -3.2 dB |
| Peaking | 2558 Hz | 2.76 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-ZX110NC/Sony%20MDR-ZX110NC.png)