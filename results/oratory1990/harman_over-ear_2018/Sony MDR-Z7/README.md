# Sony MDR-Z7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -2.3; 25 -3.2; 28 -4.3; 31 -5.3; 34 -6.0; 37 -6.5; 41 -6.8; 45 -6.9; 49 -6.9; 54 -7.0; 60 -7.2; 66 -7.4; 72 -7.5; 79 -7.7; 87 -8.0; 96 -8.4; 106 -8.7; 116 -8.8; 128 -8.8; 141 -9.0; 155 -9.2; 170 -9.2; 187 -8.8; 206 -8.1; 227 -7.3; 249 -6.6; 274 -6.1; 302 -5.7; 332 -5.5; 365 -5.2; 402 -5.1; 442 -5.2; 486 -5.4; 535 -5.7; 588 -6.0; 647 -6.6; 712 -7.4; 783 -8.0; 861 -8.1; 947 -7.5; 1042 -6.4; 1146 -5.0; 1261 -3.7; 1387 -3.3; 1526 -4.1; 1678 -5.4; 1846 -6.5; 2031 -7.3; 2234 -8.1; 2457 -9.1; 2703 -8.9; 2973 -7.1; 3270 -4.1; 3597 -0.9; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.6; 5793 -3.1; 6373 -6.6; 7010 -10.2; 7711 -13.4; 8482 -14.5; 9330 -13.2; 10263 -10.0; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.3; 20000 -16.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 2.4  | 5.7 dB  |
| Peaking | 131 Hz   | 1.3  | -2.8 dB |
| Peaking | 1357 Hz  | 5.42 | 3.6 dB  |
| Peaking | 4746 Hz  | 2.06 | 8.2 dB  |
| Peaking | 8320 Hz  | 2.33 | -9.7 dB |
| Peaking | 404 Hz   | 1.72 | 1.8 dB  |
| Peaking | 822 Hz   | 4.1  | -2.2 dB |
| Peaking | 2603 Hz  | 3.24 | -4.1 dB |
| Peaking | 3620 Hz  | 5.88 | 3.7 dB  |
| Peaking | 11680 Hz | 5.24 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sony%20MDR-Z7/Sony%20MDR-Z7.png)