# Cowin SE7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.3; 60 -2.2; 66 -3.0; 72 -3.9; 79 -4.8; 87 -5.9; 96 -6.9; 106 -7.8; 116 -8.7; 128 -9.5; 141 -10.2; 155 -10.8; 170 -11.3; 187 -11.5; 206 -11.7; 227 -12.1; 249 -12.4; 274 -12.6; 302 -12.8; 332 -12.8; 365 -12.5; 402 -11.8; 442 -11.4; 486 -11.2; 535 -10.6; 588 -10.1; 647 -9.5; 712 -9.0; 783 -8.5; 861 -7.8; 947 -7.3; 1042 -7.0; 1146 -7.2; 1261 -8.0; 1387 -8.1; 1526 -7.7; 1678 -7.0; 1846 -5.7; 2031 -4.1; 2234 -3.1; 2457 -1.7; 2703 -0.8; 2973 -1.1; 3270 -1.7; 3597 -1.9; 3957 -1.6; 4353 -1.3; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin SE7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin SE7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.45 | 7.4 dB  |
| Peaking | 234 Hz  | 0.43 | -7.0 dB |
| Peaking | 1575 Hz | 2.62 | -2.7 dB |
| Peaking | 2785 Hz | 1.05 | 5.6 dB  |
| Peaking | 5496 Hz | 2.41 | 5.2 dB  |
| Peaking | 356 Hz  | 3.81 | -0.5 dB |
| Peaking | 957 Hz  | 4.58 | 0.9 dB  |
| Peaking | 4458 Hz | 3.87 | 1.3 dB  |
| Peaking | 6473 Hz | 4.81 | 3.8 dB  |
| Peaking | 6800 Hz | 1.39 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.8 dB |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cowin%20SE7/Cowin%20SE7.png)