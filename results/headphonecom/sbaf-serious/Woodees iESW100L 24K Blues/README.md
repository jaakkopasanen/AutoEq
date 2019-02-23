# Woodees iESW100L 24K Blues
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -12.5; 25 -12.5; 28 -12.5; 31 -12.5; 34 -12.4; 37 -12.4; 41 -12.4; 45 -12.4; 49 -12.4; 54 -12.4; 60 -12.5; 66 -12.6; 72 -12.6; 79 -12.7; 87 -12.7; 96 -12.6; 106 -12.5; 116 -12.3; 128 -12.1; 141 -11.9; 155 -11.7; 170 -11.3; 187 -10.9; 206 -10.4; 227 -9.8; 249 -9.3; 274 -8.7; 302 -7.9; 332 -7.2; 365 -6.4; 402 -5.6; 442 -5.1; 486 -4.5; 535 -3.7; 588 -3.0; 647 -2.4; 712 -1.9; 783 -1.7; 861 -1.6; 947 -1.7; 1042 -1.9; 1146 -2.2; 1261 -2.7; 1387 -3.6; 1526 -4.5; 1678 -5.2; 1846 -5.5; 2031 -5.9; 2234 -6.2; 2457 -6.5; 2703 -6.5; 2973 -4.9; 3270 -2.3; 3597 -0.5; 3957 -1.7; 4353 -5.2; 4788 -9.7; 5267 -12.9; 5793 -5.0; 6373 -0.7; 7010 -3.3; 7711 -5.5; 8482 -5.8; 9330 -7.0; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Woodees iESW100L 24K Blues GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Woodees iESW100L 24K Blues ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 55 Hz   | 0.19 | -7.1 dB |
| Peaking | 743 Hz  | 0.9  | 5.4 dB  |
| Peaking | 3727 Hz | 4.46 | 6.4 dB  |
| Peaking | 5205 Hz | 4.33 | -9.5 dB |
| Peaking | 6279 Hz | 4.7  | 7.5 dB  |
| Peaking | 712 Hz  | 4.44 | -0.5 dB |
| Peaking | 1162 Hz | 3.85 | 1.1 dB  |
| Peaking | 2344 Hz | 2.93 | -1.7 dB |
| Peaking | 9283 Hz | 7.16 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB |
| Peaking | 62 Hz    | 1.41 | -5.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Woodees%20iESW100L%2024K%20Blues/Woodees%20iESW100L%2024K%20Blues.png)