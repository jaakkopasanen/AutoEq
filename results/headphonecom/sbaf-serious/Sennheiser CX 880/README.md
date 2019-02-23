# Sennheiser CX 880
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.9; 25 -8.3; 28 -8.8; 31 -9.1; 34 -9.4; 37 -9.7; 41 -10.0; 45 -10.3; 49 -10.6; 54 -10.8; 60 -11.1; 66 -11.4; 72 -11.6; 79 -11.8; 87 -12.0; 96 -12.1; 106 -12.0; 116 -12.0; 128 -12.0; 141 -11.9; 155 -11.8; 170 -11.5; 187 -11.2; 206 -10.7; 227 -10.3; 249 -9.8; 274 -9.2; 302 -8.5; 332 -7.8; 365 -7.1; 402 -6.4; 442 -5.9; 486 -5.4; 535 -4.7; 588 -4.0; 647 -3.4; 712 -2.9; 783 -2.6; 861 -2.5; 947 -2.6; 1042 -3.0; 1146 -3.1; 1261 -3.8; 1387 -3.9; 1526 -4.7; 1678 -5.1; 1846 -5.1; 2031 -4.9; 2234 -4.5; 2457 -3.8; 2703 -2.9; 2973 -1.7; 3270 -0.5; 3597 -0.5; 3957 -0.9; 4353 -3.7; 4788 -5.7; 5267 -7.3; 5793 -9.4; 6373 -9.2; 7010 -7.8; 7711 -8.4; 8482 -11.9; 9330 -13.3; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX 880 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 880 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 65 Hz    | 0.51 | -3.6 dB |
| Peaking | 167 Hz   | 0.63 | -3.7 dB |
| Peaking | 808 Hz   | 0.84 | 4.4 dB  |
| Peaking | 3427 Hz  | 2.6  | 6.6 dB  |
| Peaking | 8906 Hz  | 3.14 | -7.1 dB |
| Peaking | 2608 Hz  | 6.67 | 0.8 dB  |
| Peaking | 4035 Hz  | 9.03 | 1.9 dB  |
| Peaking | 5976 Hz  | 3.5  | -3.5 dB |
| Peaking | 7419 Hz  | 4.9  | 1.6 dB  |
| Peaking | 10943 Hz | 6.08 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX%20880/Sennheiser%20CX%20880.png)