# Sony MDR-7509 HD
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.7; 87 -1.5; 96 -2.4; 106 -3.1; 116 -3.7; 128 -3.9; 141 -4.2; 155 -4.1; 170 -4.1; 187 -4.2; 206 -3.9; 227 -3.6; 249 -3.2; 274 -2.9; 302 -3.2; 332 -4.4; 365 -6.4; 402 -8.0; 442 -8.4; 486 -8.4; 535 -8.7; 588 -8.5; 647 -8.3; 712 -8.5; 783 -8.4; 861 -7.9; 947 -7.8; 1042 -8.0; 1146 -8.1; 1261 -8.5; 1387 -9.4; 1526 -10.7; 1678 -11.8; 1846 -12.7; 2031 -13.9; 2234 -14.8; 2457 -14.3; 2703 -12.7; 2973 -10.6; 3270 -8.8; 3597 -6.7; 3957 -4.0; 4353 -1.7; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.4; 8482 -8.6; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7509 HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7509 HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.36 | 6.5 dB  |
| Peaking | 293 Hz  | 1.78 | 5.4 dB  |
| Peaking | 415 Hz  | 1.01 | -3.9 dB |
| Peaking | 2284 Hz | 1.4  | -9.1 dB |
| Peaking | 5006 Hz | 1.82 | 8.3 dB  |
| Peaking | 44 Hz   | 2.14 | -0.6 dB |
| Peaking | 78 Hz   | 2.77 | 1.1 dB  |
| Peaking | 116 Hz  | 2.94 | -0.8 dB |
| Peaking | 6437 Hz | 6.65 | 2.6 dB  |
| Peaking | 8419 Hz | 4.28 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.5 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | 3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-7509%20HD/Sony%20MDR-7509%20HD.png)