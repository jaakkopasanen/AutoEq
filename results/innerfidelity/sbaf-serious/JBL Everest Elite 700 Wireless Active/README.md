# JBL Everest Elite 700 Wireless Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -7.2; 25 -8.0; 28 -8.8; 31 -9.0; 34 -9.0; 37 -8.8; 41 -8.5; 45 -8.1; 49 -7.7; 54 -7.2; 60 -6.8; 66 -6.4; 72 -6.1; 79 -5.8; 87 -5.7; 96 -5.8; 106 -5.8; 116 -5.8; 128 -5.8; 141 -6.0; 155 -6.0; 170 -6.1; 187 -6.2; 206 -6.5; 227 -6.2; 249 -6.1; 274 -5.8; 302 -5.7; 332 -5.5; 365 -5.4; 402 -5.2; 442 -5.1; 486 -5.6; 535 -5.8; 588 -5.6; 647 -5.7; 712 -5.7; 783 -5.6; 861 -5.8; 947 -6.2; 1042 -6.6; 1146 -6.5; 1261 -7.5; 1387 -7.6; 1526 -8.2; 1678 -8.9; 1846 -9.6; 2031 -10.5; 2234 -11.4; 2457 -11.0; 2703 -9.6; 2973 -7.5; 3270 -5.7; 3597 -5.8; 3957 -5.1; 4353 -3.3; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.9; 7010 -4.0; 7711 -6.2; 8482 -8.7; 9330 -9.7; 10263 -7.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest Elite 700 Wireless Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest Elite 700 Wireless Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 1.35 | -3.5 dB |
| Peaking | 246 Hz  | 0.04 | 0.8 dB  |
| Peaking | 2249 Hz | 1.56 | -6.1 dB |
| Peaking | 5470 Hz | 1.6  | 6.7 dB  |
| Peaking | 8859 Hz | 3.02 | -4.9 dB |
| Peaking | 208 Hz  | 1.1  | -1.8 dB |
| Peaking | 231 Hz  | 0.54 | 1.2 dB  |
| Peaking | 1363 Hz | 2.58 | -0.5 dB |
| Peaking | 3862 Hz | 2.35 | 1.8 dB  |
| Peaking | 3937 Hz | 5.09 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JBL%20Everest%20Elite%20700%20Wireless%20Active/JBL%20Everest%20Elite%20700%20Wireless%20Active.png)