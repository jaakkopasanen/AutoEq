# Skullcandy Jib
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.2; 25 -6.4; 28 -6.6; 31 -6.7; 34 -6.8; 37 -6.9; 41 -7.0; 45 -7.0; 49 -7.0; 54 -7.1; 60 -7.4; 66 -7.7; 72 -7.9; 79 -8.2; 87 -8.5; 96 -8.8; 106 -9.3; 116 -9.6; 128 -10.0; 141 -10.2; 155 -10.3; 170 -10.2; 187 -10.1; 206 -9.8; 227 -9.3; 249 -8.7; 274 -8.2; 302 -7.6; 332 -7.1; 365 -6.6; 402 -6.0; 442 -5.4; 486 -4.8; 535 -4.1; 588 -3.2; 647 -2.4; 712 -1.5; 783 -0.7; 861 -0.5; 947 -0.9; 1042 -1.8; 1146 -2.6; 1261 -3.1; 1387 -3.3; 1526 -3.3; 1678 -3.5; 1846 -3.7; 2031 -3.9; 2234 -3.5; 2457 -3.2; 2703 -3.9; 2973 -4.7; 3270 -4.4; 3597 -3.8; 3957 -3.5; 4353 -3.2; 4788 -3.0; 5267 -3.5; 5793 -3.8; 6373 -5.4; 7010 -3.6; 7711 -1.4; 8482 -1.4; 9330 -3.2; 10263 -2.9; 11289 -1.4; 12418 -1.4; 13660 -1.4; 15026 -1.4; 16529 -5.5; 18182 -9.5; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Jib GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Jib ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.28 | -5.0 dB |
| Peaking | 167 Hz   | 0.84 | -6.2 dB |
| Peaking | 332 Hz   | 1.61 | -2.6 dB |
| Peaking | 3454 Hz  | 0.62 | -2.7 dB |
| Peaking | 18426 Hz | 1.51 | -9.1 dB |
| Peaking | 833 Hz   | 4.2  | 2.4 dB  |
| Peaking | 4602 Hz  | 3.73 | 1.0 dB  |
| Peaking | 6518 Hz  | 4.49 | -2.7 dB |
| Peaking | 7829 Hz  | 6.01 | 1.9 dB  |
| Peaking | 14479 Hz | 2.66 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -7.3 dB |
| Peaking | 250 Hz   | 1.41 | -6.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Jib/Skullcandy%20Jib.png)