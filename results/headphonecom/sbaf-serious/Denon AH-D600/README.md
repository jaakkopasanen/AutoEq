# Denon AH-D600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.4; 25 -7.7; 28 -8.1; 31 -8.4; 34 -8.6; 37 -8.7; 41 -8.8; 45 -8.8; 49 -8.6; 54 -8.2; 60 -8.2; 66 -8.7; 72 -9.6; 79 -10.0; 87 -10.1; 96 -10.4; 106 -10.6; 116 -10.7; 128 -10.9; 141 -11.0; 155 -11.1; 170 -10.2; 187 -10.4; 206 -9.8; 227 -8.4; 249 -6.9; 274 -6.1; 302 -6.4; 332 -6.8; 365 -6.5; 402 -6.6; 442 -6.0; 486 -5.3; 535 -5.9; 588 -5.9; 647 -6.1; 712 -6.5; 783 -6.5; 861 -6.4; 947 -6.5; 1042 -6.5; 1146 -6.6; 1261 -7.0; 1387 -7.7; 1526 -8.5; 1678 -9.0; 1846 -9.5; 2031 -9.2; 2234 -7.6; 2457 -7.3; 2703 -7.6; 2973 -7.0; 3270 -5.8; 3597 -3.7; 3957 -2.3; 4353 -1.2; 4788 -0.5; 5267 -1.9; 5793 -4.3; 6373 -6.5; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 0.3  | -1.6 dB |
| Peaking | 163 Hz  | 0.78 | -6.0 dB |
| Peaking | 253 Hz  | 0.65 | 3.7 dB  |
| Peaking | 1865 Hz | 1.91 | -3.2 dB |
| Peaking | 4592 Hz | 2.58 | 6.6 dB  |
| Peaking | 209 Hz  | 3.93 | -1.6 dB |
| Peaking | 292 Hz  | 1.31 | 2.3 dB  |
| Peaking | 340 Hz  | 2.4  | -2.6 dB |
| Peaking | 2927 Hz | 5.81 | -1.1 dB |
| Peaking | 3702 Hz | 7.84 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D600/Denon%20AH-D600.png)