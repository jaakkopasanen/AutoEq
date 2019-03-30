# Sony MDR-EX15LP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.1; 25 -4.3; 28 -4.5; 31 -4.6; 34 -4.7; 37 -4.7; 41 -4.7; 45 -4.8; 49 -4.9; 54 -4.9; 60 -4.9; 66 -5.0; 72 -4.9; 79 -4.7; 87 -4.7; 96 -4.7; 106 -4.7; 116 -4.5; 128 -4.4; 141 -4.1; 155 -3.8; 170 -3.2; 187 -3.1; 206 -3.5; 227 -3.7; 249 -3.7; 274 -3.5; 302 -3.4; 332 -3.2; 365 -3.1; 402 -2.8; 442 -2.8; 486 -2.6; 535 -2.4; 588 -2.4; 647 -2.4; 712 -2.4; 783 -2.4; 861 -2.4; 947 -2.4; 1042 -2.7; 1146 -2.8; 1261 -2.7; 1387 -2.8; 1526 -3.1; 1678 -3.2; 1846 -3.4; 2031 -4.0; 2234 -6.3; 2457 -8.1; 2703 -8.8; 2973 -8.9; 3270 -8.9; 3597 -8.6; 3957 -8.6; 4353 -8.6; 4788 -7.9; 5267 -5.9; 5793 -3.3; 6373 -0.5; 7010 -0.8; 7711 -3.0; 8482 -3.3; 9330 -3.3; 10263 -3.3; 11289 -3.3; 12418 -3.3; 13660 -3.3; 15026 -3.3; 16529 -3.3; 18182 -3.3; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX15LP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX15LP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 56 Hz    | 1.36 | 1.0 dB  |
| Peaking | 56 Hz    | 0.68 | -2.6 dB |
| Peaking | 1794 Hz  | 0.55 | 3.6 dB  |
| Peaking | 3225 Hz  | 0.8  | -8.7 dB |
| Peaking | 6582 Hz  | 3.67 | 6.1 dB  |
| Peaking | 1964 Hz  | 3.39 | 2.8 dB  |
| Peaking | 2407 Hz  | 1.43 | -2.6 dB |
| Peaking | 3312 Hz  | 1.81 | 1.8 dB  |
| Peaking | 4518 Hz  | 4.79 | -1.3 dB |
| Peaking | 10596 Hz | 1.53 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | -6.3 dB |
| Peaking | 8000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-EX15LP/Sony%20MDR-EX15LP.png)