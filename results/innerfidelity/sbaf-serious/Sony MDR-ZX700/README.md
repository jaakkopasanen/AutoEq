# Sony MDR-ZX700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -2.0; 60 -3.7; 66 -5.0; 72 -5.9; 79 -6.5; 87 -6.8; 96 -7.7; 106 -8.0; 116 -7.9; 128 -8.8; 141 -9.0; 155 -8.8; 170 -7.5; 187 -8.4; 206 -8.5; 227 -8.4; 249 -8.3; 274 -8.0; 302 -7.8; 332 -8.8; 365 -7.8; 402 -7.4; 442 -7.1; 486 -6.8; 535 -6.4; 588 -5.4; 647 -4.8; 712 -4.6; 783 -4.4; 861 -4.5; 947 -4.9; 1042 -5.3; 1146 -5.8; 1261 -6.4; 1387 -7.7; 1526 -9.3; 1678 -11.3; 1846 -12.6; 2031 -12.5; 2234 -10.7; 2457 -8.8; 2703 -7.4; 2973 -6.0; 3270 -4.9; 3597 -2.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.6; 5793 -1.6; 6373 -1.0; 7010 -4.0; 7711 -7.1; 8482 -14.0; 9330 -15.5; 10263 -8.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.49 | 8.4 dB   |
| Peaking | 100 Hz   | 0.57 | -5.3 dB  |
| Peaking | 2042 Hz  | 2.04 | -9.1 dB  |
| Peaking | 5500 Hz  | 0.57 | 7.8 dB   |
| Peaking | 8938 Hz  | 2.9  | -15.3 dB |
| Peaking | 825 Hz   | 1.86 | 2.5 dB   |
| Peaking | 1660 Hz  | 6.73 | -1.6 dB  |
| Peaking | 3173 Hz  | 3.93 | -1.9 dB  |
| Peaking | 3862 Hz  | 5.73 | 1.7 dB   |
| Peaking | 14801 Hz | 2.15 | -0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.5 dB |
| Peaking | 4000 Hz  | 1.41 | 9.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-ZX700/Sony%20MDR-ZX700.png)