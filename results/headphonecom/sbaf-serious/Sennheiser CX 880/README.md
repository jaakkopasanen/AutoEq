# Sennheiser CX 880
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -9.0; 25 -9.4; 28 -9.8; 31 -10.2; 34 -10.5; 37 -10.8; 41 -11.1; 45 -11.4; 49 -11.6; 54 -11.8; 60 -12.1; 66 -12.4; 72 -12.7; 79 -12.8; 87 -13.0; 96 -13.2; 106 -13.1; 116 -13.1; 128 -13.1; 141 -13.0; 155 -12.8; 170 -12.6; 187 -12.2; 206 -11.8; 227 -11.3; 249 -10.8; 274 -10.3; 302 -9.6; 332 -8.9; 365 -8.1; 402 -7.5; 442 -7.0; 486 -6.4; 535 -5.8; 588 -5.1; 647 -4.5; 712 -4.0; 783 -3.7; 861 -3.6; 947 -3.7; 1042 -4.0; 1146 -4.2; 1261 -4.8; 1387 -5.0; 1526 -5.8; 1678 -6.1; 1846 -6.1; 2031 -6.0; 2234 -5.6; 2457 -4.8; 2703 -4.0; 2973 -2.8; 3270 -1.3; 3597 -0.5; 3957 -1.9; 4353 -4.8; 4788 -6.8; 5267 -8.4; 5793 -10.4; 6373 -10.3; 7010 -8.9; 7711 -9.5; 8482 -13.0; 9330 -14.4; 10263 -8.8; 11289 -3.9; 12418 -3.9; 13660 -3.9; 15026 -3.9; 16529 -3.9; 18182 -3.9; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX 880 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 880 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 45 Hz    | 0.39 | -6.0 dB  |
| Peaking | 129 Hz   | 0.68 | -5.4 dB  |
| Peaking | 258 Hz   | 1.08 | -3.2 dB  |
| Peaking | 6013 Hz  | 3.62 | -6.5 dB  |
| Peaking | 8999 Hz  | 3.67 | -11.1 dB |
| Peaking | 855 Hz   | 2.08 | 1.4 dB   |
| Peaking | 1894 Hz  | 1.42 | -2.5 dB  |
| Peaking | 3637 Hz  | 2.49 | 5.4 dB   |
| Peaking | 4696 Hz  | 2.58 | -2.5 dB  |
| Peaking | 11425 Hz | 5.94 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.5 dB |
| Peaking | 125 Hz   | 1.41 | -7.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -9.5 dB |
| Peaking | 16000 Hz | 1.41 | 1.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX%20880/Sennheiser%20CX%20880.png)