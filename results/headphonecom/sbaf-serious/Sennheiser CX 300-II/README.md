# Sennheiser CX 300-II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.7; 23 -9.0; 25 -9.3; 28 -9.6; 31 -9.9; 34 -10.2; 37 -10.4; 41 -10.7; 45 -11.0; 49 -11.2; 54 -11.6; 60 -11.9; 66 -12.2; 72 -12.5; 79 -12.8; 87 -13.1; 96 -13.4; 106 -13.7; 116 -13.9; 128 -14.0; 141 -14.2; 155 -14.3; 170 -14.2; 187 -14.1; 206 -14.0; 227 -13.7; 249 -13.4; 274 -13.0; 302 -12.6; 332 -12.1; 365 -11.5; 402 -10.9; 442 -10.3; 486 -9.8; 535 -9.1; 588 -8.5; 647 -7.8; 712 -7.2; 783 -6.7; 861 -6.6; 947 -6.5; 1042 -6.4; 1146 -6.4; 1261 -6.5; 1387 -6.5; 1526 -6.4; 1678 -6.3; 1846 -6.0; 2031 -5.5; 2234 -4.9; 2457 -3.9; 2703 -2.8; 2973 -1.8; 3270 -0.7; 3597 -0.5; 3957 -2.1; 4353 -4.7; 4788 -6.7; 5267 -7.9; 5793 -11.2; 6373 -12.5; 7010 -8.2; 7711 -6.2; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX 300-II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 300-II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 68 Hz   | 0.38 | -4.5 dB |
| Peaking | 168 Hz  | 0.75 | -4.4 dB |
| Peaking | 326 Hz  | 1.17 | -2.8 dB |
| Peaking | 3361 Hz | 2.03 | 6.5 dB  |
| Peaking | 6107 Hz | 4.45 | -7.6 dB |
| Peaking | 510 Hz  | 3.64 | -0.5 dB |
| Peaking | 830 Hz  | 2.64 | 0.7 dB  |
| Peaking | 4771 Hz | 8    | -1.1 dB |
| Peaking | 7633 Hz | 7.63 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -6.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX%20300-II/Sennheiser%20CX%20300-II.png)