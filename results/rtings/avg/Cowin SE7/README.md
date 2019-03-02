# Cowin SE7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -1.4; 60 -2.3; 66 -3.2; 72 -4.0; 79 -5.0; 87 -6.1; 96 -7.1; 106 -8.0; 116 -8.9; 128 -9.7; 141 -10.4; 155 -11.0; 170 -11.4; 187 -11.7; 206 -11.9; 227 -12.2; 249 -12.4; 274 -12.7; 302 -12.8; 332 -12.8; 365 -12.5; 402 -11.9; 442 -11.5; 486 -11.2; 535 -10.6; 588 -10.1; 647 -9.5; 712 -9.0; 783 -8.4; 861 -7.7; 947 -7.2; 1042 -6.9; 1146 -7.1; 1261 -7.8; 1387 -7.9; 1526 -7.5; 1678 -6.8; 1846 -5.4; 2031 -3.7; 2234 -2.3; 2457 -0.8; 2703 -0.5; 2973 -1.0; 3270 -1.9; 3597 -2.1; 3957 -1.9; 4353 -1.6; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin SE7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin SE7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.46 | 7.5 dB  |
| Peaking | 229 Hz  | 0.42 | -7.1 dB |
| Peaking | 1624 Hz | 2.31 | -3.3 dB |
| Peaking | 2555 Hz | 1.05 | 6.3 dB  |
| Peaking | 5480 Hz | 2.39 | 5.4 dB  |
| Peaking | 220 Hz  | 1.8  | 1.5 dB  |
| Peaking | 253 Hz  | 0.87 | -1.0 dB |
| Peaking | 940 Hz  | 3.9  | 1.0 dB  |
| Peaking | 6535 Hz | 6.46 | 2.5 dB  |
| Peaking | 7792 Hz | 2.03 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.8 dB |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cowin%20SE7/Cowin%20SE7.png)