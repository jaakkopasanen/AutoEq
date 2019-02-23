# Sennheiser PX 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.0; 96 -1.8; 106 -1.9; 116 -1.5; 128 -1.9; 141 -2.4; 155 -2.7; 170 -3.2; 187 -3.8; 206 -4.2; 227 -4.3; 249 -3.9; 274 -4.3; 302 -4.7; 332 -5.2; 365 -5.5; 402 -6.1; 442 -6.3; 486 -7.2; 535 -7.9; 588 -8.6; 647 -9.6; 712 -10.3; 783 -11.0; 861 -11.1; 947 -11.1; 1042 -10.9; 1146 -10.7; 1261 -10.8; 1387 -11.1; 1526 -11.7; 1678 -12.0; 1846 -12.2; 2031 -12.0; 2234 -10.6; 2457 -9.8; 2703 -9.1; 2973 -7.4; 3270 -6.1; 3597 -5.3; 3957 -4.5; 4353 -6.6; 4788 -6.8; 5267 -4.5; 5793 -2.8; 6373 -4.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.15 | 4.8 dB  |
| Peaking | 107 Hz  | 0.24 | 2.4 dB  |
| Peaking | 849 Hz  | 1.03 | -4.9 dB |
| Peaking | 1853 Hz | 1.88 | -5.1 dB |
| Peaking | 5956 Hz | 2.59 | 3.6 dB  |
| Peaking | 77 Hz   | 4.8  | 0.4 dB  |
| Peaking | 2645 Hz | 3.48 | -1.3 dB |
| Peaking | 4043 Hz | 2.08 | 3.3 dB  |
| Peaking | 4557 Hz | 4.81 | -4.0 dB |
| Peaking | 8377 Hz | 3.87 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.8 dB  |
| Peaking | 125 Hz   | 1.41 | 3.4 dB  |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -4.3 dB |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PX%20200/Sennheiser%20PX%20200.png)