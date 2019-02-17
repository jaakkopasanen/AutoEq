# AKG K712
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.5; 25 -5.9; 28 -6.4; 31 -6.7; 34 -7.1; 37 -7.4; 41 -7.7; 45 -7.9; 49 -8.2; 54 -8.5; 60 -8.7; 66 -8.9; 72 -9.1; 79 -9.3; 87 -9.5; 96 -10.1; 106 -10.4; 116 -10.3; 128 -10.7; 141 -11.0; 155 -11.2; 170 -10.9; 187 -11.3; 206 -11.4; 227 -11.6; 249 -11.6; 274 -11.5; 302 -11.4; 332 -11.1; 365 -10.8; 402 -10.7; 442 -10.4; 486 -10.1; 535 -9.5; 588 -8.9; 647 -9.0; 712 -8.3; 783 -7.5; 861 -6.8; 947 -5.9; 1042 -4.8; 1146 -3.8; 1261 -3.8; 1387 -4.5; 1526 -5.6; 1678 -7.1; 1846 -8.8; 2031 -11.1; 2234 -10.2; 2457 -7.2; 2703 -3.0; 2973 -0.5; 3270 -2.7; 3597 -4.2; 3957 -5.9; 4353 -8.4; 4788 -7.5; 5267 -8.0; 5793 -8.6; 6373 -9.7; 7010 -12.7; 7711 -11.9; 8482 -10.0; 9330 -8.9; 10263 -8.8; 11289 -7.3; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -6.1; 18182 -7.9; 20000 -8.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 159 Hz   | 0.36 | -5.1 dB  |
| Peaking | 448 Hz   | 0.7  | -2.8 dB  |
| Peaking | 2105 Hz  | 2.31 | -15.4 dB |
| Peaking | 2407 Hz  | 0.78 | 10.9 dB  |
| Peaking | 6594 Hz  | 0.88 | -7.6 dB  |
| Peaking | 1175 Hz  | 5.09 | 1.7 dB   |
| Peaking | 2991 Hz  | 5.34 | 3.8 dB   |
| Peaking | 4840 Hz  | 0.7  | -2.5 dB  |
| Peaking | 5693 Hz  | 3.12 | 4.1 dB   |
| Peaking | 12644 Hz | 2.49 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -4.5 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K712/AKG%20K712.png)