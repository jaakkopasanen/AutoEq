# Woodees iESW100L 24K Blues
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.4; 23 -13.4; 25 -13.4; 28 -13.4; 31 -13.4; 34 -13.3; 37 -13.3; 41 -13.3; 45 -13.3; 49 -13.3; 54 -13.4; 60 -13.4; 66 -13.5; 72 -13.5; 79 -13.6; 87 -13.6; 96 -13.5; 106 -13.4; 116 -13.2; 128 -13.0; 141 -12.8; 155 -12.6; 170 -12.2; 187 -11.8; 206 -11.3; 227 -10.8; 249 -10.2; 274 -9.6; 302 -8.8; 332 -8.1; 365 -7.3; 402 -6.5; 442 -6.0; 486 -5.4; 535 -4.6; 588 -3.9; 647 -3.3; 712 -2.8; 783 -2.6; 861 -2.5; 947 -2.7; 1042 -2.8; 1146 -3.1; 1261 -3.6; 1387 -4.5; 1526 -5.4; 1678 -6.1; 1846 -6.4; 2031 -6.8; 2234 -7.1; 2457 -7.4; 2703 -7.4; 2973 -5.8; 3270 -3.2; 3597 -1.4; 3957 -2.6; 4353 -6.1; 4788 -10.6; 5267 -13.8; 5793 -6.0; 6373 -1.2; 7010 -0.5; 7711 -2.6; 8482 -4.7; 9330 -7.9; 10263 -4.0; 11289 -2.9; 12418 -2.9; 13660 -2.9; 15026 -2.9; 16529 -2.9; 18182 -2.9; 20000 -2.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Woodees iESW100L 24K Blues GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Woodees iESW100L 24K Blues ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 64 Hz    | 0.12 | -11.1 dB |
| Peaking | 1989 Hz  | 0.21 | 7.9 dB   |
| Peaking | 2150 Hz  | 0.86 | -11.7 dB |
| Peaking | 5121 Hz  | 4.9  | -15.0 dB |
| Peaking | 9378 Hz  | 3.88 | -7.6 dB  |
| Peaking | 2820 Hz  | 5.85 | -2.3 dB  |
| Peaking | 3739 Hz  | 3.19 | 3.4 dB   |
| Peaking | 4329 Hz  | 3.38 | -2.6 dB  |
| Peaking | 6650 Hz  | 8.19 | 2.4 dB   |
| Peaking | 14003 Hz | 1.4  | -0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.7 dB |
| Peaking | 62 Hz    | 1.41 | -7.6 dB  |
| Peaking | 125 Hz   | 1.41 | -8.4 dB  |
| Peaking | 250 Hz   | 1.41 | -6.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Woodees%20iESW100L%2024K%20Blues/Woodees%20iESW100L%2024K%20Blues.png)