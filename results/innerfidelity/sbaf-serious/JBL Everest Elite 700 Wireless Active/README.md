# JBL Everest Elite 700 Wireless Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -7.5; 25 -8.4; 28 -9.1; 31 -9.3; 34 -9.3; 37 -9.1; 41 -8.8; 45 -8.4; 49 -8.0; 54 -7.6; 60 -7.1; 66 -6.7; 72 -6.4; 79 -6.2; 87 -6.0; 96 -6.1; 106 -6.1; 116 -6.1; 128 -6.1; 141 -6.3; 155 -6.3; 170 -6.4; 187 -6.5; 206 -6.8; 227 -6.5; 249 -6.4; 274 -6.2; 302 -6.0; 332 -5.9; 365 -5.7; 402 -5.5; 442 -5.4; 486 -5.9; 535 -6.1; 588 -5.9; 647 -6.0; 712 -6.0; 783 -5.9; 861 -6.1; 947 -6.6; 1042 -6.9; 1146 -6.8; 1261 -7.8; 1387 -7.9; 1526 -8.5; 1678 -9.3; 1846 -10.0; 2031 -10.8; 2234 -11.7; 2457 -11.4; 2703 -9.9; 2973 -7.8; 3270 -6.0; 3597 -6.1; 3957 -5.4; 4353 -3.6; 4788 -0.6; 5267 -0.5; 5793 -0.7; 6373 -2.2; 7010 -4.0; 7711 -6.2; 8482 -9.0; 9330 -10.0; 10263 -7.9; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest Elite 700 Wireless Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest Elite 700 Wireless Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 1.74 | -3.2 dB |
| Peaking | 493 Hz  | 0.87 | 0.8 dB  |
| Peaking | 2237 Hz | 1.65 | -5.8 dB |
| Peaking | 5410 Hz | 1.67 | 7.0 dB  |
| Peaking | 9015 Hz | 3.32 | -5.1 dB |
| Peaking | 92 Hz   | 1.84 | 0.6 dB  |
| Peaking | 211 Hz  | 4.14 | -0.5 dB |
| Peaking | 3234 Hz | 8.63 | 1.2 dB  |
| Peaking | 4004 Hz | 8.71 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JBL%20Everest%20Elite%20700%20Wireless%20Active/JBL%20Everest%20Elite%20700%20Wireless%20Active.png)