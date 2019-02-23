# Sony MH1C
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.5; 23 -16.3; 25 -16.2; 28 -16.0; 31 -15.8; 34 -15.6; 37 -15.4; 41 -15.1; 45 -14.8; 49 -14.6; 54 -14.4; 60 -14.2; 66 -13.9; 72 -13.8; 79 -13.6; 87 -13.5; 96 -13.3; 106 -13.0; 116 -12.7; 128 -12.5; 141 -12.1; 155 -11.8; 170 -11.4; 187 -11.0; 206 -10.5; 227 -10.0; 249 -9.6; 274 -9.1; 302 -8.6; 332 -8.1; 365 -7.6; 402 -7.2; 442 -6.6; 486 -6.4; 535 -6.0; 588 -5.5; 647 -5.3; 712 -5.2; 783 -5.0; 861 -5.2; 947 -5.6; 1042 -5.7; 1146 -6.7; 1261 -6.8; 1387 -7.1; 1526 -7.7; 1678 -8.3; 1846 -8.5; 2031 -8.4; 2234 -8.3; 2457 -7.8; 2703 -7.3; 2973 -6.0; 3270 -4.2; 3597 -2.8; 3957 -2.5; 4353 -3.2; 4788 -2.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.1; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MH1C GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MH1C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.23 | -9.7 dB |
| Peaking | 142 Hz  | 0.92 | -3.0 dB |
| Peaking | 2104 Hz | 2.12 | -2.6 dB |
| Peaking | 3738 Hz | 3.07 | 3.6 dB  |
| Peaking | 5705 Hz | 2.8  | 6.4 dB  |
| Peaking | 147 Hz  | 1.98 | 0.9 dB  |
| Peaking | 248 Hz  | 0.71 | -0.9 dB |
| Peaking | 744 Hz  | 0.86 | 2.2 dB  |
| Peaking | 1404 Hz | 1.53 | -1.2 dB |
| Peaking | 8212 Hz | 4.63 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.1 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 16000 Hz | 1.41 | -0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MH1C/Sony%20MH1C.png)