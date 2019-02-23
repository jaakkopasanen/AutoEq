# Sleek SA1- Normal Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.4; 25 -10.5; 28 -10.6; 31 -10.6; 34 -10.6; 37 -10.7; 41 -10.8; 45 -10.9; 49 -11.1; 54 -11.3; 60 -11.6; 66 -11.9; 72 -12.2; 79 -12.5; 87 -12.8; 96 -12.9; 106 -13.1; 116 -13.2; 128 -13.4; 141 -13.5; 155 -13.6; 170 -13.5; 187 -13.4; 206 -13.2; 227 -13.0; 249 -12.7; 274 -12.3; 302 -11.8; 332 -11.2; 365 -10.6; 402 -9.9; 442 -9.4; 486 -8.9; 535 -8.2; 588 -7.5; 647 -6.8; 712 -6.1; 783 -5.6; 861 -5.2; 947 -5.1; 1042 -4.9; 1146 -4.7; 1261 -4.8; 1387 -4.7; 1526 -4.7; 1678 -4.5; 1846 -3.8; 2031 -3.1; 2234 -2.3; 2457 -1.5; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -3.4; 4788 -5.8; 5267 -8.1; 5793 -7.2; 6373 -2.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sleek SA1- Normal Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sleek SA1- Normal Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.28 | -3.9 dB |
| Peaking | 146 Hz   | 0.76 | -4.6 dB |
| Peaking | 288 Hz   | 1.34 | -3.0 dB |
| Peaking | 2884 Hz  | 1.1  | 6.2 dB  |
| Peaking | 22050 Hz | 2.34 | 0.8 dB  |
| Peaking | 951 Hz   | 2    | 1.6 dB  |
| Peaking | 3883 Hz  | 3.26 | 3.5 dB  |
| Peaking | 4906 Hz  | 0.75 | -1.7 dB |
| Peaking | 5478 Hz  | 3.94 | -3.8 dB |
| Peaking | 6511 Hz  | 5.22 | 5.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sleek%20SA1-%20Normal%20Filter/Sleek%20SA1-%20Normal%20Filter.png)